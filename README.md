# 🚀 AI Customer Intelligence Platform

### Enterprise-Grade Customer Analytics, Sales Forecasting & Business Intelligence Engine

Transforming raw customer transaction data into actionable business intelligence using Artificial Intelligence, Machine Learning, SQL Analytics and Interactive Visualization.

---

## ⭐ Project Highlights

✔ AI-Powered Customer Segmentation

✔ Customer Health Scoring Engine

✔ Sales Forecasting & Trend Prediction

✔ Revenue Outlier Detection

✔ Business Intelligence Recommendation System

✔ Interactive AI Business Assistant

✔ Geographic Customer Analytics

✔ Executive Decision Support Dashboard

---

## 📌 Project Overview

AI Customer Intelligence Platform is a next-generation Business Intelligence solution designed to help organizations understand customer behavior, optimize revenue strategies, predict future sales trends and improve customer retention.

The platform integrates Data Analytics, SQL, Machine Learning and Interactive Dashboarding into a single executive command center capable of converting large-scale customer transaction data into strategic business insights.

Unlike traditional dashboards that only display metrics, this platform provides intelligent recommendations, customer segmentation, risk identification and predictive analytics that support executive-level decision making.

---

## 🎯 Business Problem

Modern organizations collect millions of customer transactions every year, but most businesses struggle to answer critical questions such as:

* Who are the most valuable customers?
* Which customers are likely to churn?
* How can revenue be increased?
* What are future sales expected to look like?
* Which geographic regions drive the most customers?
* What business actions should management take next?

Without an intelligent analytics framework, organizations risk losing revenue opportunities, high-value customers and market growth potential.

This project addresses these challenges through a fully integrated AI-powered Customer Intelligence ecosystem.

---

## 🧠 Solution Architecture

The AI Customer Intelligence Platform combines multiple analytics modules into one unified system:

### 📊 Customer Intelligence Layer

* Customer Segmentation
* VIP Customer Detection
* At-Risk Customer Identification
* Customer Health Monitoring

### 📈 Predictive Intelligence Layer

* Sales Forecasting Engine
* Revenue Trend Analysis
* Growth Opportunity Detection

### 💰 Revenue Intelligence Layer

* Top Revenue Customer Analysis
* Customer Spending Analysis
* Outlier Detection Engine

### 🌍 Geographic Intelligence Layer

* State-wise Customer Distribution
* Regional Customer Performance Tracking

### 🤖 Artificial Intelligence Layer

* AI Business Assistant
* Automated Recommendation Engine
* Executive Decision Support System

---

## 🚀 Key Business Benefits

* Increase customer retention
* Improve revenue forecasting accuracy
* Identify hidden revenue opportunities
* Detect high-value customers
* Reduce customer churn risk
* Enable data-driven decision making
* Automate executive reporting

---

# 📸 Executive Dashboard Screenshots


## 📊 Dashboard Screenshots

