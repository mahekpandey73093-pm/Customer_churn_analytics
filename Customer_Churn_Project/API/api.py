from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predicts whether a customer will churn",
    version="1.0"
)

model = joblib.load("churn_model.pkl")

class CustomerData(BaseModel):
    CreditScore: int
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float

@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API Running"}

@app.post("/predict")
def predict(data: CustomerData):

    input_data = pd.DataFrame([{
        "CreditScore": data.CreditScore,
        "Age": data.Age,
        "Tenure": data.Tenure,
        "Balance": data.Balance,
        "NumOfProducts": data.NumOfProducts,
        "HasCrCard": data.HasCrCard,
        "IsActiveMember": data.IsActiveMember,
        "EstimatedSalary": data.EstimatedSalary
    }])

    prediction = model.predict(input_data)[0]

    return {
        "prediction": int(prediction),
        "result": "Customer Will Churn" if prediction == 1 else "Customer Will Stay"
    }