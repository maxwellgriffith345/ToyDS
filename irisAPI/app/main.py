from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

class InputData(BaseModel):
    SepalLen: float
    SepalWid: float
    PetalLen: float
    PetalWid: float

app = FastAPI(title = "Iris Prediction")

model_path = os.path.join("model", "irisdecisiontree.joblib")

with open(model_path, 'rb') as mfile:
    model = joblib.load(mfile)

@app.post("/predict")
async def predict(data: InputData):
    input_features = [[data.SepalLen, data.SepalWid,
        data.PetalLen, data.PetalWid]]

    prediction = model.predict(input_features)
    #scikit learn returns numpy data types as predictions if they are values
    #FastAPI/JSON only handles python native data types so we need to convert
    #the predicted value

    return {"Predicted Iris": int(prediction[0])}

@app.get("/hello")
async def root():
    return {"message": "hello world XD"}
