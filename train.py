import torch
import torch.nn as nn
from torchvision import datasets
from torchvision import transforms
from torchvision import models
from torch.utils.data import DataLoader

# Image preprocessing

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor()
])

# Load dataset

train_dataset = datasets.ImageFolder(
    "PetImages",
    transform=transform
)

print(train_dataset.class_to_idx)

train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True
)

# Load pretrained model

model = models.resnet18(weights="DEFAULT")

# Freeze pretrained layers

for param in model.parameters():
    param.requires_grad = False

# Change final layer

model.fc = nn.Linear(
    model.fc.in_features,
    2
)

# Device

device = torch.device(
    "cuda" if torch.cuda.is_available()
    else "cpu"
)

model = model.to(device)

# Loss and optimizer

loss_function = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(
    model.fc.parameters(),
    lr=0.001
)

# Training

epochs = 10

for epoch in range(epochs):

    total_loss = 0

    correct = 0
    total = 0

    for images, labels in train_loader:

        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)

        loss = loss_function(
            outputs,
            labels
        )

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

        _, predicted = torch.max(
            outputs,
            1
        )

        total += labels.size(0)

        correct += (
            predicted == labels
        ).sum().item()

    accuracy = (
        correct / total
    ) * 100

    print(
        "Epoch:",
        epoch + 1,
        "Loss:",
        round(total_loss, 2),
        "Accuracy:",
        round(accuracy, 2),
        "%"
    )

torch.save(
    model.state_dict(),
    "model.pth"
)

print("Training Complete")

