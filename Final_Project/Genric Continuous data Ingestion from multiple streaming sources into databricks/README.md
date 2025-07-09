# 💠 Azure Data Factory Project – Internship Final Report

## 📚 Table of Contents
- [📌 Introduction](#introduction)
- [🎯 Project Objectives](#project-objectives)
- [⚙️ Setup Instructions](#setup-instructions)
- [🚀 Usage Scenarios](#usage-scenarios)
- [🧾 Conclusion](#conclusion)

---

## 📌 Introduction

Hi there! 👋

Welcome to my Azure Data Factory internship project. This repository highlights my practical experience building real-world data pipelines using Azure Data Factory (ADF). The focus was on automating data integration tasks, implementing conditional logic, and using parameterized pipelines for scalable and maintainable ETL workflows.

---

## 🎯 Project Objectives

### ✅ 1. Fetch Country Data via REST API
- Created a pipeline to fetch data for the following countries:
  - India 🇮🇳
  - United States 🇺🇸
  - United Kingdom 🇬🇧
  - China 🇨🇳
  - Russia 🇷🇺
- Stored the data in **JSON files** in Azure Data Lake Storage (ADLS), with filenames based on each country.

### ✅ 2. Automated Trigger
- Configured a **trigger** to run the Fetch Country Data pipeline **twice daily**:
  - ⏰ 12:00 AM IST
  - ⏰ 12:00 PM IST

### ✅ 3. Conditional Data Copy
- Built a pipeline to:
  - Copy **customer data** to ADLS **only if** record count > 500.
  - If record count > 600, **triggered a child pipeline** to also copy **product data**.

### ✅ 4. Pipeline Parameterization
- Passed the **customer record count** from the parent pipeline to the child pipeline using **pipeline parameters**, enabling dynamic execution logic.

### ✅ 5. ADF Components Setup
- Created and configured the following within a single ADF instance:
  - Linked Services
  - Datasets
  - Pipelines
  - Triggers
  - Parameterized activities

---

## ⚙️ Setup Instructions

### 🔧 Prerequisites
- Azure Subscription
- Azure Data Factory (v2) instance
- Access to Azure Data Lake Storage
- Git installed (optional for cloning)

### 📥 Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ADF-Pipelines.git
cd ADF-Pipelines
```

### 🛠 Configure in Azure Data Factory
1. Open [Azure Data Factory Studio](https://adf.azure.com).
2. Import the JSON files under the `ADF/` folder.
3. Update connection strings, credentials, and dataset paths to match your environment.
4. Publish the factory and validate pipelines.

---

## 🚀 Usage Scenarios

### 🌍 Fetch Country Data
- The pipeline fetches country data from the REST API and stores it in ADLS.
- Runs automatically via the time-based trigger twice a day.

### 📈 Conditional Data Copy
- The customer data copy pipeline runs only if the record count > 500.
- If count > 600, it triggers a child pipeline to also copy product data.

### 🔁 Parameter Passing
- Dynamically passes customer count from the parent pipeline to the child pipeline using **pipeline parameters**.

---

## 🧾 Conclusion

This internship project helped me gain hands-on experience with:
- Real-world data integration scenarios using Azure Data Factory
- Designing scalable and reusable pipelines
- Automating ETL processes via triggers
- Implementing conditional logic using lookup and IF activities
- Parameterizing pipelines for modularity

I'm proud to showcase this project as a reflection of the knowledge and skills I've gained during my internship.

---

**👨‍💻 Developed by:**  
**CV Dhanush**  
**Data Engineering Intern**

📫 *Feel free to reach out for any questions or collaboration!*
