from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
import pandas as pd
import numpy as np
import joblib
import os
import joblib

# Load model
MODEL_PATH = os.path.join("models", "best_pipeline.joblib")
model = joblib.load(MODEL_PATH)

# Create FastAPI app
app = FastAPI(title="Credit Card Fraud Detection API")

# Request schema
class Transaction(BaseModel):
    Time: float
    Amount: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float

class PredictRequest(BaseModel):
    transactions: List[Transaction] = Field(..., min_items=1)

class PredictResponse(BaseModel):
    predictions: List[int]
    probabilities: List[float]

# Prediction endpoint
@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    records = [t.dict() for t in req.transactions]
    X = pd.DataFrame.from_records(records)
    X['hour'] = (X['Time'] // 3600) % 24
    X['minute'] = (X['Time'] // 60) % 60
    X['log_amount'] = np.log1p(X['Amount'])
    proba = model.predict_proba(X)[:,1]
    preds = (proba >= 0.5).astype(int).tolist()
    return PredictResponse(predictions=preds, probabilities=proba.tolist())
