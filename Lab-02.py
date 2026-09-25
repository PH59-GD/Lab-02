myEmployees = {}
AM = 0
def AddEm():
    global AM
    if(AM != 1):
        EN = input("Enter Employee name: ")
        BP = int(input("Enter Employee pay: "))
        EA = int(input("Enter Employee allowance: "))
        ED = int(input("Enter Employee deductions: "))
        ET = int(input("Enter Employee taxes: "))
        GP = BP + EA
        NP = GP - ED - ET
        myEmployees.update({"Employee" + str(len(myEmployees) + 1): {"Employee Name": EN, "Basic Pay": BP,
                                                                     "Employee Allowance": EA, "Employee Deductions": ED,
                                                                     "Employee Taxes": ET, "Gross Pay": GP, "Net Pay": NP}})
    elif (AM == 1):
        EN = input("Enter Employee name: ")
        BP = int(input("Enter Employee pay: "))
        EA = int(input("Enter Employee allowance: "))
        ED = int(input("Enter Employee deductions: "))
        ET = int(input("Enter Employee taxes: "))
        GP = BP + EA
        NP = GP - ED - ET
        myEmployees.update({"Employee" + str(len(myEmployees) + 2): {"Employee Name": EN, "Basic Pay": BP,
                                                                     "Employee Allowance": EA,
                                                                     "Employee Deductions": ED,
                                                                     "Employee Taxes": ET, "Gross Pay": GP,
                                                                     "Net Pay": NP}})
        AM -= 1
def DelEm():
    global AM
    if(len(myEmployees) > 0):
        UC = input("What Employee to delete?: ")
        del myEmployees[UC]
        AM += 1
    else:
        print("No Employees!")
def ModEm():
    MM = 0
    WE = input("What Employee?(EX: Employee1): ")
    if(WE not in myEmployees.keys()):
        print("Employee not found!")
        MM += 1
    while MM != 1:
        print("What to modfiy?")
        print("[1] Employee Name")
        print("[2] Employee Pay")
        print("[3] Employee Allowance")
        print("[4] Employee Deductions")
        print("[5] Employee Taxes")
        print("[6] Exit")
        print("")
        UC = input("Input: ")

        if (UC == "1"):
            NEN = input("Enter New Employee Name: ")
            myEmployees[WE]["Employee Name"] = NEN
        elif (UC == "2"):
            NEP = int(input("Enter New Employee Pay: "))
            myEmployees[WE]["Basic Pay"] = NEP
            GP = NEP + myEmployees[WE]["Employee Allowance"]
            NP = GP - myEmployees[WE]["Employee Deductions"] - myEmployees[WE]["Employee Taxes"]
            myEmployees[WE]["Net Pay"] = NP
            myEmployees[WE]["Gross Pay"] = GP
        elif (UC == "3"):
            NEA = int(input("Enter New Employee Allowance: "))
            myEmployees[WE]["Employee Allowance"] = NEA
            GP = myEmployees[WE]["Basic Pay"] + NEA
            NP = GP - myEmployees[WE]["Employee Deductions"] - myEmployees[WE]["Employee Taxes"]
            myEmployees[WE]["Net Pay"] = NP
            myEmployees[WE]["Gross Pay"] = GP
        elif (UC == "4"):
            NED = int(input("Enter New Employee Deductions: "))
            myEmployees[WE]["Employee Deductions"] = NED
            GP = myEmployees[WE]["Basic Pay"] + myEmployees[WE]["Employee Allowance"]
            NP = GP - NED - myEmployees[WE]["Employee Taxes"]
            myEmployees[WE]["Net Pay"] = NP
            myEmployees[WE]["Gross Pay"] = GP
        elif (UC == "5"):
            NET = int(input("Enter New Employee Taxes: "))
            myEmployees[WE]["Employee Taxes"] = NET
            GP = myEmployees[WE]["Basic Pay"] + myEmployees[WE]["Employee Allowance"]
            NP = GP - myEmployees[WE]["Employee Deductions"] - NET
            myEmployees[WE]["Net Pay"] = NP
            myEmployees[WE]["Gross Pay"] = GP
        elif (UC == "6"):
            MM += 1
def DisplayEm():
    if (len(myEmployees) > 0):
        print("You Have: " + str(len(myEmployees)) + " Employees")
        print("")
        print(myEmployees)
    else:
        print("No Employees!")
while True:
    print("")
    print("[1] Add an Employee")
    print("[2] Delete an Employee")
    print("[3] Modify an Employee")
    print("[4] Display All Employee")
    print("[5] Exit the Program")
    print("")
    UI = input("Input: ")
    if (UI == "1"):
        AddEm()
    elif (UI == "2"):
        DelEm()
    elif (UI == "3"):
        ModEm()
    elif (UI == "4"):
        DisplayEm()
    elif (UI == "5"):
        break