from file_reader import read_excel_column

def load_cases():
    # Specify the file path of the Excel file
    excel_file_path = "resources/loads.xlsx"

    # Specify the name of the sheet
    sheet_name = "Load Cases - Summary"

    # Specify the column name
    column_name = "A"

    # Specify the starting row
    start_row = 4

    # Read the values in the specified column starting from the specified row
    values = read_excel_column(excel_file_path, sheet_name, column_name, start_row)
    return  values

def load_combinations():
    # Specify the file path of the Excel file
    excel_file_path = "resources/loads.xlsx"

    # Specify the name of the sheet
    sheet_name = "Load Combination Definitions"

    # Specify the column name
    column_name = "A"

    # Specify the starting row
    start_row = 4

    # Read the values in the specified column starting from the specified row
    values = read_excel_column(excel_file_path, sheet_name, column_name, start_row)
    values = set(values)
    values = list(values)
    return  values

if __name__ == "__main__":
    pass
