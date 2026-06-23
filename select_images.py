import os
import shutil
import random

os.makedirs("PetImages_Small/Cat", exist_ok=True)
os.makedirs("PetImages_Small/Dog", exist_ok=True)

for category in ["Cat", "Dog"]:

    source = f"PetImages/{category}"

    files = os.listdir(source)

    files = random.sample(files, 500)

    for file in files:
        try:
            shutil.copy(
                os.path.join(source, file),
                os.path.join("PetImages_Small", category, file)
            )
        except:
            pass

print("Done")