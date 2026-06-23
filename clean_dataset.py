from PIL import Image
import os

dataset_path = "PetImages"

for folder in ["Cat", "Dog"]:

    folder_path = os.path.join(dataset_path, folder)

    for file in os.listdir(folder_path):

        image_path = os.path.join(folder_path, file)

        try:
            img = Image.open(image_path)
            img.verify()

        except:
            print("Deleting:", image_path)
            os.remove(image_path)

print("Dataset cleaned")