from churn_predictor import ChurnPredictor

DATA_PATH = "data/customer_data.csv"

predictor = ChurnPredictor(DATA_PATH)
predictor.start_h2o()
predictor.load_data()
predictor.train_model()


predicciones = predictor.predict()

print("\n Predicciones:")
print(predicciones.head(50))
