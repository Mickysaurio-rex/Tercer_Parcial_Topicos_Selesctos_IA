# WildQuest: Explorando la Fauna con Tecnología

Bienvenido a WildQuest, la aplicación que te sumerge en el fascinante mundo de la fauna utilizando tecnología de punta. WildQuest te permite explorar y descubrir diferentes especies animales a través de la simplicidad de cargar imágenes. Cada componente de la aplicación, desde el predictor de animales hasta el módulo de información, está diseñado para proporcionar una experiencia intuitiva y educativa sobre el reino animal.

## Características Principales

### 1. Interfaz de Usuario (FastAPI)
- **Descripción:** La interfaz de usuario proporciona puntos de entrada claros a través de endpoints simples.
- **Funcionalidad:** Permite a los usuarios verificar el estado de la aplicación y realizar predicciones sobre animales cargando imágenes.

### 2. Predictor de Animales (AnimalDetector)
- **Descripción:** Utiliza un modelo preentrenado (`mobilenet_v2`) de TensorFlow Hub para predecir el tipo de animal en una imagen.
- **Funcionalidad:** Realiza predicciones y devuelve información básica sobre el animal detectado, como su nombre y etiqueta.

### 3. Módulo de Información (AnimalTour)
- **Descripción:** Utiliza OpenAI's GPT-3.5 para generar información detallada sobre el animal detectado.
- **Funcionalidad:** Crea respuestas en formato JSON con datos científicos sobre el nombre científico, hábitat y alimentación del animal.
