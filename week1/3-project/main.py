import streamlit as st
import requests

# Titre de l'application
st.title('Prédiction de Churn des Clients')

# Définition des champs d'entrée pour l'utilisateur
gender = st.selectbox('Sexe', ['Male', 'Female'], key='gender')
senior_citizen = st.selectbox('Senior Citizen', ['No', 'Yes'], key='senior_citizen')
partner = st.selectbox('Partenaire', ['No', 'Yes'], key='partner')
dependents = st.selectbox('Personnes à charge', ['No', 'Yes'], key='dependents')
tenure = st.number_input('Durée en mois', min_value=0, key='tenure')
phone_service = st.selectbox('Service Téléphonique', ['No', 'Yes'], key='phone_service')
multiple_lines = st.selectbox('Lignes Multiples', ['No', 'Yes', 'No phone service'], key='multiple_lines')
internet_service = st.selectbox('Service Internet', ['DSL', 'Fiber optic', 'No'], key='internet_service')
online_security = st.selectbox('Sécurité en ligne', ['No', 'Yes', 'No internet service'], key='online_security')
online_backup = st.selectbox('Sauvegarde en ligne', ['No', 'Yes', 'No internet service'], key='online_backup')
device_protection = st.selectbox('Protection des appareils', ['No', 'Yes', 'No internet service'], key='device_protection')
tech_support = st.selectbox('Support technique', ['No', 'Yes', 'No internet service'], key='tech_support')
streaming_tv = st.selectbox('Streaming TV', ['No', 'Yes', 'No internet service'], key='streaming_tv')
streaming_movies = st.selectbox('Streaming Films', ['No', 'Yes', 'No internet service'], key='streaming_movies')
contract = st.selectbox('Contrat', ['Month-to-month', 'One year', 'Two year'], key='contract')
paperless_billing = st.selectbox('Facturation sans papier', ['No', 'Yes'], key='paperless_billing')
payment_method = st.selectbox('Méthode de Paiement', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], key='payment_method')
monthly_charges = st.number_input('Charges Mensuelles', min_value=0.0, format='%f', key='monthly_charges')
total_charges = st.number_input('Charges Totales', min_value=0.0, format='%f', key='total_charges')

# Créer un dictionnaire avec les données d'entrée
input_data = {
    'gender': gender,
    'SeniorCitizen': 1 if senior_citizen == 'Yes' else 0,
    'Partner': partner,
    'Dependents': dependents,
    'tenure': tenure,
    'PhoneService': phone_service,
    'MultipleLines': multiple_lines,
    'InternetService': internet_service,
    'OnlineSecurity': online_security,
    'OnlineBackup': online_backup,
    'DeviceProtection': device_protection,
    'TechSupport': tech_support,
    'StreamingTV': streaming_tv,
    'StreamingMovies': streaming_movies,
    'Contract': contract,
    'PaperlessBilling': paperless_billing,
    'PaymentMethod': payment_method,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges
}

# Envoyer la requête à l'API REST
if st.button('Prédire', key='predict'):
    response = requests.post('http://127.0.0.1:8000/predict', json=input_data)
    # Vérifiez le statut de la réponse avant de tenter de décoder le JSON
    if response.status_code == 200:
        result = response.json()
        st.write(f'La prédiction est: {result["prediction"]}')
    else:
        st.write(f'Erreur: {response.status_code}')
