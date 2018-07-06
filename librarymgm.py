# CANSOLE BASED PROJECT
import os;
import time;
#************************************ WELCOME SCREEN **********************************
def welcome():
    os.system("cls");
    os.system("color 1A");
    time.sleep(0.3);
    print(" ".rjust(78,"="))
    time.sleep(1/4);
    print("                     WELCOME TO CETPA LIBRARY MANAGEMET SYSTEM")
    time.sleep(1/4);
    print("                                INDRA NAGAR LUCKNOW UP")
    time.sleep(1/4);
    print("                        Console Based PROJECT BY MOHD MUJTABA(Batch-13June)")
    time.sleep(1/4);
    print(" ".rjust(78,"="))
    time.sleep(1/4);
    menu();
#******************************** MAIN MENU *************************************             
def menu():
    print(" ".rjust(78,"="))
    print("                     LOGIN MANAGEMENT SYSTEM<AUTHORISED>")
    print(" ".rjust(78,"="))
    print("""   1. STUDENT
   2. ADMIN/STAFF""");
    choice=int(input("     Enter Your Choice:"))
    if(choice!=1 and choice!=2):
        print("Wrong Choice Enter Again:!");
        os.system("cls");
        menu();
    elif(choice==1):
        studentMenu();
    elif(choice==2):
        adminMenu();
#************************** STUDENT MENU *******************************
def studentMenu():
    os.system("cls");
    os.system("color 2E");
    print(" ".rjust(78,"="))
    print("                     STUDENT MENU WINDOW<AUTHORISED>")
    print(" ".rjust(78,"="))
    print("""    1. EXISTING USER(LOGIN)
    2. NEW USER(SIGN UP)
    3. DELETE USER
    4. LOG OFF
    5. EXIT.""");
    choice=input("        Enter Your Choice:")
    if(choice=='1'):
        studLogin();
         
    elif(choice=='2'):
        studRegister();
    elif(choice=='3'):
        studdelete();
    elif(choice=='4'):
        welcome();
    elif(choice=='5'):
        exit();
    else:
        print("Wrong Choice Try Again:");
        time.sleep(1);
        studentMenu();
#*********************** STUDENT REGISTRATION ************************
def studRegister():
        os.system("cls");
        os.system("color 3F");
        check=1;
        print(" ".rjust(78,"="))
        print("                     NEW STUDENT REGISTRATION WINDOW")
        print(" ".rjust(78,"="))
        f=open('D:/Python Lucknow/studreg.txt'); 

        id=input("Enter STUDENT ID(MUST BE UNIQUE):");
        while True:
                l=f.readline().split(",");
                print(l);
                if(id==l[0]):
                        print("Record Already Exist! Kindly Proceed To Login:");
                        time.sleep(2);
                        f.close();
                        studentMenu();
                if(l==['']):
                        break;
        name=input("Choose Your Name(MIN 4 CHARACTER):");
        username=name[:4]+str(id);
        while(check):
                pwd=input("Enter New Password:")
                cnfpwd=input("Re-Enter Password:");
                if(pwd!=cnfpwd):
                        print("Password Do not Match! Kindly Enter Again!");
                        check=1;
                else:
                        break;
        filecontent=str(id)+","+name+","+username+","+pwd+"\n";
        open('D:/Python Lucknow/studreg.txt',"a").write(filecontent);
        print("Acocunt Created Successfully Wait(2 Second:)");
        time.sleep(2);
        f.close();
        studentMenu();
    
#*********************** STUDENT LOGIN ******************************
def studLogin():
        os.system("cls");
        os.system("color 4E");
        print(" ".rjust(78,"="))
        print("                     STUDENT LOGIN WINDOW<AUTHORISED>")
        print(" ".rjust(78,"="))
        user=input("Enter UserName:");
        pwd=input("Enter Password:");
        f=open('D:/Python Lucknow/studreg.txt');
        l=f.readlines()
        m=0
        for i in l:
                print(i.split(','))
                if (user==i.split(',')[2] and pwd==i.split(',')[3].split()[-1]):
                        print("Login SuccessFul: Wait Redirecting.....");
                        time.sleep(1/4);
                        f.close();
                        studMainMenu(i);
                        break;
        if m==0:
                print("Invalid UserName Or Password! Kindly Enter Again!:");
                time.sleep(1);
                f.close();
                studLogin();
        f.close();
            
