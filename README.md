# WildQuest: Explorando la Fauna con Tecnología 🦈

Bienvenido a WildQuest, la aplicación que te sumerge en el fascinante mundo de la fauna utilizando tecnología de punta. WildQuest te permite explorar y descubrir diferentes especies animales a través de la simplicidad de cargar imágenes. Cada componente de la aplicación, desde el predictor de animales hasta el módulo de información, está diseñado para proporcionar una experiencia intuitiva y educativa sobre el reino animal.

## Características Principales 🐼

### 1. Interfaz de Usuario (FastAPI)
- **Descripción:** La interfaz de usuario proporciona puntos de entrada claros a través de endpoints simples.
- **Funcionalidad:** Permite a los usuarios verificar el estado de la aplicación y realizar predicciones sobre animales cargando imágenes.

### 2. Predictor de Animales (AnimalDetector)
- **Descripción:** Utiliza un modelo preentrenado (`mobilenet_v2`) de TensorFlow Hub para predecir el tipo de animal en una imagen.
- **Funcionalidad:** Realiza predicciones y devuelve información básica sobre el animal detectado, como su nombre y etiqueta.

### 3. Módulo de Información (AnimalTour)
- **Descripción:** Utiliza OpenAI's GPT-3.5 para generar información detallada sobre el animal detectado.
- **Funcionalidad:** Crea respuestas en formato JSON con datos científicos sobre el nombre científico, hábitat y alimentación del animal.

## Flujo de Funcionamiento 🐅
El usuario envía una solicitud a través de la interfaz de usuario para predecir el animal en una imagen (/predict_animal endpoint).

La interfaz de usuario guarda temporalmente la imagen y utiliza el predictor de animales para realizar la predicción.

El predictor devuelve una predicción básica sobre el animal detectado, incluyendo el nombre y la etiqueta.

La interfaz de usuario utiliza el nombre del animal para solicitar información adicional al módulo de información.

El módulo de información utiliza GPT-3.5 para generar un JSON con datos científicos sobre el animal (nombre científico, hábitat, alimentación).

La interfaz de usuario devuelve la predicción y la información detallada al usuario.

## Resumen del Modelo 🐲
Entrada: Imagen de un animal.
Proceso:
Predicción básica del animal utilizando un modelo de clasificación.
Generación de información detallada utilizando GPT-3.5.
Salida: Respuesta al usuario con la predicción y detalles sobre el animal.

## Colaboradores 😎
[Miguel Molina](https://github.com/Mickysaurio-rex)

[Richard Rojas](https://github.com/RichyRed)
