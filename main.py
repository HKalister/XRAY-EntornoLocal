import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import tensorflow as tf
import numpy as np
import logging

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp'

# Configurar logging
logging.basicConfig(level=logging.INFO)

# Cargar el modelo desde un archivo local
model_path = 'path/to/your/local/best_model_improved.h5'  # Ruta al modelo local
try:
    model = tf.keras.models.load_model(model_path)
    logging.info("Modelo cargado correctamente.")
except Exception as e:
    logging.error(f"Error al cargar el modelo: {e}")

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        logging.error("No file part in the request")
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        logging.error("No selected file")
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return redirect(url_for('uploaded_file', filename=filename))
    logging.error("File not allowed")
    return redirect(request.url)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image = tf.keras.preprocessing.image.load_img(file_path, target_size=(150, 150), color_mode='grayscale')
        image = tf.keras.preprocessing.image.img_to_array(image)
        image = np.reshape(image, (1, 150, 150, 1))  # Añadir dimensiones batch y canal
        image /= 255.0  # Normalizar la imagen
        
        prediction = model.predict(image)
        categories = ['NORMAL', 'PNEUMONIA']
        confidence = np.max(prediction) * 100
        predicted_class = categories[np.argmax(prediction)]
        logging.info(f"Prediction: {predicted_class}, Confidence: {confidence:.3f}%")
        return render_template('result.html', prediction=predicted_class, confidence=confidence)
    except Exception as e:
        logging.error(f"Error en uploaded_file: {e}")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


