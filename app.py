import io
from datetime import datetime
from typing import Optional
import numpy as np
import PIL.Image as Image
from fastapi import FastAPI, File, UploadFile, HTTPException
import tensorflow as tf
import tensorflow_hub as hub
from predictor import AnimalDetector
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sklearn.decomposition import PCA
from sqlmodel import Field, SQLModel, create_engine, Session
from information import AnimalTour
from localizador import Localizador

class TextEntry(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str
    nombre_cientifico: str
    habitat: str
    alimentacion: str
    fecha: str
    latitud: str
    longitud: str


DATABASE_URL = "sqlite:///db.sqlite3"
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)

app = FastAPI(title="Deteccion de animales y descripcion de caracteristicas")
animal_predictor = AnimalDetector()
information_guide = AnimalTour()
localizador_ubi = Localizador()


@app.get("/status")
def root():
    return {"message": "Bienvenido al detector de Animales", 
            "creador": "Miguel Molina Flores && Richar Rojas Aguilar", 
            "load": "Creando y cargando el modelo",
            "status": "OK"}

@app.post("/predict_animal")
def predict_animal_endpoint(file: UploadFile = File(...)):
    try:
        with open("temp_image.jpg", "wb") as temp_image:
            temp_image.write(file.file.read())

        prediction = animal_predictor.predict_animal("temp_image.jpg")
        result = prediction[0]
        information = information_guide.obtener_información(result['name'])
        coordenadas = localizador_ubi.obtener_coordenadas_actual() 

        if result['etiqueta'].item() in range(1,398):
            prediccion = {
                "etiqueta": result['etiqueta'].item(),
                "nombre": result['name'],
                "nombre_cientifico": information["nombre_cientifico"],
                "habitat": information["habitat"],
                "alimentacion": information["alimentacion"],
                "Fecha": result['date'],
                "Latitud": str(coordenadas[0]),
                "Longitud": str(coordenadas[1])
            }

            db_text = TextEntry(
                nombre=result['name'],
                nombre_cientifico=information["nombre_cientifico"],
                habitat=information["habitat"],
                alimentacion=information["alimentacion"],
                fecha=str(result['date'])

            )

            with Session(engine) as session:
                session.add(db_text)
                session.commit()

        return prediccion
    except Exception as e:
        return {"error": str(e)}
