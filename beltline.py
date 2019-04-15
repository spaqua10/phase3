from tkinter import *
from tkinter import ttk


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

        self.new3 = Button(master, text = "User Func", command = self.user_functionality)
        self.new3.grid(row = 8)

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

        Label(self.regUser, text="Register User").grid(row = 0)

        frame = Frame(self.regUser)
        frame.grid()

        Label(frame, text="First Name: ").grid(row = 0, column = 0)
        self.fname = StringVar()
        self.fname_enter = Entry(frame, textvariable=self.fname)
        self.fname_enter.grid(row = 0, column = 1)

        Label(frame, text="Last Name: ").grid(row = 0, column = 2)
        self.lname = StringVar()
        self.lname_enter = Entry(frame, textvariable=self.lname)
        self.lname_enter.grid(row = 0, column = 3)

        Label(frame, text="Username: ").grid(row = 1, column = 0)
        self.user = StringVar()
        self.username_enter = Entry(frame, textvariable=self.user)
        self.username_enter.grid(row = 1, column = 1)

        Label(frame, text="Password: ").grid(row = 2, column = 0)
        self.password = StringVar()
        self.password_enter = Entry(frame, textvariable=self.password)
        self.password_enter.grid(row = 2, column = 1)

        Label(frame, text="Confirm Password: ").grid(row = 2, column = 2)
        self.password_confirm = StringVar()
        self.password_confirm_enter = Entry(frame, textvariable=self.password_confirm)
        self.password_confirm_enter.grid(row = 2, column = 3)

        Label(frame, text="Email: ").grid(row = 3, column = 0)
        self.email = StringVar()
        self.email_enter = Entry(frame, textvariable=self.email)
        self.email_enter.grid(row = 3, column = 1)

        self.registerUser = Button(frame, text="Back", command = self.register_user_back).grid(row = 4, column = 1)
        self.registerUser = Button(frame, text="Register", command = self.register_login_user).grid(row = 4, column = 2)


###########################################################################
    def register_visitor(self):
        self.navGUI.withdraw()
        self.regVisitor = Toplevel()
        self.regVisitor.title("Register Visitor")

        Label(self.regVisitor, text="Register Visitor").grid(row = 0)

        frame = Frame(self.regVisitor)
        frame.grid()


        Label(frame, text="First Name: ").grid(row = 0, column = 0)
        self.fname = StringVar()
        self.fname_enter = Entry(frame, textvariable=self.fname)
        self.fname_enter.grid(row = 0, column = 1)

        Label(frame, text="Last Name: ").grid(row = 0, column = 2)
        self.lname = StringVar()
        self.lname_enter = Entry(frame, textvariable=self.lname)
        self.lname_enter.grid(row = 0, column = 3)

        Label(frame, text="Username: ").grid(row = 1, column = 0)
        self.user = StringVar()
        self.username_enter = Entry(frame, textvariable=self.user)
        self.username_enter.grid(row = 1, column = 1)

        Label(frame, text="Password: ").grid(row = 2, column = 0)
        self.password = StringVar()
        self.password_enter = Entry(frame, textvariable=self.password)
        self.password_enter.grid(row = 2, column = 1)

        Label(frame, text="Confirm Password: ").grid(row = 2, column = 2)
        self.password_confirm = StringVar()
        self.password_confirm_enter = Entry(frame, textvariable=self.password_confirm)
        self.password_confirm_enter.grid(row = 2, column = 3)

        Label(frame, text="Email: ").grid(row = 3, column = 0)
        self.email = StringVar()
        self.email_enter = Entry(frame, textvariable=self.email)
        self.email_enter.grid(row = 3, column = 1)

        self.registerUser = Button(frame, text="Back", command = self.register_visitor_back).grid(row = 4, column = 1)
        self.registerUser = Button(frame, text="Register", command = self.register_login_visitor).grid(row = 4, column = 2)

