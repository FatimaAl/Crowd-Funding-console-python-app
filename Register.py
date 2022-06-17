import re
class Register:
    def takeFname(self, fname):
        fnameValid = re.fullmatch(r'[a-zA-Z]+$',fname)
        if fnameValid:
            self.fname=fname
        else:
            anotherFname = input("Enter your first name again in characters only: \n")
            self.takeFname(anotherFname)

    def takeLname(self, lname):
        lnameValid = re.fullmatch(r'[a-zA-Z]+$', lname)
        if lnameValid:
            self.lname = lname
        else:
            anotherLname = input("Enter your last name again in characters only: \n")
            self.takeLname(anotherLname)

    def takeEmail(self, email):
        emailValid = re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email)
        if emailValid:
            self.email = email
        else:
            anotherEmail = input("Enter your email again in proper format: \n")
            self.takeEmail(anotherEmail)

    def takePassword(self):
        password = input("Enter your password \n")
        confirmpwd= input("Enter your password again: \n")
        if password != confirmpwd:
            print("Make sure your password match")
            self.takePassword()
        else:
            self.password = password

    def takeMobileNumber(self, number):
        numberValid = re.match(r'^01[0125][0-9]{8}$', number)
        if numberValid:
            self.phonenum = number
        else:
            anothernum = input("Enter your phone number in proper format: \n")
            self.takeMobileNumber(anothernum)

    def register(self):
        self.id = id(self)
        fname= input("Enter your first name: \n")
        self.takeFname(fname)
        lname = input("Enter your last name: \n")
        self.takeLname(lname)
        email = input("Enter your email: \n")
        self.takeEmail(email)
        self.takePassword()
        number = input("Enter you mobile number: \n")
        self.takeMobileNumber(number)

    # def __del__(self):
        # file = open("DatabaseFile.txt","r")
        # fileLinees = file.readlines()
        # fileLinees[0] = Register.id - 1
        # file = open("DatabaseFile.txt","w")
        # file.write(fileLinees)
        # list = [self.fname, self.lname, self.email, self.password, self.phonenum]
        # str1 = " "
        # for item in list:
        #     str1 += item
        # file = open("DatabaseFile.txt","a")
        # file.write(str1)
        # file.close()