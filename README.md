# Mushroom Classification using Classical Machine Learning Models

## Overview
This project applies **multiple classical machine learning models** to classify mushrooms as **edible** or **poisonous** based on their attributes.  
It was developed as part of the *Graduate Machine Learning Assignment 2025* and includes:
- Data preprocessing & feature engineering
- Training multiple supervised and unsupervised models
- Performance evaluation with various metrics
- A simple **Flask web application** to demonstrate predictions interactively

---

## Project Structure
```
mushroom_classification/
│── Mushroom_BekirBozoklar-Copy1.html   # Jupyter Notebook (HTML) - full code & report
│── app.py                              # Flask app for model demonstration
│── diagram.png                         # Workflow diagram
│── app_screenshot.png                  # Web app screenshot
│── README.md                           # Project documentation
```

---

## Dataset
- **Source:** Public mushroom dataset from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Mushroom)
- **Size:** 8124 rows, 22 categorical attributes
- **Target Variable:** `class` — edible (`e`) or poisonous (`p`)
- **Preprocessing:**
  - Missing values handled
  - All categorical variables encoded using One-Hot Encoding
  - Dataset normalized for models sensitive to feature scaling

<img width="1676" height="843" alt="Ekran Resmi 2025-08-12 16 56 26" src="https://github.com/user-attachments/assets/3e135f1c-39ae-4584-ae51-f9c88b1c28b2" />


---

## Models Implemented
### Supervised Learning
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Naive Bayes
- Support Vector Machine (SVM)
- Gradient Boosting Classifier
- AdaBoost
- Extra Trees Classifier
- Multi-layer Perceptron (MLP)

### Unsupervised Learning (Clustering)
- K-Means
- Agglomerative Clustering
- DBSCAN
- Mean Shift
- Gaussian Mixture Models

---

## Results Summary
| Model                  | Accuracy | Precision | Recall | F1-score |
|------------------------|----------|-----------|--------|----------|
| Random Forest          | 1.000    | 1.000     | 1.000  | 1.000    |
| Gradient Boosting      | 1.000    | 1.000     | 1.000  | 1.000    |
| Decision Tree          | 1.000    | 1.000     | 1.000  | 1.000    |
| Logistic Regression    | 0.999    | 0.999     | 0.999  | 0.999    |
| SVM                    | 0.999    | 0.999     | 0.999  | 0.999    |
| KNN                    | 0.999    | 0.999     | 0.999  | 0.999    |
| Naive Bayes            | 0.948    | 0.948     | 0.948  | 0.948    |

Most models achieved near-perfect classification due to dataset characteristics.

---


## 🌐 Web Application
A **Flask** app (`app.py`) was built to demonstrate mushroom classification interactively.  
Users can input mushroom attributes and get an **"Edible"** or **"Poisonous"** prediction in real-time.

**Example Screenshot:**
<img width="1728" height="1117" alt="3" src="https://github.com/user-attachments/assets/8dcf33e1-bdef-4e4a-a6fb-c29e36275e20" />


---

## Requirements
```txt
pandas
numpy
scikit-learn
flask
matplotlib
seaborn
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## How to Run Locally

### Run the Jupyter Notebook
Open `Mushroom_BekirBozoklar-Copy1.html` or the original `.ipynb` file to see the analysis and model training steps.

### Start the Flask App
```bash
python app.py
```
Visit **http://127.0.0.1:5000/** in your browser.

---

## Conclusion
- **Random Forest** and **Gradient Boosting** achieved perfect classification.
- Dataset is highly separable due to clear feature-target correlations.
- Flask app provides an easy interface for real-time classification.

---

## Author
**Bekir Bozoklar — MSc Software Engineering **
