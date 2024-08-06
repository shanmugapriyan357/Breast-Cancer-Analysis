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

Load and preprocess the dataset.

## Feature Selection

Implement feature selection using `SelectKBest`.

## Model Training and Tuning

Train and tune the model using Grid Search CV.

## Save the Model

Save the trained model.

## Streamlit App

Create a Streamlit app for interactive predictions (`app.py`).

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

## Submission Requirements

- Python scripts in the `src/` folder
- Streamlit app code in `app.py`
- Model files in the `models/` folder
- A `README.md` file documenting the project

## Sample Prediction Web Page
 Provided is a screenshot of how the Streamlit app looks and functions.
![Web page](https://github.com/user-attachments/assets/aa9cef02-0c42-4db6-9ab7-b0ab7ced3eeb)

By following these steps, you can replicate the project, understand the process of developing a machine learning model, and deploy an interactive web application using Streamlit.
