from tkinter import *


class App:

###########################################################################
    #this function pulls up the initial gui, of the initial log in window

    def __init__(self, master):
        from datetime import datetime
        self.currentDateTime=datetime.now()
        self.currentDateTimeStr = str(self.currentDateTime)
        self.cutcurrentDateTimeStr = self.currentDateTimeStr[:19]
        self.year = self.cutcurrentDateTimeStr[:4]

        self.month = self.cutcurrentDateTimeStr[5:7]

        self.day = self.cutcurrentDateTimeStr[8:10]
        self.today = [self.month+'/'+self.day+'/'+self.year]


        self.firstGUI=master
        master.title("Atlanta Beltline")
        w = Label(root, text="Atlanta Beltline Login")
        w.grid(row = 1)

        frame = Frame(master)
        frame.grid()

        Label(root, text="Username:").grid(row = 2)

        self.user = StringVar()
        self.usernameEnter = Entry(master, textvariable=self.user)




        self.usernameEnter.grid(row = 3)



        Label(root, text="Password:").grid(row = 4)

        self.passwd = StringVar()
        self.passwordEnter = Entry(master, textvariable=self.passwd)
        self.passwordEnter.grid(row = 5)


        self.login2 = Button(master, text="Login", command = self.login)
        self.login2.grid(row = 6)


        self.new2 = Button(master, text="Register", command = self.register_nav)
        self.new2.grid(row = 7)

        #self.connect()
        #query = ("SELECT fname FROM EMPLOYEE")
        #cursor = self.db.cursor()
        #cursor.execute(query)
        #names = cursor.fetchall()
        #curr = 8
        #for x in names:
        #    Label(self.new2, text=x).grid(row = curr)
        #    curr = curr + 1
        #Label(self.new2, text=names).grid(row = 8)

###########################################################################
#this function connects to the db

    def connect(self):
        import pymysql
        try:

        #get in that database yo

                self.db=pymysql.connect(host="localhost",
				user="root",
				passwd="", # insert your db password here
				db="company")
                return self.db
        except:
               messagebox.showwarning("Internet?", "Please check your internet connection.")

###########################################################################
    def register_nav(self):
            #withdraw first log in page and pull up new user gui
            self.firstGUI.withdraw()
            self.navGUI = Toplevel()
            self.navGUI.title("Register Navigation")

            Label(self.navGUI, text="Register Navigation").grid(row = 1)

            frame = Frame(self.navGUI)
            frame.grid()

            self.register = Button(self.navGUI, text="User Only", command = self.register_user).grid(row=2)
            self.register = Button(self.navGUI, text="Visitor Only", command = self.register_visitor).grid(row=3)
            self.register = Button(self.navGUI, text="Employee Only", command = self.register_employee).grid(row=4)
            self.register = Button(self.navGUI, text="Employee-Visitor", command = self.register_employee_visitor).grid(row=5)
            self.register = Button(self.navGUI, text="Back", command = self.back).grid(row=6)

###########################################################################
    def login(self):
        pass