#******************** STUDENT DELETE USER **********************************
def studdelete():
        os.system("cls");
        os.system("color 5B");
        userid=input("Enter Your UserName(99 to Exit):");
        f=open("D:/Python Lucknow/studreg.txt");
        f1=open("D:/Python Lucknow/studreg1.txt","w");
        while True:
                if(userid==str(99)):
                        studentMenu();
                l=f.readline().split(",")
                print(l);
                if(l==['']):
                        print("User Id Does Not Exist:\nKindly Enter Again");
                        f.close();
                        f1.close();
                        studdelete();
                if(l[2]==userid):
                        f1.write(f.read());
                        f1.close();
                        f.close();
                        os.remove("D:/Python Lucknow/studreg.txt");
                        os.rename("D:/Python Lucknow/studreg1.txt","D:/Python Lucknow/studreg.txt");
                        print("Record Deleted!.....Wait(2 Sec)");
                        time.sleep(3/2);
                        studentMenu();
                filecontent=",".join(l);
                f1.write(filecontent);
#*************************STUDENT <MAIN MENU>*********************
def studMainMenu(l):
    os.system("cls");
    os.system("color 4A");
    print(" ".rjust(78,"="))
    time.sleep(1/3);
    print(" ".rjust(78,"="))
    print("                               STUDENT MAIN MENU<AUTHORISED>")
    time.sleep(1/2);
    print(" ".rjust(78,"="))
    print("""\n\n   1. ISSUE BOOK
   2. RETURN BOOK
   3. VIEW ISSUED BOOK
   4. LOG OFF.
   5. EXIT """);
    ch=0;
    while(ch<1 or ch>5):
        ch=int(input("Enter Your Choice....."));
        if(ch==1):
            issueBook(l);
        elif(ch==2):
            returnBook(l);
        elif(ch==3):
            viewIssuedBook(l);
        elif(ch==4):
            studentMenu();
        elif(ch==5):
            exit();
        else:
            print("Wrong Choice!! Enter Again...");
#********************** ISSUE BOOK(STUDENT) **********************
def issueBook(l):
    os.system("cls");
    os.system("color 5B");
    
    id=l.split(",")[0];
    name=l.split(",")[1];
    print("Student Name:",name,"  Id:",id);
    f=open("D:/Python Lucknow/addbook.txt","r");
    f1=open("D:/Python Lucknow/issuedbook.txt","a");
    f2=open("D:/Python Lucknow/addbook1.txt","w");
    bname=input("Enter BOOK NAME:");
    check=0;
    while True:
        rl=f.readline().split(",");
        if(rl==['']):
            print("No Book's Found:Redirecting...");
            time.sleep(1);
            f.close();
            f1.close();
            f2.close();
            studMainMenu(l);
            break;
        elif(bname==rl[1]):
            file=id+","+name+","+bname+"\n";
            f1.write(file);
            f.close();
            f1.close();
            f2.close();
            check=1;
            break;
    if(check==1):
        f=open("D:/Python Lucknow/addbook.txt","r").readlines();
        for i in f:
            p=i.split(",");
            if(p[1]==bname):
                p[3]=str(int(p[3])+1);
                open("D:/Python Lucknow/addbook1.txt","a").write(",".join(p));
                check=2;
            else:
                open("D:/Python Lucknow/addbook1.txt","a").write(",".join(p));
    if(check==2):
        f2.close();
        os.remove("D:/Python Lucknow/addbook.txt");
        os.rename("D:/Python Lucknow/addbook1.txt","D:/Python Lucknow/addbook.txt");
        print("Book Issued....Redirecting.....");
        time.sleep(1);
        studMainMenu(l);
