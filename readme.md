# 📊 Customer Prediction con H2O.ai y POO

Este proyecto utiliza H2O AutoML para predecir la pérdida de clientes (churn) a partir de un conjunto de datos de clientes. El modelo se entrena automáticamente y se generan predicciones sobre los datos cargados.

 Estructura del proyecto
css
.
├── churn_predictor.py
├── main.py
└── data/
    └── customer_data.csv

🚀 Requisitos
Python 3.7+

H2O.ai

Instalación de dependencias:

bash
pip install h2o

📄 Descripción de archivos
churn_predictor.py
Contiene la clase ChurnPredictor, que encapsula la lógica de:

Inicialización de H2O

Carga y preparación de datos

Entrenamiento automático de modelos con H2OAutoML

Predicción sobre nuevos datos

Visualización de predicciones

main.py
Script principal que:

Instancia la clase ChurnPredictor.

Inicia el servidor de H2O.

Carga los datos desde data/customer_data.csv.

Entrena el modelo automáticamente.

Genera y muestra las primeras 50 predicciones.

🧪 Ejecución
Asegúrate de tener el archivo customer_data.csv en la carpeta data/.

Luego, ejecuta el script:

bash
python main.py