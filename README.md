
# 🛼 Skating Athletes Analysis / Smart-Skate System implementation / Game + Interactive Floor Projection Visualization

This project uses real biometric data to assess and classify the **performance** and **risk levels** of roller skating/blading athletes. It leverages machine learning models to categorize individuals based on:

- **Heart Rate**
- **SpO₂ (Blood Oxygen Saturation)**
- **Session Duration (in minutes)**
- **Biometrics**: Age, Height, and Weight

## 📁 Project Structure

- `expanded_simulated_fitness_data.csv`: Multi-modal dataset simulating heart rate, SpO₂, and activity durations.
- `Skroovate_Model.ipynb`: Main notebook using real data, replacing synthetic inputs.
  - Includes performance and risk level classification.
  - Introduces 10% noise to both labels for realism.

## 🧠 ML Models Used

- RandomForestClassifier for both performance and risk classification.
- Labels are based on custom threshold logic derived from domain knowledge.

## 🚀 Getting Started

1. Clone the repo.
2. Open the Jupyter or Colab notebooks.
3. Upload Skroovate_Model.ipynb` and inside it `expanded_simulated_fitness_data.csv` to run the code.
4. Train and evaluate the model or export for deployment.

## ✅ Author Notes

This repo is designed for experimentation, athlete monitoring, and educational purposes in human performance analysis. Data are inspired by real physiological datasets but are simulated to avoid licensing conflicts.

---

## 📧 Author

**Amgad Thabit**  
Student Researcher | AI & Software Engineer  
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/amgad-thabit/) or via GitHub

**Ghala Bassyoni**  
Student Researcher | AI & Software Engineer  
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/ghala-bassyoni-81a847332) or via GitHub (https://github.com/Ghalapples)

