from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))
feature_names = pickle.load(open("features.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        import pandas as pd

        data = {
            "age": float(request.form["age"]),
            "study_hours": float(request.form["study_hours"]),
            "class_attendance": float(request.form["class_attendance"]),
            "internet_access": request.form["internet_access"],
            "sleep_hours": float(request.form["sleep_hours"]),
            "sleep_quality": request.form["sleep_quality"],
            "facility_rating": request.form["facility_rating"],
            "exam_difficulty": request.form["exam_difficulty"],
            "gender": request.form["gender"],
            "course": request.form["course"],
            "study_method": request.form["study_method"]
        }

        df = pd.DataFrame([data])

        # SAME preprocessing
        df['sleep_quality'] = df['sleep_quality'].map({'poor':0,'average':1,'good':2})
        df['facility_rating'] = df['facility_rating'].map({'low':0,'medium':1,'high':2})
        df['exam_difficulty'] = df['exam_difficulty'].map({'easy':0,'moderate':1,'hard':2})
        df['internet_access'] = df['internet_access'].map({'no':0,'yes':1})

        df['effort_score'] = df['study_hours'] * df['class_attendance']
        df['sleep_impact'] = df['sleep_hours'] * df['sleep_quality']
        df['stress_level'] = df['exam_difficulty'] * df['study_hours']
        df['digital_usage'] = df['internet_access'] * df['study_hours']
        df['study_sleep_ratio'] = df['study_hours'] / (df['sleep_hours'] + 1)
        df['attendance_sleep'] = df['class_attendance'] * df['sleep_quality']
        df['sleep_balance'] = df['sleep_hours'] * (df['sleep_quality'] == 2).astype(int)

        df['age_group'] = pd.cut(df['age'], bins=[0,18,25,40,100], labels=[0,1,2,3])
        df['attendance_level'] = pd.cut(df['class_attendance'], bins=[0,60,80,100], labels=[0,1,2])

        df = pd.get_dummies(df, drop_first=True)

        # ALIGN
        df = df.reindex(columns=feature_names, fill_value=0)

        # SCALE
        df = scaler.transform(df)

        prediction = model.predict(df)[0]
        if prediction >= 85:
            level = "Excellent 🟢"
        elif prediction >= 70:
            level = "Good 🟡"
        else:
            level = "Needs Improvement 🔴"

        prediction_text = f"🎯 Score: {round(prediction,2)} ({level})"

        return render_template("index.html", prediction_text=prediction_text)

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")
if __name__ == "__main__":
    app.run(debug=True)        