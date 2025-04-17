import time
import mysql.connector
from mysql.connector import Error

def create_student_table_if_not_exists():
    for attempt in range(10):  # Retry up to 10 times
        try:
            conn = mysql.connector.connect(
                host='db',
                user='user',
                password='password',
                database='faceapp',
                port=3306
            )
            if conn.is_connected():
                cursor = conn.cursor()
                
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS student (
                    Student_id INT PRIMARY KEY,
                    Dep VARCHAR(45),
                    course VARCHAR(45),
                    Year VARCHAR(45),
                    Semester VARCHAR(45),
                    Name VARCHAR(45),
                    Division VARCHAR(45),
                    Roll VARCHAR(45),
                    Gender VARCHAR(45),
                    Dob VARCHAR(45),
                    Email VARCHAR(45),
                    Phone VARCHAR(45),
                    Address VARCHAR(45),
                    Teacher VARCHAR(45),
                    PhotoSample VARCHAR(45)
                )
                # """)
                conn.commit()
                print("✅ Student table checked/created.")
                cursor.close()
                conn.close()
                break
        except Error as e:
            print(f"⏳ Attempt {attempt+1}/10: DB not ready yet, retrying in 3s...")
            time.sleep(3)
    else:
        print("❌ Error: Could not connect to MySQL after 10 attempts.")