###########################################################################
# TODO: still need to finish this, the screen is not complete yet
    def register_user(self):
        self.navGUI.withdraw()
        self.regUser = Toplevel()
        self.regUser.title("Register User")

        frame = Frame(self.regUser)
        frame.grid()

        Label(self.regUser, text="Register User").grid(row = 1, column = 1)

        Label(self.regUser, text="First Name: ").grid(row = 2, column = 0)
        self.fname = StringVar()
        self.fname_enter = Entry(self.regUser, textvariable=self.fname)
        self.fname_enter.grid(row = 2, column = 1)

        Label(self.regUser, text="Last Name: ").grid(row = 2, column = 2)
        self.lname = StringVar()
        self.lname_enter = Entry(self.regUser, textvariable=self.lname)
        self.lname_enter.grid(row = 2, column = 3)

        Label(self.regUser, text="Username: ").grid(row = 3, column = 0)
        self.user = StringVar()
        self.username_enter = Entry(self.regUser, textvariable=self.user)
        self.username_enter.grid(row = 3, column = 1)

        Label(self.regUser, text="Password: ").grid(row = 4, column = 0)
        self.password = StringVar()
        self.password_enter = Entry(self.regUser, textvariable=self.password)
        self.password_enter.grid(row = 4, column = 1)

        Label(self.regUser, text="Confirm Password: ").grid(row = 4, column = 2)
        self.password_confirm = StringVar()
        self.password_confirm_enter = Entry(self.regUser, textvariable=self.password_confirm)
        self.password_confirm_enter.grid(row = 4, column = 3)

        Label(self.regUser, text="Email: ").grid(row = 5, column = 0)
        self.email = StringVar()
        self.email_enter = Entry(self.regUser, textvariable=self.email)
        self.email_enter.grid(row = 5, column = 1)

        self.registerUser = Button(self.regUser, text="Back", command = self.register_user_back).grid(row = 6, column = 1)
        self.registerUser = Button(self.regUser, text="Register", command = self.register_login_user).grid(row = 6, column = 2)


###########################################################################
    def register_visitor(self):
        self.navGUI.withdraw()
        self.regVisitor = Toplevel()
        self.regVisitor.title("Register Visitor")

        frame = Frame(self.regVisitor)
        frame.grid()

        Label(self.regVisitor, text="Register Visitor", anchor="center", justify="center").grid(row = 1)


        Label(self.regVisitor, text="First Name: ").grid(row = 2, column = 0)
        self.fname = StringVar()
        self.fname_enter = Entry(self.regVisitor, textvariable=self.fname)
        self.fname_enter.grid(row = 2, column = 1)

        Label(self.regVisitor, text="Last Name: ").grid(row = 2, column = 2)
        self.lname = StringVar()
        self.lname_enter = Entry(self.regVisitor, textvariable=self.lname)
        self.lname_enter.grid(row = 2, column = 3)

        Label(self.regVisitor, text="Username: ").grid(row = 3, column = 0)
        self.user = StringVar()
        self.username_enter = Entry(self.regVisitor, textvariable=self.user)
        self.username_enter.grid(row = 3, column = 1)

        Label(self.regVisitor, text="Password: ").grid(row = 4, column = 0)
        self.password = StringVar()
        self.password_enter = Entry(self.regVisitor, textvariable=self.password)
        self.password_enter.grid(row = 4, column = 1)

        Label(self.regVisitor, text="Confirm Password: ").grid(row = 4, column = 2)
        self.password_confirm = StringVar()
        self.password_confirm_enter = Entry(self.regVisitor, textvariable=self.password_confirm)
        self.password_confirm_enter.grid(row = 4, column = 3)

        Label(self.regVisitor, text="Email: ").grid(row = 5, column = 0)
        self.email = StringVar()
        self.email_enter = Entry(self.regVisitor, textvariable=self.email)
        self.email_enter.grid(row = 5, column = 1)

        self.registerUser = Button(self.regVisitor, text="Back", command = self.register_visitor_back).grid(row = 6, column = 1)
        self.registerUser = Button(self.regVisitor, text="Register", command = self.register_login_visitor).grid(row = 6, column = 2)