###########################################################################
    def register_employee(self):
        self.navGUI.withdraw()
        self.regEmp = Toplevel()
        self.regEmp.title("Register Employee")

        Label(self.regEmp, text="Register Employee").grid(row = 0)

        frame = Frame(self.regEmp)
        frame.grid()

        Label(frame, text="First Name: ").grid(row = 0, column = 0)
        self.fname = StringVar()
        self.fname_enter = Entry(frame, textvariable=self.fname)
        self.fname_enter.grid(row = 0, column = 1)

        Label(frame, text="Last Name: ").grid(row = 0, column = 2)
        self.lname = StringVar()
        self.lname_enter = Entry(frame, textvariable=self.lname)
        self.lname_enter.grid(row = 0, column = 3)

        Label(frame, text="Username: ").grid(row = 1, column = 0)
        self.user = StringVar()
        self.username_enter = Entry(frame, textvariable=self.user)
        self.username_enter.grid(row = 1, column = 1)

        Label(frame, text="User Type: ").grid(row = 1, column = 2)
        self.userType = StringVar()
        choices = ["Manager", "Staff"]
        self.userType.set("Manager")
        self.popupMenu = OptionMenu(frame, self.userType, *choices)
        self.popupMenu.grid(row = 1, column = 3)

        Label(frame, text="Password: ").grid(row = 2, column = 0)
        self.password = StringVar()
        self.password_enter = Entry(frame, textvariable=self.password)
        self.password_enter.grid(row = 2, column = 1)

        Label(frame, text="Confirm Password: ").grid(row = 2, column = 2)
        self.password_confirm = StringVar()
        self.password_confirm_enter = Entry(frame, textvariable=self.password_confirm)
        self.password_confirm_enter.grid(row = 2, column = 3)

        Label(frame, text="Phone: ").grid(row = 3, column = 0)
        self.phone = IntVar()
        self.phone_enter = Entry(frame, textvariable=self.phone)
        self.phone_enter.grid(row = 3, column = 1)

        Label(frame, text="Address: ").grid(row = 3, column = 2)
        self.address = StringVar()
        self.address_enter = Entry(frame, textvariable=self.address)
        self.address_enter.grid(row = 5, column = 3)

        Label(frame, text="City: ").grid(row = 4, column = 0)
        self.city = StringVar()
        self.city_enter = Entry(frame, textvariable=self.city)
        self.city_enter.grid(row = 4, column = 1)

        Label(frame, text="State: ").grid(row = 4, column = 2)
        self.state = StringVar()
        choices_state = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "Other"]
        self.state.set("AL")
        self.popupMenuState = OptionMenu(frame, self.state, *choices_state)
        self.popupMenuState.grid(row = 4, column = 3)

        Label(frame, text="Zipcode: ").grid(row = 4, column = 4)
        self.zip = IntVar()
        self.zip_enter = Entry(frame, textvariable=self.zip)
        self.zip_enter.grid(row = 4, column = 5)

        Label(frame, text="Email: ").grid(row = 5, column = 0)
        self.email = StringVar()
        self.email_enter = Entry(frame, textvariable=self.email)
        self.email_enter.grid(row = 5, column = 1)

        self.registerUser = Button(frame, text="Back", command = self.register_emp_back).grid(row = 6, column = 1)
        self.registerUser = Button(frame, text="Register", command = self.register_login_emp).grid(row = 6, column = 2)

###########################################################################
    def register_employee_visitor(self):
        self.navGUI.withdraw()
        self.regEmpVis = Toplevel()
        self.regEmpVis.title("Register Employee-Visitor")

        Label(self.regEmpVis, text="Register Employee").grid(row = 0)

        frame = Frame(self.regEmpVis)
        frame.grid()

        Label(frame, text="First Name: ").grid(row = 0, column = 0)
        self.fname = StringVar()
        self.fname_enter = Entry(frame, textvariable=self.fname)
        self.fname_enter.grid(row = 0, column = 1)

        Label(frame, text="Last Name: ").grid(row = 0, column = 2)
        self.lname = StringVar()
        self.lname_enter = Entry(frame, textvariable=self.lname)
        self.lname_enter.grid(row = 0, column = 3)

        Label(frame, text="Username: ").grid(row = 1, column = 0)
        self.user = StringVar()
        self.username_enter = Entry(frame, textvariable=self.user)
        self.username_enter.grid(row = 1, column = 1)

        Label(frame, text="User Type: ").grid(row = 1, column = 2)
        self.userType = StringVar()
        choices = ["Manager", "Staff"]
        self.userType.set("Manager")
        self.popupMenu = OptionMenu(frame, self.userType, *choices)
        self.popupMenu.grid(row = 1, column = 3)

        Label(frame, text="Password: ").grid(row = 2, column = 0)
        self.password = StringVar()
        self.password_enter = Entry(frame, textvariable=self.password)
        self.password_enter.grid(row = 2, column = 1)

        Label(frame, text="Confirm Password: ").grid(row = 2, column = 2)
        self.password_confirm = StringVar()
        self.password_confirm_enter = Entry(frame, textvariable=self.password_confirm)
        self.password_confirm_enter.grid(row = 2, column = 3)

        Label(frame, text="Phone: ").grid(row = 3, column = 0)
        self.phone = IntVar()
        self.phone_enter = Entry(frame, textvariable=self.phone)
        self.phone_enter.grid(row = 3, column = 1)

        Label(frame, text="Address: ").grid(row = 3, column = 2)
        self.address = StringVar()
        self.address_enter = Entry(frame, textvariable=self.address)
        self.address_enter.grid(row = 3, column = 3)

        Label(frame, text="City: ").grid(row = 4, column = 0)
        self.city = StringVar()
        self.city_enter = Entry(frame, textvariable=self.city)
        self.city_enter.grid(row = 4, column = 1)

        Label(frame, text="State: ").grid(row = 4, column = 2)
        self.state = StringVar()
        choices_state = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "Other"]
        self.state.set("AL")
        self.popupMenuState = OptionMenu(frame, self.state, *choices_state)
        self.popupMenuState.grid(row = 4, column = 3)

        Label(frame, text="Zipcode: ").grid(row = 4, column = 4)
        self.zip = IntVar()
        self.zip_enter = Entry(frame, textvariable=self.zip)
        self.zip_enter.grid(row = 4, column = 5)

        Label(frame, text="Email: ").grid(row = 5, column = 0)
        self.email = StringVar()
        self.email_enter = Entry(frame, textvariable=self.email)
        self.email_enter.grid(row = 5, column = 1)

        self.registerUser = Button(frame, text="Back", command = self.register_empVis_back).grid(row = 6, column = 1)
        self.registerUser = Button(frame, text="Register", command = self.register_login_empVis).grid(row = 6, column = 2)

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