#***************************** RETURN BOOK<STUDENT> ******************************
def returnBook(l):
    os.system("cls");
    os.system("color 9E");
    check=0;
    f=open("D:/Python Lucknow/issuedbook.txt");
    line=l.split(",");
    count=0;
    while True:
        rl=f.readline().split(",");
        if(rl==['']):
            if(count==0):
                print("No Book is Issued...Redirecting....");
                time.sleep(1.3);
                f.close();
                studMainMenu(l);
            else:
                f.close();
                break;
        elif(line[1]==rl[1]):
            print(rl);
            count=1;
      
    name=input("Enter BOOK NAME:");
    #f=open("D:/Python Lucknow/addbook1.txt","w");
    f1=open("D:/Python Lucknow/issuedbook1.txt","w");
    f2=open("D:/Python Lucknow/addbook1.txt","w");
    f3=open("D:/Python Lucknow/issuedbook.txt");
    
    while True:
        if(name==str(99)):
            studentMainMenu(l);
        l3=f3.readline().split(",")
        print(l3);
        if(l3==['']):
            print("No Book Found! Redirecting.....");
            time.sleep(1);
            f1.close();
            f2.close();
            f3.close();
            os.remove("D:/Python Lucknow/issuedbook1.txt");
            os.remove("D:/Python Lucknow/addbook1.txt");
            studMainMenu(l);
        elif(l3[2].split("\n")[0]==name and line[1]==l3[1]):
            f1.write(f3.read());
            f1.close();
            f3.close();
            f2.close();
            check=1;
            os.remove("D:/Python Lucknow/issuedbook.txt");
            os.rename("D:/Python Lucknow/issuedbook1.txt","D:/Python Lucknow/issuedbook.txt");
            break;
        else:
            filecontent=",".join(l3);
            f1.write(filecontent);

    if(check==1):
        f=open("D:/Python Lucknow/addbook.txt","r").readlines();
        for i in f:
            p=i.split(",");
            if(p[1]==name):
                p[3]=str(int(p[3])-1);
                open("D:/Python Lucknow/addbook1.txt","a").write(",".join(p));
                check=2;
            else:
                open("D:/Python Lucknow/addbook1.txt","a").write(",".join(p));
    if(check==2):
        f2.close();
        os.remove("D:/Python Lucknow/addbook.txt");
        os.rename("D:/Python Lucknow/addbook1.txt","D:/Python Lucknow/addbook.txt");
        print("Record Deleted!.....Wait(2 Sec)");
        time.sleep(3/2);
        studMainMenu(l);
#******************************** VIEW ISSUED BOOK<STUDENT>*********************
def viewIssuedBook(q):
    p=q.split(",");
    os.system("cls");
    os.system("color 6E");
    f=open("D:/Python Lucknow/issuedbook.txt");
    print("UID\t\tNAME\t\t\BOOK NAME");
    while(True):
        l=f.readline().split(",");
        if(l==['']):
            f.close();
            ch=input("Enter (Y/y) To Go Back:");
            if(ch=='y' or ch=='Y'):
                studMainMenu(q);
                break;
            else:
                exit();
        elif(p[1]==l[1]):
            print(l[0],'\t\t',l[1],'\t\t',l[2]);
    
#********************* ADMIN MENU *******************************
def adminMenu():
    os.system("cls");
    os.system("color 9F");
    
    print(" ".rjust(78,"="))
    print("                     ADMINSTRATIVE MENU WINDOW<AUTHORISED>")
    print(" ".rjust(78,"="))
    print("""    1. EXISTING USER(LOGIN)
    2. NEW USER(SIGN UP)
    3. DELETE USER
    4. LOG OFF
    5. EXIT.""");
    choice=input("        Enter Your Choice:")
    if(choice=='1'):
        adminLogin();
    elif(choice=='2'):
        adminRegister();
    elif(choice=='3'):
        admindelete();
    elif(choice=='4'):
        welcome();
    elif(choice=='5'):
        exit();
        
    else:
        print("Wrong Choice Try Again:");
        time.sleep(1);
        adminMenu();
#*********************** ADMIN REGISTRATION ************************
def adminRegister():
    os.system("cls");
    os.system("color 4F");
    
    check=1;
    print(" ".rjust(78,"="))
    print("                     NEW ADMIN REGISTRATION WINDOW")
    print(" ".rjust(78,"="))
    f=open('D:/Python Lucknow/admin.txt'); 

    id=input("Enter ADMIN ID(MUST BE UNIQUE):");
    while True:
        l=f.readline().split(",");
        print(l);
        if(id==l[0]):
            print("Record Already Exist! Kindly Proceed To Login:");
            time.sleep(2);
            f.close();
            adminMenu();
        if(l==['']):
                break;
    name=input("Enter ADMIN Name(MIN 4 CHARACTER):");
    username=name[:4]+str(id);
    while(check):
        pwd=input("Enter New Password:")
        cnfpwd=input("Re-Enter Password:");
        if(pwd!=cnfpwd):
            print("Password Do not Match! Kindly Enter Again!");
            check=1;
        else:
            break;
    filecontent=str(id)+","+name+","+username+","+pwd+"\n";
    print(filecontent);
    open('D:/Python Lucknow/admin.txt',"a").write(filecontent);
    print("Acocunt Created Successfully Wait(2 Second:)");
    time.sleep(2);
    f.close();
    adminMenu();
    
