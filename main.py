import tkinter as tk
import sqlite3

cnt=sqlite3.connect("employee.sqlite")
cursor = cnt.cursor()

cursor.execute(f"PRAGMA table_info({'Departments'})")
result1 = cursor.fetchall()

cursor.execute(f"PRAGMA table_info({'Location'})")
result2 = cursor.fetchall()

cursor.execute(f"PRAGMA table_info({'Employee'})")
result3 = cursor.fetchall()

cursor.execute(f"PRAGMA table_info({'Education'})")
result4 = cursor.fetchall()

cursor.execute(f"PRAGMA foreign_keys = ON")

if len(result1) == 0:
    cnt.execute('''CREATE TABLE Departments(DeptID INTEGER PRIMARY KEY, [Department Name] Text);''')
if len(result2) == 0:
    cnt.execute('''CREATE TABLE Location(LocID Integer PRIMARY KEY, Location Text);''')
if len(result3) == 0:
    cnt.execute('''CREATE TABLE Employee(EmpID Integer PRIMARY KEY ,Name Text, Age Integer, Salary Real, DeptID Integer,LocID Integer, FOREIGN KEY(DeptID) REFERENCES Departments(DeptID),FOREIGN KEY(LocID) REFERENCES Location(LocID) );''')  
if len(result4) == 0:
    cnt.execute('''CREATE TABLE Education(EmpID Integer, [Education Level] Text, [Year of Passing] Integer,FOREIGN KEY(EmpID) REFERENCES Employee(EmpID) );''')



def get_id():
    user_input = entry.get()
    cursor.execute("SELECT COUNT(*) FROM Employee WHERE EmpID = ?", (user_input,))
    res = cursor.fetchone()[0]

    if res != 0:
        cnt.execute("BEGIN")
        cnt.execute("DELETE FROM Education WHERE EmpID = ?", (user_input,))
        cnt.execute("DELETE FROM Employee WHERE EmpID = ?", (user_input,))
        cnt.commit()
    cursor.close()
    cnt.close()
    new_window.destroy()

def delete_employee():
    # Destroy the main window
    window.destroy()

    # Create a new window
    global new_window
    new_window = tk.Tk()
    new_window.title("Delete Employee Information")
    
    # Create a label to describe the input field
    label_input = tk.Label(new_window, text="Enter Employee ID whose data is to be deleted")
    label_input.pack()
    
    global entry
    entry = tk.Entry(new_window)
    entry.pack()
    # Add contents to the new window
    button = tk.Button(new_window, text="Delete", command=get_id)
    button.pack()



def update_employee():
    # Destroy the main window
    window.destroy()

    # Create a new window
    global new_window
    new_window = tk.Tk()
    new_window.title("Update Employee Information")
    
    # Create a label to describe the input field
    label_input = tk.Label(new_window, text="Enter Employee ID whose data is to be updated")
    label_input.pack()
    
    global entry
    entry = tk.Entry(new_window)
    entry.pack()
    # Add contents to the new window
    button = tk.Button(new_window, text="Update Info", command=id_info)
    button.pack()

def id_info():
    global idd
    idd = entry.get()
    cursor.execute("SELECT COUNT(*) FROM Employee WHERE EmpID = ?", (idd,))
    res = cursor.fetchone()[0]

    if res == 0:
        new_window.destroy()
        windw = tk.Tk()
        windw.title("Error")
    
        # Create a label
        label_input = tk.Label(windw, text="Entered Employee ID doesn't exist in the database", fg="red")
        label_input.pack()     
        new_button = tk.Button(windw, text="Close", command=windw.destroy)
        new_button.pack() 
    else:
        update_info()

