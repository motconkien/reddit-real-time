from etls.aws_etl import *
import os

def aws_pipeline(ti):
    file_path = ti.xcom_pull(task_ids='reddit_extraction')
    print(f"[DEBUG] File path from XCom: {file_path}")
    print(f"[DEBUG] File exists: {os.path.exists(file_path)}")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    #conenct to s3
    s3 = connect_to_s3()

    #create bucket 
    create_bucket(s3)

    #loadfile
    s3_key = f"raw/{os.path.basename(file_path)}"

    load_to_s3(s3,file_path, s3_key)