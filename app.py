import streamlit as st
import pandas as pd
import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif

# Load model
model = joblib.load('breast_cancer_model.pkl')

# Load dataset for feature names and scaling
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Prepare features and target
X = df.drop('target', axis=1)
y = df['target']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Feature selection
k = 10  # Make sure k is consistent with your previous selection
selector = SelectKBest(score_func=f_classif, k=k)
X_selected = selector.fit_transform(X_scaled, y)

# Streamlit app
st.title('Breast Cancer Prediction App')
st.write('This app uses an MLP Classifier to predict breast cancer.')

# Display the dataset
if st.checkbox('Show dataset'):
    st.write(df)

# File uploader for user data
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    user_data = pd.read_csv(uploaded_file)
    st.write("User Input Data")
    st.write(user_data)
    
    # Preprocess user data
    user_data_scaled = scaler.transform(user_data)
    user_data_selected = selector.transform(user_data_scaled)
    
    # Predict
    predictions = model.predict(user_data_selected)
    prediction_probabilities = model.predict_proba(user_data_selected)
    
    # Display predictions
    st.write("Predictions (0 = Benign, 1 = Malignant)")
    st.write(predictions)
    st.write("Prediction Probabilities")
    st.write(prediction_probabilities)

# Sidebar input for manual data entry
st.sidebar.header('Manual Input Features')
manual_input = {}
for feature in X.columns:
    manual_input[feature] = st.sidebar.number_input(f"{feature}", value=float(df[feature].mean()))

manual_input_df = pd.DataFrame([manual_input])
st.write("Manual Input Data")
st.write(manual_input_df)

# Preprocess manual input data
manual_input_scaled = scaler.transform(manual_input_df)
manual_input_selected = selector.transform(manual_input_scaled)

# Predict for manual input
manual_prediction = model.predict(manual_input_selected)
manual_prediction_probability = model.predict_proba(manual_input_selected)

# Display manual prediction
st.write("Manual Input Prediction (0 = Benign, 1 = Malignant)")
st.write(manual_prediction)
st.write("Manual Input Prediction Probability")
st.write(manual_prediction_probability)