def update_info():
    # Destroy the main window
    new_window.destroy()

    # Create a new window 
    global new_window2
    new_window2 = tk.Tk()
    new_window2.title("Update Employee Information")

    table_label = tk.Label(new_window2, text="Only input data to be changed (Input is Case Sensitive)")
    table_label.grid(row=0,column=0)

    cursor.execute("SELECT * FROM Employee WHERE EmpID = ?", (idd,))
    existing_info = cursor.fetchone()

    cursor.execute("SELECT [Department Name] FROM Departments WHERE DeptID = ?", (existing_info[4],))
    existing_dep_info = cursor.fetchone()

    cursor.execute("SELECT Location FROM Location WHERE LocID = ?", (existing_info[5],))
    existing_loc_info = cursor.fetchone()

    cursor.execute("SELECT [Education Level], [Year of Passing] FROM Education WHERE EmpID = ?", (idd,))
    existing_edu_info = cursor.fetchone()


    # Create a label to describe the input field
    existing_id_label = tk.Label(new_window2, text="ID: " +str( existing_info[0]))
    existing_id_label.grid(row=1,column=1)    
    
    existing_name_label = tk.Label(new_window2, text="Name: " + existing_info[1])
    existing_name_label.grid(row=2,column=0)  
    global entry1
    entry1_label = tk.Label(new_window2, text="Name:")
    entry1_label.grid(row=2,column=1)  
    entry1 = tk.Entry(new_window2)
    entry1.grid(row=2,column=3)  

    existing_age_label = tk.Label(new_window2, text="Age: " + str(existing_info[2]))
    existing_age_label.grid(row=4,column=0)  
    global entry2
    entry2_label = tk.Label(new_window2, text="Age:")
    entry2_label.grid(row=4,column=1)  
    entry2 = tk.Entry(new_window2)
    entry2.grid(row=4,column=3)  

    existing_salary_label = tk.Label(new_window2, text="Salary: " + str(existing_info[3]))
    existing_salary_label.grid(row=6,column=0)  
    global entry3
    entry3_label = tk.Label(new_window2, text="Salary:")
    entry3_label.grid(row=6,column=1)  
    entry3 = tk.Entry(new_window2)
    entry3.grid(row=6,column=3)  

    existing_dep_label = tk.Label(new_window2, text="Department: " + existing_dep_info[0])
    existing_dep_label.grid(row=8,column=0)  
    global entry4
    entry4_label = tk.Label(new_window2, text="Department:")
    entry4_label.grid(row=8,column=1)  
    entry4 = tk.Entry(new_window2)
    entry4.grid(row=8,column=3)  

    existing_loc_label = tk.Label(new_window2, text="Location: " + existing_loc_info[0])
    existing_loc_label.grid(row=10,column=0)  
    global entry5
    entry5_label = tk.Label(new_window2, text="Location:")
    entry5_label.grid(row=10,column=1)  
    entry5 = tk.Entry(new_window2)
    entry5.grid(row=10,column=3)  

    existing_edu_label = tk.Label(new_window2, text="Education Level: " + existing_edu_info[0])
    existing_edu_label.grid(row=12,column=0)  
    global entry6
    entry6_label = tk.Label(new_window2, text="Education Level:")
    entry6_label.grid(row=12,column=1)  
    entry6 = tk.Entry(new_window2)
    entry6.grid(row=12,column=3)  

    existing_yrop_label = tk.Label(new_window2, text="Yr of Passing: " + str(existing_edu_info[1]))
    existing_yrop_label.grid(row=14,column=0)  
    global entry7
    entry7_label = tk.Label(new_window2, text="Year of passing:")
    entry7_label.grid(row=14,column=1)  
    entry7 = tk.Entry(new_window2)
    entry7.grid(row=14,column=3)  


    # Add contents to the new window
    button = tk.Button(new_window2, text="Update Info", command=on_select)
    button.grid(row=16,column=1)  

