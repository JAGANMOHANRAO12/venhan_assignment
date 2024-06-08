import sqlite3  
def insert_student(name: str, grade: float):
   conn = sqlite3.connect('students.db')     
   cursor = conn.cursor()  
   cursor.execute('''INSERT INTO students (name, grade) VALUES (?, ?) ''', (name, grade))     
   conn.commit()     
   conn.close()

insert_student("jagan", 75.5) 
insert_student("mohan", 91.4)  
