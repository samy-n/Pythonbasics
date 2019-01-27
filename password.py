# Program to Welcome User if password entered by user is correct

class check_password:

    def check(self,correct_pwd,user_pwd):
        if(correct_pwd==user_pwd):
            print("Welcome User")
        else:
            print("Access denied")

user_pwd=input("Enter password ")
obj=check_password()
obj.check("abc123",user_pwd)