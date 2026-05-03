import torch
import torch.nn as nn
import timm

class DeepfakeModel:
    def __init__(self):
        self.device = torch.device("cpu")

        # Model architecture (same as training)
        self.model = timm.create_model('efficientnet_b0', pretrained=False)

        self.model.classifier = nn.Sequential(
            nn.Linear(self.model.classifier.in_features, 512),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(512, 1)
        )

        # 🔥 Load YOUR model
        self.model.load_state_dict(
            torch.load("model/Nakli_Image_detector.pth", map_location=self.device)
        )

        self.model.to(self.device)
        self.model.eval()

    def predict(self, image):
        image = image.to(self.device)

        with torch.no_grad():
            output = self.model(image)
            prob = torch.sigmoid(output).item()

            label = "Real" if prob > 0.5 else "Fake"

            return label, round(prob, 3)