def on_select():
    name_value = entry1.get()
    age_value = entry2.get()
    sal_value = entry3.get()
    dep_value = entry4.get()
    loc_value = entry5.get()
    edulevel_value = entry6.get()
    yrofpass_value = entry7.get()

    if len(name_value) !=0:
        cursor.execute("Update Employee SET Name = ? WHERE EmpID = ?", (name_value, idd))
    if len(age_value) !=0:
        cursor.execute("Update Employee SET Age = ? WHERE EmpID = ?", (age_value, idd))
    if len(sal_value) !=0:    
        cursor.execute("Update Employee SET Salary = ? WHERE EmpID = ?", (sal_value, idd))
    if len(edulevel_value) !=0:     
        cursor.execute("Update Education SET [Education Level] = ? WHERE EmpID = ?", (edulevel_value, idd))
    if len(yrofpass_value) !=0:  
        cursor.execute("Update Education SET [Year of Passing] = ? WHERE EmpID = ?", (yrofpass_value, idd))
    if len(dep_value) !=0:
        cursor.execute("Select DeptID From Departments WHERE [Department Name] = ?", (dep_value,))
        result = cursor.fetchall()
        if len(result) == 0:
            cursor.execute("Insert into Departments([Department Name]) Values(?)", (dep_value,))
            cursor.execute("Select * From Departments WHERE [Department Name] = ?", (dep_value,))
            result = cursor.fetchone()[0]
        else:
            cursor.execute("Select * From Departments WHERE [Department Name] = ?", (dep_value,))
            result = cursor.fetchone()[0]
        update_query = "UPDATE Employee SET DeptID = ? WHERE EmpID = ?"
        cursor.execute(update_query, (result, idd))

    if len(loc_value) !=0:
        cursor.execute("Select LocID From Location WHERE Location = ?", (loc_value,))
        result = cursor.fetchall()
        if len(result) == 0:
            cursor.execute("Insert into Location([Location]) Values(?)", (loc_value,))
            cursor.execute("Select LocID From Location WHERE Location = ?", (loc_value,))
            result = cursor.fetchone()[0]
        else:
            cursor.execute("Select * From Location WHERE Location = ?", (loc_value,))
            result = cursor.fetchone()[0]
        update_query = "UPDATE Employee SET LocID = ? WHERE EmpID = ?"
        cursor.execute(update_query, (result, idd))

    cnt.commit()
    cursor.close()
    cnt.close()
    new_window2.destroy()



def insert_employee():
    window.destroy()

    # Create a new window 
    global new_window2
    new_window2 = tk.Tk()
    new_window2.title("Insert Employee Information")

    table_label = tk.Label(new_window2, text="Input Data (Input is Case Sensitive)")
    table_label.pack()

    # Create a label to describe the input field
    global entry
    entry_label = tk.Label(new_window2, text="Employee ID:")
    entry_label.pack()
    entry = tk.Entry(new_window2)
    entry.pack()

    global entry1
    entry1_label = tk.Label(new_window2, text="Name:")
    entry1_label.pack()
    entry1 = tk.Entry(new_window2)
    entry1.pack()

    global entry2
    entry2_label = tk.Label(new_window2, text="Age:")
    entry2_label.pack()
    entry2 = tk.Entry(new_window2)
    entry2.pack()

    global entry3
    entry3_label = tk.Label(new_window2, text="Sal:")
    entry3_label.pack()
    entry3 = tk.Entry(new_window2)
    entry3.pack()

    global entry4
    entry4_label = tk.Label(new_window2, text="Department:")
    entry4_label.pack()
    entry4 = tk.Entry(new_window2)
    entry4.pack()

    global entry5
    entry5_label = tk.Label(new_window2, text="Location:")
    entry5_label.pack()
    entry5 = tk.Entry(new_window2)
    entry5.pack()

    global entry6
    entry6_label = tk.Label(new_window2, text="Education Level:")
    entry6_label.pack()
    entry6 = tk.Entry(new_window2)
    entry6.pack()

    global entry7
    entry7_label = tk.Label(new_window2, text="Year of passing:")
    entry7_label.pack()
    entry7 = tk.Entry(new_window2)
    entry7.pack()
   
    # Add contents to the new window
    button = tk.Button(new_window2, text="Update Info", command=insert_info)
    button.pack()

def insert_info():
    id_value = entry.get()
    name_value = entry1.get()
    age_value = entry2.get()
    sal_value = entry3.get()
    dep_value = entry4.get()
    loc_value = entry5.get()
    edulevel_value = entry6.get()
    yrofpass_value = entry7.get()

    cursor.execute("Select * From Employee WHERE EmpID = ?", (id_value,))
    res = cursor.fetchall()
    if len(res)!=0:
        new_window2.destroy()
        windw = tk.Tk()
        windw.title("Error")
    
        # Create a label
        label_input = tk.Label(windw, text="Entered Employee ID already exists in the database", fg="red")
        label_input.pack()     
        new_button = tk.Button(windw, text="Close", command=windw.destroy)
        new_button.pack() 
    
    cursor.execute("Select DeptID From Departments WHERE [Department Name] = ?", (dep_value,))
    result = cursor.fetchall()
    if len(result) == 0:
        cursor.execute("Insert into Departments([Department Name]) Values(?)", (dep_value,))
        cursor.execute("Select * From Departments WHERE [Department Name] = ?", (dep_value,))
        result = cursor.fetchone()[0]
    else:
        cursor.execute("Select * From Departments WHERE [Department Name] = ?", (dep_value,))
        result = cursor.fetchone()[0]

    
    cursor.execute("Select LocID From Location WHERE Location = ?", (loc_value,))
    result2 = cursor.fetchall()
    if len(result2) == 0:
        cursor.execute("Insert into Location([Location]) Values(?)", (loc_value,))
        cursor.execute("Select LocID From Location WHERE Location = ?", (loc_value,))
        result2 = cursor.fetchone()[0]
    else:
        cursor.execute("Select * From Location WHERE Location = ?", (loc_value,))
        result2 = cursor.fetchone()[0]
 
    

    cursor.execute("Insert into Employee(EmpID, Name, Age, Salary, DeptID, LocID) Values(?,?,?,?,?,?)", (id_value,name_value,age_value,sal_value,result,result2))
    cursor.execute("Insert into Education(EmpID, [Education Level], [Year of Passing]) Values(?,?,?)", (id_value,edulevel_value,yrofpass_value))

    cnt.commit()
    cursor.close()
    cnt.close()
    new_window2.destroy()