###########################################################################
    def register_employee(self):
        self.navGUI.withdraw()
        self.regEmp = Toplevel()
        self.regEmp.title("Register Employee")

        frame = Frame(self.regEmp)
        frame.grid()

        Label(self.regEmp, text="Register Employee").grid(row = 1)

        Label(self.regEmp, text="First Name: ").grid(row = 2, column = 0)
        self.fname = StringVar()
        self.fname_enter = Entry(self.regEmp, textvariable=self.fname)
        self.fname_enter.grid(row = 2, column = 1)

        Label(self.regEmp, text="Last Name: ").grid(row = 2, column = 2)
        self.lname = StringVar()
        self.lname_enter = Entry(self.regEmp, textvariable=self.lname)
        self.lname_enter.grid(row = 2, column = 3)

        Label(self.regEmp, text="Username: ").grid(row = 3, column = 0)
        self.user = StringVar()
        self.username_enter = Entry(self.regEmp, textvariable=self.user)
        self.username_enter.grid(row = 3, column = 1)

        Label(self.regEmp, text="User Type: ").grid(row = 3, column = 2)
        self.userType = StringVar()
        choices = ["Manager", "Staff"]
        self.userType.set("Manager")
        self.popupMenu = OptionMenu(self.regEmp, self.userType, *choices)
        self.popupMenu.grid(row = 3, column = 3)

        Label(self.regEmp, text="Password: ").grid(row = 4, column = 0)
        self.password = StringVar()
        self.password_enter = Entry(self.regEmp, textvariable=self.password)
        self.password_enter.grid(row = 4, column = 1)

        Label(self.regEmp, text="Confirm Password: ").grid(row = 4, column = 2)
        self.password_confirm = StringVar()
        self.password_confirm_enter = Entry(self.regEmp, textvariable=self.password_confirm)
        self.password_confirm_enter.grid(row = 4, column = 3)

        Label(self.regEmp, text="Phone: ").grid(row = 5, column = 0)
        self.phone = IntVar()
        self.phone_enter = Entry(self.regEmp, textvariable=self.phone)
        self.phone_enter.grid(row = 5, column = 1)

        Label(self.regEmp, text="Address: ").grid(row = 5, column = 2)
        self.address = StringVar()
        self.address_enter = Entry(self.regEmp, textvariable=self.address)
        self.address_enter.grid(row = 5, column = 3)

        Label(self.regEmp, text="City: ").grid(row = 6, column = 0)
        self.city = StringVar()
        self.city_enter = Entry(self.regEmp, textvariable=self.city)
        self.city_enter.grid(row = 6, column = 1)

        Label(self.regEmp, text="State: ").grid(row = 6, column = 2)
        self.state = StringVar()
        choices_state = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "Other"]
        self.state.set("AL")
        self.popupMenuState = OptionMenu(self.regEmp, self.state, *choices_state)
        self.popupMenuState.grid(row = 6, column = 3)

        Label(self.regEmp, text="Zipcode: ").grid(row = 6, column = 4)
        self.zip = IntVar()
        self.zip_enter = Entry(self.regEmp, textvariable=self.zip)
        self.zip_enter.grid(row = 6, column = 5)

        Label(self.regEmp, text="Email: ").grid(row = 7, column = 0)
        self.email = StringVar()
        self.email_enter = Entry(self.regEmp, textvariable=self.email)
        self.email_enter.grid(row = 7, column = 1)

        self.registerUser = Button(self.regEmp, text="Back", command = self.register_emp_back).grid(row = 8, column = 1)
        self.registerUser = Button(self.regEmp, text="Register", command = self.register_login_emp).grid(row = 8, column = 2)

