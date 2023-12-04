# Image Classification API with ResNet50

Welcome to the Image Classification API with ResNet50 project! This API is designed to provide image classification using the ResNet50 model on the ImageNet dataset labels. It takes an image as input and returns the predicted class label along with the associated probability.

## Getting Started

Follow the steps below to set up and run the Image Classification API on your local machine.

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository to your local machine:**

  

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - For Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - For macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install project dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the API

1. **Start the API server:**

    ```bash
    python app.py
    ```

2. **Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the API documentation.**

## API Usage

- Send a POST request to the `/classify` endpoint with an image file attached.
- The API will respond with the predicted class label and probability.

