db = {
    101: {
        "Name": "Rohit",
        "City": "Pune",
        "Percentage": 89,
        "Course Name": "Python"
    },
    102: {
        "Name": "Rutik",
        "City": "Dehu",
        "Percentage": 90,
        "Course Name": "Python"
    },
    103: {
        "Name": "Rohan",
        "City": "Alandi",
        "Percentage": 87,
        "Course Name": "Java"
    },
    104: {
        "Name": "Rohit",
        "City": "Karad",
        "Percentage": 85,
        "Course Name": "Java"
    },
}

print("-"*85)
print(f"{" "*32} Student Management System")
print("-"*85)
while True:
    print(f"""
        {' '*25}--x-x-x--DASHBOARD--x-x-x-- \n
        {' '*25}1. Add Student Details
        {' '*25}2. Display Student Details
        {' '*25}3. Update Student Details
        {' '*25}4. Delete Student Details 
        {' '*25}5. Apply Filter 
        {' '*25}6. Quit 
        """)

    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        reg_no = eval(input("Enter Registration Number: "))
        name = input("Enter Student Name: ").capitalize()
        city = input("Enter Student's City: ").capitalize()
        percentage = eval(input("Enter Student's Percentage: "))
        course = input("Enter Name of Enrolled Course: ").capitalize()
        
        db[reg_no] = {"Name":name, "City": city, "Percentage": percentage, "Course Name": course}
        print("\nStudent details added successfully...")

    elif ch == 2:
        print("-"*85)
        print("|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|".format("Reg.No","Name","City","Percentage","Course"))
        print("-"*85)
        for i in db:
            print("|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|".format(i, db[i]["Name"], db[i]["City"], db[i]["Percentage"], db[i]["Course Name"]))
            print("-"*85)
            
    elif ch == 3:
        reg_no = eval(input("Enter Registration Number: "))
        print(f"""
        {' '*25}--x-x-x--Select to Update--x-x-x-- \n
        {' '*36}1. Name
        {' '*36}2. City
        {' '*36}3. Percentage
        {' '*36}4. Course Name
        """)
        ch = int(input("Choose what to update: "))
        if ch == 1:
            uname = input("Enter updated Name: ").capitalize()
            db[reg_no]["Name"] = uname
            print("\nName Updated Successfully...")
        elif ch == 2:
            ucity = input("Enter updated City: ").capitalize()
            db[reg_no]["City"] = ucity
            print("\nCity Updated Successfully...")
        elif ch == 3:
            upercentage = eval(input("Enter updated Percentage: "))
            db[reg_no]["Percentage"] = upercentage
            print("\nPercentage Updated Successfully...")
        elif ch == 4:
            ucourse = input("Enter updated Course Name: ").capitalize()
            db[reg_no]["Course Name"] = ucourse
            print("\nCourse Name Updated Successfully...")
        else:
            print("\nInvalid Choice!")
    elif ch == 4:
        reg_no = eval(input("Enter Registration Number: "))
        del(db[reg_no])
        print("\nData deleted successfully...")
    elif ch == 5:
        print(f"""
        {' '*25}--x-x-x--Filter BY--x-x-x-- \n
        {' '*34}1. Name
        {' '*34}2. City
        {' '*34}3. Percentage
        {' '*34}4. Course Name
        """)
        ch = int(input("Apply Filter To: "))
        if ch == 1:
            fname = input("Enter Name: ").capitalize()
            print("-"*85)
            print("|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|".format("Reg.No","Name","City","Percentage","Course"))
            print("-"*85)
            for i in db:
                if db[i]["Name"] == fname:
                    print("|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|".format(i, db[i]["Name"], db[i]["City"], db[i]["Percentage"], db[i]["Course Name"]))
                    print("-"*85)
        elif ch == 2:
            fcity = input("Enter City: ").capitalize()
            print("-"*85)
            print("|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|".format("Reg.No","Name","City","Percentage","Course"))
            print("-"*85)
            for i in db:
                if db[i]["City"] == fcity:
                    print("|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|".format(i, db[i]["Name"], db[i]["City"], db[i]["Percentage"], db[i]["Course Name"]))
                    print("-"*85)
        elif ch == 3:
            fpercentage = eval(input("Enter Percentage: "))
            print("-"*85)
            print("|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|".format("Reg.No","Name","City","Percentage","Course"))
            print("-"*85)
            for i in db:
                if db[i]["Percentage"] == fpercentage:
                    print("|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|".format(i, db[i]["Name"], db[i]["City"], db[i]["Percentage"], db[i]["Course Name"]))
                    print("-"*85)
        elif ch == 4:
            fcourse = input("Enter Course Name: ").capitalize()
            print("-"*85)
            print("|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|".format("Reg.No","Name","City","Percentage","Course"))
            print("-"*85)
            for i in db:
                if db[i]["Course Name"] == fcourse:
                    print("|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|".format(i, db[i]["Name"], db[i]["City"], db[i]["Percentage"], db[i]["Course Name"]))
                    print("-"*85)
        else:
            print("\nInvalid Filter!")
        print("\nFilter Applied Successfully...")
    elif ch == 6:
        break
    else:
        print("\nInvalid Input")
