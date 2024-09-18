db = {
    "E101": {
        "First Name": "Rohit",
        "Last Name": "Bhavsar",
        "City": "Pune",
        "Salary": 25000,
        "Department": "Testing"
    },
    "E102": {
        "First Name": "Rutik",
        "Last Name": "Choudhari",
        "City": "Dehu",
        "Salary": 30000,
        "Department": "Management"
    },
    "E103": {
        "First Name": "Rohan", 
        "Last Name": "Datar",
        "City": "Alandi",
        "Salary": 35000,
        "Department": "Development"
    },
    "E104": {
        "First Name": "Ramesh",
        "Last Name": "Thakur",
        "City": "Karad",
        "Salary": 28000,
        "Department": "Deployment"
    },
}

print("-"*85)
print(f"{" "*32} Employee Management System")
print("-"*85)
while True:
    print(f"""
        {' '*25}--x-x-x--DASHBOARD--x-x-x-- \n
        {' '*25}1. Add Employee Details
        {' '*25}2. Display Employee Details
        {' '*25}3. Update Employee Details
        {' '*25}4. Delete Employee Details 
        {' '*25}5. Apply Filter 
        {' '*25}6. Quit 
        """)

    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        emp_id = input("Enter Employee ID: ").capitalize()
        fname = input("Enter Employee's First Name: ").capitalize()
        lname = input("Enter Employee's Last Name: ").capitalize()
        city = input("Enter Employee's City: ").capitalize()
        salary = eval(input("Enter Employee's Salary: "))
        department = input("Enter Name of Department: ").capitalize()
        
        db[emp_id] = {"First Name":fname, "Last Name":lname, "City": city, "Salary": salary, "Department": department}
        print("\nEmployee details added successfully.")

    elif ch == 2:
        print("-"*87)
        print("|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^15}|".format("Emp.ID","First Name","Last Name","City","Salary","Department"))
        print("-"*87)
        for i in db:
            print("|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^15}|".format(i, db[i]["First Name"], db[i]["Last Name"], db[i]["City"], db[i]["Salary"], db[i]["Department"]))
            print("-"*87)
            
    elif ch == 3:
        emp_id = input("Enter Employee ID: ").capitalize()
        print(f"""
        {' '*25}--x-x-x--Select to Update--x-x-x-- \n
        {' '*36}1. First Name
        {' '*36}2. Last Name
        {' '*36}3. City
        {' '*36}4. Salary
        {' '*36}5. Department
        """)
        ch = int(input("Choose what to update: "))
        if ch == 1:
            ufname = input("Enter updated First Name: ").capitalize()
            db[emp_id]["First Name"] = ufname
            print("\nFirst Name Updated Successfully.")
        elif ch == 2:
            ulname = input("Enter updated Last Name: ").capitalize()
            db[emp_id]["Last Name"] = ulname
            print("\nLast Name Updated Successfully.")
        elif ch == 3:
            ucity = input("Enter updated City: ").capitalize()
            db[emp_id]["City"] = ucity
            print("\nCity Updated Successfully.")
        elif ch == 4:
            usalary = eval(input("Enter updated Salary: "))
            db[emp_id]["Salary"] = usalary
            print("\nSalary Updated Successfully.")
        elif ch == 5:
            udepartment = input("Enter updated Name of Department: ").capitalize()
            db[emp_id]["Department"] = udepartment
            print("\nDepartment Name Updated Successfully.")
        else:
            print("\nInvalid Choice!")
    elif ch == 4:
        emp_id = input("Enter Employee ID: ").capitalize()
        del(db[emp_id])
        print("\nData deleted successfully.")
    elif ch == 5:
        print(f"""
        {' '*25}--x-x-x--Filter By--x-x-x-- \n
        {' '*36}1. First Name
        {' '*36}2. Last Name
        {' '*36}3. City
        {' '*36}4. Salary
        {' '*36}5. Department
        """)
        ch = int(input("Apply Filter To: "))
        if ch == 1:
            f_fname = input("Enter First Name: ").capitalize()
            print("-"*87)
            print("|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^15}|".format("Emp.ID","First Name","Last Name","City","Salary","Department"))
            print("-"*87)
            for i in db:
                if db[i]["First Name"] == f_fname:
                    print("|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^15}|".format(i, db[i]["First Name"], db[i]["Last Name"], db[i]["City"], db[i]["Salary"], db[i]["Department"]))
                    print("-"*87)        
        if ch == 2:
            f_lname = input("Enter Last Name: ").capitalize()
            print("-"*87)
            print("|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^15}|".format("Emp.ID","First Name","Last Name","City","Salary","Department"))
            print("-"*87)
            for i in db:
                if db[i]["Last Name"] == f_lname:
                    print("|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^15}|".format(i, db[i]["First Name"], db[i]["Last Name"], db[i]["City"], db[i]["Salary"], db[i]["Department"]))
                    print("-"*87)        
        elif ch == 3:
            f_city = input("Enter City: ").capitalize()
            print("-"*87)
            print("|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^15}|".format("Emp.ID","First Name","Last Name","City","Salary","Department"))
            print("-"*87)
            for i in db:
                if db[i]["City"] == f_city:
                    print("|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^15}|".format(i, db[i]["First Name"], db[i]["Last Name"], db[i]["City"], db[i]["Salary"], db[i]["Department"]))
                    print("-"*87)        
        elif ch == 4:
            f_salary = eval(input("Enter Salary: "))
            print("-"*87)
            print("|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^15}|".format("Emp.ID","First Name","Last Name","City","Salary","Department"))
            print("-"*87)
            for i in db:
                if db[i]["Salary"] == f_salary:
                    print("|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^15}|".format(i, db[i]["First Name"], db[i]["Last Name"], db[i]["City"], db[i]["Salary"], db[i]["Department"]))
                    print("-"*87)        
        elif ch == 5:
            f_department = input("Enter Name of Department: ").capitalize()
            print("-"*87)
            print("|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^15}|".format("Emp.ID","First Name","Last Name","City","Salary","Department"))
            print("-"*87)
            for i in db:
                if db[i]["Department"] == f_department:
                    print("|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^15}|".format(i, db[i]["First Name"], db[i]["Last Name"], db[i]["City"], db[i]["Salary"], db[i]["Department"]))
                    print("-"*87)
        else:
            print("\nInvalid Filter!")
        print("\nFilter Applied Successfully.")
    elif ch == 6:
        break
    else:
        print("\nInvalid Input")
