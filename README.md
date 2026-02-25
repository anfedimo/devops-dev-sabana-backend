# API de Retos Sabana 🚀

API desarrollada con FastAPI para gestionar retos de programación con diferentes niveles de dificultad..

Esta arquitectura proporciona una base sólida y flexible para experimentar con retos de educación financiera, permitiendo a los equipos de sabana adoptar rápidamente prácticas modernas de desarrollo, automatización, calidad y seguridad, y escalar la solución según las necesidades reales del producto y del equipo.

## 🛠️ Arquitectura del Proyecto

```text
devops-dev-sabana-backend/
│
├── .github/
│   └── workflows/
│       └── ci-sabana.yml           # Pipeline de Integración Continua (GitHub Actions)
├── Jenkinsfile                     # Pipeline de Entrega Continua (Jenkins en Kubernetes)
├── app/
│   ├── routers/
│   │   └── challenges.py           # Rutas y lógica de negocio de los retos
│   ├── static/                     # Archivos estáticos (imágenes, favicon)
│   │   ├── sabana.png
│   │   └── sabana-logo.png
│   ├── templates/
│   │   └── index.html              # Plantilla HTML para el landing page
│   ├── config.py                   # Configuración general del proyecto
│   ├── main.py                     # Punto de entrada y registro de routers
│   └── models.py                   # Definición de modelos Pydantic
│
├── tests/
│   ├── __init__.py
│   ├── test_challenges.py          # Pruebas automáticas de la API
│   └── test_main.py
│
├── Dockerfile                      # Imagen de contenedor reproducible
├── requirements.txt                # Dependencias de Python
├── pytest.ini                      # Configuración de pruebas
├── sonar-project.properties        # Configuración para análisis de calidad (Sonar)
└── README.md                       # Descripción y guía del proyecto
```

## 📋 Estructura del Proyecto

- API lista para experimentación:
Expone endpoints para publicar, consultar y gestionar retos de educación financiera, alineándose con el propósito de la iniciativa sabana.


- Arquitectura modular y escalable:
La separación en módulos permite agregar nuevas funcionalidades (más rutas, seguridad, autenticación) de forma sencilla.


- Pruebas y calidad:
Incluye pruebas automáticas y configuración para análisis de calidad, asegurando robustez y facilitando la experimentación continua.


- Automatización y despliegue:
Listo para ser dockerizado y desplegado en cualquier entorno cloud, integrable fácilmente a pipelines CI/CD.


- Buenas prácticas de seguridad:
Facilita la integración de autenticación, control de acceso y prácticas de seguridad desde el diseño.


- Documentación interactiva:
Ofrece documentación automática y clara (Swagger UI y Redoc) para desarrolladores.

- Validación de Calidad (CI): Orquestador en la nube encargado de ejecutar la suite de pruebas unitarias (pytest), verificar la cobertura de código y realizar el análisis estático de seguridad (SAST) mediante SonarCloud. Una vez validado, emite la señal de disparo (Trigger) hacia el entorno local.

- Despliegue y Distribución (CD): Orquestador local ejecutado sobre Minikube. Gestiona agentes dinámicos en Kubernetes para la construcción inmutable de la imagen Docker y su posterior publicación en el registro oficial de Docker Hub tras la aprobación del Quality Gate.

## 🚀 Cómo Ejecutar

### 🔧 Requisitos Previos
- Python 3.11+
- Docker
- pip

### 🏃 Ejecución Local

1. **Configurar entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # venv\Scripts\activate   # Windows
    ```
2. **Instalar dependencias:**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Ejecutar la API:**:
   ```bash
   uvicorn app.main:app --reload
    ```
4. **Acceder a la API::**:
- Documentación Swagger: http://localhost:9000/docs
- Redoc: http://localhost:9000/redoc
##  🐳 Ejecución con Docker
1. **Construir la imagen:**
   ```bash
   docker build -t sabana-api .
   ```
2. **Ejecutar el contenedor:**
   ```bash
    docker run -p 9000:9000 sabana-api
    ```
   **Opciones útiles:**
-  -d para ejecutar en segundo plano
- --name sabana para nombrar el contenedor

##  🧪 Ejecución de Tests
1. **Tests normales:**
   ```bash
   pytest -v tests/
    ```
2. **Tests con cobertura:**
    ```bash
    pytest --cov=app tests/
     ```
3. **Generar reporte HTML:**
   ```bash
   pytest --cov=app --cov-report=html
    open htmlcov/index.html  # Ver reporte
    ```
##  📚 Documentación de Endpoints
GET
- Devuelve un mensaje de bienvenida
- Ejemplo de respuesta:
    ```bash
    {"Hello": "World"} # Ver reporte
    ```

    GET /health
- Health check de la API
- Respuesta esperada:
    ```bash
    {"status": "ok"}
    ```
  GET /challenges
- Lista todos los retos creados
  - Ejemplo de respuesta:
      ```bash
      [
    {
      "title": "Ahorrar 10%",
      "description": "Ahorro mensual",
      "difficulty": "intermedio"
    }
      ]
      ```
  POST /challenges
- Crea un nuevo reto
- Body requerido:
    ```json
    {
  "title": "string",
  "description": "string",
  "difficulty": "básico|intermedio|avanzado"
    }
    ```
- Código de respuesta: 201 (Created)
  
## 🔍 Validaciones

La API valida automáticamente:

- Que el campo difficulty sea uno de los valores permitidos

- Que todos los campos requeridos estén presentes

- Tipos de datos correctos

## 🛠️ Tecnologías Utilizadas

- FastAPI - Framework web
- Pydantic - Validación de datos
- Uvicorn - Servidor ASGI
- pytest - Testing framework
- Docker - Contenerización

## 📊 Estructura del Código
El archivo principal main.py contiene:

1. Configuración inicial:

   - Creación de la app FastAPI
   - Configuración de logging


2. Modelos Pydantic:

   - Challenge: Modelo principal para los retos
   - DifficultyLevel: Enum para los niveles de dificultad


3. Endpoints:

   - Rutas principales con sus funciones

   
4. Almacenamiento:

    - Lista en memoria challenges que persiste durante la ejecución


## Arquitectura de Software — Universidad de La Sabana — Grupo 14 — 2025




