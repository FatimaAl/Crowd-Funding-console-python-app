import linecache
class Login:

    def findUser(self, email):
        file = open("DatabaseFile.txt", "r")
        flag = 0
        index = -1
        for line in file:
            index += 1
            if email in line:
                flag = 1
                break
        file = open("DatabaseFile.txt", "r")
        lines = file.readlines()
        userData = lines[index]
        file.close()
        userInfo = userData.split(":")
        if flag == 1:
            return userInfo
        else:
            return None

    def login(self):
        email = input("Enter your email address: \n")
        password = input("Enter your password: \n")
        user = self.findUser(email)
        if user != None :
            if password == user[4]:
                return user
            else:
                print("Password is Incorrect!")
                self.login()
        else:
            print("User Not Found!")
            self.login()

