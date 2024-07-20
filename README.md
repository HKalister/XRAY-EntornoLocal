Proyecto de Predicción de Neumonía en Entorno Local
Este proyecto despliega una aplicación Flask en Entorno Local, que permite predecir si una imagen de rayos X muestra signos de neumonía.

EntornoLocal/
├── main.py
├── requirements.txt
├── best_model_improved.h5
└── templates/
    ├── index.html
    └── result.html



##Descripción de los Archivos

**EntornoLocal/:** Carpeta principal del proyecto.

- main.py: Código principal de la aplicación Flask.
- requirements.txt: Archivo que contiene las dependencias del proyecto.
- best_model_improved.h5: Archivo del modelo preentrenado en formato H5.
  (descargar desde Google Drive: https://drive.google.com/file/d/1P98YC-eicp3RwPBOk7xAKTLcZrRt7LLE/view?usp=sharing)
- templates/: Carpeta que contiene los archivos HTML.
  - index.html: Página de inicio de la aplicación.
  - result.html: Página que muestra los resultados de la predicción.
Instrucciones para Reproducir el Proyecto
PASO 1: DESCARGAR LOS ARCHIVOS DEL PROYECTO
Descarga el archivo comprimido con todos los archivos del proyecto desde el siguiente enlace:

https://github.com/HKalister/XRAY-EntornoLocal/archive/refs/heads/main.zip

Descomprimir el Archivo:

Descomprime el archivo descargado en tu computadora. Asegúrate de que todos los archivos estén en la misma carpeta.

Descargar el archivo del modelo desde el siguiente enlace: https://drive.google.com/file/d/1P98YC-eicp3RwPBOk7xAKTLcZrRt7LLE/view?usp=sharing Es necesario moverlo a la misma carpeta donde se encuentra el resto de los archivos, para su correcto funcionamiento.

PASO 2: CREAR Y ACTIVAR UN ENTORNO VIRTUAL
Abrir la Terminal (Símbolo del sistema o PowerShell):

Presiona Win + R, escribe cmd o powershell y presiona Enter.

Navegar al Directorio del Repositorio:

Cambia al directorio del repositorio clonado. Reemplaza <nombre_del_repositorio> con el nombre del directorio (ubicacion de la carpeta donde se encuentran todos los archivos)

cd <nombre_del_repositorio>
Crear un Entorno Virtual:
python -m venv env
Activar el Entorno Virtual:
env\Scripts\activate
PASO 3: INSTALAR LAS DEPENDENCIAS
Instalar las Dependencias desde requirements.txt:

pip install -r requirements.txt
PASO 4: EJECUTAR LA APLICACION
python main.py
PASO 5: ACCEDER A LA APLICACIÓN
Del paso anterior debería aparecer algo asi:

Running on all addresses (0.0.0.0)
Running on http://127.0.0.1:8080
Running on http://192.168.1.11:8080
Abre un navegador web y ve a http://127.0.0.1:8080 para usar la aplicación desde la misma máquina. Para acceder desde otro dispositivo en la misma red, usa la dirección http://192.168.1.11:8080.
