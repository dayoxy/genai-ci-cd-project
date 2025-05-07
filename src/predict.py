import mlflow.sklearn

def predict(input_data):
    model = mlflow.sklearn.load_model("models:/genai_mlops/1")
    return model.predict(input_data)