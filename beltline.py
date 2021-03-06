from tkinter import *
from tkinter import ttk, messagebox
import datetime
import hashlib


class App:

    ###########################################################################
    # this function pulls up the initial gui, of the initial log in window
    def __init__(self, master):
        self.currGui = None
        self.prevGUI = None
        self.userType = "User"
        from datetime import datetime
        self.currentDateTime = datetime.now()
        self.currentDateTimeStr = str(self.currentDateTime)
        self.cutcurrentDateTimeStr = self.currentDateTimeStr[:19]
        self.year = self.cutcurrentDateTimeStr[:4]

        self.month = self.cutcurrentDateTimeStr[5:7]

        self.day = self.cutcurrentDateTimeStr[8:10]
        self.today = [self.month + '/' + self.day + '/' + self.year]
        self.firstGUI = master
        self.currGui = self.firstGUI
        master.title("Atlanta Beltline")
        w = Label(root, text="Atlanta Beltline Login")
        w.grid(row=1)
        self.connect()

        self.cursor = self.db.cursor()
        
        self.hash_all_passwords()
        frame = Frame(master)
        frame.grid()

        Label(root, text="Username:").grid(row=2)

        self.user = StringVar()
        self.usernameEnter = Entry(master, textvariable=self.user)

        self.usernameEnter.grid(row=3)

        Label(root, text="Password:").grid(row=4)

        self.passwd = StringVar()
        self.passwordEnter = Entry(master, textvariable=self.passwd)
        self.passwordEnter.grid(row=5)

        self.login2 = Button(master, text="Login", command=self.login)
        self.login2.grid(row=6)

        self.new2 = Button(master, text="Register", command=self.register_nav)
        self.new2.grid(row=7)

        self.new3 = Button(master, text = "Manage Profile", command = self.manage_profile)
        self.new3.grid(row = 8)

        #print(self.userType)

    ###########################################################################
    # this function connects to the db

    def connect(self):
        import pymysql
        try:

            # get in that database yo

            self.db = pymysql.connect(host="localhost",
                                      user="root",
                                      passwd="savirahe",  # insert your db password here
                                      db="beltLine")
            return self.db
        except:
            messagebox.showwarning("Internet?", "Please check your internet connection.")

    ###########################################################################
    def register_nav(self):
        # withdraw first log in page and pull up new user gui
        self.firstGUI.withdraw()
        self.navGUI = Toplevel()
        self.prevGUI = self.currGui
        self.currGui = self.navGUI
        self.navGUI.title("Register Navigation")

        Label(self.navGUI, text="Register Navigation").grid(row=1)

        frame = Frame(self.navGUI)
        frame.grid()

        self.register = Button(self.navGUI, text="User Only", command=self.register_user).grid(row=2)
        self.register = Button(self.navGUI, text="Visitor Only", command=self.register_visitor).grid(row=3)
        self.register = Button(self.navGUI, text="Employee Only", command=self.register_employee).grid(row=4)
        self.register = Button(self.navGUI, text="Employee-Visitor", command=self.register_employee_visitor).grid(row=5)
        self.register = Button(self.navGUI, text="Back", command=self.back).grid(row=6)

    ###########################################################################
    def login(self):
        userTypeQuery = ("SELECT User_Type FROM normaluser WHERE Username ='" + self.user.get().__str__() + "'")
        self.cursor.execute(userTypeQuery)
        self.userType = None
        try:
            self.userType = self.cursor.fetchone()[0]
        except:
            messagebox.showinfo("Error!", "We Could Not Find a User With That Username")

        userName = self.user.get().__str__()
        userPassword = self.passwd.get().__str__()
        print(userPassword)

        # User Only
        if self.userType == "User":
            if self.check_password(userName, userPassword):
                self.user_functionality()
            else:
                messagebox.showinfo("Error!", "Your Password was Incorrect")


        elif self.userType == "Visitor":
            if self.check_password(userName,userPassword):
                self.visitor_functionality()
            else :
                messagebox.showinfo("Error!", "Your Password was Incorrect")

        # Employee Only
        elif self.userType == "Employee":
            subTypeQuery = ("SELECT Employee_Type FROM employee WHERE Username = '" + self.user.get().__str__() + "'")
            self.cursor.execute(subTypeQuery)
            self.UserSubtype = self.cursor.fetchone()[0]

            if self.UserSubtype == "Staff":
                if self.check_password(userName, userPassword):
                    self.staff_only_functionality()
                else:
                    messagebox.showinfo("Error!", "Your Password was Incorrect")
            elif self.UserSubtype == "Admin":
                if self.check_password(userName, userPassword):
                    self.admin_only_functionality()
                else:
                    messagebox.showinfo("Error!", "Your Password was Incorrect")
            elif self.UserSubtype == "Manager":
                if self.check_password(userName, userPassword):
                    self.manager_only_functionality()
                else:
                    messagebox.showinfo("Error!", "Your Password was Incorrect")

        # Employee and Visitor
        if self.userType == "Employee, Visitor":
            subTypeTwoQuery = ("SELECT Employee_Type FROM employee WHERE Username = '" + self.user.get().__str__() + "'")
            self.cursor.execute(subTypeTwoQuery)
            self.UserSubtype = self.cursor.fetchone()[0]

            if self.UserSubtype == "Staff":
                if self.check_password(userName, userPassword):
                    self.staff_visitor_functionality()
                else:
                    messagebox.showinfo("Error!", "Your Password was Incorrect")
            elif self.UserSubtype == "Admin":
                if self.check_password(userName, userPassword):
                    self.admin_vis_functionality()
                else:
                    messagebox.showinfo("Error!", "Your Password was Incorrect")
            elif self.UserSubtype == "Manager":
                if self.check_password(userName, userPassword):
                    self.manager_vis_functionality()
                else:
                    messagebox.showinfo("Error!", "Your Password was Incorrect")

    def check_password(self, username ,password):
        self.cursor.execute("SELECT User_password from normalUser WHERE Username ='" + username + "'")
        #Gets Password from Database
        databsePassword = self.cursor.fetchone()[0]

        #Hashes Password Given
        tempPass = hashlib.md5(password.encode())
        testPassword = tempPass.hexdigest()

        if databsePassword == testPassword:
            return True
        else :
            return False

    def hash_all_passwords(self):
        rows = self.cursor.execute("SELECT User_password from normaluser")
        cnt = 0
        print(rows)
        for password in self.cursor.fetchall():
            normalPassword = password
            hashedPassword = hashlib.md5(normalPassword[0].encode())
            print()
            self.cursor.execute("UPDATE beltline.normaluser SET User_password = '"+ hashedPassword.hexdigest() + "' WHERE User_password = '" + normalPassword[0]+"'")

    def reg_hash_password(self, password):
        normalPassword = password
        hashedPassword = hashlib.md5(normalPassword[0].encode())
        return hashedPassword.hexdigest()

    ###########################################################################
    # TODO: still need to finish this, the screen is not complete yet
    def register_user(self):
        self.navGUI.withdraw()
        self.regUser = Toplevel()
        self.prevGUI = self.currGui
        self.currGui = self.regUser
        self.regUser.title("Register User")

        Label(self.regUser, text="Register User").grid(row=0)

        frame = Frame(self.regUser)
        frame.grid()

        Label(frame, text="First Name: ").grid(row=0, column=0)
        self.fname = StringVar()
        self.fname_enter = Entry(frame, textvariable=self.fname)
        self.fname_enter.grid(row=0, column=1)

        Label(frame, text="Last Name: ").grid(row=0, column=2)
        self.lname = StringVar()
        self.lname_enter = Entry(frame, textvariable=self.lname)
        self.lname_enter.grid(row=0, column=3)

        Label(frame, text="Username: ").grid(row=1, column=0)
        self.user = StringVar()
        self.username_enter = Entry(frame, textvariable=self.user)
        self.username_enter.grid(row=1, column=1)

        Label(frame, text="Password: ").grid(row=2, column=0)
        self.password = StringVar()
        self.password_enter = Entry(frame, textvariable=self.password)
        self.password_enter.grid(row=2, column=1)

        Label(frame, text="Confirm Password: ").grid(row=2, column=2)
        self.password_confirm = StringVar()
        self.password_confirm_enter = Entry(frame, textvariable=self.password_confirm)
        self.password_confirm_enter.grid(row=2, column=3)

        Label(frame, text="Email: ").grid(row=3, column=0)
        self.email = StringVar()
        self.email_enter = Entry(frame, textvariable=self.email)
        self.email_enter.grid(row=3, column=1)

        self.registerUser = Button(frame, text="Back", command=self.register_user_back).grid(row=4, column=1)
        self.registerUser = Button(frame, text="Register", command=self.register_login_user).grid(row=4, column=2)

    ###########################################################################
    def register_visitor(self):
        self.navGUI.withdraw()
        self.regVisitor = Toplevel()
        self.prevGUI = self.currGui
        self.currGui = self.regVisitor
        self.regVisitor.title("Register Visitor")

        Label(self.regVisitor, text="Register Visitor").grid(row=0)

        frame = Frame(self.regVisitor)
        frame.grid()

        Label(frame, text="First Name: ").grid(row=0, column=0)
        self.fname = StringVar()
        self.fname_enter = Entry(frame, textvariable=self.fname)
        self.fname_enter.grid(row=0, column=1)

        Label(frame, text="Last Name: ").grid(row=0, column=2)
        self.lname = StringVar()
        self.lname_enter = Entry(frame, textvariable=self.lname)
        self.lname_enter.grid(row=0, column=3)

        Label(frame, text="Username: ").grid(row=1, column=0)
        self.user = StringVar()
        self.username_enter = Entry(frame, textvariable=self.user)
        self.username_enter.grid(row=1, column=1)

        Label(frame, text="Password: ").grid(row=2, column=0)
        self.password = StringVar()
        self.password_enter = Entry(frame, textvariable=self.password)
        self.password_enter.grid(row=2, column=1)

        Label(frame, text="Confirm Password: ").grid(row=2, column=2)
        self.password_confirm = StringVar()
        self.password_confirm_enter = Entry(frame, textvariable=self.password_confirm)
        self.password_confirm_enter.grid(row=2, column=3)

        Label(frame, text="Email: ").grid(row=3, column=0)
        self.email = StringVar()
        self.email_enter = Entry(frame, textvariable=self.email)
        self.email_enter.grid(row=3, column=1)

        self.registerUser = Button(frame, text="Back", command=self.register_visitor_back).grid(row=4, column=1)
        self.registerUser = Button(frame, text="Register", command=self.register_login_visitor).grid(row=4, column=2)

    ###########################################################################
    def register_employee(self):
        self.navGUI.withdraw()
        self.regEmp = Toplevel()
        self.currGui = self.regEmp
        self.regEmp.title("Register Employee")

        Label(self.regEmp, text="Register Employee").grid(row=0)

        frame = Frame(self.regEmp)
        frame.grid()

        Label(frame, text="First Name: ").grid(row=0, column=0)
        self.fname = StringVar()
        self.fname_enter = Entry(frame, textvariable=self.fname)
        self.fname_enter.grid(row=0, column=1)

        Label(frame, text="Last Name: ").grid(row=0, column=2)
        self.lname = StringVar()
        self.lname_enter = Entry(frame, textvariable=self.lname)
        self.lname_enter.grid(row=0, column=3)

        Label(frame, text="Username: ").grid(row=1, column=0)
        self.user = StringVar()
        self.username_enter = Entry(frame, textvariable=self.user)
        self.username_enter.grid(row=1, column=1)

        Label(frame, text="User Type: ").grid(row=1, column=2)
        self.userType = StringVar()
        choices = ["Manager", "Staff"]
        self.userType.set("Manager")
        self.popupMenu = OptionMenu(frame, self.userType, *choices)
        self.popupMenu.grid(row=1, column=3)

        Label(frame, text="Password: ").grid(row=2, column=0)
        self.password = StringVar()
        self.password_enter = Entry(frame, textvariable=self.password)
        self.password_enter.grid(row=2, column=1)

        Label(frame, text="Confirm Password: ").grid(row=2, column=2)
        self.password_confirm = StringVar()
        self.password_confirm_enter = Entry(frame, textvariable=self.password_confirm)
        self.password_confirm_enter.grid(row=2, column=3)

        Label(frame, text="Phone: ").grid(row=3, column=0)
        self.phone = IntVar()
        self.phone_enter = Entry(frame, textvariable=self.phone)
        self.phone_enter.grid(row=3, column=1)

        Label(frame, text="Address: ").grid(row=3, column=2)
        self.address = StringVar()
        self.address_enter = Entry(frame, textvariable=self.address)
        self.address_enter.grid(row=5, column=3)

        Label(frame, text="City: ").grid(row=4, column=0)
        self.city = StringVar()
        self.city_enter = Entry(frame, textvariable=self.city)
        self.city_enter.grid(row=4, column=1)

        Label(frame, text="State: ").grid(row=4, column=2)
        self.state = StringVar()
        choices_state = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
                         "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM",
                         "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA",
                         "WV", "WI", "WY", "Other"]
        self.state.set("AL")
        self.popupMenuState = OptionMenu(frame, self.state, *choices_state)
        self.popupMenuState.grid(row=4, column=3)

        Label(frame, text="Zipcode: ").grid(row=4, column=4)
        self.zip = IntVar()
        self.zip_enter = Entry(frame, textvariable=self.zip)
        self.zip_enter.grid(row=4, column=5)

        Label(frame, text="Email: ").grid(row=5, column=0)
        self.email = StringVar()
        self.email_enter = Entry(frame, textvariable=self.email)
        self.email_enter.grid(row=5, column=1)

        self.registerUser = Button(frame, text="Back", command=self.register_emp_back).grid(row=6, column=1)
        self.registerUser = Button(frame, text="Register", command=self.register_login_emp).grid(row=6, column=2)

    ###########################################################################
    def register_employee_visitor(self):
        self.navGUI.withdraw()
        self.regEmpVis = Toplevel()
        self.prevGUI = self.currGui
        self.currGui = self.regEmpVis
        self.regEmpVis.title("Register Employee-Visitor")

        Label(self.regEmpVis, text="Register Employee").grid(row=0)

        frame = Frame(self.regEmpVis)
        frame.grid()

        Label(frame, text="First Name: ").grid(row=0, column=0)
        self.fname = StringVar()
        self.fname_enter = Entry(frame, textvariable=self.fname)
        self.fname_enter.grid(row=0, column=1)

        Label(frame, text="Last Name: ").grid(row=0, column=2)
        self.lname = StringVar()
        self.lname_enter = Entry(frame, textvariable=self.lname)
        self.lname_enter.grid(row=0, column=3)

        Label(frame, text="Username: ").grid(row=1, column=0)
        self.user = StringVar()
        self.username_enter = Entry(frame, textvariable=self.user)
        self.username_enter.grid(row=1, column=1)

        Label(frame, text="User Type: ").grid(row=1, column=2)
        self.userType = StringVar()
        choices = ["Manager", "Staff"]
        self.userType.set("Manager")
        self.popupMenu = OptionMenu(frame, self.userType, *choices)
        self.popupMenu.grid(row=1, column=3)

        Label(frame, text="Password: ").grid(row=2, column=0)
        self.password = StringVar()
        self.password_enter = Entry(frame, textvariable=self.password)
        self.password_enter.grid(row=2, column=1)

        Label(frame, text="Confirm Password: ").grid(row=2, column=2)
        self.password_confirm = StringVar()
        self.password_confirm_enter = Entry(frame, textvariable=self.password_confirm)
        self.password_confirm_enter.grid(row=2, column=3)

        Label(frame, text="Phone: ").grid(row=3, column=0)
        self.phone = IntVar()
        self.phone_enter = Entry(frame, textvariable=self.phone)
        self.phone_enter.grid(row=3, column=1)

        Label(frame, text="Address: ").grid(row=3, column=2)
        self.address = StringVar()
        self.address_enter = Entry(frame, textvariable=self.address)
        self.address_enter.grid(row=3, column=3)

        Label(frame, text="City: ").grid(row=4, column=0)
        self.city = StringVar()
        self.city_enter = Entry(frame, textvariable=self.city)
        self.city_enter.grid(row=4, column=1)

        Label(frame, text="State: ").grid(row=4, column=2)
        self.state = StringVar()
        choices_state = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
                         "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM",
                         "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA",
                         "WV", "WI", "WY", "Other"]
        self.state.set("AL")
        self.popupMenuState = OptionMenu(frame, self.state, *choices_state)
        self.popupMenuState.grid(row=4, column=3)

        Label(frame, text="Zipcode: ").grid(row=4, column=4)
        self.zip = IntVar()
        self.zip_enter = Entry(frame, textvariable=self.zip)
        self.zip_enter.grid(row=4, column=5)

        Label(frame, text="Email: ").grid(row=5, column=0)
        self.email = StringVar()
        self.email_enter = Entry(frame, textvariable=self.email)
        self.email_enter.grid(row=5, column=1)

        self.registerUser = Button(frame, text="Back", command=self.register_empVis_back).grid(row=6, column=1)
        self.registerUser = Button(frame, text="Register", command=self.register_login_empVis).grid(row=6, column=2)

    ###########################################################################
    def back(self):
        self.navGUI.withdraw()
        self.firstGUI.deiconify()
        self.currGui = self.firstGUI

    ###########################################################################
    def register_user_back(self):
        self.regUser.withdraw()
        self.navGUI.deiconify()
        self.currGui = self.navGUI

    ###########################################################################
    def register_login_user(self):
        if self.user.get() == "":
            messagebox.showwarning("Username", "Please enter a Username")
        elif self.password.get() == "":
            messagebox.showwarning("Password", "Please enter a Password")
        elif len(self.password.get()) < 8:
            messagebox.showwarning("Password", "Password must be at least 8 characters")
        elif self.password.get() != self.password_confirm.get():
            messagebox.showwarning("Password and Confirm Password", "Password and Confirm Password do not match")
        elif self.fname.get() == "":
            messagebox.showwarning("First Name", "Please enter your First Name")
        elif self.lname.get() == "":
            messagebox.showwarning("Last Name", "Please enter your Last Name")
        elif self.email.get() == "":
            messagebox.showwarning("Email", "Please enter at least one email")
        else:
            if self.fname.get() == "":
                self.fname.set("NULL")
            if self.lname.get() == "":
                self.lname.set("NULL")
            query_check = "Select Username from NormalUser where Username=('%s')" % (self.user.get())
            name = self.cursor.execute(query_check)
            if name == 0:
                query = "Insert into NormalUser values('%s', '%s', '%s', '%s', 'Pending', 'User')" % (self.user.get(), self.reg_hash_password(self.password.get()), self.fname.get(), self.lname.get())
                self.cursor.execute(query)
                if self.email.get() != "":
                    emails = [x.strip() for x in self.email.get().split(',')]
                    for email in emails:
                        queryb = "Insert into Email values('%s', '%s')" % (self.user.get(), email)
                        self.cursor.execute(queryb)
                self.db.commit()
                self.regUser.withdraw()
                self.login()
            else:
                messagebox.showwarning("Username", "This username is taken by another user. Please enter a different username")

    ###########################################################################
    def register_visitor_back(self):
        self.regVisitor.withdraw()
        self.navGUI.deiconify()
        self.currGui = self.navGUI

    ###########################################################################
    def register_login_visitor(self):
        if self.user.get() == "":
            messagebox.showwarning("Username", "Please enter a Username")
        elif self.password.get() == "":
            messagebox.showwarning("Password", "Please enter a Password")
        elif len(self.password.get()) < 8:
            messagebox.showwarning("Password", "Password must be at least 8 characters")
        elif self.password.get() != self.password_confirm.get():
            messagebox.showwarning("Password and Confirm Password", "Password and Confirm Password do not match")
        elif self.fname.get() == "":
            messagebox.showwarning("First Name", "Please enter your First Name")
        elif self.lname.get() == "":
            messagebox.showwarning("Last Name", "Please enter your Last Name")
        elif self.email.get() == "":
            messagebox.showwarning("Email", "Please enter at least one email")
        else:
            if self.fname.get() == "":
                self.fname.set("NULL")
            if self.lname.get() == "":
                self.lname.set("NULL")
            query_check = "Select Username from NormalUser where Username=('%s')" % (self.user.get())
            name = self.cursor.execute(query_check)
            if name == 0:
                query = "Insert into NormalUser values('%s', '%s', '%s', '%s', 'Pending', 'Visitor')" % (self.user.get(), self.reg_hash_password(self.password.get()), self.fname.get(), self.lname.get())
                self.cursor.execute(query)
                queryc = "Insert into Visitor values('%s')" % (self.user.get())
                self.cursor.execute(queryc)
                if self.email.get() != "":
                    emails = [x.strip() for x in self.email.get().split(',')]
                    for email in emails:
                        queryb = "Insert into Email values('%s', '%s')" % (self.user.get(), email)
                        self.cursor.execute(queryb)
                self.db.commit()
                self.regVisitor.withdraw()
                self.login()
            else:
                messagebox.showwarning("Username", "This username is taken by another user. Please enter a different username")

    ###########################################################################
    def register_emp_back(self):
        self.regEmp.withdraw()
        self.navGUI.deiconify()
        self.currGui = self.navGUI

    ###########################################################################
    def register_login_emp(self):
        if self.user.get() == "":
            messagebox.showwarning("Username", "Please enter a Username")
        elif self.password.get() == "":
            messagebox.showwarning("Password", "Please enter a Password")
        elif len(self.password.get()) < 8:
            messagebox.showwarning("Password", "Password must be at least 8 characters")
        elif self.password.get() != self.password_confirm.get():
            messagebox.showwarning("Password and Confirm Password", "Password and Confirm Password do not match")
        elif self.fname.get() == "":
            messagebox.showwarning("First Name", "Please enter your First Name")
        elif self.lname.get() == "":
            messagebox.showwarning("Last Name", "Please enter your Last Name")
        elif self.email.get() == "":
            messagebox.showwarning("Email", "Please enter at least one email")
        elif self.phone.get() == 0:
            messagebox.showwarning("Phone", "Please enter a phone number")
        elif self.address.get() == "":
            messagebox.showwarning('Address',"Please enter a address")
        elif self.city.get() == "":
            messagebox.showwarning("City", "Please enter a city")
        elif self.zip.get() == 0:
            messagebox.showwarning("Zipcode", "Please enter a zipcode")
        else:
            query_check = "Select Username from NormalUser where Username=('%s')" % (self.user.get())
            name = self.cursor.execute(query_check)
            if name == 0:
                query = "Insert into NormalUser values('%s', '%s', '%s', '%s', 'Pending', 'Employee')" % (self.user.get(), self.reg_hash_password(self.password.get()), self.fname.get(), self.lname.get())
                self.cursor.execute(query)
                queryc = "Insert into Employee values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (self.user.get(), '', self.phone.get(), self.address.get(), self.city.get(), self.state.get(), self.zip.get(), self.userType.get())
                self.cursor.execute(queryc)
                if self.email.get() != "":
                    emails = [x.strip() for x in self.email.get().split(',')]
                    for email in emails:
                        queryb = "Insert into Email values('%s', '%s')" % (self.user.get(), email)
                        self.cursor.execute(queryb)
                self.db.commit()
                self.regEmp.withdraw()
                self.login()
                #if self.userType.get() == "Manager":
                #    self.manager_only_functionality()
                #else:
                #    self.staff_only_functionality()
            else:
                messagebox.showwarning("Username", "This username is taken by another user. Please enter a different username")

    ###########################################################################
    def register_empVis_back(self):
        self.regEmpVis.withdraw()
        self.navGUI.deiconify()
        self.currGui = self.navGUI

    ###########################################################################
    def register_login_empVis(self):
        if self.user.get() == "":
            messagebox.showwarning("Username", "Please enter a Username")
        elif self.password.get() == "":
            messagebox.showwarning("Password", "Please enter a Password")
        elif len(self.password.get()) < 8:
            messagebox.showwarning("Password", "Password must be at least 8 characters")
        elif self.password.get() != self.password_confirm.get():
            messagebox.showwarning("Password and Confirm Password", "Password and Confirm Password do not match")
        elif self.fname.get() == "":
            messagebox.showwarning("First Name", "Please enter your First Name")
        elif self.lname.get() == "":
            messagebox.showwarning("Last Name", "Please enter your Last Name")
        elif self.email.get() == "":
            messagebox.showwarning("Email", "Please enter at least one email")
        elif self.phone.get() == 0:
            messagebox.showwarning("Phone", "Please enter a phone number")
        elif self.address.get() == "":
            messagebox.showwarning('Address',"Please enter a address")
        elif self.city.get() == "":
            messagebox.showwarning("City", "Please enter a city")
        elif self.zip.get() == 0:
            messagebox.showwarning("Zipcode", "Please enter a zipcode")
        else:
            query_check = "Select Username from NormalUser where Username=('%s')" % (self.user.get())
            name = self.cursor.execute(query_check)
            if name == 0:
                query = "Insert into NormalUser values('%s', '%s', '%s', '%s', 'Pending', 'Employee, Visitor')" % (self.user.get(), self.reg_hash_password(self.password.get()), self.fname.get(), self.lname.get())
                self.cursor.execute(query)
                queryc = "Insert into Employee values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (self.user.get(), '', self.phone.get(), self.address.get(), self.city.get(), self.state.get(), self.zip.get(), self.userType.get())
                self.cursor.execute(queryc)
                queryd = "Insert into Visitor values('%s')" % (self.user.get())
                self.cursor.execute(queryd)
                if self.email.get() != "":
                    emails = [x.strip() for x in self.email.get().split(',')]
                    for email in emails:
                        queryb = "Insert into Email values('%s', '%s')" % (self.user.get(), email)
                        self.cursor.execute(queryb)
                self.db.commit()
                self.regEmpVis.withdraw()
                self.login()
                #if self.userType.get() == "Manager":
                #    self.manager_vis_functionality()
                #else:
                #    self.staff_vis_functionality()
            else:
                messagebox.showwarning("Username", "This username is taken by another user. Please enter a different username")

    ###########################################################################
    def user_functionality(self):
        self.firstGUI.withdraw()
        self.user_func_GUI = Toplevel()
        self.currGui = self.user_func_GUI
        self.user_func_GUI.title("User Functionality")

        Label(self.user_func_GUI, text="User Functionality").grid(row=1)

        frame = Frame(self.user_func_GUI)
        frame.grid()

        self.register = Button(self.user_func_GUI, text="Take Transit", command=self.take_transit).grid(row=2)
        self.register = Button(self.user_func_GUI, text="View Transit History", command=self.view_transit_history).grid(
            row=3)
        self.register = Button(self.user_func_GUI, text="Back", command=self.user_func_back).grid(row=4)

    ###########################################################################
    def admin_only_functionality(self):
        self.firstGUI.withdraw()
        self.adminOnlyGUI = Toplevel()
        self.currGui = self.adminOnlyGUI
        self.adminOnlyGUI.title("Admin Only Functionality")

        Label(self.adminOnlyGUI, text="Administrator Functionality").grid(row=0, column=0)

        frame = Frame(self.adminOnlyGUI)
        frame.grid()

        self.register = Button(self.adminOnlyGUI, text="Manage Profile", command=self.manage_profile).grid(row=1,
                                                                                                           column=0)
        self.register = Button(self.adminOnlyGUI, text="Manage User", command=self.manage_user).grid(row=2, column=0)
        self.register = Button(self.adminOnlyGUI, text="Manage Transit", command=self.manage_transit).grid(row=3,
                                                                                                           column=0)
        self.register = Button(self.adminOnlyGUI, text="Manage Site", command=self.manage_site).grid(row=4, column=0)

        self.register = Button(self.adminOnlyGUI, text="Take Transit", command=self.take_transit).grid(row=2, column=1)
        self.register = Button(self.adminOnlyGUI, text="View Transit History", command=self.view_transit_history).grid(
            row=3, column=1)
        self.register = Button(self.adminOnlyGUI, text="Back", command=self.admin_only_back).grid(row=4, column=1)

    ###########################################################################

    ###########################################################################
    def admin_vis_functionality(self):
        self.firstGUI.withdraw()
        self.adminVisGUI = Toplevel()
        self.currGui = self.adminVisGUI
        self.adminVisGUI.title("Admin-Visitor Functionality")

        Label(self.adminVisGUI, text="Admin-Visitor Functionality").grid(row=0, column=0)

        frame = Frame(self.adminVisGUI)
        frame.grid()

        self.register = Button(self.adminVisGUI, text="Manage Profile", command=self.manage_profile).grid(row=1,
                                                                                                          column=0)
        self.register = Button(self.adminVisGUI, text="Manage Transit", command=self.manage_transit).grid(row=2,
                                                                                                          column=0)
        self.register = Button(self.adminVisGUI, text="Manage Site", command=self.manage_site).grid(row=3, column=0)
        self.register = Button(self.adminVisGUI, text="Explore Event", command=self.visit_explore_event).grid(row=4, column=0)
        self.register = Button(self.adminVisGUI, text="View Transit History", command=self.view_transit_history).grid(
            row=5, column=0)

        self.register = Button(self.adminVisGUI, text="Manage User", command=self.manage_user).grid(row=1, column=1)
        self.register = Button(self.adminVisGUI, text="Take Transit", command=self.take_transit).grid(row=2, column=1)
        self.register = Button(self.adminVisGUI, text="Explore Site", command=self.visitor_explore_site).grid(row=3, column=1)
        self.register = Button(self.adminVisGUI, text="View Visit History", command=self.visit_history).grid(row=4,
                                                                                                                  column=1)
        self.register = Button(self.adminVisGUI, text="Back", command=self.admin_vis_back).grid(row=5, column=1)

    ###########################################################################
    def manager_only_functionality(self):
        self.firstGUI.withdraw()
        self.manOnlyGUI = Toplevel()
        self.currGui = self.manOnlyGUI
        self.manOnlyGUI.title("Manager Only Functionality")

        Label(self.manOnlyGUI, text="Manager Only Functionality").grid(row=0, column=0)

        frame = Frame(self.manOnlyGUI)
        frame.grid()

        self.register = Button(self.manOnlyGUI, text="Manage Profile", command=self.manage_profile).grid(row=1,
                                                                                                         column=0)
        self.register = Button(self.manOnlyGUI, text="Manage Event", command=self.manage_event).grid(row=2, column=0)
        self.register = Button(self.manOnlyGUI, text="View Staff", command=self.view_staff).grid(row=3, column=0)
        self.register = Button(self.manOnlyGUI, text="View Site Report", command=self.view_site_report).grid(row=1,
                                                                                                             column=1)

        self.register = Button(self.manOnlyGUI, text="Take Transit", command=self.take_transit).grid(row=2, column=1)
        self.register = Button(self.manOnlyGUI, text="View Transit History", command=self.view_transit_history).grid(
            row=3, column=1)
        self.register = Button(self.manOnlyGUI, text="Back", command=self.man_only_back).grid(row=4)

    ###########################################################################
    def manager_vis_functionality(self):
        self.firstGUI.withdraw()
        self.manVisGUI = Toplevel()
        self.currGui = self.manVisGUI
        self.manVisGUI.title("Manager Only Functionality")

        Label(self.manVisGUI, text="Manager Visitor Functionality").grid(row=0, column=0)

        frame = Frame(self.manVisGUI)
        frame.grid()

        self.register = Button(self.manVisGUI, text="Manage Profile", command=self.manage_profile).grid(row=1, column=0)
        self.register = Button(self.manVisGUI, text="View Staff", command=self.view_staff).grid(row=2, column=0)
        self.register = Button(self.manVisGUI, text="Explore Site", command=self.visitor_explore_site).grid(row=3, column=0)
        self.register = Button(self.manVisGUI, text="Take Transit", command=self.take_transit).grid(row=4,
                                                                                                    column=0)
        self.register = Button(self.manVisGUI, text="View Visit History", command=self.visit_history).grid(row=5,
                                                                                                                column=0)

        self.register = Button(self.manVisGUI, text="Manage Event", command=self.manage_event).grid(row=1, column=1)
        self.register = Button(self.manVisGUI, text="View Site Report", command=self.view_site_report).grid(row=2,
                                                                                                            column=1)
        self.register = Button(self.manVisGUI, text="Explore Event", command=self.visit_explore_event).grid(row=3, column=1)
        self.register = Button(self.manVisGUI, text="View Transit History", command=self.view_transit_history).grid(
            row=4, column=1)
        self.register = Button(self.manVisGUI, text="Back", command=self.man_vis_back).grid(row=5, column=1)

    ###########################################################################
    def staff_only_functionality(self):
        self.firstGUI.withdraw()
        self.staffOnlyGUI = Toplevel()
        self.currGui = self.staffOnlyGUI
        self.staffOnlyGUI.title("Staff Only Functionality")

        Label(self.staffOnlyGUI, text="Staff Only Functionalty").grid(row=0)

        frame = Frame(self.staffOnlyGUI)
        frame.grid()

        '''TODO Make Back Button Go Back To An actual Screen'''
        self.register = Button(self.staffOnlyGUI, text="Manage Profile", command=self.manage_profile).grid(row=2)
        self.register = Button(self.staffOnlyGUI, text="View Schedule", command=self.view_schedule).grid(row=3)
        self.register = Button(self.staffOnlyGUI, text="Take Transit", command=self.take_transit).grid(row=4)
        self.register = Button(self.staffOnlyGUI, text="View Transit History", command=self.view_transit_history).grid(
            row=5)
        self.register = Button(self.staffOnlyGUI, text="Back", command=self.staff_only_back).grid(row=6)

    ###########################################################################
    def staff_visitor_functionality(self):
        self.firstGUI.withdraw()
        self.staffVisGUI = Toplevel()
        self.currGui = self.staffVisGUI
        self.staffVisGUI.title("Staff Visitor Functionality")

        Label(self.staffVisGUI, text="Staff Visitor Functionalty").grid(row=0)

        frame = Frame(self.staffVisGUI)
        frame.grid()

        '''TODO Make Back Button Go Back To An actual Screen'''
        self.register = Button(self.staffVisGUI, text="Manage Profile", command=self.manage_profile).grid(row=2)
        self.register = Button(self.staffVisGUI, text="View Schedule", command=self.view_schedule).grid(row=3)
        self.register = Button(self.staffVisGUI, text="Take Transit", command=self.take_transit).grid(row=4)
        self.register = Button(self.staffVisGUI, text="View Transit History", command=self.view_transit_history).grid(
            row=5)

        self.register = Button(self.staffVisGUI, text="Explore Event", command=self.visit_explore_event).grid(row=2, column=1)
        self.register = Button(self.staffVisGUI, text="Explore Site", command=self.visitor_explore_site).grid(row=3, column=1)
        self.register = Button(self.staffVisGUI, text="View Visit History", command=self.visit_history).grid(row=4,
                                                                                                                  column=1)
        self.register = Button(self.staffVisGUI, text="Back", command=self.staff_vis_back).grid(row=5, column=1)

    ###########################################################################
    def visitor_functionality(self):
        self.firstGUI.withdraw()
        self.visitorGUI = Toplevel()
        self.currGui = self.visitorGUI
        self.visitorGUI.title("Visitor Functionality")

        Label(self.visitorGUI, text="Visitor Functionalty").grid(row=0)

        frame = Frame(self.visitorGUI)
        frame.grid()

        '''TODO Make Back Button Go Back To An actual Screen'''
        self.register = Button(self.visitorGUI, text="Explore Event", command=self.visit_explore_event).grid(row=2)
        self.register = Button(self.visitorGUI, text="Explore Site", command=self.visitor_explore_site).grid(row=3)
        self.register = Button(self.visitorGUI, text="View Visit History", command=self.visit_history).grid(row=4)
        self.register = Button(self.visitorGUI, text="Take Transit", command=self.take_transit).grid(row=5)
        self.register = Button(self.visitorGUI, text="View Transit History", command=self.view_transit_history).grid(
            row=6)
        self.register = Button(self.visitorGUI, text="Back", command=self.vis_back).grid(row=7)

    ###########################################################################
    def user_func_back(self):
        self.user_func_GUI.withdraw()
        self.firstGUI.deiconify()
        self.currGui = self.firstGUI

    def admin_only_back(self):
        self.adminOnlyGUI.withdraw()
        self.firstGUI.deiconify()
        self.currGui = self.firstGUI

    def admin_vis_back(self):
        self.adminVisGUI.withdraw()
        self.firstGUI.deiconify()
        self.currGui = self.firstGUI

    def man_only_back(self):
        self.manOnlyGUI.withdraw()
        self.firstGUI.deiconify()
        self.currGui = self.firstGUI

    def man_vis_back(self):
        self.manVisGUI.withdraw()
        self.firstGUI.deiconify()
        self.currGui = self.firstGUI

    def staff_only_back(self):
        self.staffOnlyGUI.withdraw()
        self.firstGUI.deiconify()
        self.currGui = self.firstGUI

    def staff_vis_back(self):
        self.staffVisGUI.withdraw()
        self.firstGUI.deiconify()
        self.currGui = self.firstGUI

    def vis_back(self):
        self.visitorGUI.withdraw()
        self.firstGUI.deiconify()
        self.currGui = self.firstGUI

    ###########################################################################

    def view_site_report(self):
        self.currGui.withdraw()
        self.site_report = Toplevel()
        self.currGui = self.site_report
        self.site_report.title("Site Report")

        Label(self.site_report, text="Site Report").grid(row=0)

        frame = Frame(self.site_report)
        frame.grid()

        Label(frame, text="Start Date").grid(row=0, column=0)
        self.start_date = StringVar()
        self.start_date_enter = Entry(frame, textvariable=self.start_date)
        self.start_date_enter.grid(row=0, column=1)

        Label(frame, text="End Date").grid(row=0, column=2)
        self.end_date = StringVar()
        self.end_date_enter = Entry(frame, textvariable=self.end_date)
        self.end_date_enter.grid(row=0, column=3)

        Label(frame, text="Event Count Range").grid(row=1, column=0)
        self.event_count_lower = IntVar()
        self.event_count_lower_enter = Entry(frame, textvariable=self.event_count_lower)
        self.event_count_lower_enter.grid(row=1, column=1)

        Label(frame, text=" -- ").grid(row=1, column=2)
        self.event_count_upper = IntVar()
        self.event_count_upper_enter = Entry(frame, textvariable=self.event_count_upper)
        self.event_count_upper_enter.grid(row=1, column=3)

        Label(frame, text="Staff Count Range").grid(row=1, column=4)
        self.staff_count_lower = IntVar()
        self.staff_count_lower_enter = Entry(frame, textvariable=self.staff_count_lower)
        self.staff_count_lower_enter.grid(row=1, column=5)

        Label(frame, text=" -- ").grid(row=1, column=6)
        self.staff_count_upper = IntVar()
        self.staff_count_upper_enter = Entry(frame, textvariable=self.staff_count_upper)
        self.staff_count_upper_enter.grid(row=1, column=7)

        Label(frame, text="Total Visits Range").grid(row=2, column=0)
        self.visits_lower = IntVar()
        self.visits_lower_enter = Entry(frame, textvariable=self.visits_lower)
        self.visits_lower_enter.grid(row=2, column=1)

        Label(frame, text=" -- ").grid(row=2, column=2)
        self.visits_upper = IntVar()
        self.visits_upper_enter = Entry(frame, textvariable=self.visits_upper)
        self.visits_upper_enter.grid(row=2, column=3)

        Label(frame, text="Total Revenue Range").grid(row=2, column=4)
        self.revenue_lower = IntVar()
        self.revenue_lower_enter = Entry(frame, textvariable=self.revenue_lower)
        self.revenue_lower_enter.grid(row=2, column=5)

        Label(frame, text=" -- ").grid(row=2, column=6)
        self.revenue_upper = IntVar()
        self.revenue_upper_enter = Entry(frame, textvariable=self.revenue_upper)
        self.revenue_upper_enter.grid(row=2, column=7)

        Label(frame, text="Sort By: ").grid(row=2, column=8)
        self.sort = StringVar()
        choices = ['Date Attended', 'Event Count', 'Date Attended Desc', 'Event Count Desc', 'None']
        self.sort.set('None')
        self.popup = OptionMenu(frame, self.sort, *choices)
        self.popup.grid(row=2, column = 9)

        self.filter = Button(frame, text="Filter", command=self.filter_view_site).grid(row=4, column=3)
        self.create = Button(frame, text="Daily Detail", command=self.daily_detail).grid(row=4, column=4)

        frame_tree = Frame(self.site_report)
        frame_tree.grid()

        self.site_tree = ttk.Treeview(frame_tree,
                            columns=['Date', 'Event Count', 'Staff Count', 'Total Visits', 'Total Revenue ($)'],
                            show='headings', selectmode='browse')

        self.site_tree.heading('Date', text='Date')
        self.site_tree.heading('Event Count', text='Event Count')
        self.site_tree.heading('Staff Count', text='Staff Count')
        self.site_tree.heading('Total Visits', text='Total Visits')
        self.site_tree.heading('Total Revenue ($)', text="Total Revenue ($)")
        #self.tree.insert("", "end", values=("1", "2", "3", "4", "6"))
        #self.tree.insert("", "end", values=("4", "5", "6", "7", "8"))
        self.site_tree.grid(row=1, column=3)

        frame_under = Frame(self.site_report)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_view_site).grid(row=0, column=0)

    def back_view_site(self):
        self.currGui.withdraw()
        if self.userType == "Employee, Visitor":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Employee":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Visitor":
            self.visitor_functionality()
            self.currGui = self.visitorGUI
        elif self.userType == "User":
            self.user_functionality()
            self.currGui = self.navGUI

    def filter_view_site(self):
        for i in self.site_tree.get_children():
            self.site_tree.delete(i)
        startd = None
        endd = None
        greater = False
        if self.start_date.get() != "" and self.end_date.get() != "":
            start = [x.strip() for x in self.start_date.get().split('-')]
            end = [x.strip() for x in self.end_date.get().split('-')]
            startd = datetime.datetime(int(start[0], 10), int(start[1], 10), int(start[2], 10))
            endd = datetime.datetime(int(end[0], 10), int(end[1], 10), int(end[2], 10))
        if startd != None and endd != None:
            if startd > endd:
                greater = True
        '''if self.start_date.get() == "" and self.end_date.get() == "":
            messagebox.showwarning("Date", "Please enter a date to filter on")'''
        if self.start_date.get() == "" and self.end_date.get() != "":
            messagebox.showwarning("Date", "There must be a start and end date. They can be the same date")
        elif self.start_date.get() != "" and self.end_date.get() == "":
            messagebox.showwarning("Date", "There must be a start and end date. They can be the same date")
        elif greater == True:
            messagebox.showwarning("Date", "The start date must be before the end date")
        else:
            query_id = "Select sitename from site where managerid = '%s'" % (self.user.get())
            self.cursor.execute(query_id)
            manager = self.cursor.fetchone()
            site = manager[0]
            if self.start_date.get() == "" and self.end_date.get() == "" and self.event_count_lower.get() == 0 and self.event_count_upper.get() == 0 and self.staff_count_lower.get() == 0 and self.staff_count_upper.get() == 0 and self.visits_lower.get() == 0 and self.visits_upper.get() == 0 and self.revenue_lower.get() == 0 and self.revenue_upper.get() == 0:
                #startdate, event count
                query = "Select dateattended, count(visitevent.eventname) from visitevent join staffassigned group by dateattended"
                #staff count
                query_staff = "select dateattended, count(username) from VisitEvent join staffassigned group by dateattended"
                #total visits
                #query_visits = "select (Select count(dateattended) from VisitEvent where sitename = '%s' and dateattended = '%s' group by dateattended)+(Select count(datevisited) from VisitSite where sitename='%s' and datevisited= '%s' group by datevisited)" % (site, dateattended, site, dateattended)
                #revenue
                #query_revenue = "select (count(eventname)* price) from view_eventprice where sitename= '%s'  and dateattended = '%s' group by eventname, price" % (name, date)
                if self.sort.get() == "Date Attended":
                    query = "Select dateattended, count(visitevent.eventname) from visitevent join staffassigned group by dateattended order by dateattended"
                elif self.sort.get() == "Event Count":
                    query = "Select dateattended, count(visitevent.eventname) from visitevent join staffassigned group by dateattended order by count(visitevent.eventname)"
                elif self.sort.get() == "Date Attended Desc":
                    query = "Select dateattended, count(visitevent.eventname) from visitevent join staffassigned group by dateattended order by dateattended desc"
                elif self.sort.get() == "Event Count Desc":
                    query = "Select dateattended, count(visitevent.eventname) from visitevent join staffassigned group by dateattended order by count(visitevent.eventname) desc"
                else:
                    query = "Select dateattended, count(visitevent.eventname) from visitevent join staffassigned group by dateattended"
                self.cursor.execute(query)
                events = self.cursor.fetchall()
                self.cursor.execute(query_staff)
                staff = self.cursor.fetchall()
                staffcount = {}
                for s in staff:
                    staffcount[s[0]] = s[1]
                #self.cursor.execute(query_visits)
                #visits = self.cursor.fetchall()
                #visitcount = {}
                #for v in visits:
                #    visitcount[v[0]] = v[1]
                #self.cursor.execute(query_revenue)
                #revenue = self.cursor.fetchall()
                #revenuecount = {}
                #for r in revenue:
                #    revenuecount[r[0]] = r[1]
                for event in events:
                    date = event[0]
                    event_count = event[1]
                    staff_count = 0
                    if date in staffcount:
                        staff_count = staffcount[date]
                    query_visits = "select (Select count(dateattended) from VisitEvent where sitename = '%s' and dateattended = '%s' group by dateattended)+(Select count(datevisited) from VisitSite where sitename='%s' and datevisited= '%s' group by datevisited)" % (site, date, site, date)
                    self.cursor.execute(query_visits)
                    result = self.cursor.fetchone()
                    visit_count = 0
                    if result != None:
                        vist_count = result[0]
                    #visit_count = 0
                    #if date in visitcount:
                    #    visit_count = visitcount[date]
                    query_revenue = "select (count(eventname)* price) from view_eventprice where sitename= '%s'  and dateattended = '%s' group by eventname, price" % (site, date)
                    self.cursor.execute(query_revenue)
                    result = self.cursor.fetchone()
                    revenue_count = 0
                    if result != None:
                        revenue_count = result[0]
                    #revenue_count = 0
                    #if date in revenuecount:
                    #    revenue_count = revenuecount[date]
                    self.site_tree.insert("", "end", values=(date, event_count, staff_count, visit_count, revenue_count))
            '''else:
                query = "select distinct(concat(c.FirstName, ' ', c.Lastname)),MATH from staffassigned a join BeltLineEvent b join normaluser c on a.EventName = b.EventName and a.EventStartDate=b.StartDate and a.Sitename = b.sitename and a.employee_ID = c.username where "
                site = ""
                first = ""
                last = ""
                date = ""
                startd = None
                endd = None
                greater = False
                if self.start_date.get() != "" and self.end_date.get() != "": #and self.start_date.get() <= self.end_date.get():
                    start = [x.strip() for x in self.start_date.get().split('-')]
                    end = [x.strip() for x in self.end_date.get().split('-')]
                    startd = datetime.datetime(int(start[0], 10), int(start[1], 10), int(start[2], 10))
                    endd = datetime.datetime(int(end[0], 10), int(end[1], 10), int(end[2], 10))
                if startd != None and endd != None:
                    if startd > endd:
                        greater = True
                if greater == True:
                    messagebox.showwarning("Date", "The start date must be before the end date")
                elif self.start_date.get() == "" and self.end_date.get() != "":
                    messagebox.showwarning("Date", "There must be a start and end date. They can be the same date")
                elif self.start_date.get() != "" and self.end_date.get() == "":
                    messagebox.showwarning("Date", "There must be a start and end date. They can be the same date")
                else:
                    if self.site.get() != "All":
                        site = "b.SiteName = '" + self.site.get() + "'"
                    if self.fname.get() != "":
                        first = "c.firstname = '" + self.fname.get() + "'"
                    if self.lname.get() != "":
                        last = "c.lastname '" + self.lname.get() + "'"
                    if self.start_date.get() != "" and self.end_date.get() != "":
                        date = "b.startdate = '" + self.start_date.get() + "'" + " and '" + "b.enddate = '" + self.end_date.get() + "'"
                    if site != "":
                        query = query + site
                        if first != "":
                            query = query + " and " + first
                        if last != "":
                            query = query + " and " + last
                        if date != "":
                            query = query + " and " + date
                    elif first != "":
                        query = query + first
                        if last != "":
                            query = query + " and " + last
                        if date != "":
                            query = query + " and " + date
                    elif last != "":
                        query = query + last
                        if date != "":
                            query = query + " and " + date
                    else:
                        query = query + date
                    if self.sort.get() == "Name":
                        query = query + " order by Transit_type"
                    elif self.sort.get() == "Name Desc":
                        query = query + " order by Price"
                    else:
                        query = query
                    self.cursor.execute(query)
                    results = self.cursor.fetchall()
                    for staff in results:
                        name = staff[0]
                        shifts = staff[1]
                        self.tree.insert("", "end", values=(name, shifts))'''

    def view_staff(self):
        self.currGui.withdraw()
        self.view_staff = Toplevel()
        self.currGui = self.view_staff
        self.view_staff.title("View / Manage Staff")

        Label(self.view_staff, text="View / Manage Staff").grid(row=0)

        frame = Frame(self.view_staff)
        frame.grid()

        query = "Select Distinct SiteName from Site"
        self.cursor.execute(query)
        sites = self.cursor.fetchall()

        Label(frame, text="Site").grid(row=0, column=0)
        self.site = StringVar()
        choices = []
        for site in sites:
            choices.append(site[0])
        choices.append('All')
        self.site.set('All')
        self.popup = OptionMenu(frame, self.site, *choices)
        self.popup.grid(row=0, column=1)

        Label(frame, text="First Name").grid(row=1, column=0)
        self.fname = StringVar()
        self.fname_enter = Entry(frame, textvariable=self.fname)
        self.fname_enter.grid(row=1, column=1)

        Label(frame, text="Last name").grid(row=1, column=2)
        self.lname = StringVar()
        self.lname_enter = Entry(frame, textvariable=self.lname)
        self.lname_enter.grid(row=1, column=3)

        Label(frame, text="Start Date").grid(row=2, column=0)
        self.start_date = StringVar()
        self.start_date_enter = Entry(frame, textvariable=self.start_date)
        self.start_date_enter.grid(row=2, column=1)

        Label(frame, text="End Date").grid(row=2, column=2)
        self.end_date = StringVar()
        self.end_date_enter = Entry(frame, textvariable=self.end_date)
        self.end_date_enter.grid(row=2, column=3)

        Label(frame, text="Sort By: ").grid(row=3, column=0)
        self.sort = StringVar()
        choices = ['Name', 'Name Desc', 'None']
        self.sort.set('None')
        self.popup = OptionMenu(frame, self.sort, *choices)
        self.popup.grid(row=3, column = 1)

        self.filter = Button(frame, text="Filter", command=self.filter_view_staff).grid(row=4, column=2)

        frame_tree = Frame(self.view_staff)
        frame_tree.grid()

        self.tree = ttk.Treeview(frame_tree, columns=['Staff Name', '# Event Shifts'],
                            show='headings', selectmode='browse')

        self.tree.heading('Staff Name', text='Staff Name')
        self.tree.heading('# Event Shifts', text='# Events Shifts')
        #self.tree.insert("", "end", values=("1", "2"))
        #self.tree.insert("", "end", values=("4", "5"))
        self.tree.grid(row=1, column=3)

        frame_under = Frame(self.view_staff)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_view_staff).grid(row=0, column=0)

    def filter_view_staff(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        '''startd = None
        endd = None
        greater = False
        if self.start_date.get() != "" and self.end_date.get() != "": #and self.start_date.get() <= self.end_date.get():
            start = [x.strip() for x in self.start_date.get().split('-')]
            end = [x.strip() for x in self.end_date.get().split('-')]
            startd = datetime.datetime(int(start[0], 10), int(start[1], 10), int(start[2], 10))
            endd = datetime.datetime(int(end[0], 10), int(end[1], 10), int(end[2], 10))
        if startd != None and endd != None:
            if startd > endd:
                greater = True
        if greater == True:
            messagebox.showwarning("Date", "The start date must be before the end date")
        elif self.start_date.get() == "" and self.end_date.get() != "":
            messagebox.showwarning("Date", "There must be a start and end date. They can be the same date")
        elif self.start_date.get() != "" and self.end_date.get() == "":
            messagebox.showwarning("Date", "There must be a start and end date. They can be the same date")
        else:'''
        if self.site.get() == 'All' and self.fname.get() == '' and self.lname.get() == "" and self.start_date.get() == "" and self.end_date.get() == "":
            query = ""
            if self.sort.get() == "Name":
                query = "Select concat(FirstName, ' ', Lastname), a.username from staff a join normaluser b on a.username = b.username order by concat(FirstName, ' ', Lastname)"
            elif self.sort.get() == "Name Desc":
                query = "Select concat(FirstName, ' ', Lastname), a.username from staff a join normaluser b on a.username = b.username order by concat(FirstName, ' ', Lastname) desc"
            else:
                query = "Select concat(FirstName, ' ', Lastname), a.username from staff a join normaluser b on a.username = b.username order by concat(FirstName, ' ', Lastname)"
            self.cursor.execute(query)
            staff_names = self.cursor.fetchall()
            query = "select count(employee_ID), username from staffassigned a join normaluser b on a.employee_ID=b.username group by b.username" #% (self.start_date.get(), self.end_date.get())
            self.cursor.execute(query)
            shifts = self.cursor.fetchall()
            shift = {}
            for s in shifts:
                shift[s[1]] = s[0]
            for staff in staff_names:
                name = staff[0]
                username = staff[1]
                shift_count = 0
                if username in shift:
                    shift_count = shift[username]
                self.tree.insert("", "end", values=(name, shift_count))
        else:
            query = "Select concat(FirstName,' ', Lastname), a.username from staff a join normaluser b on a.username = b.username where "
            prev_query = query
            queryb = "select count(employee_ID), username from staffassigned a join normaluser b on a.employee_ID=b.username where "
            prev_queryb = queryb
            site = ""
            first = ""
            last = ""
            date = ""
            startd = None
            endd = None
            greater = False
            if self.start_date.get() != "" and self.end_date.get() != "": #and self.start_date.get() <= self.end_date.get():
                start = [x.strip() for x in self.start_date.get().split('-')]
                end = [x.strip() for x in self.end_date.get().split('-')]
                startd = datetime.datetime(int(start[0], 10), int(start[1], 10), int(start[2], 10))
                endd = datetime.datetime(int(end[0], 10), int(end[1], 10), int(end[2], 10))
            if startd != None and endd != None:
                if startd > endd:
                    greater = True
            if greater == True:
                messagebox.showwarning("Date", "The start date must be before the end date")
            elif self.start_date.get() == "" and self.end_date.get() != "":
                messagebox.showwarning("Date", "There must be a start and end date. They can be the same date")
            elif self.start_date.get() != "" and self.end_date.get() == "":
                messagebox.showwarning("Date", "There must be a start and end date. They can be the same date")
            else:
                if self.site.get() != "All":
                    site = "a.SiteName = '" + self.site.get() + "'"
                if self.fname.get() != "":
                    first = "b.firstname = '" + self.fname.get() + "'"
                if self.lname.get() != "":
                    last = "b.lastname = '" + self.lname.get() + "'"
                if self.start_date.get() != "" and self.end_date.get() != "":
                    date = "a.eventstartdate between '" + self.start_date.get() + "'" + " and '" + self.end_date.get() + "'"
                if site != "":
                    queryb = queryb + site
                    if first != "":
                        query = query + first
                    if last != "":
                        query = query + " and " + last
                    if date != "":
                        queryb = queryb + " and " + date
                elif first != "":
                    query = query + first
                    if last != "":
                        query = query + " and " + last
                    if date != "":
                        queryb = queryb + date
                elif last != "":
                    query = query + last
                    if date != "":
                        queryb = queryb + date
                else:
                    queryb = queryb + date
                query_u = False
                queryb_u = False
                if query == prev_query:
                    query = "Select concat(FirstName, ' ', Lastname), a.username from staff a join normaluser b on a.username = b.username"
                    query_u = True
                if queryb == prev_queryb:
                    queryb = "select count(employee_ID), username from staffassigned a join normaluser b on a.employee_ID=b.username group by b.username"
                    queryb_u = True
                else:
                    queryb = queryb + " group by b.username"
                if self.sort.get() == "Name":
                    query = query + " order by concat(FirstName, ' ', Lastname) "
                elif self.sort.get() == "Name Desc":
                    query = query + " order by concat(FirstName, ' ', Lastname) desc"
                else:
                    query = query
                print(query)
                print(queryb)
                self.cursor.execute(query)
                staff_names = self.cursor.fetchall()
                self.cursor.execute(queryb)
                shifts = self.cursor.fetchall()
                if query_u == True:
                    staff = {}
                    for s in staff_names:
                        staff[s[1]] = s[0]
                    for shift in shifts:
                        count = shift[0]
                        username = shift[1]
                        self.tree.insert("", "end", values=(staff[username], count))
                if queryb_u == True:
                    shift = {}
                    for s in shifts:
                        shift[s[1]] = s[0]
                    for staff in staff_names:
                        name = staff[0]
                        username = staff[1]
                        shift_count = 0
                        if username in shift:
                            shift_count = shift[username]
                        self.tree.insert("", "end", values=(name, shift_count))

    def back_view_staff(self):
        self.currGui.withdraw()
        if self.userType == "Employee, Visitor":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Employee":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Visitor":
            self.visitor_functionality()
            self.currGui = self.visitorGUI
        elif self.userType == "User":
            self.user_functionality()
            self.currGui = self.navGUI

    def manage_event(self):
        site_query = "select sitename from Site where managerid = '%s'" % (self.user.get())
        result = self.cursor.execute(site_query)
        if result == 0:
            messagebox.showinfo("No Site", "You do not manage a site so you cannot access this screen.")
        else:
            self.currGui.withdraw()
            self.manageEvent = Toplevel()
            self.currGui = self.manageEvent
            self.manageEvent.title("Manage Event")

            Label(self.manageEvent, text="Manage Event").grid(row=0)

            frame = Frame(self.manageEvent)
            frame.grid()

            Label(frame, text="Name ").grid(row=0, column=0)
            self.name = StringVar()
            self.name_enter = Entry(frame, textvariable=self.name)
            self.name_enter.grid(row=0, column=1)

            Label(frame, text="Description Keyword ").grid(row=0, column=2)
            self.description = StringVar()
            self.description_enter = Entry(frame, textvariable=self.description)
            self.description_enter.grid(row=0, column=3)

            Label(frame, text="Start Date").grid(row=1, column=0)
            self.start_date = StringVar()
            self.start_date_enter = Entry(frame, textvariable=self.start_date)
            self.start_date_enter.grid(row=1, column=1)

            Label(frame, text="End Date").grid(row=1, column=2)
            self.end_date = StringVar()
            self.end_date_enter = Entry(frame, textvariable=self.end_date)
            self.end_date_enter.grid(row=1, column=3)

            Label(frame, text="Duration Range").grid(row=2, column=0)
            self.duration_lower = IntVar()
            self.duration_lower_enter = Entry(frame, textvariable=self.duration_lower)
            self.duration_lower_enter.grid(row=2, column=1)

            Label(frame, text=" -- ").grid(row=2, column=2)
            self.duration_upper = IntVar()
            self.duration_upper_enter = Entry(frame, textvariable=self.duration_upper)
            self.duration_upper_enter.grid(row=2, column=3)

            Label(frame, text="Total Visits Range").grid(row=2, column=4)
            self.visits_lower = IntVar()
            self.visits_lower_enter = Entry(frame, textvariable=self.visits_lower)
            self.visits_lower_enter.grid(row=2, column=5)

            Label(frame, text=" -- ").grid(row=2, column=6)
            self.visits_upper = IntVar()
            self.visits_upper_enter = Entry(frame, textvariable=self.visits_upper)
            self.visits_upper_enter.grid(row=2, column=7)

            Label(frame, text="Total Revenue Range").grid(row=3, column=0)
            self.revenue_lower = IntVar()
            self.revenue_lower_enter = Entry(frame, textvariable=self.revenue_lower)
            self.revenue_lower_enter.grid(row=3, column=1)

            Label(frame, text=" -- ").grid(row=3, column=2)
            self.revenue_upper = IntVar()
            self.revenue_upper_enter = Entry(frame, textvariable=self.revenue_upper)
            self.revenue_upper_enter.grid(row=3, column=3)

            Label(frame, text="Sort By: ").grid(row=3, column=4)
            self.sort = StringVar()
            choices = ['Name', 'Name Desc', 'None']
            self.sort.set('None')
            self.popup = OptionMenu(frame, self.sort, *choices)
            self.popup.grid(row=3, column = 5)

            self.filter = Button(frame, text="Filter", command=self.filter_manage_event).grid(row=4, column=0)
            self.create = Button(frame, text="Create", command=self.create_event).grid(row=4, column=1)
            self.view = Button(frame, text="View/Edit", command=self.view_edit_event).grid(row=4, column=2)
            self.delete = Button(frame, text="Delete", command=self.delete_event).grid(row=4, column=3)

            frame_tree = Frame(self.manageEvent)
            frame_tree.grid()

            self.tree = ttk.Treeview(frame_tree,
                                columns=['Name', 'Staff Count', 'Duration (Days)', 'Total Visits', 'Total Revenue', 'Start Date'],
                                show='headings', selectmode='browse')

            self.tree.heading('Name', text='Name')
            self.tree.heading('Staff Count', text='Staff Count')
            self.tree.heading('Duration (Days)', text='Duration (Days)')
            self.tree.heading('Total Visits', text='Total Visits')
            self.tree.heading('Total Revenue', text="Total Revenue")
            self.tree.heading('Start Date', text='Start Date')
            #self.tree.insert("", "end", values=("1", "2", "3", "4", "6"))
            #self.tree.insert("", "end", values=("4", "5", "6", "7", "8"))
            self.tree.grid(row=1, column=3)

            frame_under = Frame(self.manageEvent)
            frame_under.grid()

            self.back = Button(frame_under, text="Back", command=self.back_manage_event).grid(row=0, column=0)

    def filter_manage_event(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        if self.name.get() == '' and self.description.get() == '' and self.start_date.get() == "" and self.end_date.get() == "" and self.duration_lower.get() == 0 and self.duration_upper.get() == 0 and self.visits_lower.get() == 0 and self.visits_upper.get() == 0 and self.revenue_lower.get() == 0 and self.revenue_upper.get() == 0:
            query = ""
            site_query = "select sitename from Site where managerid = '%s'" % (self.user.get())
            self.cursor.execute(site_query)
            site = self.cursor.fetchone()
            if self.sort.get() == "Name":
                query = "SELECT eventname, startdate, sitename from beltlineevent where sitename = '%s' order by eventname" % (site[0])
            elif self.sort.get() == "Name Desc":
                query = "SELECT eventname, startdate, sitename from beltlineevent where sitename = '%s' order by eventname desc" % (site[0])
            else:
                query = "SELECT eventname, startdate, sitename from beltlineevent where sitename = '%s' order by eventname" % (site[0])
            self.cursor.execute(query)
            self.events = self.cursor.fetchall()
            for event in self.events:
                name = event[0]
                start = event[1]
                site = event[2]
                query_staff = "select eventname as Name, count(employee_id) as 'Staff Count' from staffassigned where eventname= '%s' AND eventstartdate='%s' AND sitename= '%s'" % (name, start, site)
                self.cursor.execute(query_staff)
                staff = self.cursor.fetchone()
                query_duration = "select Distinct staffassigned.eventname as Name, (enddate-startdate) as Duration from staffassigned join beltlineevent on staffassigned.eventname = beltlineevent.eventname where beltlineevent.eventname= '%s' AND beltlineevent.startdate='%s' AND beltlineevent.sitename= '%s'" % (name, start, site)
                self.cursor.execute(query_duration)
                duration = self.cursor.fetchone()
                query_visits = "select eventname as Name,count(dateattended) as 'Total Visits' from visitevent where eventname= '%s' AND eventstartdate='%s' AND sitename= '%s'" % (name, start, site)
                self.cursor.execute(query_visits)
                visits = self.cursor.fetchone()
                query_revenue = "Select beltlineevent.eventname, (any_value(price)*count(dateattended)) from visitevent join beltlineevent where beltlineevent.eventname= '%s' AND beltlineevent.startdate='%s' AND beltlineevent.sitename= '%s'" % (name, start, site)
                self.cursor.execute(query_revenue)
                revenue = self.cursor.fetchone()
                self.tree.insert("", "end", values=(name, staff[1], duration[1], visits[1], revenue[1], start))
        '''else:
            query = "SELECT eventname, startdate, sitename from BeltLineEvent where "
            query_duration = "select Distinct staffassigned.eventname as Name, (enddate-startdate) as Duration from staffassigned join beltlineevent on staffassigned.eventname = beltlineevent.eventname where "
            query_visits = "select eventname as Name,count(dateattended) as TotalVisits from visitevent where "
            query_revenue = "Select beltlineevent.eventname, (any_value(price)*count(dateattended)) as Rev from visitevent join beltlineevent where "
            name = ""
            desc = ""
            duration = ""
            visits = ""
            revenue = ""
            if self.destination.get() != "All":
                site = "SiteName = '" + self.destination.get() + "'"
            if self.trans_type.get() != "All":
                tran = "TransitType = '" + self.trans_type.get() + "'"
            if self.price_upper.get() != 0 and self.price_lower.get() <= self.price_upper.get():
                price = price + "Price between '" + str(self.price_lower.get()) + "' and '" + str(self.price_upper.get()) + "'"
            if site != "":
                query = query + site
                if tran != "":
                    query = query + " and " + tran
                if price != "":
                    query = query + " and " + price
            elif tran != "":
                query = query + tran
                if price != "":
                    query = query + " and " + price
            else:
                query = query + price
            if self.sort.get() == "Name":
                query = query + " order by eventname"
            elif self.sort.get() == "Name Desc":
                query = query + " order by eventname desc"
            else:
                query = query
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            for transit in results:
                route = transit[0]
                type = transit[1]
                price = transit[2]
                queryb = "Select count(sitename) from connects where transitroute = '%s'" % (route)
                self.cursor.execute(queryb)
                connected = self.cursor.fetchone()
                self.tree.insert("", "end", values=(route, type, price, connected))'''

    def delete_event(self):
        if len(self.tree.selection()) == 0:
            messagebox.showwarning("Select Event", "Please select a event to delete")
        else:
            select = self.tree.item(self.tree.selection())
            startDate = ""
            sitename = ""
            for event in self.events:
                if event[0] == select["values"][0]:
                    startDate = event[1]
                    sitename = event[2]
            query = "Delete from beltlineevent where eventname = '%s' and startdate ='%s' and sitename = '%s'" % (select["values"][0], startDate, sitename)
            self.cursor.execute(query)
            self.db.commit()
            self.tree.delete(self.tree.selection()[0])
            messagebox.showinfo("Success!!", "The Event have been successfully deleted")

    def back_manage_event(self):
        self.currGui.withdraw()
        if self.userType == "Employee, Visitor":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Employee":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Visitor":
            self.visitor_functionality()
            self.currGui = self.visitorGUI
        elif self.userType == "User":
            self.user_functionality()
            self.currGui = self.navGUI

    def view_edit_event(self):
        if len(self.tree.selection()) == 0:
            messagebox.showwarning("Select Event", "Please select a event to edit")
        else:
            self.currGui.withdraw()
            self.view_event = Toplevel()
            self.currGui = self.view_event
            self.view_event.title("View/Edit Event")

            Label(self.view_event, text="View/Edit Event").grid(row=0)

            frame = Frame(self.view_event)
            frame.grid()

            query = "Select sitename from site where managerID = '%s'" % (self.user.get())
            self.cursor.execute(query)
            site = self.cursor.fetchone()
            self.site = site[0]

            select = self.tree.item(self.tree.selection())
            self.name = select["values"][0]
            self.start = select["values"][5]
            query = "Select eventname, startdate, enddate, price, capacity, minstaffreq, eventdesc from BeltLineEvent where eventname = '%s' and startdate = '%s' and sitename = '%s'" % (self.name, self.start, self.site)
            self.cursor.execute(query)
            event_details = self.cursor.fetchone()


            Label(frame, text="Name ").grid(row=0, column=0)
            Label(frame, text=event_details[0]).grid(row=0, column=1)

            Label(frame, text="Price ($) ").grid(row=0, column=2)
            Label(frame, text=event_details[3]).grid(row=0, column=3)

            Label(frame, text="Start Date").grid(row=1, column=0)
            Label(frame, text=event_details[1]).grid(row=1, column=1)

            Label(frame, text="End Date").grid(row=1, column=2)
            Label(frame, text=event_details[2]).grid(row=1, column=3)

            Label(frame, text="Minimum Staff Required").grid(row=2, column=0)
            Label(frame, text=event_details[5]).grid(row=2, column=1)

            Label(frame, text="Capacity").grid(row=2, column=2)
            Label(frame, text=event_details[4]).grid(row=2, column=3)

            query = "Select distinct concat(firstname, ' ', lastname) from view_staffnames"
            self.cursor.execute(query)
            staff = self.cursor.fetchall()

            query = "select concat(firstname, ' ', lastname) from view_staffnames where eventname = '%s' and eventstartdate = '%s' and sitename = '%s'" % (self.name, self.start, self.site)
            self.cursor.execute(query)
            selected = self.cursor.fetchall()
            self.previously_selected = []

            Label(frame, text="Staff Assigned").grid(row=3, column=0)
            self.list = Listbox(frame, selectmode=MULTIPLE)
            count = 0
            dict = {}
            for s in staff:
                self.list.insert(count, s[0])
                dict[s[0]] = count
                count = count + 1
            #list.insert(0, 'Staff 1')
            #list.insert(1, 'Staff 2')
            #list.insert(2, 'Staff 3')
            self.list.grid(row=3, column=1)

            for s in selected:
                index = dict[s[0]]
                self.list.select_set(index)
                self.previously_selected.append(s[0])

            Label(frame, text="Description").grid(row = 4, column = 0)
            self.description = StringVar()
            self.desc = Text(frame,height=7)
            self.scroll = Scrollbar(frame, orient='vertical')
            self.desc.grid(row=4,column=1,pady=4)
            frame.columnconfigure(1,weight=1)
            self.desc.insert(END,event_details[6])
            self.scroll.config(command=self.desc.yview)
            self.desc.config(yscrollcommand=self.scroll.set)

            Label(frame, text="Daily Visits Range").grid(row=5, column=0)
            self.visits_lower = IntVar()
            self.visits_lower_enter = Entry(frame, textvariable=self.visits_lower)
            self.visits_lower_enter.grid(row=5, column=1)

            Label(frame, text=" -- ").grid(row=5, column=2)
            self.visits_upper = IntVar()
            self.visits_upper_enter = Entry(frame, textvariable=self.visits_upper)
            self.visits_upper_enter.grid(row=5, column=3)

            Label(frame, text="Daily Revenue Range").grid(row=5, column=4)
            self.revenue_lower = IntVar()
            self.revenue_lower_enter = Entry(frame, textvariable=self.revenue_lower)
            self.revenue_lower_enter.grid(row=5, column=5)

            Label(frame, text=" -- ").grid(row=5, column=6)
            self.revenue_upper = IntVar()
            self.revenue_upper_enter = Entry(frame, textvariable=self.revenue_upper)
            self.revenue_upper_enter.grid(row=5, column=7)

            self.filter = Button(frame, text="Filter", command=self.filter_view_edit_event).grid(row=6, column=0)
            self.create = Button(frame, text="Update", command=self.update_event).grid(row=6, column=1)

            frame_tree = Frame(self.view_event)
            frame_tree.grid()

            self.tree = ttk.Treeview(frame_tree, columns=['Date', 'Daily Visits', 'Daily Revenue'],
                                show='headings', selectmode='browse')

            self.tree.heading('Date', text='Date')
            self.tree.heading('Daily Visits', text='Daily Visits')
            self.tree.heading('Daily Revenue', text='Daily Revenue')
            #self.tree.insert("", "end", values=("1", "2", "3"))
            #self.tree.insert("", "end", values=("4", "5", "6"))
            self.tree.grid(row=1, column=3)

            frame_under = Frame(self.view_event)
            frame_under.grid()

            self.back = Button(frame_under, text="Back", command=self.view_edit_transit_back).grid(row=0, column=0)

    def view_edit_transit_back(self):
        self.currGui.withdraw()
        self.manageEvent.deiconify()
        self.currGui = self.manageEvent

    def filter_view_edit_event(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        if self.visits_lower.get() == 0 and self.visits_upper.get() == 0 and self.revenue_lower.get() == 0 and self.revenue_upper.get() == 0:
            #This Needs To be passed in another argument, I don't have access to it from here (dont have the most up to date one), should be an easy replacement
            query = "select any_value(dateattended) as Date ,count(dateattended) as Visits, (any_value(price)*count(dateattended)) as Revenue from visitevent a join beltlineevent b on a.eventname = b.eventname and a.sitename=b.sitename and a.eventstartdate= b. startdate where b.eventname = '%s' group by a.dateattended" % (self.name)
            self.cursor.execute(query)
            list = self.cursor.fetchall()
            for item in list:
                date = item[0]
                visits = item[1]
                revenue = item[2]
                self.tree.insert("", "end", values = (date, visits, revenue))



    def update_event(self):
        query = "Update BeltLineEvent set EventDesc= '%s' where eventname = '%s' and startdate = '%s' and sitename = '%s'" % (self.desc.get("1.0",END), self.name, self.start, self.site)
        self.cursor.execute(query)
        indices = self.list.curselection()
        currently_selected = []
        for index in indices:
            currently_selected.append(self.list.get(index))
        for index in indices:
            staff = self.list.get(index)
            id_query = "select username from normaluser where concat(firstname, ' ',lastname)= '%s'" % (staff)
            self.cursor.execute(id_query)
            employee_id = self.cursor.fetchone()
            if staff not in self.previously_selected:
                query = "Insert into staffassigned values('%s','%s','%s','%s')" % (employee_id[0], self.name, self.start, self.site)
                self.cursor.execute(query)
        for site in self.previously_selected:
            id_query = "select username from normaluser where concat(firstname, ' ',lastname)= '%s'" % (staff)
            self.cursor.execute(id_query)
            employee_id = self.cursor.fetchone()
            if site not in currently_selected:
                query = "Delete from staffassigned where eventstartdate= '%s' AND username = '%s' and eventname = '%s' and sitename = '%s'" % (self.start, employee_id[0], self.name, self.site)
                self.cursor.execute(query)
        self.db.commit()
        messagebox.showinfo("Success!!", "The event has been edited")
        self.currGui.withdraw()
        self.manage_event()

    def create_event(self):
        self.currGui.withdraw()
        self.create_event = Toplevel()
        self.currGui = self.create_event
        self.create_event.title("Create Event")

        Label(self.create_event, text="Create Event").grid(row=0)

        frame = Frame(self.create_event)
        frame.grid()

        Label(frame, text="Name ").grid(row=0, column=0)
        self.name = StringVar()
        self.name_entry = Entry(frame, textvariable=self.name)
        self.name_entry.grid(row=0, column=1)

        Label(frame, text="Price ($) ").grid(row=1, column=0)
        self.price = IntVar()
        self.price_entry = Entry(frame, textvariable=self.price)
        self.price_entry.grid(row=1, column=1)

        Label(frame, text="Capacity").grid(row=1, column=2)
        self.capacity = IntVar()
        self.capacity_entry = Entry(frame, textvariable=self.capacity)
        self.capacity_entry.grid(row=1, column=3)

        Label(frame, text="Minimum Staff Required").grid(row=1, column=4)
        self.min_staff = IntVar()
        self.min_staff_entry = Entry(frame, textvariable=self.min_staff)
        self.min_staff_entry.grid(row=1, column=5)

        Label(frame, text="Start Date").grid(row=2, column=0)
        self.start_date = StringVar()
        self.start_date_enter = Entry(frame, textvariable=self.start_date)
        self.start_date_enter.grid(row=2, column=1)

        Label(frame, text="End Date").grid(row=2, column=2)
        self.end_date = StringVar()
        self.end_date_enter = Entry(frame, textvariable=self.end_date)
        self.end_date_enter.grid(row=2, column=3)

        Label(frame, text="Description").grid(row = 3, column = 0)
        self.description = StringVar()
        self.desc = Text(frame,height=7)
        self.scroll = Scrollbar(frame, orient='vertical')
        self.desc.grid(row=3,column=1,pady=4)
        frame.columnconfigure(1,weight=1)
        self.desc.insert(END,'description goes here')
        self.scroll.config(command=self.desc.yview)
        self.desc.config(yscrollcommand=self.scroll.set)

        Label(frame, text="Assign Staff").grid(row=4, column=0)
        self.list = Listbox(frame, selectmode=MULTIPLE)
        #list.insert(0, 'Staff 1')
        #list.insert(1, 'Staff 2')
        #list.insert(2, 'Staff 3')
        self.list.grid(row=4, column=1)

        self.load_staff = Button(frame, text="Load Available Staff", command=self.load_staff).grid(row = 4, column= 2)

        self.back = Button(frame, text="Back", command=self.create_event_back).grid(row=5, column=0)
        self.create = Button(frame, text="Create", command=self.create_event_btn).grid(row=5, column=1)

    def create_event_back(self):
        self.currGui.withdraw()
        self.manageEvent.deiconify()
        self.currGui = self.manageEvent

    def load_staff(self):
        self.list.delete(0,'end')
        if self.start_date.get() == "" or self.end_date.get() == "":
            messagebox.showwarning("Start Date and End Date", "Please select a start date and end date in order to see the available staff")
        else:
            query = "select distinct concat(firstname, ' ',lastname) as Staff from view_staffnames where employee_ID not in (select employee_ID from staffassigned where eventstartdate between '2019-03-20' and '1019-03-24' )"
            self.cursor.execute(query)
            staff = self.cursor.fetchall()
            for s in staff:
                self.list.insert('end', s[0])

    def create_event_btn(self):
        startd = None
        endd = None
        greater = False
        if self.start_date.get() != "" and self.end_date.get() != "": #and self.start_date.get() <= self.end_date.get():
            start = [x.strip() for x in self.start_date.get().split('-')]
            end = [x.strip() for x in self.end_date.get().split('-')]
            startd = datetime.datetime(int(start[0], 10), int(start[1], 10), int(start[2], 10))
            endd = datetime.datetime(int(end[0], 10), int(end[1], 10), int(end[2], 10))
        if startd != None and endd != None:
            if startd > endd:
                greater = True
        if self.name.get() == "":
            messagebox.showwarning("Name", "Please enter a event name")
        elif self.min_staff.get() == 0:
            messagebox.showwarning("Minimum Staff", "Please enter the miminum staff required for this event")
        elif greater == True:
            messagebox.showwarning("Date", "The start date must be before the end date")
        elif self.start_date.get() == "" and self.end_date.get() != "":
            messagebox.showwarning("Date", "There must be a start and end date. They can be the same date")
        elif self.start_date.get() != "" and self.end_date.get() == "":
            messagebox.showwarning("Date", "There must be a start and end date. They can be the same date")
        elif self.desc.get("1.0",END) == "":
            messagebox.showwarning("Description", "Please enter a description for the event")
        elif len(self.list.curselection()) == 0:
            messagebox.showwarning("Staff", "Please assign staff to this event")
        elif len(self.list.curselection()) < self.min_staff.get():
            messagebox.showwarning("Staff", "The number of staff assigned must not be fewer than the minimum staff required")
        else:
            query_site = "select sitename from site where managerID = '%s'" % (self.user.get())
            self.cursor.execute(query_site)
            site = self.cursor.fetchone()
            query_check = "select eventname, startdate from beltlineevent where startdate = '%s' and eventname = '%s' and sitename = '%s'" % (self.start_date.get(), self.name.get(), site[0])
            check = self.cursor.execute(query_check)
            #query_c = "select exists (select eventname, startdate from beltlineevent where startdate = '%s' and eventname = '%s' and sitename = '%s')"
            if check == 1:
                messagebox.showwarning("Error!", "There is already an event with this name and start date at your site. Please enter a different start date or a different name")
            query = "insert into beltlineevent values('%s','%s','%s','%s','%s','%s','%s','%s')" % (self.name.get(),self.start_date.get() ,site[0],self.end_date.get() ,self.price.get(),self.capacity.get(),self.min_staff.get(),self.desc.get("1.0", END))
            self.cursor.execute(query)
            indicies = self.list.curselection()
            for index in indicies:
                staff = self.list.get(index)
                query_id = "select username from normaluser where concat(firstname, ' ',lastname)= '%s'" % (staff)
                self.cursor.execute(query_id)
                username = self.cursor.fetchone()
                query = "Insert into staffassigned values('%s','%s','%s','%s')" % (username[0], self.name.get(), self.start_date.get(), site[0])
                self.cursor.execute(query)
            self.db.commit()
            messagebox.showinfo("Success!", "The event has been created")
            self.currGui.withdraw()
            self.manage_event()

    def view_visit_history(self):
        pass

    def view_transit_history(self):
        self.currGui.withdraw()
        self.view_tran = Toplevel()
        self.currGui = self.view_tran
        self.view_tran.title("Transit History")

        Label(self.view_tran, text="Transit History").grid(row=0)

        frame = Frame(self.view_tran)
        frame.grid()

        Label(frame, text="Transport Type ").grid(row=0, column=0)
        self.trans_type = StringVar()
        choices_type = ['MARTA', 'Bus', 'Bike', 'All']
        self.trans_type.set('All')
        self.popup = OptionMenu(frame, self.trans_type, *choices_type)
        self.popup.grid(row=0, column=1)

        query = "Select Distinct SiteName from Site"
        self.cursor.execute(query)
        sites = self.cursor.fetchall()

        Label(frame, text="Contain Site ").grid(row=0, column=2)
        self.destination = StringVar()
        choices = []
        for site in sites:
            choices.append(site[0])
        choices.append('All')
        self.destination.set("All")
        self.popupMenu = OptionMenu(frame, self.destination, *choices)
        self.popupMenu.grid(row=0, column=3)

        Label(frame, text="Route").grid(row=1, column=0)
        self.route = StringVar()
        self.route_enter = Entry(frame, textvariable=self.route)
        self.route_enter.grid(row=1, column=1)

        Label(frame, text="Start Date").grid(row=1, column=2)
        self.start_date = StringVar()
        self.start_date_enter = Entry(frame, textvariable=self.start_date)
        self.start_date_enter.grid(row=1, column=3)

        Label(frame, text="End Date").grid(row=1, column=4)
        self.end_date = StringVar()
        self.end_date_enter = Entry(frame, textvariable=self.end_date)
        self.end_date_enter.grid(row=1, column=5)

        Label(frame, text="Sort By: ").grid(row=2, column=0)
        self.sort = StringVar()
        choices = ['Date', 'Route', 'Transport Type', 'Price','Date Desc', 'Route Desc', 'Transport Type Desc', 'Price Desc', 'None']
        self.sort.set('None')
        self.popup = OptionMenu(frame, self.sort, *choices)
        self.popup.grid(row=2, column = 1)

        self.filter = Button(frame, text="Filter", command=self.filter_transit_history).grid(row=2, column=2)

        frame_tree = Frame(self.view_tran)
        frame_tree.grid()

        self.tree = ttk.Treeview(frame_tree, columns=['Date', 'Route', 'Transport Type', 'Price'],
                            show='headings', selectmode='browse')

        self.tree.heading('Date', text='Date')
        self.tree.heading('Route', text='Route')
        self.tree.heading('Transport Type', text='Transport Type')
        self.tree.heading('Price', text='Price')
        self.tree.grid(row=1, column=3)

        frame_under = Frame(self.view_tran)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_transit_history).grid(row=0, column=0)

    def filter_transit_history(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        if self.destination.get() == 'All' and self.trans_type.get() == 'All' and self.route.get() == "" and self.start_date.get() == "" and self.end_date.get() == "":
            query = ""
            if self.sort.get() == "Date":
                query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s' order by DateTaken" % self.user.get()
            elif self.sort.get() == "Route":
                query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s' order by Transit_route" % self.user.get()
            elif self.sort.get() == "Transport Type":
                query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s' order by Transit_type" % self.user.get()
            elif self.sort.get() == "Price":
                query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s' order by price" % self.user.get()
            elif self.sort.get() == "Date Desc":
                query = query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s' order by DateTaken desc" % self.user.get()
            elif self.sort.get() == "Route Desc":
                query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s' order by Transit_route desc" % self.user.get()
            elif self.sort.get() == "Transport Type Desc":
                query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s' order by Transit_type desc" % self.user.get()
            elif self.sort.get() == "Price Desc":
                query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s' order by price desc" % self.user.get()
            else:
                query = query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s'" % self.user.get()
            self.cursor.execute(query)
            transits = self.cursor.fetchall()
            for transit in transits:
                date = transit[0]
                route = transit[1]
                type = transit[2]
                price = transit[3]
                self.tree.insert("", "end", values=(date, route, type, price))
        else:
            query = "select Distinct DateTaken, a.Transit_route, a.Transit_Type, price from transit a join takes b join connects c on b.transit_route = a.Transit_Route and b.transit_route = c.TransitRoute where b.username = '%s' " % (self.user.get())
            site = ""
            trans = ""
            route = ""
            date = ""
            startd = None
            endd = None
            greater = False
            if self.start_date.get() != "" and self.end_date.get() != "": #and self.start_date.get() <= self.end_date.get():
                start = [x.strip() for x in self.start_date.get().split('-')]
                end = [x.strip() for x in self.end_date.get().split('-')]
                startd = datetime.datetime(int(start[0], 10), int(start[1], 10), int(start[2], 10))
                endd = datetime.datetime(int(end[0], 10), int(end[1], 10), int(end[2], 10))
            if startd != None and endd != None:
                if startd > endd:
                    greater = True
            if greater == True:
                messagebox.showwarning("Date", "The start date must be before the end date")
            elif self.start_date.get() == "" and self.end_date.get() != "":
                messagebox.showwarning("Date", "There must be a start and end date. They can be the same date")
            elif self.start_date.get() != "" and self.end_date.get() == "":
                messagebox.showwarning("Date", "There must be a start and end date. They can be the same date")
            else:
                if self.destination.get() != "All":
                    site = "c.SiteName = '" + self.destination.get() + "'"
                if self.trans_type.get() != "All":
                    trans = "a.Transit_Type = '" + self.trans_type.get() + "'"
                if self.route.get() != "":
                    route = "a.Transit_route = '" + self.route.get() + "'"
                if self.start_date.get() != "" and self.end_date.get() !="" and self.start_date.get() <= self.end_date.get():
                    date = "DateTaken between '" + self.start_date.get() + "'" + " and '" + self.end_date.get() + "'"
                if site != "":
                    query = query + "and " + site
                    if trans != "":
                        query = query + " and " + trans
                    if route != "":
                        query = query + " and " + route
                    if date != "":
                        query = query + " and " + date
                elif trans != "":
                    query = query + "and " + trans
                    if route != "":
                        query = query + " and " + route
                    if date != "":
                        query = query + " and " + date
                elif route != "":
                    query = query + "and " + route
                    if date != "":
                        query = query + " and " + date
                else:
                    query = query + "and " + date
                query = ""
                if self.sort.get() == "Date":
                    query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s' order by DateTaken" % self.user.get()
                elif self.sort.get() == "Route":
                    query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s' order by Transit_route" % self.user.get()
                elif self.sort.get() == "Transport Type":
                    query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s' order by Transit_type" % self.user.get()
                elif self.sort.get() == "Price":
                    query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s' order by price" % self.user.get()
                elif self.sort.get() == "Date Desc":
                    query = query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s' order by DateTaken desc" % self.user.get()
                elif self.sort.get() == "Route Desc":
                    query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s' order by Transit_route desc" % self.user.get()
                elif self.sort.get() == "Transport Type Desc":
                    query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s' order by Transit_type desc" % self.user.get()
                elif self.sort.get() == "Price Desc":
                    query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s' order by price desc" % self.user.get()
                else:
                    query = query = "Select Distinct DateTaken, a.Transit_route, a.Transit_type, price from transit a join takes b on b.transit_route = a.Transit_Route where username = '%s'" % self.user.get()
                self.cursor.execute(query)
                results = self.cursor.fetchall()
                for transit in results:
                    date = transit[0]
                    route = transit[1]
                    type = transit[2]
                    price = transit[3]
                    self.tree.insert("", "end", values=(date, route, type, price))

    def back_transit_history(self):
        self.currGui.withdraw()
        if self.userType == "Employee, Visitor":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Employee":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Visitor":
            self.visitor_functionality()
            self.currGui = self.visitorGUI
        elif self.userType == "User":
            self.user_functionality()
            self.currGui = self.navGUI

    def explore_event(self):
        pass

    def manage_profile(self):
        self.currGui.withdraw()
        self.manageProGui = Toplevel()
        self.currGui = self.manageProGui
        self.manageProGui.title("Manage Profile")

        Label(self.manageProGui, text="Manage Profile").grid(row=0)

        frame = Frame(self.manageProGui)
        frame.grid()

        query = "select firstname, lastname, phone from normaluser a join employee b on a.username = b.username where a.username = '%s'" % (self.user.get())
        self.cursor.execute(query)
        result = self.cursor.fetchone()

        Label(frame, text="First Name: ").grid(row=0, column=0)
        self.fname = StringVar()
        self.fname_enter = Entry(frame, textvariable=self.fname)
        self.fname_enter.grid(row=0, column=1)
        self.fname.set(result[0])

        Label(frame, text="Last Name: ").grid(row=0, column=2)
        self.lname = StringVar()
        self.lname_enter = Entry(frame, textvariable=self.lname)
        self.lname_enter.grid(row=0, column=3)
        self.lname.set(result[1])

        Label(frame, text="Username: ").grid(row=1, column=0)
        Label(frame, text=self.user.get()).grid(row=1, column=1)

        query = "Select sitename from site where managerID = '%s'" % (self.user.get())
        self.cursor.execute(query)
        result1 = self.cursor.fetchone()

        Label(frame, text="Site Name: ").grid(row=1, column=2)
        text = ""
        if result1 != None:
            test = result1[0]
        Label(frame, text=text).grid(row=1, column=3)

        query = "Select employee_ID, concat(employee_address,', ', employee_city,', ', employee_state, ' ', employee_zipcode) as Address from employee where username = '%s'" % (self.user.get())
        self.cursor.execute(query)
        result2 = self.cursor.fetchone()

        Label(frame, text="Employee ID: ").grid(row=2, column=0)
        Label(frame, text=result2[0]).grid(row=2, column=1)

        Label(frame, text="Phone ").grid(row=2, column=2)
        self.phone = IntVar()
        self.phone_enter = Entry(frame, textvariable=self.phone)
        self.phone_enter.grid(row=2, column=3)
        self.phone.set(result[2])

        Label(frame, text="Address: ").grid(row=3, column=0)
        Label(frame, text = result2[1]).grid(row=3, column=1)

        query = "Select email from email where username = '%s'" % (self.user.get())
        self.cursor.execute(query)
        result3 = self.cursor.fetchall()
        email_c = ""
        for email in result3:
            email_c = email_c + " " + email[0] + ","
        self.prev_email = email_c

        Label(frame, text="Email: ").grid(row=4, column=0)
        self.email = StringVar()
        self.email_enter = Entry(frame, textvariable=self.email)
        self.email_enter.grid(row=4, column=1)
        self.email.set(email_c)

        query = "Select * from Visitor where Username = '%s'" % (self.user.get())
        vis = self.cursor.execute(query)

        self.visitor = IntVar()
        self.visitor.set(vis)
        Checkbutton(frame, text="Visitor Account", variable=self.visitor).grid(row=5, column=0)

        self.registerUser = Button(frame, text="Update", command=self.update_profile).grid(row=6, column=0)
        self.registerUser = Button(frame, text="Back", command=self.back_manage_profile).grid(row=6, column=1)

    def update_profile(self):
        query = "Update NormalUser set Firstname = '%s', LastName = '%s' where Username = '%s'" % (self.fname.get(), self.lname.get(), self.user.get())
        queryb = "Update Employee set Phone = '%s' where Username = '%s'" % (self.phone.get(), self.user.get())
        self.cursor.execute(query)
        self.cursor.execute(queryb)
        email_split = [x.strip() for x in self.email.get().split(',')]
        for email in email_split:
            if email != "" and email not in self.prev_email:
                querye = "Insert into Email values('%s', '%s')" % (self.user.get(), email)
                self.cursor.execute(querye)
        if self.visitor.get() == 0:
            queryd = "delete from visitor where username = '%s'" % (self.user.get())
            self.cursor.execute(queryd)
        self.db.commit()
        messagebox.showinfo("Success!!", "Your profile has been successfully updated!")

    def back_manage_profile(self):
        self.currGui.withdraw()
        if self.userType == "Employee, Visitor":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Employee":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Visitor":
            self.visitor_functionality()
            self.currGui = self.visitorGUI
        elif self.userType == "User":
            self.user_functionality()
            self.currGui = self.navGUI

    def manage_user(self):
        self.currGui.withdraw()
        self.manageUserGui = Toplevel()
        self.currGui = self.manageUserGui
        self.manageUserGui.title("Manage User")

        Label(self.manageUserGui, text="Manage User").grid(row=0)

        frame = Frame(self.manageUserGui)
        frame.grid()

        Label(frame, text="Username ").grid(row=0, column=0)
        self.username = StringVar()
        self.username_enter = Entry(frame, textvariable=self.username)
        self.username_enter.grid(row=0, column=1)

        Label(frame, text="Type ").grid(row=0, column=2)
        self.type = StringVar()
        choices = ['User', 'Visitor', 'Staff', 'Manager', 'All']
        self.type.set("All")
        self.popupMenu = OptionMenu(frame, self.type, *choices)
        self.popupMenu.grid(row=0, column=3)

        Label(frame, text="Status ").grid(row=0, column=4)
        self.status = StringVar()
        choices_type = ['Approved', 'Declined', 'Pending', 'All']
        self.status.set('All')
        self.popup = OptionMenu(frame, self.status, *choices_type)
        self.popup.grid(row=0, column=5)

        Label(frame, text="Sort By: ").grid(row=1, column=0)
        self.sort = StringVar()
        choices = ['Username', 'Status', 'Username Desc', 'Status Desc', 'None']
        self.sort.set('None')
        self.popup = OptionMenu(frame, self.sort, *choices)
        self.popup.grid(row=1, column = 1)

        self.filter = Button(frame, text="Filter", command=self.filter_manage_user).grid(row=2, column=0)

        self.approve = Button(frame, text="Approve", command=self.approve_user).grid(row=2, column=1)
        self.decline = Button(frame, text='Decline', command=self.decline_user).grid(row=2, column=2)

        frame_tree = Frame(self.manageUserGui)
        frame_tree.grid()

        self.tree = ttk.Treeview(frame_tree, columns=['Username', 'Email Count', 'User Type', 'Status'],
                            show='headings', selectmode='browse')

        self.tree.heading('Username', text='Username')
        self.tree.heading('Email Count', text='Email Count')
        self.tree.heading('User Type', text='User Type')
        self.tree.heading("Status", text='Status')
        #self.tree.insert("", "end", values=("1", "2", "3", "4"))
        #self.tree.insert("", "end", values=("4", "5", "6", "7"))
        self.tree.grid(row=1, column=3)

        frame_under = Frame(self.manageUserGui)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_manage_user).grid(row=0, column=0)

    def approve_user(self):
        if len(self.tree.selection()) == 0:
            messagebox.showwarning("Select User", "Please select a user to approve")
        else:
            select = self.tree.item(self.tree.selection())
            query = "Update NormalUser set User_Status = 'Approved' where Username = '%s'" % (select['values'][0])
            self.cursor.execute(query)
            self.db.commit()
            messagebox.showinfo("Success!!", "The User has been approved!")
            user = select["values"][0]
            count = select["values"][1]
            type = select["values"][2]
            self.tree.insert("", "end", values=(user, count, type, "Approved"))
            self.tree.delete(self.tree.selection()[0])

    def decline_user(self):
        if len(self.tree.selection()) == 0:
            messagebox.showwarning("Select User", "Please select a user to decline")
        elif self.tree.item(self.tree.selection())['values'][3] == "Approved":
            messagebox.showwarning("Select User", "You cannot decline an approved user. Please select a pending account to decline")
        else:
            select = self.tree.item(self.tree.selection())
            query = "Update NormalUser set User_Status = 'Declined' where Username = '%s'" % (self.username.get())
            self.cursor.execute(query)
            self.db.commit()
            messagebox.showinfo("Success!!", "The User has been declined!")
            user = select["values"][0]
            count = select["values"][1]
            type = select["values"][2]
            self.tree.insert("", "end", values=(user, count, type, "Approved"))
            self.tree.delete(self.tree.selection()[0])

    def filter_manage_user(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        if self.username.get() == '' and self.type.get() == 'All' and self.status.get() == 'All':
            query = ""
            if self.sort.get() == "Username":
                query = "Select username, user_status from normaluser where username != '%s' order by username" % (self.user.get())
            elif self.sort.get() == "Status":
                query = "Select username, user_status from normaluser where username != '%s' order by user_status" % (self.user.get())
            elif self.sort.get() == "Username Desc":
                query = "Select username, user_status from normaluser where username != '%s' order by username desc" % (self.user.get())
            elif self.sort.get() == "Status Desc":
                query = "Select username, user_status from normaluser where username != '%s' order by user_status desc" % (self.user.get())
            else:
                query = "Select username, user_status from normaluser where username != '%s'" % (self.user.get())
            self.cursor.execute(query)
            people = self.cursor.fetchall()
            for p in people:
                user = p[0]
                status = p[1]
                queryb = "Select count(*) from Email where Username = '%s'" % (user)
                self.cursor.execute(queryb)
                emails = self.cursor.fetchone()
                self.tree.insert("", "end", values=(user, emails, "User", status))
        else:
            query = ""
            if self.type.get() == "User" or self.type.get() == 'All':
                query = "Select username, user_status from normaluser where " #username = usernamevar from the box AND user_status = userstatusvar"
                user = ""
                status = ""
                if self.username.get() != "":
                    user = "username = '" + self.username.get() + "'"
                if self.status.get() != 'All':
                    status = "user_status = '" + self.status.get() + "'"
                if user != "":
                    query = query + user
                    if status != "":
                        query = query + " and " + status
                else:
                    query = query + status
                if self.sort.get() == "Username":
                    query = query + " order by username"
                elif self.sort.get() == "Status":
                    query = query + " order by user_status"
                elif self.sort.get() == "Username Desc":
                    query = query + " order by username desc"
                elif self.sort.get() == "Status Desc":
                    query = query + " order by user_status desc"
                else:
                    query = query
                self.cursor.execute(query)
                result = self.cursor.fetchall()
                for entry in result:
                    username = entry[0]
                    status = entry[1]
                    type = "User"
                    querye = "Select count(*) from Email where Username = '%s'" % (username)
                    self.cursor.execute(querye)
                    count = self.cursor.fetchone()
                    self.tree.insert("", "end", values=(username, count, type, status))
            elif self.type.get() == "Visitor":
                query = "SELECT visitor.username,user_status from visitor join normaluser on visitor.username= normaluser.username where "
                user = ""
                status = ""
                if self.username.get() != "":
                    user = "username = '" + self.username.get() + "'"
                if self.status.get() != 'All':
                    status = "user_status = '" + self.status.get() + "'"
                if user != "":
                    query = query + user
                    if status != "":
                        query = query + " and " + status
                else:
                    query = query + status
                if self.sort.get() == "Username":
                    query = query + " order by visitor.username"
                elif self.sort.get() == "Status":
                    query = query + " order by user_status"
                elif self.sort.get() == "Username Desc":
                    query = query + " order by visitor.username desc"
                elif self.sort.get() == "Status Desc":
                    query = query + " order by user_status desc"
                else:
                    query = query
                self.cursor.execute(query)
                result = self.cursor.fetchall()
                for entry in result:
                    username = entry[0]
                    status = entry[1]
                    type = "Visitor"
                    querye = "Select count(*) from Email where Username = '%s'" % (username)
                    self.cursor.execute(querye)
                    count = self.cursor.fetchone()
                    self.tree.insert("", "end", values=(username, count, type, status))
            else:
                query = "SELECT employee.username,user_status from employee join normaluser on employee.username= normaluser.username where "
                user = ""
                status = ""
                type = ""
                if self.username.get() != "":
                    user = "employee.username = '" + self.username.get() + "'"
                if self.status.get() != 'All':
                    status = "user_status = '" + self.status.get() + "'"
                if self.type.get() != 'All':
                    type = "Employee_Type = '" + self.type.get() + "'"
                if user != "":
                    query = query + user
                    if status != "":
                        query = query + " and " + status
                    if type != "":
                        query = query + " and " + type
                elif status != "":
                    query = query + status
                    if type != "":
                        query = query + " and " + type
                else:
                    query = query + type
                if self.sort.get() == "Username":
                    query = query + " order by employee.username"
                elif self.sort.get() == "Status":
                    query = query + " order by user_status"
                elif self.sort.get() == "Username Desc":
                    query = query + " order by employee.username desc"
                elif self.sort.get() == "Status Desc":
                    query = query + " order by user_status desc"
                else:
                    query = query
                self.cursor.execute(query)
                result = self.cursor.fetchall()
                for entry in result:
                    username = entry[0]
                    status = entry[1]
                    type = self.type.get()
                    querye = "Select count(*) from Email where Username = '%s'" % (username)
                    self.cursor.execute(querye)
                    count = self.cursor.fetchone()
                    self.tree.insert("", "end", values=(username, count, type, status))

    def back_manage_user(self):
        self.currGui.withdraw()
        if self.userType == "Employee, Visitor":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Employee":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Visitor":
            self.visitor_functionality()
            self.currGui = self.visitorGUI
        elif self.userType == "User":
            self.user_functionality()
            self.currGui = self.navGUI

    def manage_transit(self):
        self.currGui.withdraw()
        self.manageTranGui = Toplevel()
        self.currGui = self.manageTranGui
        self.manageTranGui.title("Manage Transit")

        Label(self.manageTranGui, text="Manage Transit").grid(row=0)

        frame = Frame(self.manageTranGui)
        frame.grid()

        Label(frame, text="Transport Type ").grid(row=0, column=0)
        self.trans_type = StringVar()
        choices = ["MARTA", "Bus", "Bike", 'All']
        self.trans_type.set("All")
        self.popupMenu = OptionMenu(frame, self.trans_type, *choices)
        self.popupMenu.grid(row=0, column=1)

        Label(frame, text="Route ").grid(row=0, column=2)
        self.route = StringVar()
        self.route_enter = Entry(frame, textvariable=self.route)
        self.route_enter.grid(row=0, column=3)

        query = "Select Distinct SiteName from Site"
        self.cursor.execute(query)
        sites = self.cursor.fetchall()

        Label(frame, text="Contain Site ").grid(row=1, column=0)
        self.site = StringVar()
        choices_type = []
        for site in sites:
            choices_type.append(site[0])
        choices_type.append('All')
        self.site.set('All')
        self.popup = OptionMenu(frame, self.site, *choices_type)
        self.popup.grid(row=1, column=1)

        Label(frame, text="Price Range ").grid(row=1, column=2)
        self.price_lower = IntVar()
        self.price_lower_enter = Entry(frame, textvariable=self.price_lower)
        self.price_lower_enter.grid(row=1, column=3)

        Label(frame, text=" -- ").grid(row=1, column=4)
        self.price_upper = IntVar()
        self.price_upper_enter = Entry(frame, textvariable=self.price_upper)
        self.price_upper_enter.grid(row=1, column=5)

        Label(frame, text="Sort By: ").grid(row=2, column=0)
        self.sort = StringVar()
        choices = ['Transport Type', 'Price', 'Transport Type Desc', 'Price Desc', 'None']
        self.sort.set('None')
        self.popup = OptionMenu(frame, self.sort, *choices)
        self.popup.grid(row=2, column = 1)

        self.filter = Button(frame, text="Filter", command=self.filter_manage_transit).grid(row=3, column=0)

        self.create = Button(frame, text="Create", command=self.create_transit).grid(row=3, column=1)
        self.edit = Button(frame, text='Edit', command=self.edit_transit).grid(row=3, column=2)
        self.delete = Button(frame, text='Delete', command=self.delete_transit).grid(row=3, column=3)

        frame_tree = Frame(self.manageTranGui)
        frame_tree.grid()

        self.tree = ttk.Treeview(frame_tree,
                            columns=['Route', 'Transport Type', 'Price', '# Connected Sites', '# Transit Logged'],
                            show='headings', selectmode = 'browse')

        self.tree.heading('Route', text='Route')
        self.tree.heading('Transport Type', text='Transport Type')
        self.tree.heading('Price', text='Price')
        self.tree.heading("# Connected Sites", text='# Connected Sites')
        self.tree.heading("# Transit Logged", text='# Transit Logged')
        #self.tree.insert("", "end", values=("1", "2", "3", "4", "5"))
        #self.tree.insert("", "end", values=("4", "5", "6", "7", "8"))
        self.tree.grid(row=1, column=3)

        frame_under = Frame(self.manageTranGui)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_manage_transit).grid(row=0, column=0)

    def filter_manage_transit(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        if self.trans_type.get() == 'All' and self.route.get() == '' and self.site.get() == "All" and self.price_lower.get() == 0 and self.price_upper.get() == 0:
            query = ""
            queryc = "select transit_route,count(transit_route) from takes group by transit_route"
            if self.sort.get() == "Transport Type":
                query = "Select Transit_route, Transit_type, Price from Transit order by Transit_type"
            elif self.sort.get() == "Price":
                query = "Select Transit_route, Transit_type, Price from Transit order by Price"
            elif self.sort.get() == "Transport Type Desc":
                query = "Select Transit_route, Transit_type, Price from Transit order by Transit_type desc"
            elif self.sort.get() == "Price Desc":
                query = "Select Transit_route, Transit_type, Price from Transit order by Price desc"
            else:
                query = "Select Transit_route, Transit_type, Price from Transit"
            self.cursor.execute(query)
            transits = self.cursor.fetchall()
            self.cursor.execute(queryc)
            transits_logged = self.cursor.fetchall()
            logged = {}
            for t in transits_logged:
                logged[t[0]] = t[1]
            for transit in transits:
                route = transit[0]
                type = transit[1]
                price = transit[2]
                queryb = "Select count(sitename) from connects where transitroute = '%s'" % (route)
                self.cursor.execute(queryb)
                connected = self.cursor.fetchone()
                transits_logged = 0
                if route in logged:
                    transits_logged = logged[route]
                self.tree.insert("", "end", values=(route, type, price, connected, transits_logged))
        else:
            query = "select distinct Transit_route, Transit_type, Price from transit join connects on transit.transit_route = connects.TransitRoute where "
            site = ""
            tran = ""
            price = ""
            route = ""
            if self.site.get() != "All":
                site = "SiteName = '" + self.site.get() + "'"
            if self.trans_type.get() != "All":
                tran = "TransitType = '" + self.trans_type.get() + "'"
            if self.price_upper.get() != 0 and self.price_lower.get() <= self.price_upper.get():
                price = price + "Price between '" + str(self.price_lower.get()) + "' and '" + str(self.price_upper.get()) + "'"
            if self.route.get() != "":
                route = "TransitRoute = '" + self.route.get() + "'"
            if site != "":
                query = query + site
                if tran != "":
                    query = query + " and " + tran
                if price != "":
                    query = query + " and " + price
                if route != "":
                    query = query + " and " + route
            elif tran != "":
                query = query + tran
                if price != "":
                    query = query + " and " + price
                if route != "":
                    query = query + " and " + route
            elif price != "":
                query = query + price
                if route != "":
                    query = query + " and " + route
            else:
                query = query + route
            if self.sort.get() == "Transport Type":
                query = query + " order by Transit_type"
            elif self.sort.get() == "Price":
                query = query + " order by Price"
            elif self.sort.get() == "Transport Type Desc":
                query = query + " order by Transit_type desc"
            elif self.sort.get() == "Price Desc":
                query = query + " order by Price desc"
            else:
                query = query
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            queryc = "select transit_route,count(transit_route) from takes group by transit_route"
            self.cursor.execute(queryc)
            transits_logged = self.cursor.fetchall()
            logged = {}
            for t in transits_logged:
                logged[t[0]] = t[1]
            for transit in results:
                route = transit[0]
                type = transit[1]
                price = transit[2]
                queryb = "Select count(sitename) from connects where transitroute = '%s'" % (route)
                self.cursor.execute(queryb)
                connected = self.cursor.fetchone()
                self.tree.insert("", "end", values=(route, type, price, connected, logged[route]))

    def back_manage_transit(self):
        self.currGui.withdraw()
        if self.userType == "Employee, Visitor":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Employee":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Visitor":
            self.visitor_functionality()
            self.currGui = self.visitorGUI
        elif self.userType == "User":
            self.user_functionality()
            self.currGui = self.navGUI

    def create_transit(self):
        self.manageTranGui.withdraw()
        self.createTransit = Toplevel()
        self.prevGUI = self.currGui
        self.currGui = self.createTransit
        self.createTransit.title("Create Transit")

        Label(self.createTransit, text="Create Transit").grid(row=0)

        frame = Frame(self.createTransit)
        frame.grid()

        Label(frame, text="Transport Type").grid(row=0, column=0)
        self.transType = StringVar()
        choices_type = ['MARTA', 'Bus', 'Bike']
        self.transType.set('MARTA')
        self.popup = OptionMenu(frame, self.transType, *choices_type)
        self.popup.grid(row=0, column=1)

        Label(frame, text="Route").grid(row=0, column=2)
        self.route = StringVar()
        self.route_enter = Entry(frame, textvariable=self.route)
        self.route_enter.grid(row=0, column=3)

        Label(frame, text="Price").grid(row=0, column=4)
        self.price = IntVar()
        self.price_enter = Entry(frame, textvariable=self.price)
        self.price_enter.grid(row=0, column=5)

        query = "select sitename from site"
        self.cursor.execute(query)
        sites = self.cursor.fetchall()

        Label(frame, text="Connected Sites").grid(row=1, column=0)

        self.list = Listbox(frame, selectmode=MULTIPLE)
        for site in sites:
            self.list.insert('end', site[0])
        #list.insert(0, 'Atlanta Beltline Center')
        #list.insert(1, 'Gorden-White Park')
        #list.insert(2, 'Inman Park')
        self.list.grid(row=1, column=1)

        self.registerUser = Button(frame, text="Back", command=self.create_transit_back).grid(row=2, column=1)
        self.registerUser = Button(frame, text="Create", command=self.create_transit_btn).grid(row=2, column=2)

    def create_transit_back(self):
        self.currGui.withdraw()
        self.manageTranGui.deiconify()
        self.currGui = self.manageTranGui

    def create_transit_btn(self):
        if self.transType.get() == "":
            messagebox.showwarning("Transport Type", "Please select somthing for Transport Type")
        elif self.route.get() == "":
            messagebox.showwarning("Route", "Please enter a route")
        elif len(self.list.curselection()) == 0:
            messagebox.showwarning("Connected Sites", "Please select some sites for the transit to service")
        else:
            query = "Insert into Transit values('%s', '%s', '%s')" % (self.transType.get(), self.route.get(), str(self.price.get()))
            self.cursor.execute(query)
            indicies = self.list.curselection()
            for index in indicies:
                site = self.list.get(index)
                query = "Insert into Connects values('%s', '%s', '%s')" % (site, self.transType.get(), self.route.get())
                self.cursor.execute(query)
            self.db.commit()
            messagebox.showinfo("Success!!", "The Transit has been successfully created")
            self.currGui.withdraw()
            self.manage_transit()

    def edit_transit(self):
        if len(self.tree.selection()) == 0:
            messagebox.showwarning("Select Site", "Please select a site to edit")
        else:
            select = self.tree.item(self.tree.selection())
            route = select['values'][0]
            self.original_route = route
            self.type = select['values'][1]
            price = select['values'][2]
            self.manageTranGui.withdraw()
            self.editTransit = Toplevel()
            self.prevGUI = self.currGui
            self.currGui = self.editTransit
            self.editTransit.title("Edit Transit")

            Label(self.editTransit, text="Edit Transit").grid(row=0)

            frame = Frame(self.editTransit)
            frame.grid()

            Label(frame, text="Transport Type").grid(row=0, column=0)
            Label(frame, text=self.type).grid(row=0, column=1)

            Label(frame, text="Route").grid(row=0, column=2)
            self.route = StringVar()
            self.route.set(route)
            self.route_enter = Entry(frame, textvariable=self.route)
            self.route_enter.grid(row=0, column=3)

            Label(frame, text="Price").grid(row=0, column=4)
            self.price = IntVar()
            self.price.set(price)
            self.price_enter = Entry(frame, textvariable=self.price)
            self.price_enter.grid(row=0, column=5)

            Label(frame, text="Connected Sites").grid(row=1, column=0)

            query = "select sitename from site"
            self.cursor.execute(query)
            sites = self.cursor.fetchall()

            query = "select sitename from connects where transitroute= '%s'" % (route)
            self.cursor.execute(query)
            selected = self.cursor.fetchall()
            self.previously_selected = []

            self.list = Listbox(frame, selectmode=MULTIPLE)
            count = 0
            dict = {}
            for site in sites:
                self.list.insert(count, site[0])
                dict[site[0]] = count
                count = count + 1
            #list.insert(0, 'Atlanta Beltline Center')
            #list.insert(1, 'Gorden-White Park')
            #list.insert(2, 'Inman Park')
            self.list.grid(row=1, column=1)

            for site in selected:
                index = dict[site[0]]
                self.list.select_set(index)
                self.previously_selected.append(site[0])


            self.registerUser = Button(frame, text="Back", command=self.edit_transit_back).grid(row=2, column=1)
            self.registerUser = Button(frame, text="Update", command=self.edit_transit_btn).grid(row=2, column=2)

    def edit_transit_back(self):
        self.currGui.withdraw()
        self.manageTranGui.deiconify()
        self.currGui = self.manageTranGui

    def edit_transit_btn(self):
        query = "Update Transit set Transit_Route = '%s', Price = '%s' where Transit_Type = '%s' and Transit_Route = '%s'" % (self.route.get(), str(self.price.get()), self.type, self.original_route)
        self.cursor.execute(query)
        indices = self.list.curselection()
        currently_selected = []
        for index in indices:
            currently_selected.append(self.list.get(index))
        for index in indices:
            site = self.list.get(index)
            if site not in self.previously_selected:
                query = "Insert into Connects values('%s', '%s', '%s')" % (site, self.type, self.route.get())
                self.cursor.execute(query)
        for site in self.previously_selected:
            if site not in currently_selected:
                query = "Delete from Connects where TransitType = '%s' and Transitroute = '%s' and SiteName = '%s'" % (self.type, self.original_route, site)
                self.cursor.execute(query)
        self.db.commit()
        messagebox.showinfo("Success!!", "The transit has been edited")
        self.currGui.withdraw()
        self.manage_transit()

    def delete_transit(self):
        if len(self.tree.selection()) == 0:
            messagebox.showwarning("Select Transit", "Please select a transit to delete")
        else:
            select = self.tree.item(self.tree.selection())
            query = "Delete from transit where transit_route = '%s'" % (select["values"][0])
            self.cursor.execute(query)
            self.db.commit()
            self.tree.delete(self.tree.selection()[0])
            messagebox.showinfo("Success!!", "The Transit have been successfully deleted")

    def manage_site(self):
        self.currGui.withdraw()
        self.manageSiteGui = Toplevel()
        self.currGui = self.manageSiteGui
        self.manageSiteGui.title("Manage Site")

        Label(self.manageSiteGui, text="Manage Site").grid(row=0)

        frame = Frame(self.manageSiteGui)
        frame.grid()

        query = "Select Distinct SiteName from Site"
        self.cursor.execute(query)
        sites = self.cursor.fetchall()

        Label(frame, text="Site ").grid(row=0, column=0)
        self.site = StringVar()
        choices = []
        for site in sites:
            choices.append(site[0])
        choices.append('All')
        self.site.set("All")
        self.popupMenu = OptionMenu(frame, self.site, *choices)
        self.popupMenu.grid(row=0, column=1)

        query = "select concat(firstname,' ', lastname) from manager a  join normaluser b on a.username=b.username"
        self.cursor.execute(query)
        managers = self.cursor.fetchall()

        Label(frame, text="Manager ").grid(row=0, column=2)
        self.managers = StringVar()
        choices = []
        for manager in managers:
            choices.append(manager[0])
        choices.append('All')
        self.managers.set('All')
        self.popup = OptionMenu(frame, self.managers, *choices)
        self.popup.grid(row=0, column=3)

        Label(frame, text="Open Everyday ").grid(row=1, column=2)
        self.open = StringVar()
        choices_type = ['Yes', 'No', 'All']
        self.open.set('All')
        self.popup = OptionMenu(frame, self.open, *choices_type)
        self.popup.grid(row=1, column=3)

        Label(frame, text="Sort By: ").grid(row=1, column=4)
        self.sort = StringVar()
        choices = ['Name', 'Manager', 'Open Everyday', 'Name Desc','Manager Desc', 'Open Everyday Desc', 'None']
        self.sort.set('None')
        self.popup = OptionMenu(frame, self.sort, *choices)
        self.popup.grid(row=1, column = 5)

        self.filter = Button(frame, text="Filter", command=self.filter_manage_site).grid(row=2, column=0)

        self.create = Button(frame, text="Create", command=self.create_site).grid(row=2, column=1)
        self.edit = Button(frame, text='Edit', command=self.edit_site).grid(row=2, column=2)
        self.delete = Button(frame, text='Delete', command=self.delete_site).grid(row=2, column=3)

        frame_tree = Frame(self.manageSiteGui)
        frame_tree.grid()

        self.tree = ttk.Treeview(frame_tree, columns=['Name', 'Manager', 'Open Everyday'],
                            show='headings', selectmode='browse')

        self.tree.heading('Name', text='Name')
        self.tree.heading('Manager', text='Manager')
        self.tree.heading('Open Everyday', text='Open Everyday')
        #self.tree.insert("", "end", values=("1", "2", "3"))
        #self.tree.insert("", "end", values=("4", "5", "6"))
        self.tree.grid(row=1, column=3)

        frame_under = Frame(self.manageSiteGui)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_manage_site).grid(row=0, column=0)

    def filter_manage_site(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        if self.site.get() == 'All' and self.managers.get() == 'All' and self.open.get() == 'All':
            query = "SELECT sitename, concat(firstname,' ', lastname), openeveryday FROM Site a join normaluser b on a.managerID=b.username"
            if self.sort.get() == "Name":
                query = "SELECT sitename, concat(firstname,' ', lastname), openeveryday FROM Site a join normaluser b on a.managerID=b.username order by sitename"
            elif self.sort.get() == "Manager":
                query = "SELECT sitename, concat(firstname,' ', lastname), openeveryday FROM Site a join normaluser b on a.managerID=b.username order by concat(firstname,' ', lastname)"
            elif self.sort.get() == "Open Everyday":
                query = "SELECT sitename, concat(firstname,' ', lastname), openeveryday FROM Site a join normaluser b on a.managerID=b.username order by openeveryday"
            elif self.sort.get() == "Name Desc":
                query = "SELECT sitename, concat(firstname,' ', lastname), openeveryday FROM Site a join normaluser b on a.managerID=b.username order by sitename desc"
            elif self.sort.get() == "Manager Desc":
                query = "SELECT sitename, concat(firstname,' ', lastname), openeveryday FROM Site a join normaluser b on a.managerID=b.username order by concat(firstname,' ', lastname) desc"
            elif self.sort.get() == "Open Everyday Desc":
                query = "SELECT sitename, concat(firstname,' ', lastname), openeveryday FROM Site a join normaluser b on a.managerID=b.username order by openeveryday desc"
            else:
                query = "SELECT sitename, concat(firstname,' ', lastname), openeveryday FROM Site a join normaluser b on a.managerID=b.username"
            self.cursor.execute(query)
            sites = self.cursor.fetchall()
            for site in sites:
                name = site[0]
                manager = site[1]
                open = site[2]
                self.tree.insert("", "end", values=(name, manager, open))
        else:
            query = "SELECT sitename, concat(firstname,' ', lastname), openeveryday FROM Site a join normaluser b on a.managerID=b.username where "
            site = ""
            manager = ""
            open = ""
            if self.site.get() != "All":
                site = "SiteName = '" + self.site.get() + "'"
            if self.managers.get() != "All":
                manager = "concat(b.Firstname, ' ', b.LastName) = '" + self.managers.get() + "'"
                print(manager)
            if self.open.get() != 'All':
                open = "openeveryday = '" + self.open.get() + "'"
            if site != "":
                query = query + site
                if manager != "":
                    query = query + " and " + manager
                if open != "":
                    query = query + " and " + open
            elif manager != "":
                query = query + manager
                if open != "":
                    query = query + " and " + open
            else:
                query = query + open
            if self.sort.get() == "Name":
                query = query + " order by sitename"
            elif self.sort.get() == "Manager":
                query = query + " order by concat(firstname,' ', lastname)"
            elif self.sort.get() == "Open Everyday":
                query = query + " order by openeveryday"
            elif self.sort.get() == "Name Desc":
                query = query + " order by sitename desc"
            elif self.sort.get() == "Manager Desc":
                query = query + " order by concat(firstname,' ', lastname) desc"
            elif self.sort.get() == "Open Everyday Desc":
                query = query + " order by openeveryday desc"
            else:
                query = query
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            for site in results:
                name = site[0]
                manager = site[1]
                open = site[2]
                self.tree.insert("", "end", values=(name, manager, open))

    def delete_site(self):
        if len(self.tree.selection()) == 0:
            messagebox.showwarning("Select Site", "Please select a site to delete")
        else:
            select = self.tree.item(self.tree.selection())
            query = "Delete from Site where SiteName = '%s'" % (select["values"][0])
            self.cursor.execute(query)
            self.db.commit()
            self.tree.delete(self.tree.selection()[0])
            messagebox.showinfo("Success!!", "The Site have been successfully deleted")

    def back_manage_site(self):
        self.currGui.withdraw()
        if self.userType == "Employee, Visitor":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Employee":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Visitor":
            self.visitor_functionality()
            self.currGui = self.visitorGUI
        elif self.userType == "User":
            self.user_functionality()
            self.currGui = self.navGUI

    ###########################################################################
    def create_site(self):
        self.manageSiteGui.withdraw()
        self.createSite = Toplevel()
        self.prevGUI = self.currGui
        self.currGui = self.createSite
        self.createSite.title("Create Site")

        Label(self.createSite, text="Create Site").grid(row=0)

        frame = Frame(self.createSite)
        frame.grid()

        Label(frame, text="Name: ").grid(row=0, column=0)
        self.fname = StringVar()
        self.fname_enter = Entry(frame, textvariable=self.fname)
        self.fname_enter.grid(row=0, column=1)

        Label(frame, text="Zipcode: ").grid(row=0, column=2)
        self.zip = StringVar()
        self.zip_enter = Entry(frame, textvariable=self.zip)
        self.zip_enter.grid(row=0, column=3)

        Label(frame, text="Address: ").grid(row=1, column=0)
        self.address = StringVar()
        self.address_enter = Entry(frame, textvariable=self.address)
        self.address_enter.grid(row=1, column=1)

        query = "select concat(FirstName, ' ', Lastname) as 'Manager Name' from NormalUser join manager on manager.username = NormalUser.Username where concat(FirstName, ' ', Lastname) not in(select concat(FirstName, ' ', Lastname) as 'Manager Name' from NormalUser join site on site.managerID = NormalUser.Username)"
        self.cursor.execute(query)
        managers_other = self.cursor.fetchall()

        Label(frame, text="Manager: ").grid(row=2, column=0)
        self.manager = StringVar()
        choices = []
        for m in managers_other:
            choices.append(m[0])
        self.popup = OptionMenu(frame, self.manager, *choices)
        self.popup.grid(row=2, column=1)

        self.open = IntVar()
        Checkbutton(frame, text="Open Everyday", variable=self.open).grid(row=2, column=2)

        self.registerUser = Button(frame, text="Back", command=self.create_site_back).grid(row=4, column=1)
        self.registerUser = Button(frame, text="Create", command=self.create_site_btn).grid(row=4, column=2)

    def create_site_back(self):
        self.currGui.withdraw()
        self.manageSiteGui.deiconify()
        self.currGui = self.manageSiteGui

    def create_site_btn(self):
        if self.fname.get() == "":
            messagebox.showwarning("Name?", "Please enter a name for the site")
        elif self.zip.get() == "":
            messagebox.showwarning("Zipcode?", "Please enter a zipcode")
        elif self.manager.get() == "":
            messagebox.showwarning("Manager", "Please select a manager")
        else:
            open = ""
            if self.open.get() == 1:
                open = "Yes"
            else:
                open = "No"
            manager_query = "select username from normaluser where concat(firstname, ' ' , lastname)= '%s'" % (self.manager.get())
            self.cursor.execute(manager_query)
            managerid = self.cursor.fetchone()
            query = "Insert into Site set SiteName = '%s', Zipcode = '%s', Address = '%s', ManagerID = '%s', OpenEveryday = '%s'" % (self.fname.get(), self.zip.get(), self.address.get(), managerid[0], open)
            self.cursor.execute(query)
            self.db.commit()
            messagebox.showinfo("Success!", "The site was successfully inserted!")
            self.currGui.withdraw()
            self.manage_site()


    def edit_site(self):
        if len(self.tree.selection()) == 0:
            messagebox.showwarning("Select Site", "Please select a site to edit")
        else:
            select = self.tree.item(self.tree.selection())
            name = select['values'][0]
            manager = select['values'][1]
            open = select['values'][2]

            self.manageSiteGui.withdraw()
            self.editSite = Toplevel()
            self.prevGUI = self.currGui
            self.currGui = self.editSite
            self.editSite.title("Edit Site")

            Label(self.editSite, text="Edit Site").grid(row=0)

            frame = Frame(self.editSite)
            frame.grid()

            query = "Select address, zipcode from site where sitename= '%s'" % (name)
            self.cursor.execute(query)
            result = self.cursor.fetchone()

            self.name_original = name

            Label(frame, text="Name: ").grid(row=0, column=0)
            self.site = StringVar()
            self.site.set(name)
            self.site_enter = Entry(frame, textvariable=self.site)
            self.site_enter.grid(row=0, column=1)

            Label(frame, text="Zipcode: ").grid(row=0, column=2)
            self.zip = StringVar()
            if result[1] != None:
                self.zip.set(result[1])
            self.zip_enter = Entry(frame, textvariable=self.zip)
            self.zip_enter.grid(row=0, column=3)

            Label(frame, text="Address: ").grid(row=1, column=0)
            self.address = StringVar()
            if result[0] != None:
                self.address.set(result[0])
            self.address_enter = Entry(frame, textvariable=self.address)
            self.address_enter.grid(row=1, column=1)

            query = "select concat(Firstname, ' ', LastName) as 'Manager Name' from NormalUser join site on site.managerID = NormalUser.Username where sitename = '%s'" % (name)
            self.cursor.execute(query)
            managers = self.cursor.fetchone()
            manager_name = managers[0]

            query = "select concat(FirstName, ' ', Lastname) as 'Manager Name' from NormalUser join manager on manager.username = NormalUser.Username where concat(FirstName, ' ', Lastname) not in(select concat(FirstName, ' ', Lastname) as 'Manager Name' from NormalUser join site on site.managerID = NormalUser.Username)"
            self.cursor.execute(query)
            managers_other = self.cursor.fetchall()

            Label(frame, text="Manager: ").grid(row=2, column=0)
            self.manager = StringVar()
            choices = []
            choices.append(manager_name)
            for m in managers_other:
                choices.append(m[0])
            self.manager.set(manager_name)
            self.popup = OptionMenu(frame, self.manager, *choices)
            self.popup.grid(row=2, column=1)

            self.open = IntVar()
            if open == "Yes":
                self.open.set(1)
            else:
                self.open.set(0)
            Checkbutton(frame, text="Open Everyday", variable=self.open).grid(row=2, column=2)

            self.registerUser = Button(frame, text="Back", command=self.edit_site_back).grid(row=4, column=1)
            self.registerUser = Button(frame, text="Update", command=self.edit_site_btn).grid(row=4, column=2)

    def edit_site_back(self):
        self.currGui.withdraw()
        self.manageSiteGui.deiconify()
        self.currGui = self.manageSiteGui

    def edit_site_btn(self):
        open = ""
        if self.open.get() == 1:
            open = "Yes"
        else:
            open = "No"

        print(self.site.get())
        query_manager_id = "select username from normaluser where concat(firstname, ' ' , lastname)= '%s'" % (self.manager.get())
        self.cursor.execute(query_manager_id)
        id = self.cursor.fetchone()
        query = "Update Site set SiteName = '%s', Zipcode = '%s', Address = '%s', ManagerID = '%s', OpenEveryday = '%s' where SiteName = '%s'" % (self.site.get(), self.zip.get(), self.address.get(), id[0], open, self.name_original)
        self.cursor.execute(query)
        self.db.commit()
        messagebox.showinfo("Success!!", "The site has been edited")
        self.currGui.withdraw()
        self.manage_site()

    ###########################################################################
    def take_transit(self):
        self.currGui.withdraw()
        self.take_tran = Toplevel()
        self.currGui = self.take_tran
        self.take_tran.title("Take Transit")

        Label(self.take_tran, text="Take Transit").grid(row=0)

        frame = Frame(self.take_tran)
        frame.grid()

        query = "Select Distinct SiteName from Site"
        self.cursor.execute(query)
        sites = self.cursor.fetchall()

        Label(frame, text="Contain Site ").grid(row=0, column=0)
        self.destination = StringVar()
        choices = []
        for site in sites:
            choices.append(site[0])
        choices.append('All')
        self.destination.set("All")
        self.popupMenu = OptionMenu(frame, self.destination, *choices)
        self.popupMenu.grid(row=0, column=1)

        Label(frame, text="Transport Type ").grid(row=0, column=2)
        self.trans_type = StringVar()
        choices_type = ['MARTA', 'Bus', 'Bike', 'All']
        self.trans_type.set('All')
        self.popup = OptionMenu(frame, self.trans_type, *choices_type)
        self.popup.grid(row=0, column=3)

        Label(frame, text="Price Range ").grid(row=1, column=0)
        self.price_lower = IntVar()
        self.price_lower_enter = Entry(frame, textvariable=self.price_lower)
        self.price_lower_enter.grid(row=1, column=1)

        Label(frame, text=" -- ").grid(row=1, column=2)
        self.price_upper = IntVar()
        self.price_upper_enter = Entry(frame, textvariable=self.price_upper)
        self.price_upper_enter.grid(row=1, column=3)

        Label(frame, text="Sort By: ").grid(row=1, column=4)
        self.sort = StringVar()
        choices = ['Transport Type', 'Price', 'Transport Type Desc', 'Price Desc', 'None']
        self.sort.set('None')
        self.popup = OptionMenu(frame, self.sort, *choices)
        self.popup.grid(row=1, column = 5)

        self.filter = Button(frame, text="Filter", command=self.filter_take_trans).grid(row=1, column=6)

        frame_tree = Frame(self.take_tran)
        frame_tree.grid()

        self.tree = ttk.Treeview(frame_tree, columns=['Route', 'Transport Type', 'Price', '# Connected Sites'],
                            show='headings', selectmode='browse')

        self.tree.heading('Route', text='Route')
        self.tree.heading('Transport Type', text='Transport Type')
        self.tree.heading('Price', text='Price')
        self.tree.heading("# Connected Sites", text='# Connected Sites')
        self.tree.grid(row=1, column=3)

        frame_under = Frame(self.take_tran)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=0, column=0)

        Label(frame_under, text="Transit Date ").grid(row=0, column=2)
        self.date = StringVar()
        self.date_entry = Entry(frame_under, textvariable=self.date)
        self.date_entry.grid(row=0, column=3)

        self.log = Button(frame_under, text="Log Transit", command=self.log_transit).grid(row=0, column=4)

    ###########################################################################
    def OnDoubleClick(self):
        pass

    def onSingleClick(self):
        pass

    def filter_take_trans(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        if self.destination.get() == 'All' and self.trans_type.get() == 'All' and self.price_lower.get() == 0 and self.price_upper.get() == 0:
            query = ""
            if self.sort.get() == "Transport Type":
                query = "Select Transit_route, Transit_type, Price from Transit order by Transit_type"
            elif self.sort.get() == "Price":
                query = "Select Transit_route, Transit_type, Price from Transit order by Price"
            elif self.sort.get() == "Transport Type Desc":
                query = "Select Transit_route, Transit_type, Price from Transit order by Transit_type desc"
            elif self.sort.get() == "Price Desc":
                query = "Select Transit_route, Transit_type, Price from Transit order by Price desc"
            else:
                query = "Select Transit_route, Transit_type, Price from Transit"
            self.cursor.execute(query)
            transits = self.cursor.fetchall()
            for transit in transits:
                route = transit[0]
                type = transit[1]
                price = transit[2]
                queryb = "Select count(sitename) from connects where transitroute = '%s'" % (route)
                self.cursor.execute(queryb)
                connected = self.cursor.fetchone()
                self.tree.insert("", "end", values=(route, type, price, connected))
        else:
            query = "select distinct Transit_route, Transit_type, Price from transit join connects on transit.transit_route = connects.TransitRoute where "
            site = ""
            tran = ""
            price = ""
            if self.destination.get() != "All":
                site = "SiteName = '" + self.destination.get() + "'"
            if self.trans_type.get() != "All":
                tran = "TransitType = '" + self.trans_type.get() + "'"
            if self.price_upper.get() != 0 and self.price_lower.get() <= self.price_upper.get():
                price = price + "Price between '" + str(self.price_lower.get()) + "' and '" + str(self.price_upper.get()) + "'"
            if site != "":
                query = query + site
                if tran != "":
                    query = query + " and " + tran
                if price != "":
                    query = query + " and " + price
            elif tran != "":
                query = query + tran
                if price != "":
                    query = query + " and " + price
            else:
                query = query + price
            if self.sort.get() == "Transport Type":
                query = query + " order by Transit_type"
            elif self.sort.get() == "Price":
                query = query + " order by Price"
            elif self.sort.get() == "Transport Type Desc":
                query = query + " order by Transit_type desc"
            elif self.sort.get() == "Price Desc":
                query = query + " order by Price desc"
            else:
                query = query
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            for transit in results:
                route = transit[0]
                type = transit[1]
                price = transit[2]
                queryb = "Select count(sitename) from connects where transitroute = '%s'" % (route)
                self.cursor.execute(queryb)
                connected = self.cursor.fetchone()
                self.tree.insert("", "end", values=(route, type, price, connected))

    ###########################################################################
    def back_take_trans(self):
        self.currGui.withdraw()
        if self.userType == "Employee, Visitor":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Employee":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Visitor":
            self.visitor_functionality()
            self.currGui = self.visitorGUI
        elif self.userType == "User":
            self.user_functionality()
            self.currGui = self.navGUI

    ###########################################################################
    def log_transit(self):
        if self.date.get() == "":
            messagebox.showwarning("Date", "Please enter the date to log the transit")
        elif len(self.tree.selection()) == 0:
            messagebox.showwarning("Select Transit", "Please select a transit to log")
        else:
            select = self.tree.item(self.tree.selection())
            query = "Insert into Takes values('%s', '%s', '%s', '%s')" % (self.user.get(), select["values"][1], select["values"][0], self.date.get())
            self.cursor.execute(query)
            self.db.commit()
            messagebox.showinfo("Success!!", "Your Transit has been logged")


    def on_backbutton_clicked(self):
        self.currGui.withdraw()
        if self.userType == "Employee, Visitor":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Employee":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Visitor":
            self.visitor_functionality()
            self.currGui = self.visitorGUI
        elif self.userType == "User":
            self.user_functionality()
            self.currGui = self.navGUI

    def daily_detail(self):
        if len(self.site_tree.selection()) == 0:
            messagebox.showwarning("Select Site Report", "Please select a site report")
        else:
            self.currGui.withdraw()
            self.dailyDetailGUI = Toplevel()
            self.dailyDetailGUI.title("Daily Detail")

            Label(self.dailyDetailGUI, text="Daily Detail").grid(row=0)

            frame = Frame(self.dailyDetailGUI)
            frame.grid()

            frame_tree = Frame(self.dailyDetailGUI)
            frame_tree.grid()

            self.tree = ttk.Treeview(frame_tree, columns=['Event Name', 'Staff Names', 'Visits', 'Revenue ($)'],
                                show='headings', selectmode='browse')

            self.tree.heading('Event Name', text='Event Name')
            self.tree.heading('Staff Names', text='Staff Names')
            self.tree.heading('Visits', text='Visits')
            self.tree.heading("Revenue ($)", text='Revenue ($)')
            #self.tree.insert("", "end", values=("1", "2", "3", "4"))
            #self.tree.insert("", "end", values=("4", "5", "6", "7"))
            self.tree.grid(row=1, column=3)
            self.populate_daily_detail()

            frame_under = Frame(self.dailyDetailGUI)
            frame_under.grid()

            self.back = Button(frame_under, text="Back", command=self.daily_detail_back).grid(row=0, column=0)

    def populate_daily_detail(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        query = "select sitename from site where managerid = '%s'" % (self.user.get())
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        site = result[0]

        select = self.site_tree.item(self.site_tree.selection())
        date = select["values"][0]
        query = "select any_value(a.eventname) as Name , group_concat(distinct any_value(concat(firstname, ' ',lastname))) as Staff, count(dateattended) as Visits, (select (Select count(dateattended) from VisitEvent where sitename = '%s' and dateattended = '%s' group by dateattended)+(Select count(datevisited) from VisitSite where sitename= '%s' and datevisited = '%s' group by datevisited)), (any_value(price)*count(dateattended)) as Revenue from visitevent a join beltlineevent b on a.eventname= b.eventname and a.sitename = b.sitename and a.eventstartdate = b.startdate join view_staffnames s on s.eventname = a.eventname where a.dateattended = '%s' group by a.dateattended, a.eventname, a.sitename" % (site, date, site, date, date)
        self.cursor.execute(query)
        self.events = self.cursor.fetchall()
        for event in self.events:
            eventName = event[0]
            staffNames = event[1]
            visists = event[2]
            revenue = event[3]
            self.tree.insert("", "end", values=(eventName, staffNames, visists, revenue))





    def daily_detail_back(self):
        self.dailyDetailGUI.withdraw()
        self.site_report.deiconify()
        self.currGui = self.site_report

    def view_schedule(self):
        self.currGui.withdraw()
        self.view_sched_gui = Toplevel()
        self.currGui = self.view_sched_gui
        self.view_sched_gui.title("View Schedule")

        Label(self.view_sched_gui, text="View Schedule").grid(row=0)

        frame = Frame(self.view_sched_gui)
        frame.grid()

        Label(frame, text="Event Name").grid(row=1, column=1)
        self.event_name = StringVar()
        self.event_name_enter = Entry(frame, textvariable=self.event_name)
        self.event_name_enter.grid(row=1, column=2)

        Label(frame, text="Description Keyword").grid(row=1, column=3)
        self.desc_key = StringVar()
        self.desc_key_enter = Entry(frame, textvariable=self.desc_key)
        self.desc_key_enter.grid(row=1, column=4)

        Label(frame, text="Start Date").grid(row=2, column=1)
        self.start_date = StringVar()
        self.start_date_enter = Entry(frame, textvariable=self.start_date)
        self.start_date_enter.grid(row=2, column=2)

        Label(frame, text="End Date").grid(row=2, column=3)
        self.end_date = StringVar()
        self.end_date_enter = Entry(frame, textvariable=self.end_date)
        self.end_date_enter.grid(row=2, column=4)

        self.filter = Button(frame, text="Filter", command=self.filter_view_schedule).grid(row=3, column=2)
        self.view_event = Button(frame, text="View Event", command=self.staff_event_detail).grid(row=3, column=4)



        frame_tree = Frame(self.view_sched_gui)
        frame_tree.grid()

        self.tree = ttk.Treeview(frame_tree, columns=['Event Name', 'Site Name', 'Start Date', 'End Date', 'Staff Count'],
                            show='headings', selectmode='browse')

        self.tree.heading('Event Name', text='Event Name')
        self.tree.heading('Site Name', text='Site Name')
        self.tree.heading('Start Date', text='Start Date')
        self.tree.heading('End Date', text='End Date')
        self.tree.heading('Staff Count', text='Staff Count')
        #self.tree.insert("", "end", values=("1", "2", "3", "4", "0"))
        #self.tree.insert("", "end", values=("4", "5", "6", "7", "0"))
        self.tree.grid(row=1, column=3)
        self.tree.bind('<ButtonRelease-1>', self.selectItem)

        self.selection = self.tree.item(self.tree.focus())
        print(self.selection)

        frame_under = Frame(self.view_sched_gui)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_view_schedule).grid(row=0, column=0)

    def selectItem(self, event):
        curItem = self.tree.item(self.tree.focus())
        col = self.tree.identify_column(event.x)
        curItem.values()
        items = curItem.get("values")
        self.eventDetailName = items[0]
        self.siteDetailName = items[1]
        self.startDetailDate = items[2]
        self.endDetailDate = items[3]
        self.staffDetailCount = items[4]

        query = "Select eventname, sitename, startdate, enddate, (enddate-startdate) as duration, capacity, price, eventdesc from beltlineevent where eventname = \'" + self.eventDetailName + "\' and startdate = \'" + self.startDetailDate + "\'"
        self.cursor.execute(query)

        self.eventName = ""
        self.siteName = ""
        self.startDate = ""
        self.endDate = ""
        self.duration = ""
        self.capacity = ""
        self.price = ""
        self.detailDesc = ""

        for self.item in self.cursor.fetchall():
            self.eventName = self.item[0]
            self.siteName = self.item[1]
            self.startDate = self.item[2]
            self.endDate = self.item[3]
            self.duration = self.item[4]
            self.capacity = self.item[5]
            self.price = self.item[6]
            self.detailDesc = self.item[7]

    def staff_event_detail(self):
        self.currGui.withdraw()
        self.event_detail = Toplevel()
        self.currGui = self.event_detail
        self.event_detail.title("Event Detail")

        Label(self.event_detail, text="Event Detail").grid(row=0)

        frame = Frame(self.event_detail)
        frame.grid()

        Label(frame, text="Event: ").grid(row=0, column=0)
        self.eventName = self.eventDetailName
        Label(frame, text=self.eventName).grid(row=0, column=1)

        Label(frame, text="Site: ").grid(row=0, column=2)
        self.siteName = self.siteDetailName
        Label(frame, text=self.siteName).grid(row=0, column=3)

        Label(frame, text="Start Date: ").grid(row=1, column=0)
        self.startDate = self.startDetailDate
        Label(frame, text=self.startDate).grid(row=1, column=1)

        Label(frame, text="End Date: ").grid(row=1, column=2)
        self.endDate = self.endDetailDate
        Label(frame, text=self.endDate).grid(row=1, column=3)

        Label(frame, text="Duration Days: ").grid(row=1, column=4)
        start = [x.strip() for x in self.startDetailDate.split('-')]
        end = [x.strip() for x in self.endDetailDate.split('-')]
        startd = datetime.datetime(int(start[0], 10), int(start[1], 10), int(start[2], 10))
        endd = datetime.datetime(int(end[0], 10), int(end[1], 10), int(end[2], 10))
        duration = endd - startd
        self.durationDays = duration.__str__()
        Label(frame, text=self.durationDays).grid(row=1, column=5)

        self.staffsAssigned = ""
        query = "Select concat(FirstName,\" \", Lastname) as Name from NormalUser join staffassigned where NormalUser.Username=staffassigned.employee_id and EventName = \'" + self.eventDetailName +"\' and EventStartDate = \'" + self.startDetailDate + "\'"
        self.cursor.execute(query)
        staffList = self.cursor.fetchall()
        for staff in staffList:
            self.staffsAssigned = self.staffsAssigned + staff[0] + ", "

        Label(frame, text="Staffs Assigned: ").grid(row=2, column=0)
        Label(frame, text=self.staffsAssigned).grid(row=2, column=1)

        Label(frame, text="Capacity: ").grid(row=2, column=2)
        self.capacity = self.capacity
        Label(frame, text=self.capacity).grid(row=2, column=3)

        Label(frame, text="Price:  ").grid(row=2, column=4)
        self.price = self.price
        Label(frame, text=self.price).grid(row=2, column=5)


        Label(frame, text="Description:  ").grid(row=3, column=0)
        self.description = StringVar()
        self.desc = Text(frame, height=7)
        self.scroll = Scrollbar(frame, orient='vertical')
        self.desc.grid(row=3, column=1, pady=4)
        frame.columnconfigure(1, weight=1)
        self.desc.insert(END, self.detailDesc)
        self.scroll.config(command=self.desc.yview)
        self.desc.config(yscrollcommand=self.scroll.set)

        self.registerUser = Button(frame, text="Back", command=self.event_detail_back).grid(row=6, column=1)



    #TODO Get Staff Count (defaulting to 1)
    def filter_view_schedule(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        '''
        # Every thing is Blank
        if self.event_name == "" and self.desc_key == "" and self.start_date == "" and self.end_date == "":
            query = "Select a.eventname, a.sitename, a.startdate,a.enddate from beltlineevent a"
            self.cursor.execute(query)
            self.sched = self.cursor.fetchall()
            for sched in self.sched:
                eventName = sched[0]
                siteName = sched[1]
                startDate = sched[2]
                endDate = sched[3]
                self.tree.insert("", "end", values = (eventName, siteName, startDate, endDate, "1"))

        '''

        eventName = self.event_name.get()
        descKeyWord = self.desc_key.get()
        startDate = self.start_date.get()
        endDate = self.end_date.get()
        query = "Select a.eventname, a.sitename, a.startdate, a.enddate from beltlineevent a"

        #Eventname is Not Empty and Another
        if eventName != "" and descKeyWord != "" and startDate == "" and endDate == "":
            query = query + " where eventname = \'" + eventName + "\' and eventdesc LIKE \'%" + descKeyWord + "%\'"
        elif eventName != "" and startDate != "" and descKeyWord == "" and endDate == "":
            query = query + " where eventname = \'" + eventName + "\' and startdate > \'" + startDate + "\'"
        elif eventName != "" and endDate != "" and descKeyWord == "" and startDate == "":
            query = query + " where eventname = \'" + eventName + "\' and enddate < \'" + endDate + "\'"

        #Eventname, Desc Not Empty
        elif eventName != "" and descKeyWord != "" and startDate != "" and endDate == "":
            query = query + " where eventname = \'" + eventName + "' and eventdesc LIKE \'%" + descKeyWord + "%\'" + " and startdate > \'" + startDate + "\'"
        elif eventName != "" and descKeyWord != "" and endDate != "" and startDate == "":
            query = query + " where eventname = \'" + eventName + "\' and eventdesc LIKE \'%" + descKeyWord + "%\'" + " and enddate < \'" + endDate + "\'"

        #Eventname, StartDate Not Empty
        elif descKeyWord != "" and startDate != "" and eventName == "" and endDate == "":
            query = query + " where eventdesc LIKE \'%" + descKeyWord + "%\'" + " and startdate > \'" + startDate + "\'"
        elif descKeyWord != "" and endDate != "" and eventName == "" and startDate == "":
            query = query + " where eventdesc LIKE \'%" + descKeyWord + "%\'" + " and enddate < \'" + endDate + "\'"

        elif startDate != "" and endDate != "" and eventName == "" and descKeyWord == "":
            query = query + " where startdate > \'" + startDate + "\'" + " and enddate < \'" + endDate + "\'"

        elif eventName != "" and startDate != "" and endDate != "" and descKeyWord == "":
            query = query + " where eventname = \'" + eventName + "\' and startdate > \'" + descKeyWord + "\'" + " and enddate < \'" + endDate + "\'"

        elif eventName == "" and descKeyWord == "" and startDate == "" and endDate == "":
            query = query + " where "
        elif eventName != "":
            query = query + " where a.eventname = \'" + eventName + "\'"
        elif descKeyWord != "":
            query = query + " where a.eventdesc LIKE \'%" + descKeyWord + "%\'"
        elif startDate != "":
            query = query + " where a.startdate > \'" + startDate + "\'"
        elif endDate != "":
            query = query + " where a.enddate < \'" + endDate + "\'"

        self.cursor.execute(query)
        startd = None
        endd = None
        greater = False
        self.sched = self.cursor.fetchall()
        for sched in self.sched:
            eventName = sched[0]
            siteName = sched[1]
            startDate = sched[2]
            endDate = sched[3]

            if self.start_date.get() != "" and self.end_date.get() != "":  # and self.start_date.get() <= self.end_date.get():
                start = [x.strip() for x in self.start_date.get().split('-')]
                end = [x.strip() for x in self.end_date.get().split('-')]
                startd = datetime.datetime(int(start[0], 10), int(start[1], 10), int(start[2], 10))
                endd = datetime.datetime(int(end[0], 10), int(end[1], 10), int(end[2], 10))
            if startd != None and endd != None:
                if startd > endd:
                    greater = True
            if greater == True:
                messagebox.showwarning("Date", "The start date must be before the end date")
            else:
                self.tree.insert("", "end", values=(eventName, siteName, startDate, endDate, 1))


    def back_view_schedule(self):
        self.currGui.withdraw()
        if self.userType == "Employee, Visitor":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Employee":
            if self.UserSubtype == "Staff":
                self.staff_only_functionality()
                self.currGui = self.staffOnlyGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Visitor":
            self.visitor_functionality()
            self.currGui = self.visitorGUI
        elif self.userType == "User":
            self.user_functionality()
            self.currGui = self.navGUI



    def event_detail_back(self):
        self.currGui.withdraw()
        self.view_sched_gui.deiconify()
        self.currGui = self.view_sched_gui

    def visit_explore_event(self):
        self.currGui.withdraw()
        self.visit_explore_event_gui = Toplevel()
        self.currGui = self.visit_explore_event_gui
        self.visit_explore_event_gui.title("Explore Event")

        Label(self.visit_explore_event_gui, text="Explore Event").grid(row=0)

        frame = Frame(self.visit_explore_event_gui)
        frame.grid()

        Label(frame, text="Name: ").grid(row=0, column=0)
        self.name = StringVar()
        self.name_enter = Entry(frame, textvariable=self.name)
        self.name_enter.grid(row=0, column=1)

        Label(frame, text="Description Keyword: ").grid(row=0, column=2)
        self.desc = StringVar()
        self.desc_enter = Entry(frame, textvariable=self.desc)
        self.desc_enter.grid(row=0, column=3)

        Label(frame, text = "Site Name: ").grid  (row = 1, column = 0)
        self.site_name = StringVar()
        choices = ["MARTA", "Bus", "Bike", "-- ALL --"]
        self.site_name.set("-- ALL --")
        self.popupMenu = OptionMenu(frame, self.site_name, *choices)
        self.popupMenu.grid(row=1, column=1)

        Label(frame, text="Sort By: ").grid(row=1, column=2)
        self.sort = StringVar()
        choices = ['Event Name', 'Site Name', 'Ticket Price', 'Ticket Remaining', 'Total Visits', 'My Visits']
        self.sort.set('None')
        self.popup = OptionMenu(frame, self.sort, *choices)
        self.popup.grid(row=1, column=3)

        Label(frame, text="Start Date: ").grid(row=2, column=0)
        self.start_date_explore = StringVar()
        self.start_date_explore_enter = Entry(frame, textvariable=self.start_date_explore)
        self.start_date_explore_enter.grid(row=2, column=1)

        Label(frame, text="End Date: ").grid(row=2, column=2)
        self.end_date_explore = StringVar()
        self.end_date_explore_enter = Entry(frame, textvariable=self.end_date_explore)
        self.end_date_explore_enter.grid(row=2, column=3)

        Label(frame, text="Total Visits Range").grid(row=3, column=0)
        self.visits_count_lower = IntVar()
        self.visits_count_lower_enter = Entry(frame, textvariable=self.visits_count_lower)
        self.visits_count_lower_enter.grid(row=3, column=1)

        Label(frame, text=" -- ").grid(row=3, column=2)
        self.visits_count_upper = IntVar()
        self.visits_count_upper_enter = Entry(frame, textvariable=self.visits_count_upper)
        self.visits_count_upper_enter.grid(row=3, column=3)

        Label(frame, text="Ticket Price Range").grid(row=3, column=4)
        self.ticket_price_lower = IntVar()
        self.ticket_price_lower_enter = Entry(frame, textvariable=self.ticket_price_lower)
        self.ticket_price_lower_enter.grid(row=3, column=5)

        Label(frame, text=" -- ").grid(row=3, column=6)
        self.ticket_price_upper = IntVar()
        self.ticket_price_upper_enter = Entry(frame, textvariable=self.ticket_price_upper)
        self.ticket_price_upper_enter.grid(row=3, column=7)

        include_visited_var = IntVar()
        Checkbutton(frame, text="Include Visited", var = include_visited_var).grid(row = 4, column = 3)

        include_soldout_var = IntVar()
        Checkbutton(frame, text="Include Sold Out Event", var=include_soldout_var).grid(row=4, column=4)

        self.filter = Button(frame, text="Filter", command=self.filter_explore_event).grid(row = 5, column=0)
        self.eventdetail = Button(frame, text="Event Detail", command=self.visitor_event_detail).grid(row=5, column=1)

        frame_tree = Frame(self.visit_explore_event_gui)
        frame_tree.grid()

        self.tree = ttk.Treeview(frame_tree, columns=['Event Name', 'Site Name', 'Ticket Price', 'Tickets Remaining',
                                                 'Total Visits', 'My Visits', 'Start Date'],
                            show='headings', selectmode='browse')

        self.tree.heading('Event Name', text='Event Name')
        self.tree.heading('Site Name', text='Site Name')
        self.tree.heading('Ticket Price', text='Ticket Price')
        self.tree.heading('Tickets Remaining', text='Tickets Remaining')
        self.tree.heading('Total Visits', text='Total Visits')
        self.tree.heading('My Visits', text='My Visits')
        self.tree.heading('Start Date', text="Start Date")
        #self.tree.insert("", "end", values=("1", "2", "3", "4", "0", "0"))
        #self.tree.insert("", "end", values=("4", "5", "6", "7", "0", "0"))
        self.tree.grid(row=4, column=3)
        self.tree.bind('<ButtonRelease-1>', self.visit_explore_event_selection)

        self.selection = self.tree.item(self.tree.focus())
        print(self.selection)

        frame_under = Frame(self.visit_explore_event_gui)
        frame_under.grid()

        self.registerUser = Button(frame_under, text="Back", command=self.back_explore_event).grid(row=6, column=3)




    #TODO Fix this. Tbh i dont know wtf is going on here
    def filter_explore_event(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        queryOne = "select b.eventname, b.sitename, b.price, b.startdate from beltlineevent b"
        queryTotalVisits = "select eventname, count(dateattended) from visitevent group by eventname, sitename, eventstartdate"
        queryTixRemain = "Select event, (capacity-visits) as tickets_remaining from tickets_remaining"
        #queryMyVisits = "select eventname, username, count(dateattended) from visitevent group by username, eventname, sitename where username = \'" + self.username.get() + "\'"

        self.cursor.execute(queryOne)
        #self.cursor.execute(queryTotalVisits)
        #self.cursor.execute(queryTixRemain)

        for i in self.tree.get_children():
            self.tree.delete(i)
        if self.name.get() == ''and self.desc.get() == "" and self.site_name.get() == "-- ALL --" and self.start_date_explore.get() == "" and self.end_date_explore.get() == "": #and self.visits_count_lower.get() == ""# and self.visits_count_upper.get() == "" and self.ticket_price_lower.get() == "" and self.ticket_price_upper.get() == "":
            query = "select b.eventname, b.sitename, b.price, b.startdate from beltlineevent b"
            if self.sort.get() == "Event Name":
                query = "select b.eventname, b.sitename, b.price, b.startdate from beltlineevent b order by eventname"
                queryTotalVisits = "select eventname, count(dateattended) from visitevent group by eventname, sitename, eventstartdate order by eventname"
                queryTixRemain = "Select event, (capacity-visits) as tickets_remaining from tickets_remaining order by eventname"
                queryMyVisits = "select eventname, username, count(dateattended) from visitevent group by username, eventname, sitename where username = \'" + self.username.get() + "\' order by eventname"
            elif self.sort.get() == "Site Name":
                query = "select b.eventname, b.sitename, b.price from beltlineevent b order by sitename"
                queryTotalVisits = "select eventname, count(dateattended) from visitevent group by eventname, sitename, eventstartdate order by sitename"
                queryTixRemain = "Select event, (capacity-visits) as tickets_remaining from tickets_remaining order by sitename"
            elif self.sort.get() == "Ticket Price":
                query = "select b.eventname, b.sitename, b.price from beltlineevent b order by price"
                queryTotalVisits = "select eventname, count(dateattended) from visitevent group by eventname, sitename, eventstartdate order by price"
                queryTixRemain = "Select event, (capacity-visits) as tickets_remaining from tickets_remaining order by price"
            self.cursor.execute(query)
            events = self.cursor.fetchall()
            self.cursor.execute(queryTotalVisits)
            totalVisits = self.cursor.fetchall()
            self.cursor.execute(queryTixRemain)
            tixRemain = self.cursor.fetchall()
            #self.cursor.execute(queryMyVisits)
            #myVis = self.cursor.fetchall()
            cnt = 0
            for event in events:
                eventName = event[0]
                siteName = event[1]
                tixPrice = event[2]
                queryTotalVisits= "select eventname, count(dateattended), eventstartdate from visitevent where eventname = \'" + eventName + "\' group by eventname, sitename, eventstartdate order by eventname"
                self.cursor.execute(queryTotalVisits)
                #totalVisits = self.cursor.fetchone()[1]
                visits = self.cursor.fetchone()
                totalVisits = visits[1]
                startdate = visits[2]
                self.exploreStartDate = event[3]
                queryTixRemaining = "Select event, (capacity-visits) as tickets_remaining from tickets_remaining where event = '%s'" % (eventName)
                self.cursor.execute(queryTixRemaining)
                tixRemaining = self.cursor.fetchone()[1]
                queryMyVis = "select eventname, username, count(dateattended) from visitevent where username = \'" + self.user.get() + "\' and eventname = \'" + eventName + "\' group by username, eventname, sitename order by eventname"
                self.cursor.execute(queryMyVis)
                #myVis = self.cursor.fetchone()[2]
                vis = self.cursor.fetchone()
                if vis == None:
                    self.tree.insert("", "end", values=(eventName, siteName, tixPrice, totalVisits, totalVisits, 0, startdate))
                else:
                    myVis = vis[2]
                    self.tree.insert("", "end", values=(eventName, siteName, tixPrice, totalVisits, totalVisits, myVis, startdate))


                #totalVisitsVar = totalVisits[cnt]
                #tixRemaining = tixRemain[cnt]
                #myVis[cnt]
                #self.tree.insert("", "end", values=(eventName, siteName, tixPrice, self.exploreStartDate, "1", "1"))
                cnt = cnt + 1
        else:
            query =""
            site = ""
            trans = ""
            route = ""
            date = ""
            startd = None
            endd = None
            greater = False
            if self.start_date.get() != "" and self.end_date.get() != "":  # and self.start_date.get() <= self.end_date.get():
                start = [x.strip() for x in self.start_date.get().split('-')]
                end = [x.strip() for x in self.end_date.get().split('-')]
                startd = datetime.datetime(int(start[0], 10), int(start[1], 10), int(start[2], 10))
                endd = datetime.datetime(int(end[0], 10), int(end[1], 10), int(end[2], 10))
            if startd != None and endd != None:
                if startd > endd:
                    greater = True
            if greater == True:
                messagebox.showwarning("Date", "The start date must be before the end date")
            elif self.start_date.get() == "" and self.end_date.get() != "":
                messagebox.showwarning("Date", "There must be a start and end date. They can be the same date")
            elif self.start_date.get() != "" and self.end_date.get() == "":
                messagebox.showwarning("Date", "There must be a start and end date. They can be the same date")
            else:
                pass

    def back_explore_event(self):
        self.currGui.withdraw()
        if self.userType == "Employee, Visitor":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Employee":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Visitor":
            self.visitor_functionality()
            self.currGui = self.visitorGUI
        elif self.userType == "User":
            self.user_functionality()
            self.currGui = self.navGUI

    def visit_explore_event_selection(self, event):
        curItem = self.tree.item(self.tree.focus())
        col = self.tree.identify_column(event.x)
        curItem.values()
        items = curItem.get("values")
        self.exploreEventName = items[0]
        self.exploreStartDate = items[2]

        query = "select b.eventname, b.sitename, b.startdate, b.enddate ,b.price, b.eventdesc from beltlineevent b where eventname = \'" + self.exploreEventName + "\' and startdate = \'" + self.exploreStartDate + "\'"
        self.cursor.execute(query)

        self.exploreEventName = ""
        self.exploreEventSiteName = ""
        self.exploreEventStartDate = ""
        self.exploreEventEndDate = ""
        self.exploreEventPrice = ""
        self.exploreEventDesc = ""

        for self.item in self.cursor.fetchall():
            self.exploreEventName = self.item[0]
            self.exploreEventSiteName = self.item[1]
            self.exploreEventStartDate = self.item[2]
            self.exploreEventEndDate = self.item[3]
            self.exploreEventPrice = self.item[4]
            self.exploreEventDesc = self.item[5]

    def visitor_event_detail(self):
        if len(self.tree.selection()) == 0:
            messagebox.showwarning("Select Event", "Please select an event to view")
        else:
            self.currGui.withdraw()
            self.event_detail = Toplevel()
            self.currGui = self.event_detail
            self.event_detail.title("Event Detail")

            select = self.tree.item(self.tree.selection())
            name = select["values"][0]
            self.name_ = name
            site = select["values"][1]
            self.site_ = site
            price = select["values"][2]
            remaining = select["values"][3]
            self.remaining_ = remaining
            startdate = select["values"][6]
            self.startdate_ = startdate

            Label(self.event_detail, text="Event Detail").grid(row=0)

            frame = Frame(self.event_detail)
            frame.grid()

            Label(frame, text="Event: ").grid(row=0, column=0)
            Label(frame, text = name).grid(row=0, column=1)

            Label(frame, text="Site: ").grid(row=0, column=2)
            self.site = "Temp Site"
            Label(frame, text = site).grid(row=0, column=3)

            Label(frame, text="Start Date: ").grid(row=1, column=0)
            Label(frame, text = startdate).grid(row=1, column=1)

            query = "select enddate, eventdesc from beltlineevent where eventname = '%s' and sitename = '%s' and startdate = '%s'" % (name, site, startdate)
            self.cursor.execute(query)
            results = self.cursor.fetchone()
            enddate = results[0]
            desc = results[1]

            Label(frame, text="End Date: ").grid(row=1, column=2)
            Label(frame, text = enddate).grid(row=1, column=3)


            Label(frame, text="Ticket Price ($): ").grid(row=2, column=0)
            Label(frame, text = price).grid(row=2, column=1)

            Label(frame, text="Tickets Remaining: ").grid(row=2, column=2)
            Label(frame, text = remaining).grid(row=2, column=3)


            Label(frame, text="Description:  ").grid(row=3, column=0)
            self.description = StringVar()
            self.desc = Text(frame,height=7)
            self.scroll = Scrollbar(frame, orient='vertical')
            self.desc.grid(row=3,column=1,pady=4)
            frame.columnconfigure(1,weight=1)
            self.desc.insert(END, desc)
            self.scroll.config(command=self.desc.yview)
            self.desc.config(yscrollcommand=self.scroll.set)

            Label(frame, text="Visit Date:  ").grid(row=4, column=0)
            self.visit_date = StringVar()
            self.visit_date_enter = Entry(frame, textvariable=self.visit_date)
            self.visit_date_enter.grid(row=4, column=1)

            self.registerUser = Button(frame, text="Log Visit", command=self.event_detail_log_visit).grid(row=6, column=1)
            self.registerUser = Button(frame, text="Back", command=self.visitor_event_detail_back).grid(row=6, column=2)



    def event_detail_log_visit(self):
        if self.visit_date.get() == "":
            messagebox.showwarning("Date", "Please enter a visit date")
        elif self.remaining_ == 0:
            messagebox.showwarning("Cannot Log Visit", "This event has 0 tickets remaining")
        else:
            query = "Insert into VisitEvent values('%s', '%s', '%s', '%s', '%s')" % (self.user.get(), self.name_, self.startdate_, self.site_, self.visit_date.get())
            print(query)
            self.cursor.execute(query)
            self.db.commit()
            messagebox.showinfo("Success!", 'The visit has been logged')
            self.currGui.withdraw()
            self.visitor_explore_event()

    def visitor_event_detail_back(self):
        self.currGui.withdraw()
        self.visit_explore_event_gui.deiconify()
        self.currGui = self.visit_explore_event_gui

    def visitor_explore_site(self):
        self.currGui.withdraw()
        self.explore_site = Toplevel()
        self.currGui = self.explore_site
        self.explore_site.title("Explore Site")

        Label(self.explore_site, text="Explore Site").grid(row=0)

        frame = Frame(self.explore_site)
        frame.grid()

        query = "Select Distinct SiteName from Site"
        self.cursor.execute(query)
        sites = self.cursor.fetchall()

        Label(frame, text="Name: ").grid(row=0, column=0)
        self.name = StringVar()
        choices = []
        for site in sites:
            choices.append(site[0])
        choices.append('All')
        self.name.set('All')
        self.popup = OptionMenu(frame, self.name, *choices)
        self.popup.grid(row=0, column=1)

        Label(frame, text="Open Everyday: ").grid(row=0, column=2)
        self.open = StringVar()
        choices_type = ['Yes','No', 'All']
        self.open.set('All')
        self.popup = OptionMenu(frame, self.open, *choices_type)
        self.popup.grid(row=0, column=3)

        Label(frame, text="Start Date: ").grid(row=1, column=0)
        self.start_date_detail = StringVar()
        self.start_date_detail_enter = Entry(frame, textvariable=self.start_date_detail)
        self.start_date_detail_enter.grid(row=1, column=1)

        Label(frame, text="End Date: ").grid(row=1, column=2)
        self.end_date_detail = StringVar()
        self.end_date_detail_enter = Entry(frame, textvariable=self.end_date_detail)
        self.end_date_detail_enter.grid(row=1, column=3)

        Label(frame, text="Total Visits Range").grid(row=2, column=0)
        self.visits_count_lower = IntVar()
        self.visits_count_lower_enter = Entry(frame, textvariable=self.visits_count_lower)
        self.visits_count_lower_enter.grid(row=2, column=1)

        Label(frame, text=" -- ").grid(row=2, column=2)
        self.visits_count_upper = IntVar()
        self.visits_count_upper_enter = Entry(frame, textvariable=self.visits_count_upper)
        self.visits_count_upper_enter.grid(row=2, column=3)

        Label(frame, text="Event Count Range").grid(row=2, column=4)
        self.event_count_lower = IntVar()
        self.event_count_lower_enter = Entry(frame, textvariable=self.event_count_lower)
        self.event_count_lower_enter.grid(row=2, column=5)

        Label(frame, text=" -- ").grid(row=2, column=6)
        self.event_count_upper = IntVar()
        self.event_count_upper_enter = Entry(frame, textvariable=self.event_count_upper)
        self.event_count_upper_enter.grid(row=2, column=7)


        include_visited_var = IntVar()
        Checkbutton(frame, text="Include Visited", var=include_visited_var).grid(row=3, column=3)

        self.filter = Button(frame, text="Filter", command=self.filter_explore_site).grid(row=4, column=2)
        self.filter = Button(frame, text="Site Detail", command=self.site_detail).grid(row=4, column=4)
        self.filter = Button(frame, text="Transit Detail", command=self.transit_detail).grid(row=4, column=5)

        frame_tree = Frame(self.explore_site)
        frame_tree.grid()

        self.tree = ttk.Treeview(frame_tree, columns=['Site Name', 'Event Count', 'Total Visits', 'My Visits'],
                            show='headings', selectmode='browse')

        self.tree.heading('Site Name', text='Site Name')
        self.tree.heading('Event Count', text='Event Count')
        self.tree.heading('Total Visits', text = 'Total Visits')
        self.tree.heading('My Visits', text = 'My Visits')
        #self.tree.insert("", "end", values=("1", "2", "0", "0"))
        #self.tree.insert("", "end", values=("4", "5", "0", "0"))
        self.tree.grid(row=1, column=3)

        frame_under = Frame(self.explore_site)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_explore_site).grid(row=0, column=0)

    def filter_explore_site(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        if self.name.get() == "All" and self.open.get() == 'All' and self.start_date_detail.get() == "" and self.end_date_detail.get() == "" and self.visits_count_lower.get() == 0 and self.visits_count_upper.get() == 0 and self.event_count_lower.get() == 0 and self.event_count_upper.get() == 0:
            sitename = "Select distinct sitename from site"
            eventcount = "select beltlineevent.sitename, count(eventname) from beltlineevent group by sitename"
            visits = "select sitename, count(datevisited) from visitsite group by sitename"
            my_visits = "select sitename, count(datevisited) from visitsite group by sitename, username"
            self.cursor.execute(sitename)
            sites = self.cursor.fetchall()
            self.cursor.execute(eventcount)
            events = self.cursor.fetchall()
            event = {}
            for e in events:
                event[e[0]] = e[1]
            self.cursor.execute(visits)
            visit = self.cursor.fetchall()
            total_visits = {}
            for v in visit:
                total_visits[v[0]] = v[1]
            self.cursor.execute(my_visits)
            myvis = self.cursor.fetchall()
            vis = {}
            for v in myvis:
                vis[v[0]] = v[1]
            for site in sites:
                name = site[0]
                event_count = 0
                if name in event:
                    event_count = event[name]
                total_vis = 0
                if name in total_visits:
                    total_vis = total_visits[name]
                my_vis = 0
                if name in vis:
                    my_vis = vis[name]
                self.tree.insert("", "end", values=(name, event_count, total_vis, my_vis))

    def back_explore_site(self):
        self.currGui.withdraw()
        if self.userType == "Employee, Visitor":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Visitor":
            self.visitor_functionality()
            self.currGui = self.visitorGUI


    def transit_detail(self):
        if len(self.tree.selection()) == 0:
            messagebox.showwarning("Select a Site", "Please select a site to view transit detail")
        else:
            select = self.tree.item(self.tree.selection())
            sitename = select["values"][0]
            self.currGui.withdraw()
            self.trans_detail = Toplevel()
            self.currGui = self.trans_detail
            self.trans_detail.title("Transit Detail")

            Label(self.trans_detail, text="Transit Detail").grid(row=0)

            frame = Frame(self.trans_detail)
            frame.grid()

            query = "select any_value(transit_route), any_value(transit_type), any_value(price), count(connects.sitename) from transit join connects where transit_route = transitroute and sitename = '%s' group by transitroute" % (sitename)
            self.cursor.execute(query)
            results = self.cursor.fetchall()

            Label(frame, text="Site ").grid(row=0, column=0)
            self.siteName = "Temp Site"
            Label(frame, text = sitename).grid(row=0, column=1)

            Label(frame, text="Transport Type: ").grid(row=0, column=2)
            self.trans_type = StringVar()
            choices_type = ['MARTA', 'Bus', 'Bike']
            self.trans_type.set('MARTA')
            self.popup = OptionMenu(frame, self.trans_type, *choices_type)
            self.popup.grid(row=0, column=3)

            frame_tree = Frame(self.trans_detail)
            frame_tree.grid()

            self.tree = ttk.Treeview(frame_tree,
                                columns=['Route', 'Transport Type', 'Price', '# Connected Sites'],
                                show='headings', selectmode='browse')

            self.tree.heading('Route', text='Route')
            self.tree.heading('Transport Type', text='Transport Type')
            self.tree.heading('Price', text='Price')
            self.tree.heading("# Connected Sites", text='# Connected Sites')
            for r in results:
                route = r[0]
                type = r[1]
                price = r[2]
                connected = r[3]
                self.tree.insert("", "end", values=(route, type, price, connected))
            #self.tree.insert("", "end", values=("1", "2", "3", "4"))
            #self.tree.insert("", "end", values=("4", "5", "6", "7"))
            self.tree.grid(row=1, column=3)

            frame_under = Frame(self.trans_detail)
            frame_under.grid()

            self.back = Button(frame_under, text="Back", command=self.transit_detail_back).grid(row=0, column=0)
            Label(frame_under, text="Transit Date ").grid(row=0, column=1)
            self.trans_date = StringVar()
            self.trans_date_enter = Entry(frame_under, textvariable=self.trans_date)
            self.trans_date_enter.grid(row=0, column=2)
            self.log_transit = Button(frame_under, text="Log Transit", command=self.transit_detail_log_transit).grid(row=0, column=3)

    def transit_detail_back(self):
        self.currGui.withdraw()
        self.explore_site.deiconify()
        self.currGui = self.explore_site

    def transit_detail_log_transit(self):
        if self.trans_date.get() == "":
            messagebox.showwarning("Date", "Please enter the date to log the transit")
        elif len(self.tree.selection()) == 0:
            messagebox.showwarning("Select Transit", "Please select a transit to log")
        else:
            select = self.tree.item(self.tree.selection())
            query = "Insert into Takes values('%s', '%s', '%s', '%s')" % (self.user.get(), select["values"][1], select["values"][0], self.trans_date.get())
            self.cursor.execute(query)
            self.db.commit()
            messagebox.showinfo("Success!!", "Your Transit has been logged")

    def site_detail(self):
        if len(self.tree.selection()) == 0:
            messagebox.showwarning("Select a Site", "Please select a site to view site detail")
        else:
            select = self.tree.item(self.tree.selection())
            self.name = select["values"][0]
            self.currGui.withdraw()
            self.site_detail = Toplevel()
            self.currGui = self.site_detail
            self.site_detail.title("Site Detail")

            Label(self.site_detail, text="Site Detail").grid(row=0)

            frame = Frame(self.site_detail)
            frame.grid()

            query = "Select SiteName as Site, Address as Address, openeveryday from Site where sitename = '%s'" % (self.name)
            self.cursor.execute(query)
            results = self.cursor.fetchone()
            self.address = results[1]
            self.open = results[2]

            Label(frame, text="Site: ").grid(row=0, column=0)
            Label(frame, text=self.name).grid(row=0, column=1)

            Label(frame, text="Open Everyday: ").grid(row=0, column=2)
            Label(frame, text=self.open).grid(row=0, column=3)

            Label(frame, text="Address ").grid(row=1, column=0)
            Label(frame, text=self.address).grid(row=1, column=1)

            frame_under = Frame(self.site_detail)
            frame_under.grid()

            Label(frame_under, text="Visit Date ").grid(row=0, column=1)
            self.visit_date = StringVar()
            self.visit_date_enter = Entry(frame_under, textvariable=self.visit_date)
            self.visit_date_enter.grid(row=0, column=2)
            self.log_visit = Button(frame_under, text="Log Visit", command=self.site_detail_log_visit).grid(row=0, column=3)

            self.back = Button(frame_under, text="Back", command=self.site_detail_back).grid(row=1, column=2)

    def site_detail_log_visit(self):
        if self.visit_date.get() == "":
            messagebox.showwarning("Date", "Please enter the date to log the transit")
        else:
            query = "Select Username, sitename, datevisited from VisitSite where sitename = '%s' and username = '%s' and datevisited = '%s'" % (self.name, self.user.get(), self.visit_date.get())
            result = self.cursor.execute(query)
            if result == 1:
                messagebox.showwarning("Already Visited Today", "You have already visited this site today so you cannot log another visit")
            else:
                select = self.tree.item(self.tree.selection())
                query = "Insert into VisitSite values('%s', '%s', '%s')" % (self.user.get(), self.name, self.visit_date.get())
                self.cursor.execute(query)
                self.db.commit()
                messagebox.showinfo("Success!!", "Your Transit has been logged")
                self.currGui.withdraw()
                self.visitor_explore_site()


    def site_detail_back(self):
        self.currGui.withdraw()
        self.explore_site.deiconify()
        self.currGui = self.explore_site

    def visit_history(self):
        self.currGui.withdraw()
        self.visit_history_gui = Toplevel()
        self.visit_history_gui.title("Visit History")

        Label(self.visit_history_gui, text="Visit History").grid(row=0)

        frame = Frame(self.visit_history_gui)
        frame.grid()

        Label(frame, text="Event ").grid(row=1, column=1)
        self.event_name = StringVar()
        self.event_name_enter = Entry(frame, textvariable=self.event_name)
        self.event_name_enter.grid(row=1, column=2)

        query = "Select Distinct SiteName from Site"
        self.cursor.execute(query)
        sites = self.cursor.fetchall()

        Label(frame, text="Site ").grid(row=1, column=3)
        self.site = StringVar()
        choices = []
        for site in sites:
            choices.append(site[0])
        choices.append('All')
        self.site.set('All')
        self.popup = OptionMenu(frame, self.site, *choices)
        self.popup.grid(row=1, column=4)

        Label(frame, text="Start Date").grid(row=2, column=1)
        self.start_date = StringVar()
        self.start_date_enter = Entry(frame, textvariable=self.start_date)
        self.start_date_enter.grid(row=2, column=2)

        Label(frame, text="End Date").grid(row=2, column=3)
        self.end_date = StringVar()
        self.end_date_enter = Entry(frame, textvariable=self.end_date)
        self.end_date_enter.grid(row=2, column=4)

        self.filter = Button(frame, text="Filter", command=self.filter_visit_history).grid(row=3, column=3)

        frame_tree = Frame(self.visit_history_gui)
        frame_tree.grid()

        self.tree = ttk.Treeview(frame_tree, columns=['Date', 'Event Name', 'Site', 'Price'],
                            show='headings', selectmode='browse')

        self.tree.heading('Date', text='Date')
        self.tree.heading('Event Name', text='Event Name')
        self.tree.heading('Site', text='Site')
        self.tree.heading('Price', text='Price')
        #self.tree.insert("", "end", values=("1", "2", "3", "4"))
        #self.tree.insert("", "end", values=("4", "5", "6", "7"))
        self.tree.grid(row=1, column=3)

        frame_under = Frame(self.visit_history_gui)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_visit_history).grid(row=0, column=0)

    def filter_visit_history(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        if self.event_name.get() == "" and self.site.get() == 'All' and self.start_date.get() == "" and self.end_date.get() == "":
            query = "Select distinct dateattended, visitevent.eventname, visitevent.sitename, beltlineevent.price from VisitEvent join beltlineevent where visitevent.eventname = beltlineevent.eventname"
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            for r in results:
                date = r[0]
                name = r[1]
                site = r[2]
                price = r[3]
                self.tree.insert("", "end", values=(date, name, site, price))

    def back_visit_history(self):
        self.currGui.withdraw()
        if self.userType == "Employee, Visitor":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Employee":
            if self.UserSubtype == "Staff":
                self.staff_visitor_functionality()
                self.currGui = self.staffVisGUI
            elif self.UserSubtype == "Admin":
                self.admin_vis_functionality()
                self.currGui = self.adminVisGUI
            elif self.UserSubtype == "Manager":
                self.manager_vis_functionality()
                self.currGui = self.manVisGUI
        elif self.userType == "Visitor":
            self.visitor_functionality()
            self.currGui = self.visitorGUI
        elif self.userType == "User":
            self.user_functionality()
            self.currGui = self.navGUI



root = Tk()

app = App(root)

root.mainloop()
