import os
import mysql.connector as sc
import datetime as dt

#Function to check availibity of a Book no. 
def checkbook(bno):
    try:
        con=sc.connect(host='localhost',user=username,passwd=password,database='library')
        cur=con.cursor()
        cur.execute("Select count(*) from book where bno={} ".format(bno))
        data=cur.fetchall()
        d=data[0][0]
        con.close()
        return d
    except:
        return 

#Function to check availibity of a Member no.. 
def checkmember(idd):
    con=sc.connect(host='localhost',user=username,passwd=password,database='library')
    cur=con.cursor()
    cur.execute("Select count(*) from member where id={} ".format(idd))
    data=cur.fetchall()
    d=data[0][0]
    con.close()
    return d

#Function to check availibity of a issue no. 
def checkissue(iss):
    con=sc.connect(host='localhost',user=username,passwd=password,database='library')
    cur=con.cursor()
    cur.execute("Select count(*) from register where is_no={} ".format(iss))
    data=cur.fetchall()
    d=data[0][0]
    con.close()
    return d

#Function to check book with member. 
def checki_book_member(iss):
    con=sc.connect(host='localhost',user=username,passwd=password,database='library')
    cur=con.cursor()
    cur.execute("Select count(*) from register where id={} ".format(iss))
    data=cur.fetchall()
    d=data[0][0]
    con.close()
    return d

#Function to check availibity of a issue no. 
def checkqty(bno):
    con=sc.connect(host='localhost',user=username,passwd=password,database='library')
    cur=con.cursor()
    cur.execute("Select copy from book where bno={} ".format(bno))
    data=cur.fetchone()
    d=data[0]
    con.close()
    return d

    
#Function to register a book
def book():
    os.system('cls')
    ch='y'
    while ch=='y' or ch=='Y':
        con=sc.connect(host='localhost',database='library',user=username,password=password)  
        cur=con.cursor()
        try:
            os.system('cls')
            print('************************************************************')
            print('*                Library Management System                 *')
            print('************************************************************')
            bno=int(input("    Enter Book No. \t\t\t: "))
            bno=int("102"+str(bno))
            while checkbook(bno):
                print("    Entered Book No. already Exits ")
                bno=int(input("    Enter Book No. \t\t\t: "))
                bno=int("102"+str(bno))
                
            bname=input("    Enter Book Name\t\t\t: ")
            author=input("    Enter Author Name\t\t\t: ")
            price=float(input("    Enter Book Price\t\t\t: "))
            qty=int(input("    Enter Quantity   \t\t\t: "))
            cur.execute("insert into book(bno,bname,author,price,copy) values({},'{}','{}',{},{})".format(bno,bname,author,price,qty))
            con.commit()
            print('************************************************************')
            print("\t\tBook Succesfully Registered")
            print('************************************************************')
            ch=input("\tDo you want to register another book?(y/n)")
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during registering book.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")

#Function to register a member
def member():
    os.system('cls')
    ch='y'
    while ch=='y' or ch=='Y':
        con=sc.connect(host='localhost',database='library',user=username,password=password)  
        cur=con.cursor()
        try:
            os.system('cls')
            print('************************************************************')
            print('*                Library Management System                 *')
            print('************************************************************')
            mno=int(input("    Enter Member No. \t\t\t: "))
            mno=int("101"+str(mno))
            while checkmember(mno):
                print("    Entered Member No. already Exits ")
                mno=int(input("    Enter Member No. \t\t\t: "))
                mno=int("101"+str(mno))
                
            name=input("    Enter Member Name\t\t\t: ")
            mob=input("    Enter Mobile No.   \t\t\t: ")
            df=dt.date.today()
            if df.month<10:
                jdate=str(df.year)+"-0"+str(df.month)+"-"+str(df.day)
            else:
                jdate=str(df.year)+"-"+str(df.month)+"-"+str(df.day)
            cur.execute("insert into member(id,name,join_date,mob) values({},'{}','{}','{}')".format(mno,name,jdate,mob))
            con.commit()
            print('************************************************************')
            print("\t\tMember Registered Succesfully")
            print('************************************************************')
            ch=input("\tDo you want to register other member?(y/n)")
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during Member Registration.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")


