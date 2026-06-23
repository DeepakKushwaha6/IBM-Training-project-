import torch
import torch.nn as nn
from torchvision import models, transforms

# Class names
classes = ["Cat", "Dog"]

# Load model
model = models.resnet18(weights=None)

model.fc = nn.Linear(
    model.fc.in_features,
    2
)

model.load_state_dict(
    torch.load(
        "model.pth",
        map_location="cpu"
    )
)

model.eval()

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def predict_image(image):

    image = transform(image)

    image = image.unsqueeze(0)

    with torch.no_grad():

        output = model(image)

        probabilities = torch.softmax(
            output,
            dim=1
        )

        confidence, prediction = torch.max(
            probabilities,
            1
        )

    prediction = classes[
        prediction.item()
    ]

    confidence = confidence.item() * 100

    return prediction, confidence

