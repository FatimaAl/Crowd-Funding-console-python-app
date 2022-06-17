from  Register import  Register
from Login import Login
from project import Project

def second_display(ch, user):
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
    elif ch == 3:
        print("Enter The Name of The Project You Want To Edit: ")
        userID = user[0]
        file = open("projects.txt", "r")
        lines = file.readlines()
        userProjects = []
        i=0
        for line in lines:
            projectList = line.split(":")
            if projectList[i] == userID:
                userProjects.append(projectList[1])
            i+=1
        j=1
        print(userProjects)
        for project in userProjects:
            print(j, "_", project)
            j += 1
        choice = int(input())
        Project.editProject(choice)

    elif ch == 4:
        pass
    elif ch == 5:
        pass
    elif ch == 6:
        pass
    else:
        pass

def first_display (choice):
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
        return
    elif choice==2:
        user = Login()
        userInfo = user.login()
        print(userInfo)
        ch = int(input("Please enter the number of the operation you want: \n 1_ Create a Project \n 2_View All Projects  \n 3_Edit Your Projects \n "
                           "4_Delete a Project \n 5_Search For a Project By Date \n"))
        second_display(ch, userInfo)
    elif choice==3:
        pass
    else:
        first_display()

firstChoice=int(input("Please enter the number of the operation you want: \n 1_ Register \n 2_Login \n 3_Quit \n"))
first_display(firstChoice)