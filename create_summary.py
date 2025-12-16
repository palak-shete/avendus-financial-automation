import pandas as pd

INPUT_FILE = "output.xlsx"
TARGET_YEAR = "2023"

TARGET_METRICS = {
    "Total Income": ["Total Income", "Revenue"],
    "EBITDA": ["EBITDA", "Profit / (Loss) before Interest"],
    "Finance Cost": ["Finance Cost"],
    "Net Profit": ["Net Profit", "Profit After Tax"],
    "Total Assets": ["Total Assets"],
    "Total Liabilities": ["Total Liabilities"]
}

def detect_header_row(df):
    for i in range(10):  # scan first 10 rows
        row_values = df.iloc[i].astype(str).str.lower()
        if row_values.str.contains("particular").any():
            return i
    return None

def create_summary():
    raw_df = pd.read_excel(INPUT_FILE, header=None)

    header_row = detect_header_row(raw_df)
    if header_row is None:
        raise Exception("Could not detect header row containing 'Particulars'")

    # Promote header row
    df = raw_df.iloc[header_row + 1:].copy()
    df.columns = raw_df.iloc[header_row]

    # Drop completely empty rows
    df = df.dropna(how="all")

    # Identify columns
    particulars_col = None
    year_col = None

    for col in df.columns:
        if "particular" in str(col).lower():
            particulars_col = col
        if TARGET_YEAR in str(col):
            year_col = col

    if not particulars_col or not year_col:
        raise Exception("Required columns not found after header normalization")

    summary_data = []

    for metric, keywords in TARGET_METRICS.items():
        for kw in keywords:
            match = df[df[particulars_col].astype(str).str.contains(kw, case=False, na=False)]
            if not match.empty:
                value = match.iloc[0][year_col]
                summary_data.append([metric, value])
                break

    summary_df = pd.DataFrame(summary_data, columns=["Metric", "Amount"])

    with pd.ExcelWriter(INPUT_FILE, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        summary_df.to_excel(writer, sheet_name="Summary", index=False)

    print("[SUCCESS] Summary sheet created successfully")

if __name__ == "__main__":
    create_summary()
