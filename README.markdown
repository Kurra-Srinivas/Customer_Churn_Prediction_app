![Customer churn prediction App](https://github.com/Kurra-Srinivas/Customer_Churn_Prediction_app/blob/main/Project%20img.png)
# Customer Churn Prediction ML Project with Streamlit

## Overview
This project develops a machine learning model to predict customer churn using Python. It includes data analysis, feature engineering, and model training with scikit-learn, optimized using GridSearchCV across multiple models. The final model is deployed as an interactive Streamlit web app for real-time churn predictions. This project is designed for beginners and professionals to learn churn prediction, gain insights, and showcase results through a user-friendly interface.

## Key Features
- **Data Analysis**: Visualize and explore customer data to uncover churn patterns.
- **Feature Engineering**: Process and create features to improve model performance.
- **Machine Learning**: Train and optimize multiple models (4–5) using scikit-learn with GridSearchCV for hyperparameter tuning.
- **Streamlit App**: Deploy an interactive web app to predict churn based on user inputs.
- **Dataset**: Expects a churn dataset (e.g., `churn_data.csv`) with features like tenure, charges, and a binary churn column.

## Tools and Dependencies
- **Python Libraries**:
  - pandas, numpy: Data processing.
  - matplotlib, seaborn: Data visualization.
  - scikit-learn: Machine learning and GridSearchCV.
  - streamlit: Web app deployment.
  - jupyter: Notebook environment.
- Install dependencies via `requirements.txt`:
  ```
  pandas>=2.0.0
  numpy>=1.24.0
  matplotlib>=3.7.0
  seaborn>=0.12.0
  scikit-learn>=1.2.0
  streamlit>=1.20.0
  jupyter>=1.0.0
  ```

## Project Structure
- `notebooks/churn_prediction.ipynb`: Notebook for data analysis, feature engineering, and model training.
- `app.py`: Streamlit app for deploying the churn prediction model.
- `data/churn_data.csv`: Sample or user-provided dataset.
- `requirements.txt`: List of dependencies.

### Deployed Streamlit App The app is deployed on Streamlit Community Cloud. Access it at https://fraud-detection-app-taqhypmjn8savxewsib3yw.streamlit.app/.

Build and deploy your churn prediction model with ease! 🚀
