# Skroovate_model

# 🛹 Roller Skate Player Classification using Vital Signs (AI Model)

This project simulates a classification model that analyzes professional roller skate players based on synthetic biometric data. It uses machine learning to determine **performance levels** and **risk levels** from vital signs such as:

- Heart Rate (BPM)
- SpO2 (Oxygen Saturation %)
- Time Spent Skating (minutes)

---

## 🧠 Project Objective

To build a classification model that can:
- Classify player **performance level** as: Beginner, Intermediate, Advanced, or Elite.
- Assess player **risk level** as: Low Risk, Mid Risk, or High Risk.
- Use synthetic data for training and evaluation.
- Simulate realistic challenges by including outliers in the dataset.

---

## 🛠️ How It Works

1. **Synthetic Data Generation**  
   - Creates 100,000 fake samples for:
     - Heart Rate: values between 50–200 BPM
     - SpO2: values between 85–101%
     - Time Skating: values between 1–45 minutes
   - Injects 10,000 *outliers* manually (e.g. HR=210 or SpO2=70)

2. **Labeling the Data**  
   - **Performance Level** is determined based on a combination of HR, SpO2, and Time:
     - `Beginner`, `Intermediate`, `Advanced`, `Elite`
   - **Risk Level** is labeled based on critical thresholds:
     - `High Risk`, `Mid Risk`, `Low Risk`

3. **Preprocessing**  
   - Converts string labels to numeric values using `map()`

4. **Model Training**  
   - Uses `RandomForestClassifier` with low complexity to avoid perfect accuracy.
   - Splits data into 80% training and 20% testing.
   - Trains the model to predict **performance level** (can be changed to predict risk).

5. **Model Evaluation**  
   - Prints Accuracy Score
   - Generates a full Classification Report (Precision, Recall, F1)
   - Shows examples of predicted vs actual performance levels

---

## 🚀 How to Run (Google Colab)

1. Open [Google Colab](https://colab.research.google.com/)
2. Upload the `.ipynb` or paste the full code from `classification_model.ipynb`
3. Run all cells to:
   - Generate data
   - Train the model
   - Evaluate predictions

---

## 📦 Project Files

- `classification_model.ipynb` → Main Python notebook with full model
- `README.md` → This documentation

---

## 📝 Notes

- This is a simulation using synthetic data.
- Model accuracy may vary depending on random seed.
- Risk and performance labels are **estimated rules**, not medical or athletic standards.

---

## 📧 Author

**Amgad Thabit**  
Student Researcher | AI & Software Developer  
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/amgad-thabit/) or via GitHub

