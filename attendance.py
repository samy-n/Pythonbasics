# Program to check student attendance.
#If attendance>75%, student can sit for attendance.
#If attendance<75%, he cannot

class Student_attendance:

    def att(self,attendance):

        if(attendance>75):
            print("Student can sit for unit test")
        else:
            print("Student cannot sit for unit test.")

attendance = int(input("Enter percentage attendance of student"))
ob=Student_attendance()
ob.att(attendance)