### 🏠 Executive Command Center Dashboard
![Executive Command Center Dashboard](https://github.com/dipendra-pardhi/AI-Customer-Intelligence-Dashboard/blob/main/Redmy%20screen%20shorts/Screenshot%202026-06-08%20235445.png)

The Executive Command Center serves as the primary control hub of the AI Customer Intelligence Platform. It provides a comprehensive overview of business operations by displaying key metrics such as total customers, orders, and products. This dashboard enables stakeholders to monitor overall business performance and make informed strategic decisions through real-time insights.

---

### 📈 Sales Intelligence Monitor
![Sales Intelligence Monitor](https://github.com/dipendra-pardhi/AI-Customer-Intelligence-Dashboard/blob/main/Redmy%20screen%20shorts/Screenshot%202026-06-08%20235521.png)

The Sales Intelligence Monitor analyzes monthly sales trends and order volumes across the business. By tracking historical performance patterns, this module helps identify growth opportunities, seasonal fluctuations, and sales momentum. These insights support better forecasting and business planning.

---

### 🎯 AI Customer Segmentation Center
![AI Customer Segmentation Center](https://github.com/dipendra-pardhi/AI-Customer-Intelligence-Dashboard/blob/main/Redmy%20screen%20shorts/Screenshot%202026-06-08%20235549.png)

This AI-powered segmentation engine categorizes customers into VIP, At-Risk, and Regular customer groups based on purchasing behavior and engagement patterns. The dashboard enables businesses to create personalized retention strategies and maximize customer lifetime value through targeted marketing initiatives.

---

### 📋 Smart Order Explorer
![Smart Order Explorer](https://github.com/dipendra-pardhi/AI-Customer-Intelligence-Dashboard/blob/main/Redmy%20screen%20shorts/Screenshot%202026-06-08%20235610.png)

The Smart Order Explorer provides detailed order-level visibility through interactive filtering and exploration features. Users can analyze order status, purchase timelines, delivery performance, and customer transactions. The module also supports data export functionality for further business analysis.

---

### 🎯 Customer Health Score Engine
![Customer Health Score Engine](https://github.com/dipendra-pardhi/AI-Customer-Intelligence-Dashboard/blob/main/Redmy%20screen%20shorts/Screenshot%202026-06-08%20235847.png)

The Customer Health Score Engine evaluates overall business performance using customer engagement and operational metrics. A dynamically calculated health score helps organizations assess customer satisfaction, identify performance gaps, and monitor business stability in real time.

---

### 🚀 AI Sales Forecast Engine
![AI Sales Forecast Engine](https://github.com/dipendra-pardhi/AI-Customer-Intelligence-Dashboard/blob/main/Redmy%20screen%20shorts/Screenshot%202026-06-08%20235823.png)

The AI Sales Forecast Engine utilizes historical order trends and predictive analytics techniques to estimate future sales performance. This forecasting capability enables businesses to optimize inventory management, resource allocation, and revenue planning with greater confidence.

---

### 💰 Customer Spending Outlier Detection
![Customer Spending Outlier Detection](https://github.com/dipendra-pardhi/AI-Customer-Intelligence-Dashboard/blob/main/Redmy%20screen%20shorts/Screenshot%202026-06-08%20235800.png)

This advanced analytics module identifies high-value spending behaviors and unusual revenue patterns within the customer base. By detecting outliers, organizations can uncover premium customer segments, reduce risk, and discover untapped revenue opportunities.

---

### 🏆 Revenue Champions Leaderboard
![Revenue Champions Leaderboard](https://github.com/dipendra-pardhi/AI-Customer-Intelligence-Dashboard/blob/main/Redmy%20screen%20shorts/Screenshot%202026-06-08%20235738.png)

The Revenue Champions Leaderboard highlights the highest revenue-generating customers within the platform. This feature enables businesses to recognize top contributors, strengthen customer relationships, and develop exclusive engagement strategies for valuable customers.

---

### 🧠 AI Business Intelligence Engine
![AI Business Intelligence Engine](https://github.com/dipendra-pardhi/AI-Customer-Intelligence-Dashboard/blob/main/Redmy%20screen%20shorts/Screenshot%202026-06-08%20235705.png)

The AI Business Intelligence Engine automatically generates actionable business recommendations using customer segmentation, revenue analysis, and behavioral insights. It functions as a strategic decision-support system that helps organizations improve profitability and customer retention.

---

### 🤖 Smart AI Business Assistant
![Smart AI Business Assistant](https://github.com/dipendra-pardhi/AI-Customer-Intelligence-Dashboard/blob/main/Redmy%20screen%20shorts/Screenshot%202026-06-08%20235638.png)

The Smart AI Business Assistant provides an interactive conversational interface for exploring business insights. Users can ask questions related to customer behavior, revenue growth, market opportunities, and business performance, receiving instant AI-generated recommendations.

---

### 🌍 Customer State Analysis Dashboard
![Customer State Analysis Dashboard](https://github.com/dipendra-pardhi/AI-Customer-Intelligence-Dashboard/blob/main/Redmy%20screen%20shorts/Screenshot%202026-06-09%20000447.png)

The Customer State Analysis Dashboard visualizes customer distribution across different geographic regions and states. This module helps businesses identify high-performing markets, understand regional customer concentration, and support data-driven expansion strategies.


## 🗄 PostgreSQL Database Integration

### Database Schema Creation

```sql
CREATE TABLE customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_unique_id VARCHAR(50),
    customer_city VARCHAR(100),
    customer_state VARCHAR(10)
);

CREATE TABLE orders (
    order_id VARCHAR(50) PRIMARY KEY,
    customer_id VARCHAR(50),
    order_status VARCHAR(50),
    order_purchase_timestamp TIMESTAMP
);
```

### Business Analysis Queries

```sql
SELECT
    COUNT(*) AS total_orders,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM orders;
```

```sql
SELECT
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(p.payment_value) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN payments p ON o.order_id = p.order_id
GROUP BY c.customer_unique_id
ORDER BY total_spent DESC
LIMIT 10;
```

📂 Complete SQL scripts are available inside the `SQL/` folder.


---

# ⚙️ Data Engineering & Machine Learning Pipeline

This project follows a complete end-to-end Data Science workflow, transforming raw e-commerce data into AI-powered business intelligence through PostgreSQL, Python, Machine Learning, and Interactive Analytics.

---

## 📂 Project Architecture

```text
Raw Data
    ↓
PostgreSQL Database
    ↓
Data Cleaning
    ↓
Exploratory Data Analysis (EDA)
    ↓
Feature Engineering
    ↓
Machine Learning Model
    ↓
AI Business Intelligence Dashboard
```

---

## 🗄 PostgreSQL Database Integration

The platform uses PostgreSQL as the central enterprise data warehouse for storing and analyzing e-commerce transactions.

### Database Components

- Customers Table
- Orders Table
- Order Items Table
- Products Table
- Payments Table
- Reviews Table
- Sellers Table

### Database Setup

![Database Setup](images/database-schema-setup.png)

### Key Achievements

- Designed relational database schema
- Imported Olist E-Commerce Dataset
- Connected PostgreSQL with Python
- Built business intelligence queries
- Created centralized analytics database

📂 Complete SQL scripts are available inside the `SQL/` folder.

---

## 📊 Data Quality & Cleaning Engine

### Data Cleaning Process

![Data Cleaning Engine](images/data-cleaning-engine.png)

### Tasks Performed

- Missing Value Analysis
- Duplicate Record Detection
- Data Validation
- Dataset Quality Reporting
- Data Consistency Checks

### Results

✅ Zero duplicate records detected

✅ Clean customer dataset generated

✅ Analytics-ready structured data

---

## 📈 Exploratory Data Analysis (EDA)

### Monthly Orders Trend Analysis

![Monthly Orders Trend Analysis](https://github.com/dipendra-pardhi/AI-Customer-Intelligence-Dashboard/blob/main/Redmy%20screen%20shorts/Monthly%20orders%20Trend%20Screenshot%20.png)

### Insights Generated

- Monthly order growth trends
- Customer purchasing patterns
- Seasonal demand fluctuations
- Business performance tracking
- Order volume forecasting insights

---

## 🧠 Feature Engineering Pipeline

### Customer Feature Generation

![Feature Engineering Pipeline](images/feature-engineering-pipeline.png)

### Features Created

- Total Orders
- Customer Revenue
- Purchase Frequency
- Customer State
- Customer Behavior Metrics

### Outcome

Generated machine-learning-ready customer feature dataset for predictive analytics.

---

## 🤖 Machine Learning Model Development

### Customer Intelligence Prediction Model

![Machine Learning Model](images/customer-intelligence-ml-model.png)

### Model Details

- Algorithm: Random Forest Classifier
- Train/Test Split: 80/20
- Customer Prediction Engine
- Automated Evaluation Pipeline

### Performance

✅ Model Successfully Trained

✅ Prediction Pipeline Executed

✅ Customer Intelligence Features Generated

---

# 🚀 Advanced Analytics Capabilities

### Implemented Intelligence Modules

✅ Customer Segmentation Engine

✅ AI Business Recommendation System

✅ Customer Health Score Engine

✅ Revenue Outlier Detection

✅ Sales Forecasting Analytics

✅ State-wise Customer Intelligence

✅ Revenue Champions Leaderboard

✅ Smart AI Business Assistant

✅ Enterprise PostgreSQL Data Warehouse

---

## 📌 End-to-End Workflow

1. Data Collection
2. PostgreSQL Data Warehousing
3. Data Cleaning & Validation
4. Exploratory Data Analysis
5. Feature Engineering
6. Machine Learning Modeling
7. Customer Intelligence Generation
8. AI Business Recommendations
9. Interactive Dashboard Deployment

---
