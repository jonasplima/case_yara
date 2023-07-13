if __name__ == '__main__':
    import sys 
    sys.path.append('python/main')    
    from prepare_case_database import prepare_database_main    
    from dataset_task_1 import task_1_main 
    
    prepare_database_main()
    
    dataset_task_1 = task_1_main()
    dataset_task_1.to_excel(r"output_file/dataset_task_1.xlsx", index = False)