#*********************** ADMIN LOGIN ******************************
def adminLogin():
    os.system("cls");
    os.system("color 8E");
    print(" ".rjust(78,"="))
    print("                     ADMIN LOGIN WINDOW<AUTHORISED>");
    print(" ".rjust(78,"="))
    user=input("Enter UserName(99 for Main Menu):");
    pwd=input("Enter Password:");
    f=open('D:/Python Lucknow/admin.txt');
    l=f.readlines()
    m=0
    
    for i in l:
        if(user=='99'):
            welcome();
            break;
        print(i.split(','))
        if (user==i.split(',')[2] and pwd==i.split(',')[3].split()[-1]):
                print("Login SuccessFul:");
                m=1;
                f.close();
                adminMainMenu(i);     
    if m==0:
        print("Invalid UserName Or Password:Redirecting...");
        time.sleep(1/2);
        f.close();
        adminLogin();
         
#******************** ADMIN DELETE USER ********************************
def admindelete():
    print(" ".rjust(78,"="))
    print("                    DELETE USER WINDOW<AUTHORISED>")
    print(" ".rjust(78,"="))
    userid=input("Enter Your UserName(99 to Exit):");
    f=open("D:/Python Lucknow/admin.txt");
    f1=open("D:/Python Lucknow/admin1.txt","w");
    while True:
        if(userid==str(99)):
            adminMenu();
        l=f.readline().split(",")
        print(l);
        if(l==['']):
            print("User Id Does Not Exist:\nKindly Enter Again");
            f.close();
            f1.close();
            admindelete();
        if(l[2]==userid):
            f1.write(f.read());
            f1.close();
            f.close();
            os.remove("D:/Python Lucknow/admin.txt");
            os.rename("D:/Python Lucknow/admin1.txt","D:/Python Lucknow/admin.txt");
            print("Record Deleted!.....Wait(2 Sec)");
            time.sleep(3/2);
            adminMenu();
    filecontent=",".join(l);
    f1.write(filecontent);
# ************************* ADMIN MAIN MENU *****************************
def adminMainMenu(l):
    os.system("cls");
    os.system("color 9F");
    time.sleep(1/5);
    print(" ".rjust(78,"="))
    time.sleep(1/5);
    print("                     WELCOME TO CETPA LIBRARY MANAGEMET SYSTEM")
    time.sleep(1/5);
    print("                                INDRA NAGAR LUCKNOW UP")
    time.sleep(1/5);
    print("                        Console Based PROJECT BY MOHD MUJTABA")
    time.sleep(1/5);
    print(" ".rjust(78,"="))
    time.sleep(1/4);
    print(" ".rjust(78,"="))
    print("                               ADMIN MAIN MENU<AUTHORISED>")
    print(" ".rjust(78,"="))
    print("""\n\n   1. ADD NEW BOOK
   2. Delete BOOK
   3. View BOOKS
   4. Charge Fine
   5. Total Fine Collected
   6. LOG OFF.
   7. EXIT""");
#5. Fine Collected(Student Wise)
    choice=input("Enter Your Choice.......:");
    if(choice=='1'):
        addBook(l);
    elif(choice=='2'):
        delBook(l);
    elif(choice=='3'):
        viewBook(l);
    elif(choice=='4'):
        chargeFine(l);
##    elif(choice==5):
##        totalFineStudentWise(l);
    elif(choice=='5'):
        totalFine(l);
    elif(choice=='6'):
        adminMenu();
    elif(choice=='7'):
        exit();
    else:
        print("Wrong Option Selected! Try again..:");
        time.sleep(3/2);
        adminMainMenu(l);