def get_info():
    idd = entry.get()
    cursor.execute("SELECT COUNT(*) FROM Employee WHERE EmpID = ?", (idd,))
    res = cursor.fetchone()[0]

    if res == 0:
        new_window.destroy()
        windw = tk.Tk()
        windw.title("Error")
    
        # Create a label
        label_input = tk.Label(windw, text="Entered Employee ID doesn't exists in the database", fg="red")
        label_input.pack()     
        new_button = tk.Button(windw, text="Close", command=windw.destroy)
        new_button.pack() 
    else:
        new_window.destroy()
        new_window2 = tk.Tk()
        new_window2.title("Employee Data")
        cursor.execute("SELECT * FROM Employee WHERE EmpID = ?", (idd,))
        existing_info = cursor.fetchone()
        
        existing_id_label = tk.Label(new_window2, text="ID: " +str( existing_info[0]))
        existing_id_label.pack()
        
        existing_name_label = tk.Label(new_window2, text="Name: " + existing_info[1])
        existing_name_label.pack()

        existing_age_label = tk.Label(new_window2, text="Age: " + str(existing_info[2]))
        existing_age_label.pack()

        existing_salary_label = tk.Label(new_window2, text="Salary: " + str(existing_info[3]))
        existing_salary_label.pack()

        cursor.execute("SELECT [Department Name] FROM Departments WHERE DeptID = ?", (existing_info[4],))
        existing_dep_info = cursor.fetchone()
        existing_dep_label = tk.Label(new_window2, text="Department: " + existing_dep_info[0])
        existing_dep_label.pack()

        cursor.execute("SELECT Location FROM Location WHERE LocID = ?", (existing_info[5],))
        existing_loc_info = cursor.fetchone()
        existing_loc_label = tk.Label(new_window2, text="Location: " + existing_loc_info[0])
        existing_loc_label.pack()

        cursor.execute("SELECT [Education Level], [Year of Passing] FROM Education WHERE EmpID = ?", (idd,))
        existing_edu_info = cursor.fetchone()
        existing_edu_label = tk.Label(new_window2, text="Education Level: " + existing_edu_info[0])
        existing_edu_label.pack()

        existing_yrop_label = tk.Label(new_window2, text="Yr of Passing: " + str(existing_edu_info[1]))
        existing_yrop_label.pack()
        cursor.close()
        cnt.close()
    
def select_employee():
    # Destroy the main window
    window.destroy()

    # Create a new window
    global new_window
    new_window = tk.Tk()
    new_window.title("Display Employee Information")
    
    # Create a label to describe the input field
    label_input = tk.Label(new_window, text="Enter Employee ID whose data is to be displayed")
    label_input.pack()
    
    global entry
    entry = tk.Entry(new_window)
    entry.pack()
    # Add contents to the new window
    button = tk.Button(new_window, text="Select", command=get_info)
    button.pack()

# Create the main window
window = tk.Tk()
window.title("Employee Database")

# Create buttons to open a new window
delete_button = tk.Button(window, text="Delete", command= delete_employee)
update_button = tk.Button(window, text="Update", command= update_employee)
insert_button = tk.Button(window, text="Insert", command= insert_employee)
select_button = tk.Button(window, text="Select", command= select_employee)
# Pack the button
insert_button.pack()
update_button.pack()
select_button.pack()
delete_button.pack()
window.mainloop()
