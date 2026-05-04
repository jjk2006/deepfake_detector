# 🔍 Deepfake Detection System

An AI-based web application that detects whether an image is **Real** or **Fake (Deepfake)** using a deep learning model (EfficientNet).

---

## 🚀 Features
- Upload an image and get prediction instantly
- Classifies image as **Real** or **Fake**
- Displays **confidence score**
- Clean and interactive **Flask web UI**

---

## 🧠 Model Details
- Architecture: EfficientNet-B0
- Framework: PyTorch
- Loss Function: BCEWithLogitsLoss
- Trained on: Real vs Fake Faces dataset (Kaggle)

---

## 📁 Project Structure
```

deepfake_detector/
│
├── app.py
├── model.py
├── utils.py
├── requirements.txt
├── templates/
├── static/

````

---

## ⚙️ Installation & Run

```bash
# Clone the repo
git clone https://github.com/your-username/deepfake_detector.git

# Go to project folder
cd deepfake_detector

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py
````

---

## 📥 Model Download

⚠️ Model file is not included in repo due to size.

Download here:
👉 https://drive.google.com/file/d/1paj1lly4oqRKPQB2yzlOxnot6UE8XsW4/view?usp=sharing
Place the file inside:

```
model/Nakli_Image_detector.pth
```

---

## 🧪 How it works

1. User uploads an image
2. Image is preprocessed
3. Model predicts Real/Fake
4. Result + confidence displayed

---

## 🎯 Use Cases

* Detect fake images / deepfakes
* Prevent misinformation
* Social media content verification
* Cybersecurity applications

---

## ⚠️ Limitations

* Model may fail on unseen manipulation styles
* Performance depends on training data diversity

---

## 🔮 Future Improvements

* Support video deepfake detection
* Improve accuracy with multi-dataset training
* Deploy on cloud

---

## 👨‍💻 Author

* JIBRAN KHOT
* COMMUNICATION ENGAGEMENT PROJECT(CEP)

---

## ⭐ If you like this project, give it a star!



