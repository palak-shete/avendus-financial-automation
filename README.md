# Avendus Financial Report Automation (Python + Power BI)

This project automates a real-world analyst workflow commonly used in
investment banking and wealth management firms like Avendus.

## Problem
Financial analysts spend significant time manually extracting data from
PDF reports, cleaning Excel sheets, and preparing management dashboards.

## Solution
An end-to-end automation pipeline that:
1. Extracts raw financial tables from PDF reports
2. Handles noisy, shifted headers from real-world PDFs
3. Cleans and normalizes the data using Python
4. Generates a summarized financial layer automatically
5. Feeds the clean data into Power BI for KPI dashboards and visuals

## Workflow
PDF → Python Extraction → Data Normalization → Summary Sheet → Power BI Dashboard

## Tech Stack
- Python
- pandas
- pdfplumber
- openpyxl
- Power BI

## Key Features
- Automatic header detection from messy PDFs
- Programmatic creation of summary financial metrics
- KPI-ready data model for Power BI
- Eliminates manual Excel work for analysts

## Files
- extractor.py – Extracts tables from PDF to Excel
- create_summary.py – Creates clean summary layer automatically
- output_with_summary.xlsx – Final Power BI-ready dataset
- Avendus_Automated_Financial_Report.pbix – Power BI dashboard

## Outcome
This automation reduces analyst reporting time from hours to minutes and
demonstrates how Python can be used to support financial reporting and MIS.
