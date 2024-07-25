from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Chargement du modèle pré-entraîné
model = joblib.load('random_forest_model.pkl')

class Customer(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

# @app.post('/predict')
# def predict(customer: Customer):
#     # Convertir les données de l'entrée en DataFrame
#     input_data = pd.DataFrame([customer.dict()])
    
#     # Prédiction
#     prediction = model.predict(input_data)
    
#     result = 'Churn' if prediction[0] == 1 else 'Not Churn'
#     return {"prediction": result}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)


@app.post('/predict')
def predict(customer: Customer):
    try:
        # Convertir les données de l'entrée en DataFrame
        input_data = pd.DataFrame([customer.dict()])
        
        # Assurez-vous que les colonnes sont dans le même ordre que celles utilisées pour l'entraînement
        # input_data = preprocess(input_data)  # Appliquer le prétraitement nécessaire
        
        # Prédiction
        prediction = model.predict(input_data)
        
        result = 'Churn' if prediction[0] == 1 else 'Not Churn'
        return {"prediction": result}
    except Exception as e:
        return {"error": str(e)}



# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Customer(BaseModel):
#     gender: str
#     SeniorCitizen: int
#     Partner: str
#     Dependents: str
#     tenure: int
#     PhoneService: str
#     MultipleLines: str
#     InternetService: str
#     OnlineSecurity: str
#     OnlineBackup: str
#     DeviceProtection: str
#     TechSupport: str
#     StreamingTV: str
#     StreamingMovies: str
#     Contract: str
#     PaperlessBilling: str
#     PaymentMethod: str
#     MonthlyCharges: float
#     TotalCharges: float

# @app.post('/predict')
# def predict(customer: Customer):
#     # Simule une prédiction
#     return {"prediction": "Churn"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
