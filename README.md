# 📱 SMS Spam Classifier

A machine learning web application that classifies SMS messages as **Spam** or **Ham** using Natural Language Processing and Machine Learning.

---

## 🚀 Live Demo

🔗 **Live Application:** Add your Streamlit deployment URL here after deployment.

---

## 📌 Project Overview

Spam messages are unwanted messages that may contain fraudulent offers, advertisements, or misleading information.

This project uses a Machine Learning classification model to automatically identify whether an SMS message is:

- 🚨 **Spam** — potentially unwanted or suspicious
- ✅ **Ham** — legitimate message

The trained model is integrated into a Streamlit web application for real-time predictions.

---

## 🧠 Machine Learning Approach

The project uses Natural Language Processing and Machine Learning to classify SMS messages as Spam or Ham.

---

## 🔄 Prediction Pipeline

The complete prediction process is:

**SMS Message**  
↓  
**Text Preprocessing**  
↓  
**TF-IDF Vectorization**  
↓  
**3000 Features**  
↓  
**Multinomial Naive Bayes**  
↓  
**Spam / Ham Prediction**

---

## 📝 Text Representation

TF-IDF (Term Frequency–Inverse Document Frequency) is used to convert SMS text into numerical features that can be processed by the machine learning model.

The final vectorizer uses 3000 features

---

## 🤖 Classification Model

The final model used for deployment is:

Multinomial Naive Bayes

The model was selected based on its performance for the SMS classification task.

---

## 📊 Model Performance

The final model achieved the following results on the test set:

Metric	Score
Accuracy	98%
Spam Precision	96%
Spam Recall	91%
Spam F1 Score	94%

These metrics represent the model's performance on the evaluation dataset. They do not guarantee the same accuracy for every new SMS message.

---

## 🛠️ Technologies Used
- 🐍 Python
- 🤖 Scikit-learn
- 🌐 Streamlit
- 📊 TF-IDF Vectorization
- 🧠 Multinomial Naive Bayes
- 💾 Pickle

---

## ✨ Features
- 📱 SMS spam detection
- 🔍 Real-time message analysis
- 🚨 Spam/Ham classification
- 📊 Prediction probability
- 🧹 Clear message functionality
- 🌐 Web-based interface using Streamlit

---

## 📂 Project Structure

```text
SMS-Spam-Classifier/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
├── SMS_Spam_Classifier.ipynb
└── email.csv
```

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Yash1014/SMS-Spam-Classifier.git
```

### 2. Navigate to the project directory

```bash
cd SMS-Spam-Classifier
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```
---

## 🧪 Example
###🚨 Spam

Congratulations! You have won a free prize. Reply YES to claim now!

###✅ Ham

Hey, are you coming to college tomorrow?
