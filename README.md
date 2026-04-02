# 🎓 Student Performance Prediction App

A Machine Learning web application that predicts student exam scores based on study habits, lifestyle, and academic factors.

---

## 🚀 Project Overview

This project combines **data science + web development**:

- Built a complete ML pipeline from raw data
- Applied feature engineering and preprocessing
- Trained an optimized XGBoost model
- Deployed a Flask web app for real-time predictions

---

## 🧠 Machine Learning Pipeline

### 📊 Data Processing
- Handled missing values
- Removed duplicates
- Cleaned categorical values (lowercase, strip)
- Outlier detection and clipping

### ⚙️ Feature Engineering
Created new features such as:
- `effort_score` = study_hours × attendance
- `sleep_impact` = sleep_hours × sleep_quality
- `stress_level`
- `digital_usage`
- `study_sleep_ratio`
- `attendance_sleep`
- `sleep_balance`
- Age and attendance grouping

### 🔄 Encoding
- Ordinal encoding for:
  - sleep_quality
  - facility_rating
  - exam_difficulty
- One-hot encoding for categorical variables

### 📏 Scaling
- StandardScaler applied to features

---

## 🤖 Model

- **XGBoost Regressor**
- Hyperparameter tuning using RandomizedSearchCV
- Evaluation metrics:
  - RMSE
  - MAE
  - R² Score

---

## 🌐 Web Application

Built with **Flask**

### Features:
- User-friendly input form
- Real-time prediction
- Manual preprocessing replicated from training
- Dynamic feature alignment using saved feature names

---

## 📥 Input Features

- Age  
- Study Hours  
- Class Attendance  
- Sleep Hours  
- Sleep Quality  
- Facility Rating  
- Exam Difficulty  
- Gender  
- Course  
- Study Method  
- Internet Access  

---

## 🎯 Output

- Predicted **Exam Score (0–100)**

---

## 🗂️ Project Structure
student-ml-app/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── features.pkl
├── student_final.ipynb
├── requirements.txt
├── README.md
└── templates/
└── index.html


---

## ⚙️ Installation & Usage

### 1️⃣ Clone repository

```bash
git clone https://github.com/souhahamami-ship-it/student-ml-app.git
cd student-ml-app

### 2️⃣ Install dependencies
pip install -r requirements.txt

### 3️⃣ Run the app
python app.py

### 4️⃣ Open in browser
http://127.0.0.1:5000/