###########################################################################
    def register_employee_visitor(self):
        self.navGUI.withdraw()
        self.regEmpVis = Toplevel()
        self.regEmpVis.title("Register Employee-Visitor")

        frame = Frame(self.regEmpVis)
        frame.grid()

        Label(self.regEmpVis, text="Register Employee").grid(row = 1)

        Label(self.regEmpVis, text="First Name: ").grid(row = 2, column = 0)
        self.fname = StringVar()
        self.fname_enter = Entry(self.regEmpVis, textvariable=self.fname)
        self.fname_enter.grid(row = 2, column = 1)

        Label(self.regEmpVis, text="Last Name: ").grid(row = 2, column = 2)
        self.lname = StringVar()
        self.lname_enter = Entry(self.regEmpVis, textvariable=self.lname)
        self.lname_enter.grid(row = 2, column = 3)

        Label(self.regEmpVis, text="Username: ").grid(row = 3, column = 0)
        self.user = StringVar()
        self.username_enter = Entry(self.regEmpVis, textvariable=self.user)
        self.username_enter.grid(row = 3, column = 1)

        Label(self.regEmpVis, text="User Type: ").grid(row = 3, column = 2)
        self.userType = StringVar()
        choices = ["Manager", "Staff"]
        self.userType.set("Manager")
        self.popupMenu = OptionMenu(self.regEmpVis, self.userType, *choices)
        self.popupMenu.grid(row = 3, column = 3)

        Label(self.regEmpVis, text="Password: ").grid(row = 4, column = 0)
        self.password = StringVar()
        self.password_enter = Entry(self.regEmpVis, textvariable=self.password)
        self.password_enter.grid(row = 4, column = 1)

        Label(self.regEmpVis, text="Confirm Password: ").grid(row = 4, column = 2)
        self.password_confirm = StringVar()
        self.password_confirm_enter = Entry(self.regEmpVis, textvariable=self.password_confirm)
        self.password_confirm_enter.grid(row = 4, column = 3)

        Label(self.regEmpVis, text="Phone: ").grid(row = 5, column = 0)
        self.phone = IntVar()
        self.phone_enter = Entry(self.regEmpVis, textvariable=self.phone)
        self.phone_enter.grid(row = 5, column = 1)

        Label(self.regEmpVis, text="Address: ").grid(row = 5, column = 2)
        self.address = StringVar()
        self.address_enter = Entry(self.regEmpVis, textvariable=self.address)
        self.address_enter.grid(row = 5, column = 3)

        Label(self.regEmpVis, text="City: ").grid(row = 6, column = 0)
        self.city = StringVar()
        self.city_enter = Entry(self.regEmpVis, textvariable=self.city)
        self.city_enter.grid(row = 6, column = 1)

        Label(self.regEmpVis, text="State: ").grid(row = 6, column = 2)
        self.state = StringVar()
        choices_state = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "Other"]
        self.state.set("AL")
        self.popupMenuState = OptionMenu(self.regEmpVis, self.state, *choices_state)
        self.popupMenuState.grid(row = 6, column = 3)

        Label(self.regEmpVis, text="Zipcode: ").grid(row = 6, column = 4)
        self.zip = IntVar()
        self.zip_enter = Entry(self.regEmpVis, textvariable=self.zip)
        self.zip_enter.grid(row = 6, column = 5)

        Label(self.regEmpVis, text="Email: ").grid(row = 7, column = 0)
        self.email = StringVar()
        self.email_enter = Entry(self.regEmpVis, textvariable=self.email)
        self.email_enter.grid(row = 7, column = 1)

        self.registerUser = Button(self.regEmpVis, text="Back", command = self.register_empVis_back).grid(row = 8, column = 1)
        self.registerUser = Button(self.regEmpVis, text="Register", command = self.register_login_empVis).grid(row = 8, column = 2)

###########################################################################
    def back(self):
        self.navGUI.withdraw()
        self.firstGUI.deiconify()

###########################################################################
    def register_user_back(self):
        self.regUser.withdraw()
        self.navGUI.deiconify()

###########################################################################
    def register_login_user(self):
        pass

###########################################################################
    def register_visitor_back(self):
        self.regVisitor.withdraw()
        self.navGUI.deiconify()

###########################################################################
    def register_login_visitor(self):
        pass

###########################################################################
    def register_emp_back(self):
        self.regEmp.withdraw()
        self.navGUI.deiconify()

###########################################################################
    def register_login_emp(self):
        pass

###########################################################################
    def register_empVis_back(self):
        self.regEmpVis.withdraw()
        self.navGUI.deiconify()

###########################################################################
    def register_login_empVis(self):
        pass

root = Tk()

app = App(root)


root.mainloop()
