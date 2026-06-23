# Cat vs Dog Image Classifier

A simple Deep Learning project that classifies images as **Cat** or **Dog** using **Transfer Learning** with ResNet18 and PyTorch.

The project also includes a **Streamlit web application** where users can upload an image and get predictions.

---

## Project Features

* Cat vs Dog Image Classification
* Transfer Learning using ResNet18
* Image Upload using Streamlit
* Confidence Score Display
* Easy-to-use Web Interface
* Beginner-Friendly Project

---

## Technologies Used

* Python
* PyTorch
* Torchvision
* Streamlit
* PIL (Python Imaging Library)

---

## Dataset

Dataset Used: **PetImages Dataset**

Classes:

* Cat
* Dog

Dataset Structure:

```text
PetImages/
│
├── Cat/
│
└── Dog/
```

---

## Project Structure

```text
Cat-Dog-Classifier/
│
├── PetImages/
│   ├── Cat/
│   └── Dog/
│
├── train.py
├── predict.py
├── app.py
├── model.pth
├── requirements.txt
└── README.md
```

---

## How the Project Works

### Step 1: Load Dataset

The PetImages dataset is loaded using Torchvision.

### Step 2: Image Preprocessing

Images are:

* Resized to 224 × 224
* Converted to Tensor
* Augmented using random flip

### Step 3: Transfer Learning

A pretrained ResNet18 model is used.

The final classification layer is modified to classify:

* Cat
* Dog

### Step 4: Model Training

The model is trained using:

* CrossEntropyLoss
* Adam Optimizer

### Step 5: Save Model

After training, the model is saved as:

```text
model.pth
```

### Step 6: Prediction

The user uploads an image.

The model predicts:

* Cat
* Dog

and displays the confidence score.

### Step 7: Deployment

The application is deployed using Streamlit.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/cat-dog-classifier.git
```

Move to project folder:

```bash
cd cat-dog-classifier
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Train the Model

```bash
python train.py
```

This will create:

```text
model.pth
```

---

## Run the Application

```bash
python -m streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Example Output

### Cat Image

```text
Prediction: Cat
Confidence: 97.5%
```

### Dog Image

```text
Prediction: Dog
Confidence: 96.8%
```

---

## Limitations

The model is trained only on:

* Cat Images
* Dog Images

It may not correctly classify objects such as:

* Cars
* Chairs
* Mobile Phones
* Laptops

---

## Future Improvements

* Add more animal classes
* Improve accuracy
* Add Grad-CAM visualization
* Deploy online
* Add unknown object detection

---

## Learning Outcomes

Through this project I learned:

* Image Classification
* Transfer Learning
* Deep Learning using PyTorch
* Computer Vision Basics
* Model Deployment using Streamlit

---

## Author

**Deepak K Kushwaha**

B.Tech CSE (AI/ML)

IMSEC, AKTU

```
```
