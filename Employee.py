class Employee:
    Organization = "SAAS Services"
    employeeData = []
    employeeDict = {}
    def __init__(self,employee_id,first_name,last_name,team,department,age):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.team = team
        self.department = department
        self.age = age
    def updateEmployeedata(self):
        self.employeeDict = {
            "employee_id": self.employee_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "team": self.team,
            "department": self.department,
            "age": self.age
        }
        self.employeeData.append(self.employeeDict)
    def getEmployeedata(self):
        for employee in range(len(self.employeeData)):
            if self.employee_id in self.employeeData[employee].values():
                return self.employeeData[employee]

        

    

e2 = Employee(789,'Ram','Rama','BI','IT',32)
e2.updateEmployeedata()
print(e2.getEmployeedata())

#,employee_id,first_name,last_name,team,department,age