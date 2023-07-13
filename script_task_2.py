if __name__ == '__main__':
    import sys 
    sys.path.append('python/main')     
    from task_2 import task_2_main
    
    # ------------------------------------------------------------------------------------------------------------
    # Bring the result for the question A of Task 2
    case_dataset_task_2_question_a, average_days = task_2_main.question_a()
    
    # Create a file with the result
    case_dataset_task_2_question_a.to_excel(r"output_file/dataset_task_2_question_a.xlsx", index = False)
    
    # print the data with the result
    print("A) How many days are there between the registration and last event from users in CC-BGX, CC-GUI and CC-PAM?")
    print("The average number of days between registration and the last event for users in the CC-BGX, CC-GUI, and CC-PAM business units is {:,.2f}. This information can be found in the variable 'case_dataset_task_2_question_a' by taking the average of the 'days_between' column. Also can be found at output_file/dataset_task_2_question_a.xlsx\n\n".format(average_days))
    
    # ------------------------------------------------------------------------------------------------------------
    # Bring the result for the question B of Task 2
    kpi_df, active_users, active_users_percent, active_fields, active_fields_percent, active_hectares, active_hectares_percent = task_2_main.question_b()
    
    # Create a file with the result
    kpi_df.to_excel(r"output_file/dataset_task_2_question_b.xlsx", index = False)
    
    # print the data with the result
    print("B) Please provide the values for the three previously explained KPIs, segmented by user_type. The reported values should include the metric in absolute value and it’s percentual contribution (e.g., 100 ha / 32%).")
    print(f"""
    The values for the three KPIs, segmented by user_type, are as follows:
    
               Active Users  Active Users %  Active Fields  Active Fields %  Active Hectares  Active Hectares %
    user_type
    advisor            {active_users['advisor']:6,}      {active_users_percent['advisor']:10,.2f}%   {active_fields['advisor']:14,}      {active_fields_percent['advisor']:15,.2f}%  {active_hectares['advisor']:16,.2f}      {active_hectares_percent['advisor']:17,.2f}%
    farmer             {active_users['farmer']:6,}      {active_users_percent['farmer']:10,.2f}%   {active_fields['farmer']:14,}      {active_fields_percent['farmer']:15,.2f}%  {active_hectares['farmer']:16,.2f}      {active_hectares_percent['farmer']:17,.2f}%
    \n
    For the user_type "advisor," there are {active_users['advisor']:,.0f} active users, which account for {active_users_percent['advisor']:,.2f}% of the total active users. The number of active fields is {active_fields['advisor']:,.0f}, contributing to {active_fields_percent['advisor']:,.2f}% of the total active fields. The active hectares for advisor users are {active_hectares['advisor']:,.2f}, representing {active_hectares_percent['advisor']:,.2f}% of the total active hectares.
    
    On the other hand, for the user_type "farmer," there are {active_users['farmer']:,.0f} active users, making up {active_users_percent['farmer']:,.2f}% of the total active users. The number of active fields is {active_fields['farmer']:,.0f}, accounting for {active_fields_percent['farmer']:,.2f}% of the total active fields. The active hectares for farmer users are {active_hectares['farmer']:,.2f}, representing {active_hectares_percent['farmer']:,.2f}% of the total active hectares.
    
    This information can be found in the variable 'kpi_df' and it is store at output_file/dataset_task_2_question_b.xlsx.
    """)