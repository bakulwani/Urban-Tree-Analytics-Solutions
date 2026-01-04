# Urban Tree Analytics Solution

## Pune Tree Census 2019

The Pune Municipal Corporation conducted a city-wide Tree Census in 2019, generating a comprehensive dataset containing information on tree species, health condition, and spatial distribution across city wards.  
While the raw dataset is rich, it does not directly support actionable insights or policy-level decisions.

This project transforms the raw census data into a decision-support analytics solution using **Python, SQLite, and Power BI**, enabling city officials, urban planners, and civic stakeholders to monitor green cover, assess tree health, and proactively identify areas requiring attention.

---

## Objectives

The solution provides:

- **Operational visibility** into tree distribution and health across city wards  
- **Management insights** through intuitive dashboards and KPIs  
- **Analytical indicators** to highlight high-risk or under-served zones  

It answers key questions such as:

- Which wards are under-served in terms of green cover?  
- Which tree species dominate the city and individual wards?  
- Are there patterns of poor tree health requiring intervention?  
- Can high-risk zones be proactively identified using data?  

---

## Tech Stack

- **Python (Pandas):** Data ingestion, cleaning, transformation, feature engineering  
- **SQLite:** Lightweight backend database for structured storage  
- **Power BI:** Interactive dashboards and visual analytics  
- **ODBC Driver:** Connecting SQLite backend to Power BI  

---

## Data & Backend Processing

- Large raw datasets are merged, cleaned, and standardized using Python  
- Missing values and inconsistent categorical fields are handled  
- Derived analytical columns include health indicators, risk levels, and monitoring status  
- Ward-level summary tables are created for efficient analysis  
- Processed data is stored in a SQLite database for direct integration with Power BI  
- The backend is modular and database-agnostic, allowing migration to **PostgreSQL** for production-scale deployment  

---

## Dashboards

### 1. City-Level Overview Dashboard
- Ward-wise tree distribution and green cover gaps  
- Risk index and monitoring status  
- High-level KPIs for quick decision-making  

### 2. Ward-Level Operational Dashboard
- Dominant species by ward  
- Tree health and condition analysis  
- Protective collar and infrastructure conflict insights  
- Economic importance and phenology patterns  

### 3. Insights & Conclusions Dashboard
- Identification of high-risk and well-performing wards  
- City-wide trends in species, health, and seasonality  
- Key findings summarized for stakeholders  

---

## Power BI File Access

Due to GitHub file size constraints, the Power BI `.pbix` file is hosted on Google Drive:  

📌 [Download Power BI file]https://drive.google.com/file/d/1_WZsf_pKscxCdeGe-jI8smmCLRajqiQS/view?usp=drive_link  

---

## Usage

1. Clone the repository  
2. Use Python scripts to process or update the SQLite database  
3. Connect the SQLite database to Power BI using the ODBC driver  
4. Explore dashboards for city-level or ward-level insights  

---

## Future Work

- Migrate backend to PostgreSQL for scalable deployment  
- Add predictive analytics for proactive tree health management  
- Integrate geospatial mapping for advanced ward-level visualization  

---

## Author

**Bakul Wani**  
Computer Science Student | Data Analytics & Visualization Enthusiast

