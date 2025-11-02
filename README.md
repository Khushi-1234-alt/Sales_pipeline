# 🚀 Sales Data Pipeline & Analytics Dashboard  

### 📊 End-to-End Data Engineering Project using PostgreSQL, Python & Power BI  

---

## 🧠 Project Overview  
This project demonstrates an **end-to-end Data Engineering pipeline** — from raw data extraction and cleaning to database storage and visualization.  
The goal is to **build a scalable and automated sales analytics system** for business insights such as top-selling products, revenue trends, and customer segmentation.

---

## 🧱 Project Architecture  

```mermaid
flowchart TD
    A[📥 Raw CSV Data (Kaggle)] --> B[🧹 Python ETL Script]
    B --> C[(🗄 PostgreSQL Database)]
    C --> D[📈 Power BI Dashboard]
    D --> E[💡 Business Insights]
