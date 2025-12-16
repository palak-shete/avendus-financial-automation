import pdfplumber
import pandas as pd

def extract_pdf_to_excel(pdf_path, output_path="output.xlsx"):
    tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            table = page.extract_table()
            if table:
                df = pd.DataFrame(table)
                tables.append(df)
                print(f"[INFO] Extracted table from page {i+1}")

    if not tables:
        print("[WARNING] No tables found in the PDF.")
        return

    # Combine all extracted tables
    final_df = pd.concat(tables, ignore_index=True)

    # Clean: remove empty rows and fix header
    final_df = final_df.dropna(how="all")
    final_df.columns = final_df.iloc[0]         # first row as header
    final_df = final_df[1:]                     # remove header row

    final_df.to_excel(output_path, index=False)
    print(f"[SUCCESS] Data extracted to: {output_path}")


if __name__ == "__main__":
    extract_pdf_to_excel("sample.pdf")
