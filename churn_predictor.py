import h2o
from h2o.automl import H2OAutoML

class ChurnPredictor:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = None
        self.model = None
        self.x = None
        self.y = "Churn"

    def start_h2o(self):
        h2o.init()

    def load_data(self):
        self.data = h2o.import_file(self.data_path)
        self.data[self.y] = self.data[self.y].asfactor()
        self.x = self.data.columns
        self.x.remove(self.y)

    def train_model(self, max_models=10):
        aml = H2OAutoML(max_models=max_models, seed=42)
        aml.train(x=self.x, y=self.y, training_frame=self.data)
        self.model = aml.leader

    def predict(self, new_data=None):
        if new_data is None:
            new_data = self.data
        return self.model.predict(new_data)

    def show_predictions(self, n=5):
        preds = self.predict()
        print(preds.head(n))