import re
class Project:

    @classmethod
    def searchByDate(cls, date):
        file = open("projects.txt", "r")
        lines = file.readlines()
        projects = []
        for line in lines:
            if date in line:
                projects.append(line.split(":"))
        return projects

    @classmethod
    def deleteProject(cls, projectName, userID):
        filer = open("projects.txt", "r")
        fileLines = filer.readlines()
        index=-1
        filew = open("projects.txt", "w")
        for line in fileLines:
            index += 1
            if userID in line:
                if projectName in line:
                    continue
                else:
                    filew.write(line)
            else:
                filew.write(line)




    @classmethod
    def editProject(cls, projectName):
        filer = open("projects.txt", "r")
        fileLines = filer.readlines()
        index = -1
        for line in fileLines:
            index += 1
            if projectName in line:
                found = line.split(":")
                break;
        print("FOUND ISSS:  ", found)
        pname = input("Enter The New Project's Name: \n")
        if pname != "":
            del found[1]
            found.insert(1,pname)
        pdiscribtion = input("Enter The New Project's discribtion: \n")
        if pdiscribtion != "":
            del found[2]
            found.insert(2, pdiscribtion)
        ptotaltarget = input("Enter The New Project's total target: \n")
        if ptotaltarget != "":
            del found[3]
            found.insert(3, ptotaltarget)
        pstartd = input("Enter The New Project's total start date: \n")
        if pstartd != "":
            del found[4]
            if re.match(r'^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$', pstartd):
                found.insert(4, pstartd)
            else:
                print("Wrong Format")
        pendd = input("Enter The New Project's total start date: \n")
        if pstartd != "":
            del found[4]
            if re.match(r'^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$', pendd):
                found.insert(4, pendd)
            else:
                print("Wrong Format")
        updatedP = ':'.join(found)
        filer = open("projects.txt", "r")
        fileLines = filer.readlines()
        fileLines[index]=updatedP
        filew = open("projects.txt", "w")
        filew.writelines(fileLines)
        filer.close()
        filew.close()


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
