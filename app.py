from flask import Flask
from datetime import datetime

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta y su función asociada
@app.route('/')
def hello_world():
    # Obtener la fecha y hora actual
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f'¡Hola, Aaron Sarmiento! Bienvenido a Cloud9. Fecha y hora actual: {now}'

# Ejecutar la aplicación si este archivo se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)
