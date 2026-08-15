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

The project follows this pipeline:

```text
SMS Message
     ↓
Text Preprocessing
     ↓
TF-IDF Vectorization
     ↓
3000 Features
     ↓
Multinomial Naive Bayes
     ↓
Spam / Ham Prediction
