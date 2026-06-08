# 🚀 AI Customer Intelligence Platform

## 📌 Project Overview

AI Customer Intelligence Platform is an end-to-end Data Analytics & Business Intelligence solution built using Python, SQL, Machine Learning, PostgreSQL and Streamlit.

The platform analyzes customer behavior, identifies high-value customers, performs customer segmentation, generates business recommendations, forecasts future sales, and provides an executive dashboard for decision-making.

---

## 🎯 Business Problem

Companies often struggle to:

- Identify valuable customers
- Detect customer churn risks
- Monitor sales performance
- Generate business insights
- Predict future demand

This platform solves these challenges using Data Analytics and AI-driven insights.

---

# 🏗️ Project Architecture

![Architecture](images/architecture.png)

---

# ⚙️ Tech Stack

### Programming
- Python

### Database
- PostgreSQL
- SQL

### Data Analysis
- Pandas
- NumPy

### Data Visualization
- Plotly
- Matplotlib
- Streamlit

### Machine Learning
- Scikit-Learn
- Random Forest

---

# 📂 Project Structure

```text
AI_Customer_Intelligence_Project
│
├── Dashboard
│   └── app.py
│
├── Data
│   ├── Raw
│   └── Processed
│
├── Scripts
│   ├── 01_data_loading.py
│   ├── 02_data_cleaning.py
│   ├── 03_eda.py
│   ├── 04_feature_engineering.py
│   ├── 05_ml_model.py
│   ├── 06_customer_segmentation.py
│   ├── 07_rfm_features.py
│   ├── 08_kmeans_segmentation.py
│   └── 09_sales_forecasting.py
│
├── SQL
│   ├── database_schema.sql
│   └── analysis_queries.sql
│
└── README.md
```

---

# 🗄️ Database Design

### PostgreSQL Database

Tables Created:

- Customers
- Orders
- Products
- Sellers
- Reviews
- Payments
- Order Items

---

## SQL Schema Screenshot

![SQL Schema](images/sql_schema.png)

---

## Database Validation

![Database Validation](images/database_validation.png)

---

# 🔥 Data Engineering Pipeline

### Step 1: Data Loading

- Loaded Olist E-Commerce Dataset
- Connected PostgreSQL Database
- Imported CSV Files

### Step 2: Data Cleaning

- Missing Value Detection
- Duplicate Removal
- Data Quality Checks

### Step 3: Exploratory Data Analysis

- Customer Analysis
- Revenue Analysis
- Order Trends

### Step 4: Feature Engineering

Created:

- Total Orders
- Customer Revenue
- Purchase Frequency
- Customer State Features

---

## Feature Engineering Output

![Feature Engineering](images/feature_engineering.png)

---

# 🤖 Machine Learning Model

### Customer Intelligence Model

Algorithm Used:

- Random Forest Classifier

Features:

- Total Orders
- Customer Activity

Output:

- Customer Classification

---

## ML Model Result

![ML Model](images/ml_model.png)

---

# 📊 Dashboard Features

## Executive Command Center

- Total Customers
- Total Orders
- Total Products

![Dashboard Home](images/dashboard_home.png)

---

## Sales Intelligence Monitor

Tracks Monthly Order Trends

![Sales Intelligence](images/sales_intelligence.png)

---

## Customer Segmentation Center

Segments Customers Into:

- VIP Customers
- Regular Customers
- At Risk Customers

![Customer Segmentation](images/customer_segmentation.png)

---

## Customer State Analysis

Top Performing States

![State Analysis](images/state_analysis.png)

---

## Customer Health Score

Business Health Monitoring

![Health Score](images/health_score.png)

---

## AI Sales Forecast Engine

Future Sales Prediction

![Sales Forecast](images/sales_forecast.png)

---

## Revenue Champions Leaderboard

Top Revenue Generating Customers

![Revenue Champions](images/revenue_champions.png)

---

## Customer Spending Outlier Detection

Detect High Spending Customers

![Outlier Analysis](images/outlier_analysis.png)

---

## AI Business Intelligence Engine

Automatically Generates:

- Customer Insights
- Revenue Recommendations
- Retention Strategies
- Upselling Opportunities

![Business Intelligence](images/business_intelligence.png)

---

## Smart AI Business Assistant

Business Q&A Engine

Supports Questions Like:

- Which segment is largest?
- How can revenue be increased?
- What is business health status?
- Which state has most customers?
- Who are highest value customers?

![AI Assistant](images/ai_assistant.png)

---

# 📈 Key Insights

### Customer Distribution

- Regular Customers: 89,935
- VIP Customers: 3,195
- At Risk Customers: 2,965

### Business Health Score

- 92/100

### Top Customer State

- São Paulo (SP)

### Revenue Opportunity

- Customer Upselling
- Loyalty Programs
- At-Risk Customer Recovery

---

# 🚀 How To Run

### Clone Repository

```bash
git clone https://github.com/dipendra-pardhi/AI-Customer-Intelligence-Dashboard.git
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Dashboard

```bash
streamlit run Dashboard/app.py
```

---

# 👨‍💻 Author

### Dipendra Pardhi

BBA (Business Analytics)

Skills:

- SQL
- Python
- Power BI
- PostgreSQL
- Machine Learning
- Data Analytics
- Streamlit

---

# ⭐ Project Highlights

✅ End-to-End Data Analytics Project

✅ PostgreSQL Database Integration

✅ Machine Learning Implementation

✅ Customer Segmentation

✅ Sales Forecasting

✅ Business Intelligence Dashboard

✅ AI Recommendation Engine

✅ Executive Decision Support System

---

## ⭐ If you like this project, don't forget to star the repository.
