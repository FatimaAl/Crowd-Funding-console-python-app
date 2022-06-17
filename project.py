import re
class Project:

    @classmethod
    def editProject(cls, projectName):
        file = open("projects.txt", "r")
        fileLines = file.readlines()
        index = -1
        for line in fileLines:
            index += 1
            if projectName in line:
                found = line.split()


    def sDateSet(self, date):
        dateValid = re.match(r'^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$', date)
        if dateValid:
            self.startDate = date
        else:
            anotherDate = input("Enter date in proper format (dd/mm/yyyy) : \n")
            self.sDateSet(anotherDate)

    def eDateSet(self,date):
        dateValid = re.match(r'^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$', date)
        if dateValid:
            self.endtDate = date
        else:
            anotherDate = input("Enter date in proper format (dd/mm/yyyy) : \n")
            self.eDateSet(anotherDate)

    def create(self):
        self.title = input("Enter your project title: \n")
        self.Discribtion = input("Enter the project discribtion : \n")
        self.totalTarget = input("Enter total target: \n")
        startDate = (input("enter start date: \n"))
        self.sDateSet(startDate)
        endDate =  input("Enter end date: \n")
        self.eDateSet(endDate)
