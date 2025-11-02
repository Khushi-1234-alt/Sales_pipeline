# 📊 End-to-End Data Engineering Project using PostgreSQL, Python & Power BI

## 🌟 Project Overview
This project demonstrates an **end-to-end Data Engineering pipeline** — from raw data extraction and cleaning to database storage and visualization.

The goal is to **build a scalable and automated sales analytics system** for deriving business insights such as:
- Top-selling products  
- Revenue trends over time  
- Country-based customer segmentation  

---

## 🧱 Project Architecture  

```mermaid
flowchart TD
    A[Raw Sales Data (Kaggle CSV)] --> B[Python ETL Script 🐍]
    B --> C[(PostgreSQL Database 🐘)]
    C --> D[Power BI Dashboard 📈]
    D --> E[Actionable Business Insights 💡]