#Function to view issue a book
def register():
    os.system('cls')
    ch='y'
    while ch=='y' or ch=='Y':
        con=sc.connect(host='localhost',database='library',user=username,password=password)  
        cur=con.cursor()
        try:
            os.system('cls')
            print('************************************************************')
            print('*                Library Management System                 *')
            print('************************************************************')
            ino=int(input("    Enter Issue No. \t\t\t: "))
            ino=int("103"+str(ino))
            while checkissue(ino):
                print("    Entered Issue No. already Exits ")
                ino=int(input("    Enter Issue No. \t\t\t: "))
                ino=int("103"+str(ino))
            bno=int(input("    Enter Book no.\t\t\t: "))
            bno=int("102"+str(bno))
            while checkbook(bno)==0 or checkqty(bno)==0:
                print("    Entered Book no. not exits ")
                bno=int(input("    Enter Book no.\t\t\t: "))
                bno=int("102"+str(bno))
            mno=int(input("    Enter Member No. \t\t\t: "))
            mno=int("101"+str(mno))
            while checkmember(mno)==0:
                print("    Entered Member Not already Exits ")
                mno=int(input("    Enter Member No. \t\t\t: "))
                mno=int("101"+str(mno))
            df=dt.date.today()
            if df.month<10:
                idate=str(df.year)+"-0"+str(df.month)+"-"+str(df.day)
            else:
                idate=str(df.year)+"-"+str(df.month)+"-"+str(df.day)
            dew=input("    Enter Due date (yyyy-mm-dd) \t: ")  
            cur.execute("insert into register(is_no,bno,id,issue_date,dew_date) values({},{},{},'{}','{}')".format(ino,bno,mno,idate,dew))
            con.commit()
            cur.execute("update book set copy=copy-1 where bno={}".format(bno))
            con.commit()
            print('************************************************************')
            print("\t\tBook Issued Succesfully")
            print('************************************************************')
            ch=input("\tDo you want to Issue more books?(y/n)")
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during Issuing Book.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")






#Function to view member details 
def view():
    ch='y'
    while ch=='y' or ch=='Y':
        try:
            con=sc.connect(host='localhost',database='library',user=username,password=password)  
            cur=con.cursor()
            os.system('cls')
            print('************************************************************')
            print('*                Library Management System                 *')
            print('************************************************************')
            mno=int(input("    Enter Member No. \t\t\t: "))
            mno=int("101"+str(mno))
            while checkmember(mno)==0:
                print("    Entered Member Not Exits ")
                mno=int(input("    Enter Member No. \t\t\t: "))
                mno=int("101"+str(mno))
               
            cur.execute("Select name,bname,issue_date,dew_date,return_date, mob from book b,register r,member m where b.bno=r.bno and m.id=r.id and m.id={}".format(mno))
            data=cur.fetchone()
            os.system('cls')
            print('************************************************************')
            print('*                     Member  Details                      *')
            print('************************************************************')
            print('                 Member No.       : ',mno)
            print('                 Member Name      : ',data[0])
            print('                 Book Name        : ',data[1])
            print('                 Issue Date       : ',data[2])
            print('                 Due Date         : ',data[3])
            print('                 Return Date      : ',data[4])
            print('                 Mobile           : ',data[5])
            print('************************************************************')
            ch=input("\tDo you want to View another record?(y/n)")
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during viewing.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")
    
 

#Function to view list of Book present in library
def list_all_book():
    ch='y'
    while ch=='y' or ch=='Y':
        try:
            con=sc.connect(host='localhost',database='library',user=username,password=password)  
            cur=con.cursor()
            os.system('cls')
            print('************************************************************')
            print('*                Library Management System                 *')
            print('************************************************************')
            cur.execute("Select bno,bname,copy from book ")
            data=cur.fetchall()
            os.system('cls')
            print('************************************************************')
            print('*                     List of Books                        *')
            print('************************************************************')
            print('\tBook No.\t Book Name\t\tQty')
            print('------------------------------------------------------------')
            print('\t',end="")
            for row in data:
                for d in row:
                    print(d,end='\t\t')
                print()
                if not row==data[-1]:
                    print('\t',end="")
            print('************************************************************')
            ch=input("Press any key to Continue...")
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during Viewing.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")


#Function to view list of Registered members
def list_all_members():
    ch='y'
    while ch=='y' or ch=='Y':
        try:
            con=sc.connect(host='localhost',database='library',user=username,password=password)  
            cur=con.cursor()
            os.system('cls')
            print('************************************************************')
            print('*                Library Management System                 *')
            print('************************************************************')
            cur.execute("Select id,name,mob from member ")
            data=cur.fetchall()
            os.system('cls')
            print('************************************************************')
            print('*                     List of Members                      *')
            print('************************************************************')
            print('\tMember No.\t Member Name\t\tMobile')
            print('------------------------------------------------------------')
            print('\t',end="")
            for row in data:
                for d in row:
                    print(d,end='\t\t')
                print()
                if not row==data[-1]:
                    print('\t',end="")
            print('************************************************************')
            ch=input("Press any key to Continue...")
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during Viewing.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")


