# Breast Cancer Analysis

This repository contains the code and resources for the Breast Cancer Analysis project, which aims to develop a machine learning model to predict breast cancer based on a dataset of medical measurements. The project includes data preprocessing, feature selection, model training and tuning, and a Streamlit app for interactive predictions.

## Project Structure

- `breast_cancer_csv/`: Contains the dataset CSV file.
- `breast_cancer_analysis/`: Jupyter notebooks for data exploration and model development.
- `app.py`: Streamlit application for interactive predictions.
- `breast_cancer_model/`: Saved machine learning models.
- `README.md`: Project documentation.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/shanmugapriyan357/Breast-Cancer-Analysis.git
    cd Breast-Cancer-Analysis
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Data Preparation

The dataset is loaded from the sklearn.datasets library, and basic preprocessing steps are performed:

Load Dataset: The dataset is loaded using load_breast_cancer() from sklearn.datasets.
Data Preparation: The dataset is split into features and target variables.
Feature Scaling: Features are scaled using StandardScaler to normalize the data.

## Feature Selection

Feature selection is implemented to improve the model's performance by reducing dimensionality:

SelectKBest: The SelectKBest method from sklearn.feature_selection is used to select the top features based on univariate statistical tests. In this project, the top 10 features are selected to improve the efficiency and accuracy of the model.

## Model Training and Tuning

A machine learning model is trained and optimized using grid search:

Model Training: An MLPClassifier (Multi-layer Perceptron) is trained on the selected features.
Hyperparameter Tuning: Grid Search with Cross-Validation (GridSearchCV) is used to find the best hyperparameters for the model. Various parameters, including hidden layer sizes, activation functions, solvers, and learning rates, are tested to find the optimal configuration.

## Save the Model

The trained model, along with the preprocessing tools, is saved for future use:

Model Saving: The trained MLPClassifier, feature selector, and scaler are saved to disk using joblib to enable easy loading and use in production.

## Streamlit App

An interactive web application is created using Streamlit to make predictions based on user input:

App Development: The app.py file contains the Streamlit code to build an interactive web interface.
Features:
Users can upload their CSV files with feature data for prediction.
Users can enter manual input data for immediate prediction.
The app displays prediction results and probabilities for both benign and malignant classes.

## Deployment and Version Control

1. Initialize a Git repository:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```

2. Push to GitHub:
    ```bash
    git remote add origin https://github.com/shanmugapriyan357/Breast-Cancer-Analysis.git
    git branch -M main
    git push -u origin main
    ```

## Sample Prediction Web Page
 Provided is a screenshot of how the Streamlit app looks and functions.
![Web page](https://github.com/user-attachments/assets/aa9cef02-0c42-4db6-9ab7-b0ab7ced3eeb)

By following these steps, you can replicate the project, understand the process of developing a machine learning model, and deploy an interactive web application using Streamlit.
