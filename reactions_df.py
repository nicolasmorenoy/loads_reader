import pandas as pd
from boa_ultimate_service import service, ultimate

def create_dataframe(file_path, sheet_name, service_list, ultimate_list):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=1)  # Assuming headers are in row 2
    # Drop the first three rows (assuming values start from row 4)
    df = df.iloc[3:]
    # Reset index
    df.reset_index(drop=True, inplace=True)
    
    # Add a new column "type"
    df['type'] = ''
    
    # Update "type" column based on conditions
    for index, row in df.iterrows():
        if row['Output Case'] in service_list:
            df.at[index, 'type'] = "Service"
        elif row['Output Case'] in ultimate_list:
            df.at[index, 'type'] = "Ultimate"
    
    return df

if __name__ == "__main__":
    # Specify the file path of the Excel file
    excel_file_path = "resources/loads.xlsx"
    
    # Specify the name of the sheet
    sheet_name = "Joint Reactions"

    # Define the filter lists for "Service" and "Ultimate"
    service_list = service
    ultimate_list = ultimate

    # Create the DataFrame
    joint_reactions_df = create_dataframe(excel_file_path, sheet_name, service_list, ultimate_list)

    # Display the DataFrame
    print("Joint Reactions DataFrame:")
    print(joint_reactions_df)
    
    service_joint_reactions_df = joint_reactions_df[joint_reactions_df['type'] == 'Service']
    ultimate_joint_reactions_df = joint_reactions_df[joint_reactions_df['type'] == 'Ultimate']


    print(ultimate_joint_reactions_df)