#Function to view list of Book issued with member name 
def list_all():
    ch='y'
    while ch=='y' or ch=='Y':
        try:
            con=sc.connect(host='localhost',database='library',user=username,password=password)  
            cur=con.cursor()
            os.system('cls')
            print('************************************************************')
            print('*                Library Management System                 *')
            print('************************************************************')
            cur.execute("Select is_no,name,bname,dew_date from book b,register r,member m where b.bno=r.bno and m.id=r.id")
            data=cur.fetchall()
            os.system('cls')
            print('************************************************************')
            print('*                     List of Books Issued                 *')
            print('************************************************************')
            print('\tIssue No. Member Name   Book Name\tDue date')
            print('------------------------------------------------------------')
            print('\t',end="")
            for row in data:
                for d in row:
                    print(d,end='\t')
                print()
                if not row==data[-1]:
                    print('\t',end="")
            print('************************************************************')
            ch=input("Press any key to Continue...")
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during Viewing.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")




#Function to Extend due Date
def extend():
    ch='y'
    while ch=='y' or ch=='Y':
        try:
            con=sc.connect(host='localhost',database='library',user=username,password=password)  
            cur=con.cursor()
            os.system('cls')
            print('************************************************************')
            print('*                Library Management System                 *')   
            print('************************************************************')
            print('*                                                          *')
            print('*                 1. Extend Due date                       *')
            print('*                 2. Cancel Membership                     *')
            print('*                                                          *')
            print('************************************************************')
            opt=int(input('                  Enter Option :- '))
            print('************************************************************')
            if opt==1:
                os.system('cls')
                list_all()
                ino=int(input("    Enter Issue No. \t\t\t: "))
                ino=int("103"+str(ino))
                while checkissue(ino)==0:
                    print("    Entered Issue No. not Exits ")
                    ino=int(input("    Enter Issue No. \t\t\t: "))
                    ino=int("103"+str(ino))
                print('************************************************************')
                dew=input("\t\tEnter new Due Date  :  ")
                cur.execute("update register set dew_date='{}' where is_no={}".format(dew,ino))     
                con.commit()
                print('************************************************************')
                print("\t\tDue date Succesfully Extended")
                print('************************************************************')
            elif opt==2:
                list_all_members()
                mno=int(input("    Enter Member No. \t\t\t: "))
                mno=int("101"+str(mno))
                while checkmember(mno)==0:
                    print("    Entered Member Not Exits ")
                    mno=int(input("    Enter Member No. \t\t\t: "))
                    mno=int("101"+str(mno))
                while checki_book_member(mno):
                    print('************************************************************')
                    print("\tBooks pending = ",checki_book_member(mno),"\n\tPlease Return all book First")
                    print('************************************************************')
                    input("Press any key to return books.")
                    ret_book()
                    
                cur.execute("delete from member where id={}".format(mno))     
                con.commit()
                print('************************************************************')
                print("\t\tMembership successfully cancelled")
                print('************************************************************')

            ch=input("\tDo you want to update anything else?(y/n)")
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during updating.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")
        


#Function to Return a book
def ret_book():
    ch='y'
    while ch=='y' or ch=='Y':
        try:
            con=sc.connect(host='localhost',database='library',user=username,password=password)  
            cur=con.cursor()
            os.system('cls')
            list_all()
            ino=int(input("    Enter Issue No. \t\t\t: "))
            ino=int("103"+str(ino))
            while checkissue(ino)==0:
                print("    Entered Issue No. not Exits ")
                ino=int(input("    Enter Issue No. \t\t\t: "))
                ino=int("103"+str(ino))
            cur.execute("update book set copy=copy+1 where bno in(select bno from register where is_no={})".format(ino))
            con.commit()
            cur.execute("delete from register where is_no={}".format(ino))
            con.commit()
            print('************************************************************')
            print('*                                                          *')
            print('*               Book Returned Successfully                 *')
            print('*                                                          *')
            print('************************************************************')
            ch=input("\tDo you want to return another book?(y/n)")
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during returning book.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")
    



#Main

username = input("Enter your username: ")
password = input("Enter your password: ")

ch=1

while ch!=0 :
    os.system('cls')
    print('************************************************************')
    print('*                Library Management System                 *')
    print('************************************************************')
    print('*                                                          *')
    print('*                 1. Book Entry                            *')
    print('*                 2. Register Member                       *')
    print('*                 3. Issue Book                            *')
    print('*                 4. View Member issued Books              *')
    print('*                 5. View All Books                        *')
    print('*                 6. View All Members                      *')
    print('*                 7. View All issued Books                 *')
    print('*                 8. Update details                        *')
    print('*                 9. Return Book                           *')
    print('*                 0. Exit                                  *')
    print('*                                                          *')
    print('************************************************************')
    ch=int(input('                  Enter Option :- '))

    if ch==1:
        book()
    elif ch==2:
        member()
    elif ch==3:
        register()
    elif ch==4:
        view()
    elif ch==5:
        list_all_book()
    elif ch==6:
        list_all_members()
    elif ch==7:
        list_all()
    elif ch==8:
        extend()
    elif ch==9:
        ret_book()
