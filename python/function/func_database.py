class database_functions():
    
    def __init__(self):
        pass
        
    @staticmethod
    def create_database(db_file):
        """ create a database connection to a SQLite database """
        
        import sqlite3
        from sqlite3 import Error
        
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version) 
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
                
    @staticmethod
    def create_connection(db_file):
        """ create a database connection to a SQLite database """
        
        import sqlite3
        from sqlite3 import Error
        
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        finally:
            if conn:
                return conn
    
    @staticmethod
    def create_table_structure(conn, create_table_sql):
        """ create a table from the create_table_structure statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        
        import sqlite3
        from sqlite3 import Error 
        
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)


if __name__ == '__main__':
    conn = database_functions.create_database(db_file=r"sql_database\case_yara.db")

