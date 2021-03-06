from  Register import  Register
from Login import Login
from project import Project
import re


def validateDate(date):
    if re.match(r'^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$', date):
        return date
    else:
        newDate = input("Enter date in proper format: \n")
        validateDate(newDate)

def second_display(user):
    ch = int(input("Please enter the number of the operation you want: \n 1_ Create a Project \n 2_View All Projects  \n 3_Edit Your Projects \n "
        "4_Delete a Project \n 5_Search For a Project By Date \n 6_LogOut \n"))
    if ch == 1:
        project = Project()
        project.create()
        projectAttr = [user[0], project.title, project.Discribtion, project.totalTarget, project.startDate, project.endtDate]
        listToStr = " "
        for item in projectAttr:
            listToStr += item
            listToStr += ":"
        file = open("projects.txt", "a")
        file.write(listToStr)
        file.write("\n")
        file.close()
        second_display(user)
    elif ch==2:
        file = open("projects.txt", "r")
        lines = file.readlines()
        for line in lines:
            projectAttr=line.split(":")
            print("Project Title: ", projectAttr[1])
            print("Project Details: ", projectAttr[2])
            print("Project Total Target: ", projectAttr[3])
            print("Project Start Date: ", projectAttr[4])
            print("Project End Date: ", projectAttr[5])
            print("____________________________________________")
        second_display(user)
    elif ch == 3:
        print("Enter The Name of The Project You Want To Edit: ")
        userID = user[0]
        file = open("projects.txt", "r")
        lines = file.readlines()
        userProjects = []
        i=0
        for line in lines:
            projectList = line.split(":")
            if projectList[0] == userID:
                userProjects.append(projectList[1])
            i+=1
        j=1
        for project in userProjects:
            print(j, "_", project)
            j += 1
        choice = input()
        Project.editProject(choice)
        second_display(user)

    elif ch == 4:
        print("Enter The Name of The Project You Want To Delete: ")
        userID = user[0]
        file = open("projects.txt", "r")
        lines = file.readlines()
        userProjects = []
        i = 0
        for line in lines:
            projectList = line.split(":")
            if projectList[0] == userID:
                userProjects.append(projectList[1])
            i += 1
        j = 1
        for project in userProjects:
            print(j, "_", project)
            j += 1
        choice = input()
        Project.deleteProject(choice, user[0])
        second_display(user)

    elif ch == 5:
        date = input("Enter Date Of The Projects You Want review: \n")
        checkdate = validateDate(date)
        if checkdate:
            projects = Project.searchByDate(checkdate)
        for project in projects:
            print("Project Title: ", project[1])
            print("Project Details: ", project[2])
            print("Project Total Target: ", project[3])
            print("Project Start Date: ", project[4])
            print("Project End Date: ", project[5])
            print("____________________________________________")
            second_display(user)

    elif ch == 6:
        pass

def first_display ():
    choice = int(input("Please enter the number of the operation you want: \n 1_ Register \n 2_Login \n 3_Quit \n"))
    if choice==1:
        user = Register()
        user.register()
        strID= str(user.id)
        list = [strID, user.fname, user.lname, user.email, user.password, user.phonenum]
        listToStr = " "
        for item in list:
            listToStr += item
            listToStr += ":"
        file = open("DatabaseFile.txt","a")
        file.write(listToStr)
        file.write("\n")
        file.close()
        first_display()
    elif choice==2:
        user = Login()
        userInfo = user.login()
        second_display(userInfo)
        first_display()
    elif choice==3:
        pass

first_display()