###########################################################################
    def user_functionality(self):
        self.firstGUI.withdraw()
        self.navGUI = Toplevel()
        self.navGUI.title("User Functionality")

        Label(self.navGUI, text="User Functionality").grid(row = 1)

        frame = Frame(self.navGUI)
        frame.grid()

        '''TODO Make Back Button Go Back To An actual Screen'''
        self.register = Button(self.navGUI, text="Take Transit", command = self.take_transit).grid(row=2)
        self.register = Button(self.navGUI, text="View Transite History", command = self.register_visitor).grid(row=3)
        self.register = Button(self.navGUI, text="Back", command = self.register_employee).grid(row=4)

###########################################################################
    def take_transit(self):
        self.navGUI.withdraw()
        self.take_tran = Toplevel()
        self.take_tran.title("Take Transit")

        Label(self.take_tran, text="Take Transit").grid(row = 0)

        frame = Frame(self.take_tran)
        frame.grid()

        Label(frame, text="Contain Site ").grid(row = 0, column = 0)
        self.destination = StringVar()
        choices = ["Manager", "Staff"]
        self.destination.set("Manager")
        self.popupMenu = OptionMenu(frame, self.destination, *choices)
        self.popupMenu.grid(row = 0, column = 1)

        Label(frame, text="Transport Type ").grid(row = 0, column = 2)
        self.trans_type = StringVar()
        choices_type = ['MARTA', 'Bus', 'Bike']
        self.trans_type.set('MARTA')
        self.popup = OptionMenu(frame, self.trans_type, *choices_type)
        self.popup.grid(row = 0, column = 3)

        Label(frame, text="Price Range ").grid(row = 1, column = 0)
        self.price_lower = IntVar()
        self.price_lower_enter = Entry(frame, textvariable=self.price_lower)
        self.price_lower_enter.grid(row = 1, column = 1)

        Label(frame, text=" -- ").grid(row = 1, column = 2)
        self.price_upper = IntVar()
        self.price_upper_enter = Entry(frame, textvariable=self.price_upper)
        self.price_upper_enter.grid(row = 1, column = 3)

        self.filter = Button(frame, text="Filter", command = self.filter_take_trans).grid(row = 1, column = 5)


        frame_tree = Frame(self.take_tran)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree, columns=['Route', 'Transport Type', 'Price', '# Connected Sites'], show='headings')

        tree.heading('Route', text='Route')
        tree.heading('Transport Type', text='Transport Type')
        tree.heading('Price', text='Price')
        tree.heading("# Connected Sites", text='# Connected Sites')
        tree.insert("", "end", values=("1", "2", "3", "4"))
        tree.insert("", "end", values=("4", "5", "6", "7"))
        tree.grid(row = 1, column = 3)

        frame_under = Frame(self.take_tran)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command = self.back_take_trans).grid(row = 0, column = 0)

        Label(frame_under, text="Transit Date ").grid(row = 0, column = 2)
        self.date = StringVar()
        self.date_entry = Entry(frame_under, textvariable=self.date)
        self.date_entry.grid(row = 0, column = 3)

        self.log = Button(frame_under, text="Log Transit", command = self.log_transit).grid(row = 0, column = 4)

###########################################################################
    def filter_take_trans(self):
        pass

###########################################################################
    def back_take_trans(self):
        pass

###########################################################################
    def log_transit(self):
        pass

root = Tk()

app = App(root)


root.mainloop()
