def signin(username, passwords):
    """This code is for login by the administrator"""
    k=3
    for i in range(0,4):
        users=input("Enter Users Name Here:")
        passcode=input("Enter your PassCode Here:")
        if( users == username and passcode == passwords):
            print("Logged in Successfully")
            break            
        else:
            print("The User Id or PassCode you have Entered is Incorrect",k,"Left!")
            k=k-1
    return k 
def pass_change(bpass):
    """This Code Here is For To Change Pass Code"""
    tem=input("Enter your Current Password To Proceed:")
    if(tem==bpass):
        newpass=input("Enter your New Password:")
        bpass=newpass
        print("Password Changed Successfully:")
    else:
        print("The Password you have Entered is inCorrect:")
    return bpass
  
def studentpop(student_data):
    """This function Deletes The Student Data From The systuuumm"""
    named=input("Enter the Student Name :")
    if named in student_data:
        print("Are you Sure You Want to Remove Student: Y or N:")
        ch=input()
        if(ch=='y'or ch=='Y'):
            student_data.pop(named)
        elif(ch == 'n' or ch == 'N'):
            exit()
        else:
            print("Enter A Valid Input:")
    return student_data
def studentadd(student_data):
    """This Function Add New Student """
    name=input("Enter the Name of student:")
    age=int(input("Enter the Age of student:"))
    gender=input("Enter the Gender:")
    dateofbirth=input("Enter the Date of Birth of student:")
    contactnumber=input("Enter the contact number of the student:")
    dateofadmission=input("Date of Admission:")
    collegeid=int(input("Enter the New College Id:"))
    fathersname=input("Enter the Father's Name of Student:")
    daysattended=int(input("Enter the Dates Attended Till Now:"))
    daysabsent=int(input("Enter the Days Absent Till Now:"))
    student_data[name]={
        'age':age,
        'gender':gender,
        'dateofbirth':dateofbirth,
        'contactnumber':contactnumber,
        'dateofadmission':dateofadmission,
        'collegeid':collegeid,
        'fathersname':fathersname,
        'daysattended':daysattended,
        'daysabsent':daysabsent
    }
    return student_data
def markattendance(student_data):
    """This Function Marks Students Attendance"""
    naming=input("Enter the Name of student to mark attendance of:")
    dateofattendance=int(input("Enter the Date for attendance In ddmmyyyy format:"))
    if naming in student_data:
        student_data[naming]['daysattended'].append(dateofattendance)
        print("Attendance Marked")
    else:
        print("Enter A Valid Student Name")
    return student_data
def studentdataview(student_data):
    """This Function Return Student data"""
    nam=input("Enter The Student Name to View Data:")
    if nam in student_data:
        print(student_data[nam])
    else:
        print("Enter A Valid Student Name:")

def studentreport(student_data):
    """This program generates student Report"""
    na=input("Enter the name of the student")
    if na in student_data:
        print("Days on Which student was present are:",student_data[na]['daysattended'])
        print("Days on Which Student was Absent was",student_data[na]['daysabsent'])
        p=len(student_data[na]['daysattended'])
        a=len(student_data[na]['daysabsent'])
        percentatt=(p)/(p+a)
        print("Student Has :",percentatt*100,"% Attendance")

def main():
    """This is the Main Function Of the Software, contains all the data ,user id , password"""
    username='ut5472'
    usedname=username
    passwords='292929'
    bpass=passwords
    print("Hello Welcome to the student management ERP and attendance portal:")
    student_data={    
        'akshat':{
            'age':'20',
            'gender':'male',
            'dateofbirth':'21-08-2003',
            'contactnumber':'xxxxxxxxxx',
            'dateofadmission':'04-05-2020',
            'collegeid':'001',
            'fathersname':'sukesh',
            'daysattended':[21062023,22062023,23062023],
            'daysabsent':[20062023,24062023],
        },
        'bhavya':{
            'age':'21',
            'gender':'female',
            'dateofbirth':'01-08-2002',
            'contactnumber':'xxxxxxxxxx',
            'dateofadmission':'06-05-2020',
            'collegeid':'002',
            'fathersname':'ramesh',
            'daysattended':[20062023,22062023,23062023],
            'daysabsent':[21062023,24062023],
            
        },
        'daksh':{
            'age':'22',
            'gender':'male',
            'dateofbirth':'21-03-2001',
            'contactnumber':'xxxxxxxxxx',
            'dateofadmission':'21-05-2023',
            'collegeid':'003',
            'fathersname':'sukesh',
            'daysattended':[21062023,22062023,23062023],
            'daysabsent':[20062023,24062023],
        },
        'kushal':{
            'age':'20',
            'gender':'male',
            'dateofbirth':'21-03-2002',
            'contactnumber':'xxxxxxxxxx',
            'dateofadmission':'04-05-2020',
            'collegeid':'004',
            'fathersname':'sukesh',
            'daysattended':[21062023,22062023,23062023],
            'daysabsent':[20062023,24062023],
        }

    }
    las=0
    k=signin(usedname,bpass)        
    if(k != -1):
                while(las<20):
                    las=las+1
                    print('''
                          1.Change Password
                          2.Add New Student
                          3.Remove Student
                          4.Mark Attendance
                          5.View student Data
                          6.Get the Attendance Report
                          7.Logout
                          ''')
                    option=int(input("Enter the service No. Given Above:"))
                    if(option == 1):
                        bpass=pass_change(bpass)
                    elif(option == 2):
                            student_data=studentadd(student_data)
                            print("Student Added Successfully:")
                    elif(option == 3):
                            student_data=studentpop(student_data)
                            print("Student Deleted Successfully:")
                    elif(option == 4):
                        student_data=markattendance(student_data)
                    elif(option == 5):
                        studentdataview(student_data)
                    elif(option == 6):
                        studentreport(student_data)
                    elif(option == 7):
                        main()
                    else:
                                print("Enter A valid Option")
    else:
                print("Please Try Again after Some Time:(Blocked)")     
main()       