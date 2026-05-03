from flask import Flask, render_template, request
import os
import torch
from PIL import Image
from torchvision import transforms
from model import DeepfakeModel

app = Flask(__name__)

# Load model
model = DeepfakeModel()

# Image preprocess
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])

    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)
    return image

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']

        if file:
            path = os.path.join("static/uploads", file.filename)
            file.save(path)

            # preprocess
            image = preprocess_image(path)

            # predict
            result, confidence = model.predict(image)

            return render_template(
                'index.html',
                result=result,
                confidence=confidence,
                image=path
            )

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)