# UIDAI Data Hackathon 2026: Service Delivery Optimization Framework

**Team Name: NIT UK
**Problem Statement:** Analysis of Enrolment Saturation & Update Trends
**Submission Date:** January 20, 2026

## 📄 Project Overview
This project analyzes **5 million+ Aadhaar transaction records** (Fiscal Year 2025-2026) to assist UIDAI in optimizing service center allocation. By comparing "Enrolment Saturation" against "Update Request Volumes," we identified specific districts that require a shift from static enrolment kits to mobile update units.

## 📊 Key Findings from Analysis
1.  **Enrolment Saturation:** New adult enrolments (18+) have dropped to <2% in top states, indicating near-total saturation. 90% of new intake is now in the **0-5 age group (Bal Aadhaar)**.
2.  **The "Update Burden":** Districts in **Maharashtra** and **Uttar Pradesh** show a critical bottleneck, where **Biometric Update requests (9.2M)** act as the primary load, exceeding Demographic updates by 2x.
3.  **Resource Mismatch:** Current infrastructure heavily favors new enrolments. We propose a "Dynamic Kit Reallocation" strategy to convert under-utilized enrolment stations into dedicated **Biometric Update Hubs**.

## 📂 Repository Structure
* `analysis.py` - The Python script used to process the raw CSV data and generate insights.
* `api_data_aadhar_enrolment.csv` - Cleaned dataset for new enrolments.
* `api_data_aadhar_biometric.csv` - Cleaned dataset for biometric update transactions.
* `Project_Report.pdf` - The final consolidated report submitted to the OGD portal.

## 🛠️ Technology Stack
* **Language:** Python 3.10
* **Libraries:** Pandas (Data Processing), Matplotlib & Seaborn (Data Visualization)
* **Environment:** Jupyter Notebook / VS Code

## 🚀 How to Run
To replicate the analysis locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[Your-Username]/UIDAI-Hackathon-2026.git
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas matplotlib seaborn
    ```

3.  **Run the script:**
    ```bash
    python analysis.py
    ```

---
*Submitted as part of the UIDAI Data Hackathon 2026 (Open Government Data Platform).*
