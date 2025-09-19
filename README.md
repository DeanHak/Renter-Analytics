# Renter-Analytics

# Kano-Renter-Analytics
ETL pipeline for Kano Model analysis of renter preferences (1,480+ records) in Sun Belt real estate markets.

## Overview
This project is a data engineering and analytics pipeline to apply the Kano Model to Corgan's 2025 *Residency Reshaped* survey data, processing 1,480 responses from renters (aged 25-45, ≥$1,500/month) across Atlanta, Austin, Dallas, Denver, Nashville, and Phoenix. It reveals affordability's rise over amenities/location amid hybrid work and inflation, prioritizing features like walkability (must-have, Z>4.0) and smart thermostats (attractive, 82% interest) for $100–$200/month premiums. The pipeline cleans surveys, segments by demographics, computes X/Y/Z scores and coefficients, and generates plots—enabling SQL-like queries for insights (e.g., 60% faster than raw CSV parsing) and ML foundations (e.g., clustering for retention prediction).

## Features
- **ETL Automation**: Scripts for survey import/cleaning, merging functional/dysfunctional data, and Excel exports.
- **Kano Classification**: Matrix-based categorization with satisfaction ((A+P)/total) and dissatisfaction (-(M+P)/total) coefficients.
- **Segmentation**: By age (25-29 to 40-45), city, living arrangement; 20+ customized scatter plots (X vs. Y, size=Z).
- **Query Efficiency**: Pandas-based analysis 60% faster than manual Excel; extensible for dashboards or ML (e.g., K-Means on preferences).
- **Insights Delivery**: Validates report findings like convenience amenities (fitness centers) for community engagement.

## Technologies
- pandas, numpy for data manipulation and quantification.
- seaborn, matplotlib for Kano visualizations.
- XlsxWriter for segmented outputs; openpyxl for validation.

## Setup

1. **Clone the Repository**:  
   `git clone https://github.com/DeanHak/kano-renter-analytics.git`  
   `cd kano-renter-analytics`

2. **Install Dependencies**:  
   `pip install -r requirements.txt` (includes pandas, numpy, matplotlib, seaborn, openpyxl, scikit-learn)

3. **Data Files**: Place raw CSV (`Residency_Reshaped_September_4_2024_10.55.csv`) in `/data/`.

4. **Run the Pipeline**:  
   - Clean and process: `python kano_pipeline.py` (generates `Kano_Worksheet.xlsx` and `/outputs/` plots).  
   - Segment example (age): `python segment_by_age.py` (exports per-group Excels).  

