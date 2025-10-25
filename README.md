# Retail Data Preprocessing, Analysis & EDA Dashboard

This repository demonstrates a complete data cleaning, preprocessing, and analysis pipeline for retail transaction data. Interactive EDA is provided through a Gradio dashboard.

***

## 📦 Dataset

- `Retail_Transactions_2000.csv` (raw)
- `Retail_Cleaned.csv` (cleaned output)

Data columns: TransactionID, CustomerID, Gender, Age, City, ProductCategory, Quantity, Price, PurchaseDate, PaymentMode, TotalAmount

***

## 🚀 Features

- **Comprehensive Data Cleaning & Feature Engineering:**
  - Handles missing values, fixes categorical inconsistencies, and corrects data errors.
  - Feature extraction: TotalAmount formula, month & weekday from date, age groups.
- **Automated Preprocessing Code (see notebook/script).**
- **Powerful EDA Visualizations:**
  - Age, gender, city, and sales insights.
  - Product, payment, and customer segment insights.
- **Interactive Gradio Web Dashboard.**

***

## 📝 How to Run

1. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Preprocess your data:**
    - Edit and run the code provided in the notebook/script for Part A (Preprocessing).
    - Output is `Retail_Cleaned.csv`.

3. **Interact with the dashboard:**
    ```python
    python dashboard.py
    ```
    Or run the Gradio cells in your notebook. Select plots via the Gradio UI.

***

## 📊 Example Plots

- **Age Distribution**
- **Gender Distribution**
- **Top 10 Cities**
- **Product Category Sales**
- **Monthly Sales Trend**
- **Payment Modes Usage (pie)**
- **City-wise Revenue**
- **Product vs Payment Heatmap**
  
*(See gradio app for live plots)*

***

## 🖥️ Dashboard Code (Gradio snippet)

```python
import gradio as gr
# (See dashboard.py for full code with all features/plots!)
```

***

## 👨‍💻 Requirements

See `requirements.txt`:
```
pandas
numpy
scikit-learn
matplotlib
seaborn
gradio
```

***

## 📂 Project Structure

```
.
├── Retail_Transactions_2000.csv       # raw data
├── Retail_Cleaned.csv                # cleaned data after preprocessing
├── dashboard.py                      # gradio interface file
├── requirements.txt
├── README.md
└── (Optional images/plots)
```

***

## 📚 Learning Outcomes

- Real-world data preprocessing (cleaning, missing data, encoding)
- Feature engineering and visualization for business insights
- Creating ready-to-analyze datasets and deployable EDA dashboards

***

