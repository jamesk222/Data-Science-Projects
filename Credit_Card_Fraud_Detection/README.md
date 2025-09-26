
# Credit Card Fraud Detection 

##  Project Summary

This project builds and deploys a **Machine Learning system for detecting fraudulent credit card transactions**.
It combines **data exploration, feature engineering, model training, and a FastAPI service inside Docker**, ready for real-world use.

The goal: help banks and fintech companies **reduce financial losses** and **increase trust** by catching fraud before it happens.


##  Business Value

* Fraud costs the global economy **billions of dollars every year**.
* Even a **1% improvement** in fraud detection accuracy can save companies millions.
* By deploying this solution, businesses can:

  * Protect customers from financial harm.
  * Maintain trust and reputation.
  * Optimize manual fraud review teams by flagging only the most suspicious cases.

---

## What We Did

1. **Exploratory Data Analysis (EDA)**

   * Visualized transaction patterns, fraud ratios, and correlations.
   * Identified strong signals in anonymized PCA components.

2. **Preprocessing & Feature Engineering**

   * Handled class imbalance with **SMOTE**.
   * Engineered features: transaction **hour, minute, log\_amount**.

3. **Modeling & Evaluation**

   * Tested **Logistic Regression, Random Forest, XGBoost**.
   * Applied **cross-validation and hyperparameter tuning**.
   * Used **ROC-AUC, Precision-Recall AUC, Confusion Matrix** for evaluation.

4. **Deployment**

   * Packaged the best pipeline into **FastAPI**.
   * Containerized using **Docker** for easy portability.
   * Built an endpoint `/predict` that accepts JSON and returns predictions + probabilities.

---

##  Results

* **Logistic Regression (baseline)**: Solid, interpretable, but limited.
* **Random Forest**: Higher recall, better fraud detection but more false positives.
* **XGBoost (final choice)**: Best balance of precision + recall, with **ROC-AUC > 0.98** and strong PR AUC.

 Final model: **XGBoost in a production-ready pipeline**.

---

##  Reproduction Steps

### 1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/credit-card-fraud-detection.git
cd credit-card-fraud-detection
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the API locally

```bash
uvicorn app:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

### 5️⃣ Run inside Docker

```bash
docker build -t cc-fraud-api .
docker run -p 8000:8000 cc-fraud-api
```

### 6️⃣ Test the API

```python
import requests

url = "http://localhost:8000/predict"
payload = {"transactions": [{
  "Time": 10000.0, "Amount": 50.0,
  "V1": -1.0, "V2": 0.5, "V3": 0.1, "V4": -0.1, "V5": 0.0,
  "V6": 0.0, "V7": 0.1, "V8": -0.2, "V9": 0.05, "V10": 0.0,
  "V11": 0.0, "V12": 0.0, "V13": 0.0, "V14": 0.0, "V15": 0.0,
  "V16": 0.0, "V17": 0.0, "V18": 0.0, "V19": 0.0, "V20": 0.0,
  "V21": 0.0, "V22": 0.0, "V23": 0.0, "V24": 0.0, "V25": 0.0,
  "V26": 0.0, "V27": 0.0, "V28": 0.0
}]}

print(requests.post(url, json=payload).json())


##  Achievements

* Built **end-to-end ML pipeline**: EDA → Feature Engineering → Modeling → Deployment.
* Achieved **high ROC-AUC & PR AUC with XGBoost**.
* Deployed production-ready **FastAPI + Dockerized service**.
* Showcased ability to **translate data science into real business value**.




