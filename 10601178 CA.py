class Employee:
    employdata = {}
    
    def __init__(self, StaffID, LastName, FirstName, RegHours, HourlyRate, OTMulti, TaxCredit, StandardBand):
        self.StaffID = StaffID
        self.LastName = LastName
        self.FirstName = FirstName
        self.RegHours = RegHours
        self.HourlyRate = HourlyRate
        self.OTMulti= OTMulti
        self.TaxCredit = TaxCredit
        self.StandardBand = StandardBand
        Employee.employdata[StaffID] = self
    
    # Computes the employee tax, net salary, PRSI and net deductions 
    # based on the number of regular and overhead hours 
    # worked by the employee
    def computePayment(self,HoursWorked, date):
        employeeDetail = {}
        #Assign value inside the object employeeDetail
        employeeDetail['Hours Worked'] = HoursWorked 
        employeeDetail['Regular Hours Worked'] = Employee.employdata[self.StaffID].RegHours
        employeeDetail['Regular Rate'] = Employee.employdata[self.StaffID].HourlyRate
        OTMulti = Employee.employdata[self.StaffID].OTMulti
        employeeDetail['Tax Credit'] = Employee.employdata[self.StaffID].TaxCredit
        StandardBand = Employee.employdata[self.StaffID].StandardBand
        employeeDetail['Date'] = date
        employeeDetail['Name'] = Employee.employdata[self.StaffID].FirstName + ' ' + Employee.employdata[self.StaffID].LastName
        employeeDetail['Regular Pay'] = employeeDetail['Regular Rate'] * employeeDetail['Regular Hours Worked']
        employeeDetail['Standard Rate Pay'] = StandardBand
        employeeDetail['Gross Pay'] = employeeDetail['Regular Pay']

        if (employeeDetail['Hours Worked'] > employeeDetail['Regular Hours Worked']):
            employeeDetail['Overtime Hours Worked'] =  employeeDetail['Hours Worked'] - employeeDetail['Regular Hours Worked']
            employeeDetail['OverTime Rate'] = int(employeeDetail['Regular Rate'] * OTMulti)
            employeeDetail['OverTime Pay'] = employeeDetail['Overtime Hours Worked'] * employeeDetail['OverTime Rate']
            employeeDetail['Gross Pay'] = employeeDetail['Regular Pay'] + employeeDetail['OverTime Pay']
            employeeDetail['Standard Rate Pay'] = StandardBand
        else: 
            employeeDetail['Overtime Hours Worked'] = 0
           

        if (employeeDetail['Gross Pay'] > employeeDetail['Standard Rate Pay']):
            employeeDetail['Higher Rate Pay'] = employeeDetail['Gross Pay'] - employeeDetail['Standard Rate Pay']
            employeeDetail['Standard Tax'] = int(employeeDetail['Standard Rate Pay'] * 0.2)
            employeeDetail['Higher Tax'] = round(employeeDetail['Higher Rate Pay'] * 0.4, 2)
            employeeDetail['Total Tax'] = round(employeeDetail['Standard Tax'] + employeeDetail['Higher Tax'], 2)
            employeeDetail['Net Tax'] = round(employeeDetail['Total Tax'] - employeeDetail['Tax Credit'], 2)
            employeeDetail['PRSI']=round(0.04*employeeDetail['Gross Pay'],2)
            employeeDetail['Net Deductions'] = employeeDetail['Net Tax'] + employeeDetail['PRSI']
            employeeDetail['Net Pay'] = round(employeeDetail['Gross Pay'] - employeeDetail['Net Deductions'], 2)

        else:
            employeeDetail['Higher Rate Pay'] = 0

        print(employeeDetail)
        return employeeDetail


employeeDetails = Employee(12345, 'Smith', 'Neil', 37, 16, 1.5, 72, 710)
employeeDetails.computePayment(42, '11/11/21')#compute the tax for specified hours