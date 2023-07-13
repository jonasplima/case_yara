class data_cleaning_and_processing():
    
    def prepare_dataset(file_path):
        import pandas as pd
        import warnings 
        
        # The code `warnings.filterwarnings('ignore')` is used to ignore any warning messages that may be generated during the execution of the code. By setting it to 'ignore', the code will not display any warning messages, allowing the code to run without interruption.
        warnings.filterwarnings('ignore')
        
        # read the file 
        case_dataset = pd.read_csv(file_path, sep=";", decimal=',')
        
        # The code `case_dataset['user_reg_date'] = case_dataset['user_reg_date'].str.replace('.', '/')` is replacing all occurrences of the dot character '.' with the forward slash character '/' in 
        # the 'user_reg_date' and 'last_event_date' columns of the 'case_dataset' DataFrame. This is done to ensure that the date format is consistent and can be properly converted to a datetime format later on.
        case_dataset['user_reg_date'] = case_dataset['user_reg_date'].str.replace('.', '/')
        case_dataset['last_event_date'] = case_dataset['last_event_date'].str.replace('.', '/')
        
        # The code `case_dataset['user_reg_date'] = pd.to_datetime(case_dataset['user_reg_date'], format='%d/%m/%Y')` is converting the values in the 'user_reg_date', 'last_event_date', 'recommendation_generated_last_date'
        # 'map_created_last_date', 'monitoring_last_date', 'field_exploring_last_date' columns of the 'case_dataset' DataFrame from a string format to a datetime format. 
        # The format '%d/%m/%Y' specifies that the date is in the format day/month/year.
        case_dataset['user_reg_date'] = pd.to_datetime(case_dataset['user_reg_date'], format='%d/%m/%Y')
        case_dataset['last_event_date'] = pd.to_datetime(case_dataset['last_event_date'], format='%d/%m/%Y')
        case_dataset['recommendation_generated_last_date'] = pd.to_datetime(case_dataset['recommendation_generated_last_date'], format='%d/%m/%Y')
        case_dataset['map_created_last_date'] = pd.to_datetime(case_dataset['map_created_last_date'], format='%d/%m/%Y')
        case_dataset['monitoring_last_date'] = pd.to_datetime(case_dataset['monitoring_last_date'], format='%d/%m/%Y')
        case_dataset['field_exploring_last_date'] = pd.to_datetime(case_dataset['field_exploring_last_date'], format='%d/%m/%Y')
        
        # The code `case_dataset['user_type'] = case_dataset['user_type'].replace({'famer': 'farmer', 'advsor': 'advisor'}, regex=True)` is replacing specific values in the 'user_type' column of the 'case_dataset' DataFrame.
        case_dataset['user_type'] = case_dataset['user_type'].replace({'famer': 'farmer', 'advsor': 'advisor', 'Advisor': 'advisor'}, regex=True) 
        
        # The code `case_dataset['loyalty'] = case_dataset['loyalty'].apply(lambda x: True if x == 'Yes' else False)` is applying a lambda function to the 'loyalty' column of the 'case_dataset' DataFrame. If the cell contains YES, it is TRUE, otherwise it is FALSE.
        case_dataset['loyalty'] = case_dataset['loyalty'].apply(lambda x: True if x == 'Yes' else False)  
        
        # The code `case_dataset['main_crop'] = case_dataset['main_crop'].str.lstrip()` is removing any leading whitespace from the values in the 'main_crop' column of the 'case_dataset' DataFrame. 
        # This is done to ensure that there are no extra spaces before the crop names, which could cause issues when analyzing or grouping the data based on the crop names.
        case_dataset['main_crop'] = case_dataset['main_crop'].str.lstrip()
        
        return case_dataset

