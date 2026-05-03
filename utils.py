import cv2
import torch
import numpy as np
from PIL import Image

def preprocess(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.transpose(img, (2, 0, 1))
    img = torch.tensor(img, dtype=torch.float32).unsqueeze(0)
    return img

def predict(model, image_tensor):
    with torch.no_grad():
        output = model(image_tensor)
        prob = torch.softmax(output, dim=1)
        return prob.argmax().item(), prob.max().item()