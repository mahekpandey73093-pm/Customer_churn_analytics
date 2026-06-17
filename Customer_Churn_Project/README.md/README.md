🏦 AI-Powered Customer Churn Intelligence Platform

📌 Project Overview

The AI-Powered Customer Churn Intelligence Platform is a Machine Learning-based solution designed to identify customers who are likely to leave a bank. The project combines predictive analytics, interactive visualizations, and API deployment to help businesses improve customer retention strategies.

This platform enables data-driven decision-making by analyzing customer behavior, identifying churn risks, and providing actionable business insights.

---

🎯 Objectives

* Predict customer churn using Machine Learning.
* Analyze customer demographics and banking behavior.
* Visualize churn patterns through an interactive dashboard.
* Provide business insights for customer retention.
* Deploy prediction services using FastAPI.

---

🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Plotly
* Streamlit
* FastAPI
* Joblib

---

📊 Dataset

Dataset: European Bank Customer Dataset

Key Features:

* Credit Score
* Age
* Tenure
* Balance
* Number of Products
* Has Credit Card
* Active Member Status
* Estimated Salary
* Geography
* Gender

Target Variable:

* Exited (0 = Stay, 1 = Churn)

---

🤖 Machine Learning Model

Model Used:

* Random Forest Classifier

Model Workflow:

1. Data Cleaning
2. Feature Engineering
3. Data Preprocessing
4. Model Training
5. Model Evaluation
6. Model Saving using Joblib

Saved Model:

* churn_model.pkl

---

📈 Dashboard Features
Executive KPIs

* Total Customers
* Churn Rate
* Average Balance
* High Value Customers
* Revenue Risk Analysis

Interactive Visualizations

* Customer Churn Distribution
* Age vs Churn Analysis
* Geography-wise Churn Rate
* Balance vs Churn Analysis
* High Value Customer Analysis

AI Prediction Module

Users can enter customer details and receive:

* Churn Prediction
* Churn Probability
* Risk Classification
* Downloadable Prediction Report

🚀 FastAPI Integration

API Features:

* REST API Endpoint
* Real-Time Churn Prediction
* JSON Response Format
* Interactive Swagger Documentation

Endpoints:

GET /

POST /predict

Swagger Documentation:

http://127.0.0.1:8000/docs

---

📂 Project Structure

AI-Customer-Churn-Intelligence-Platform/

├── Dashboard/

│   ├── app.py

│   ├── churn_model.pkl

│   ├── European_Bank.csv

│   └── requirements.txt

├── API/

│   └── api.py

├── Notebook/

│   └── churn_analysis.ipynb

├── Report/

│   └── Customer_Churn_Project_Report.pdf

├── Screenshots/

│   ├── Dashboard_Home.png

│   ├── Analytics_Page.png

│   ├── Prediction_Result.png

│   └── API_Docs.png

└── README.md

---

▶️ Run Dashboard

```bash
streamlit run app.py
```

▶️ Run API

```bash
uvicorn api:app --reload
```

---

💡 Business Impact

* Improves customer retention strategy.
* Identifies high-risk customers proactively.
* Reduces revenue loss due to customer churn.
* Supports data-driven business decisions.

---
👩‍💻 Author

Mahek Pandey

BCA with AI

V.T. Poddar College

Machine Learning | Data Analytics | Artificial Intelligence
