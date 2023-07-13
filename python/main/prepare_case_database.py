def prepare_database_main():
    import sys 
    
    sys.path.append('python/function')
    
    from func_database import database_functions
    
    database = r"sql_database\case_yara.db"
    
    sql_employee_table = """CREATE TABLE IF NOT EXISTS employee_table (
                            employee_id integer PRIMARY KEY, 
                            employee_name text, 
                            bu_name text, 
                            is_valid integer
                        )"""
                        
    sql_user_table = """CREATE TABLE IF NOT EXISTS user_table (
                        yara_user_id integer PRIMARY KEY, 
                        user_type text, 
                        user_reg_date text,
                        last_event_date text, 
                        days_since_last_visit integer
                    )"""
                    
    sql_field_table = """CREATE TABLE field_table (
                            field_id INTEGER,
                            yara_user_id INTEGER,
                            field_archived INTEGER,
                            field_area INTEGER,
                            crop TEXT,
                            CONSTRAINT field_table_PK PRIMARY KEY (field_id),
                            CONSTRAINT field_table_FK FOREIGN KEY (yara_user_id) REFERENCES user_table(yara_user_id)
                        );"""
    
    sql_service_account_table = """CREATE TABLE IF NOT EXISTS service_account_table (
                                account_id integer, 
                                account_number integer, 
                                created_date text,
                                yara_user_id INTEGER,
                                CONSTRAINT service_account_table_PK PRIMARY KEY (account_id),
                                CONSTRAINT service_account_table_FK FOREIGN KEY (yara_user_id) REFERENCES user_table(yara_user_id)
                            )"""
    
    sql_promo_code_table = """CREATE TABLE IF NOT EXISTS promo_code_table (
                                promo_code integer, 
                                employee_id integer,
                                is_valid integer,
                                CONSTRAINT promo_code_table_PK PRIMARY KEY (promo_code),
                                CONSTRAINT promo_code_table_FK FOREIGN KEY (employee_id) REFERENCES employee_table(employee_id)
                            )""" 
    
    sql_service_subscription_table = """CREATE TABLE IF NOT EXISTS service_subscription_table (
                                    subscription_id integer, 
                                    account_id integer,
                                    created_date text, 
                                    promo_code integer,
                                    CONSTRAINT service_subscription_table_PK PRIMARY KEY (subscription_id),
                                    CONSTRAINT service_subscription_table_account_id_FK FOREIGN KEY (account_id) REFERENCES service_account_table(account_id),
                                    CONSTRAINT service_subscription_table_promo_code_FK FOREIGN KEY (promo_code) REFERENCES promo_code_table(promo_code)
                                )""" 
    
    # create a database connection
    conn = database_functions.create_connection(db_file=database)
    
    # create tables
    if conn is not None:
        # create employee table
        database_functions.create_table_structure(conn, sql_employee_table)
        
        # create user table
        database_functions.create_table_structure(conn, sql_user_table)
        
        # create field table
        database_functions.create_table_structure(conn, sql_field_table)
        
        # create service account table
        database_functions.create_table_structure(conn, sql_service_account_table)
        
        # create promo code table
        database_functions.create_table_structure(conn, sql_promo_code_table)
        
        # create service subscription table
        database_functions.create_table_structure(conn, sql_service_subscription_table)
        
        conn.close()    
        
    else:
        print("Error! cannot create the database connection.")