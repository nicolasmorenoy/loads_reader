import openpyxl

def read_excel_column(file_path, sheet_name, column_name, start_row):
    # Load the Excel workbook
    wb = openpyxl.load_workbook(file_path)

    # Get the specified sheet
    sheet = wb[sheet_name]

    # Initialize an empty list to store the values
    values = []

    # Iterate over the rows starting from the specified row
    for row in sheet.iter_rows(min_row=start_row, min_col=1, max_col=1, values_only=True):
        # Append the value in the specified column to the list
        values.append(row[0])

    return values

if __name__ == "__main__":
    pass