from fastapi import FastAPI, Request
from pydantic import BaseModel
import pandas as pd
from src.predict import predict

app = FastAPI()

class InputData(BaseModel):
    features: dict

@app.post("/predict")
def make_prediction(input: InputData):
    df = pd.DataFrame([input.features])
    prediction = predict(df)
    return {"prediction": prediction.tolist()}
