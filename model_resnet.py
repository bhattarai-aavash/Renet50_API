import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image



def resnet_classification(img):

    model = models.resnet50(pretrained=True)
    model.eval()

    # Preprocess the image
    
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(img)
    input_batch = input_tensor.unsqueeze(0)

    # Make predictions
    with torch.no_grad():
        output = model(input_batch)

    # Load the labels
    LABELS_URL = 'https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json'
    LABELS_PATH = 'imagenet-simple-labels.json'

    import requests
    import json

    response = requests.get(LABELS_URL)
    labels = json.loads(response.text)
    with open(LABELS_PATH, 'w') as f:
        json.dump(labels, f)

    # Process the predictions
    probs = torch.nn.functional.softmax(output[0], dim=0)
    confidence_score, predicted_idx = torch.max(probs, 0)
    predicted_label = labels[predicted_idx.item()]

    return predicted_label