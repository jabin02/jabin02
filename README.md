# Fraud Detection Using Machine Learning

## Overview
This project focuses on detecting fraudulent transactions using machine learning techniques. We have trained an optimized XGBoost model to classify transactions as fraud or non-fraud based on various transaction features.

## Features
- Data preprocessing and feature engineering to enhance fraud detection accuracy.
- Handling class imbalance using **ADASYN**.
- Feature selection for optimized model performance.
- Model training using **XGBoost**.
- Fraud detection using probability thresholds for better precision-recall balance.
- Evaluation using **ROC-AUC, confusion matrices, and classification reports**.

## Dataset
The dataset consists of anonymized transaction details, including:
- **Transaction ID**
- **Transaction Amount**
- **Card Information (card1, card2, card3, etc.)**
- **Email Domains (P_emaildomain, R_emaildomain)**
- **Address Information (addr1, addr2)**
- **Fraud Labels (`isFraud` - if available)**

## Installation
To run this project, ensure you have the required dependencies installed:

```bash
pip install pandas numpy scikit-learn xgboost seaborn matplotlib imbalanced-learn
```

## Usage
### 1. Train the Model
```python
python train.py
```
### 2. Test on New Data
```python
python predict.py --input test_transaction.csv --output predictions.csv
```
### 3. Visualize Results
```python
python visualize_results.py
```

## Model Performance
| Metric | Value |
|--------|--------|
| Accuracy | 91% |
| Precision | 96% |
| Recall | 90% |
| ROC-AUC | 0.91 |

## Future Improvements
- Integrate **real-time fraud detection** via an API.
- Deploy model using **AWS Lambda** or **Google Cloud Functions**.
- Implement **feature importance analysis** with SHAP.

## Contributors
- **Jabinbalan Ravinbalan** 

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Kaggle for providing transaction datasets.
- Open-source tools like **XGBoost, Scikit-Learn, and Pandas** for efficient data processing.

