import openai
import json
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

client = openai.OpenAI(api_key=api_key)

class AnimalTour:
    def obtener_información(self, nombre_animal):
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un biólogo con amplios conocimientos en animales de toda clase. Conoces sobre su alimentación, sus hábitats, sus nombres científicos y más."},
            {"role": "user", "content": f'Devuelve un JSON en español con los siguientes datos de "{nombre_animal}".'},
            {"role": "assistant", "content": f'"{nombre_animal}": \n\n{{\n  "nombre_animal": "{nombre_animal}",\n  "nombre_cientifico": "Nombre científico de {nombre_animal}",\n  "habitat": "Habitat de {nombre_animal}",\n  "alimentacion": "Alimentación de {nombre_animal}"\n}}'},
            {"role": "user", "content": "Devuelveme solo el JSON, sin ningun texto ante o despues de los corchetes que tiene el JSON"}
        ],
        max_tokens=500,
        temperature=0.3
        )
        respuesta = response.choices[0].message.content
        obejto_json = json.loads(respuesta)

        return obejto_json