#************************* ADD BOOK ********************************
def addBook(l):
    os.system("cls");
    os.system("color 4F");
    f=open("D:/Python Lucknow/addbook.txt","a");
    f1=open("D:/Python Lucknow/addbook.txt");

    isbn=input("Enter ISBN Number:");
    while True:
        l=f1.readline().split(",");
        print(l);
        
        if(isbn==l[0]):
            print("Record Already Exist! Redirecting To Main Menu......:");
            time.sleep(1.5);
            f.close();
            f1.close();
            adminMainMenu(l);
            
            
        if(l==['']):
                break;
    name=input("Enter Book Name:");
    author=input("Enter Author Name:");
    quantity=input("Enter Quantity:");
    issued=0;
    file=isbn+","+name+","+quantity+","+str(issued)+","+author+"\n"
    f.write(file);
    print("Record Updated Successfully.......");
    ch=input("Do You Want To Add More....(Y/N):");
    f.close();
    f1.close();
    if(ch=="y" or ch=='Y'):     
        addBook();
    else:
        adminMainMenu(l);
#****************************** VIEW BOOK *******************************
def viewBook(l):
    os.system("cls");
    os.system("color 6E");
    f=open("D:/Python Lucknow/addbook.txt");
    print("ISBN\t\tName\t\t\tQuantity\t\tIssued\t\tAuthor");
    while(True):
        l=f.readline().split(",");
        if(l==['']):
            f.close();
            ch=input("Enter (Y/y) To Go Back:");
            if(ch=='y' or ch=='Y'):
                adminMainMenu(l);
            else:
                exit();
        else:
            print(l[0],'\t\t',l[1],'\t\t',l[2],'\t\t',l[3]+'\t\t'+l[4]);    
# ******************************* DELETE BOOK ****************************
def delBook(l):
    print(" ".rjust(78,"="))
    print("                    DELETE BOOK RECORD<ADMIN>")
    print(" ".rjust(78,"="))
    isbn=input("Enter ISBN Number(99 to Exit):");
    f=open("D:/Python Lucknow/addbook.txt");
    f1=open("D:/Python Lucknow/addbook1.txt","w");
    while True:
        if(isbn==str(99)):
            adminMainMenu(l);
        else:
            l=f.readline().split(",")
            if(l==['']):
                print("Book Does Not Exist:\nKindly Enter Again");
                f.close();
                f1.close();
                delBook();
            if(l[0]==isbn):
                f1.write(f.read());
                f1.close();
                f.close();
                os.remove("D:/Python Lucknow/addbook.txt");
                os.rename("D:/Python Lucknow/addbook1.txt","D:/Python Lucknow/addbook.txt");
                print("Record Deleted!.....Wait(2 Sec)");
                time.sleep(3/2);
                adminMainMenu(l);
            else:
                filecontent=",".join(l);
                f1.write(filecontent);
#****************************** CHARGE FINE**************************
def chargeFine(l):
    os.system("cls");
    print(" ".rjust(78,"="))
    print("                    FINE COLLECTION WINDOW<ADMIN>")
    print(" ".rjust(78,"="))
    p=l.split(",");
    uid=p[0];
    name=p[1];
    print(uid,name);
    studid=input("Enter Student UID:");
    f=open("D:/Python Lucknow/studreg.txt","r").readlines();
    p=[i for i in f if(i.split(",")[0]==studid)]
    if(len(p)==0):
        print("NO UID FOUND! Redirecting.....");
        time.sleep(3/2);
        chargeFine(l);
    else:
        print("Student Name: ",p[0].split(",")[1]);
        studname=p[0].split(",")[1];
        bname=input("Enter Book Name for fine to be Charged:");
        f=open("D:/Python Lucknow/addbook.txt","r").readlines();
        p=[i for i in f if(i.split(",")[1]==bname)]
        if(len(p)==0):
            print("NO BOOK FOUND! Redirecting.....");
            time.sleep(3/2);
            chargeFine(l);
        else:
            fine=input("Enter Fine Amount:");
            file=studid+","+studname+","+bname+","+fine+","+uid+","+name+"\n";
            open("D:/Python Lucknow/fine.txt","a").write(file);
            print("Congrats!",studname,"You Have Been Fined for Rs:",fine);
            print("Please Wait Redirecting......");
            time.sleep(1);
            adminMainMenu(l);
#*******************************TOTAL FINE(STUDENT WISE)*******************
#*******************************TOTAL FINE**********************************
def totalFine(l):
    tot=0;
    f=open("D:/Python Lucknow/fine.txt","r").readlines();
    for i in f:
        tot+=int(i.split(",")[3])
    print("Total Fine Collected Till Now:",tot);
    ch=input("Press (Y/y) To Go Back:");
    if(ch=='y' or ch=="Y"):
        adminMainMenu(l);
    else:
        exit();
#************************** CALLING THE MAIN FUNCTION ****************
welcome();
