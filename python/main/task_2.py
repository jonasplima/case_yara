
class task_2_main():
    
    def question_a():
        import sys 
        import pandas as pd
        from datetime import datetime
        sys.path.append('python/function')
        from data_cleaning_and_processing import data_cleaning_and_processing
        
        # Load the dataset
        case_dataset = data_cleaning_and_processing.prepare_dataset(r"dataset_provided\agtech_use_case.csv")
        
        # --------------------------------------------------------------------------------------------------------------------------------
        # A – How many days are there between the registration and last event from users in CC-BGX, CC-GUI and CC-PAM?  
        # --------------------------------------------------------------------------------------------------------------------------------
        
        # Filter the dataset for users in CC-BGX, CC-GUI, and CC-PAM business units
        filtered_case_dataset = case_dataset.loc[case_dataset['bu_name'].isin(['CC-BGX', 'CC-GUI', 'CC-PAM'])] 
        
        # Calculate the number of days between registration and last event
        filtered_case_dataset['days_between'] = (filtered_case_dataset['last_event_date'] - filtered_case_dataset['user_reg_date']).dt.days
        
        # Calculate the average number of days between registration and last event
        average_days = filtered_case_dataset['days_between'].mean()
        
        # Print the average number of days 
        return filtered_case_dataset, average_days
    
    
    def question_b():
        import sys 
        import pandas as pd
        from datetime import datetime
        sys.path.append('python/function')
        from data_cleaning_and_processing import data_cleaning_and_processing
        
        # Load the dataset
        case_dataset = data_cleaning_and_processing.prepare_dataset(r"dataset_provided\agtech_use_case.csv")
        # --------------------------------------------------------------------------------------------------------------------------------
        # B – Please provide the values for the three previously explained KPIs, segmented by user_type. The reported values should 
        # include the metric in absolute value and it’s percentual contribution (e.g., 100 ha / 32%).
        # --------------------------------------------------------------------------------------------------------------------------------
        
        # Set the float format option
        pd.options.display.float_format = '{:.2f}'.format
        
        # Calculate the current date for churn calculation
        current_date = pd.to_datetime('today')
        
        ### Active users: users that have used the app at least once in the last 12-rolling months. If last event is earlier than that, the user is considered to have churned.
        # Calculate active users
        active_users = case_dataset[case_dataset['last_event_date'] >= current_date - pd.DateOffset(years=1)].groupby('user_type')['id'].nunique()
        
        ### Active fields: non-archived fields belonging to active users.
        # Calculate active fields
        active_fields = case_dataset[(case_dataset['last_event_date'] >= current_date - pd.DateOffset(years=1)) & (~case_dataset['n_active_fields'].isnull())].groupby('user_type')['n_active_fields'].sum()
        
        ### Active hectares: field area belonging to active fields.
        # Calculate active hectares
        active_hectares = case_dataset[(case_dataset['last_event_date'] >= current_date - pd.DateOffset(years=1)) & (~case_dataset['total_active_field_area'].isnull())].groupby('user_type')['total_active_field_area'].sum()
        
        # Calculate percentual contribution
        active_users_percent = (active_users / active_users.sum()) * 100
        active_fields_percent = (active_fields / active_fields.sum()) * 100
        active_hectares_percent = (active_hectares / active_hectares.sum()) * 100
        
        # Create a new DataFrame to store the results
        kpi_df = pd.DataFrame({
            'Active Users': active_users,
            'Active Users %': active_users_percent,
            'Active Fields': active_fields,
            'Active Fields %': active_fields_percent,
            'Active Hectares': active_hectares,
            'Active Hectares %': active_hectares_percent
        })
        
        # return the KPIs segmented by user_type
        return kpi_df, active_users, active_users_percent, active_fields, active_fields_percent, active_hectares, active_hectares_percent
    
