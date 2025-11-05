from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from user_input import Userinput1, Userinput2, Userinput3
from predict import predict_output, predict_outpu1, predict_output3
from typing import Annotated
import pandas as pd
import uvicorn
import os

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Farm AI API working"}

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "model_loaded": "true"
    }

@app.post("/predict_crop")
def predict_premium(data: Userinput1):
    user_input = {
        "TYPE_OF_CROP": data.type_of_crop,
        "SOIL": data.soil,
        "SEASON": data.season,
        "WATER_SOURCE": data.water_source,
        "CROPDURATION": data.crop_production,
        "TEMP": data.temp,
        "RELATIVE_HUMIDITY": data.relative_humidity
    }
    prediction = predict_output(user_input)
    return JSONResponse(status_code=200, content={"prediction": prediction})

@app.post("/predict_fert")
def predict_fert(data: Userinput2):
    user_input1 = {
        "Nitrogen": data.nitrogen,
        "Phosphorous": data.phosphorous,
        "Potassium": data.potassium,
        "Carbon": data.carbon,
        "Soil": data.soil,
        "Crop": data.crop
    }
    prediction1 = predict_outpu1(user_input1)
    return JSONResponse(status_code=200, content={"prediction1": prediction1})

@app.post("/predict_health")
def predict_health(data: Userinput3):
    user_input2 = {
        "Soil_Moisture": data.soil_moisture,
        "Soil_Temperature": data.soil_temp,
        "Soil_pH": data.soil_ph,
        "Nitrogen_Level": data.nitrogen_level,
        "Phosphorus_Level": data.phos_level,
        "Potassium_Level": data.potass
    }
    prediction2 = predict_output3(user_input2)
    return JSONResponse(status_code=200, content={"prediction3": str(prediction2[0])})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
