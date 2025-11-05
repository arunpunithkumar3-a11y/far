from pydantic import BaseModel, Field,field_validator
from typing import Annotated
import pandas as pd
import pickle


class Userinput1(BaseModel):
    type_of_crop: Annotated[str, Field(..., description="Type of crop to grow")]
    soil: Annotated[str, Field(..., description="Type of soil")]
    season: Annotated[str, Field(..., description="Season to grow the crop")]
    water_source: Annotated[str, Field(..., description="Source of water")]
    crop_production: Annotated[float,Field(..., gt=0, description="Crop duration or production (days)")]
    temp: Annotated[float, Field(..., gt=0, description="Temperature of the area (°C)")]
    relative_humidity: Annotated[float, Field(..., gt=0, description="Relative humidity of the area (%)")]
    
    @field_validator("soil")
    @classmethod
    def soi(cls, v:str) -> str:
        v = v.strip().title()
        return v
class Userinput2(BaseModel):   
    nitrogen:Annotated[float,Field(...,description="nitrogen content in the soil")]
    phosphorous:Annotated[float,Field(...,description="phosphorous content in the soil")]
    potassium:Annotated[float,Field(...,description="potassium content in the soil")]    
    carbon:Annotated[float,Field(...,description="carbon content in the soil")]
    soil:Annotated[str,Field(...,description="type of soil")]
    crop:Annotated[str,Field(...,description="type of crop")]

class Userinput3(BaseModel):
    soil_moisture:Annotated[float,Field(...,description="moisture of soil")]
    soil_temp:Annotated[float,Field(...,description="temperature of the soil")]
    soil_ph:Annotated[float,Field(...,gt=0,lt=14,description="ph of the soil")]
    nitrogen_level:Annotated[float,Field(...,description="nitrogen")]
    phos_level:Annotated[float,Field(...,description="phosphorous level")]
    potass:Annotated[float,Field(...,description="k level")]