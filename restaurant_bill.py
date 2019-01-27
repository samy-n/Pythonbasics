# Program to enter user's restaurant bill and print total amout by adding GST 18%
#If user wishes, add 20% tip as well.

class restaurant_bill:

    def calculate(self,users_restaurant_bill):


        service_tip=input("Do you want to add 20% service tip? Enter y/n ")
        if(service_tip=='y'):
            print("Total amount is= "+str(users_restaurant_bill+.18*users_restaurant_bill+.2*users_restaurant_bill))
        else:
            print("Total amount is= "+str(users_restaurant_bill+.18*users_restaurant_bill))


bill=int(input("Enter restaurant  bill "))
ob=restaurant_bill()
ob.calculate(bill)