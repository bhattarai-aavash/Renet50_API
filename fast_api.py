from fastapi import FastAPI ,UploadFile, File
from PIL import Image
from model_resnet import resnet_classification
import io
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.post("/upload")
async def upload_file(image: UploadFile = File(...)):
    contents = await image.read()
    image_bytes =io.BytesIO(contents)
    img = Image.open(image_bytes)
    result = resnet_classification(img)
     
    
    
    return {'prediction': result}