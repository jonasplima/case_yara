def main():
    import sys 
    import pandas as pd
    
    sys.path.append('python/function')
    
    from func_database import database_functions
    
    database = r"sql_database\case_yara.db"
    
    sql_script_task_1 = """SELECT 
                                users.yara_user_id as user_id
                                ,emp.bu_name as business_unit
                                ,emp.employee_name as employee
                                ,promo.promo_code as promo_code
                                ,users.user_reg_date as date_of_registration
                                ,count(distinct field.field_id) as total_number_of_fields
                                ,sum(case 
                                        when field.field_archived = 1 then 0
                                        else 1
                                    end) as total_number_of_active_fields
                                ,sum(field.field_area) as total_field_area
                                ,sum(case 
                                        when field.field_archived = 1 then 0
                                        else field.field_area
                                    end) as total_active_field_area
                            FROM user_table as users
                            INNER JOIN field_table as field ON field.yara_user_id = users.yara_user_id 
                            INNER JOIN service_account_table as serv_acc ON serv_acc.yara_user_id = users.yara_user_id 
                            INNER JOIN service_subscription_table as sub ON sub.account_id = serv_acc.account_id 
                            INNER JOIN promo_code_table as promo ON promo.promo_code = sub.promo_code
                            INNER JOIN employee_table as emp ON emp.employee_id = promo.employee_id 
                            GROUP BY 
                                users.yara_user_id """ 
    
    # create a database connection
    conn = database_functions.create_connection(db_file=database)
    
    # create tables
    if conn is not None:
        # create employee table
        dataset_task_1 = pd.read_sql(sql_script_task_1, conn)
        
        # close connection
        conn.close()   
        
        # return dataset_task_1
        return dataset_task_1 
        
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    dataset_task_1 = main()
    dataset_task_1.to_excel(r"output_file/dataset_task_1.xlsx", index = False)

