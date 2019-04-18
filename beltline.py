from tkinter import *
from tkinter import ttk, messagebox


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

        self.new3 = Button(master, text="User Func", command=self.user_functionality)
        self.new3.grid(row=8)

        self.new4 = Button(master, text="Admin Only Func", command=self.admin_only_functionality)
        self.new4.grid(row=9)

        self.new5 = Button(master, text="Admin-Visitor Func", command=self.admin_vis_functionality)
        self.new5.grid(row=10)

        self.new6 = Button(master, text="Manager Only Func", command=self.manager_only_functionality)
        self.new6.grid(row=11)

        self.new7 = Button(master, text="Manager-Visitor Func", command=self.manager_vis_functionality)
        self.new7.grid(row=12)

        self.new4 = Button(master, text="Staff Only Func", command=self.staff_only_functionality)
        self.new4.grid(row=13)

        self.new5 = Button(master, text="Staff-Visit Fun", command=self.staff_visitor_functionality)
        self.new5.grid(row=14)

        self.new6 = Button(master, text="Visit History", command=self.visit_history)
        self.new6.grid(row=15)

        # self.connect()
        # query = ("SELECT fname FROM EMPLOYEE")
        # cursor = self.db.cursor()
        # cursor.execute(query)
        # names = cursor.fetchall()
        # curr = 8
        # for x in names:
        #    Label(self.new2, text=x).grid(row = curr)
        #    curr = curr + 1
        # Label(self.new2, text=names).grid(row = 8)

    ###########################################################################
    # this function connects to the db

    def connect(self):
        import pymysql
        try:

            # get in that database yo

            self.db = pymysql.connect(host="localhost",
                                      user="root",
                                      passwd="",  # insert your db password here
                                      db="company")
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
        #User Only
        if self.userType == "User" :
            self.user_functionality()

        #Visitor Only
        elif self.userType == "Visitor":
            self.visitor_functionality()

        #Employee Only
        elif self.userType == "Employee":
            self.UserSubtype = "Staff"
            #TODO Implement Query From Employee Table

        #Employee and Visitor
        elif self.userType == "Employee, Visitor":
            #TODO Currently Fixing This
            pass
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
        pass

    ###########################################################################
    def register_visitor_back(self):
        self.regVisitor.withdraw()
        self.navGUI.deiconify()
        self.currGui = self.navGUI

    ###########################################################################
    def register_login_visitor(self):
        pass

    ###########################################################################
    def register_emp_back(self):
        self.regEmp.withdraw()
        self.navGUI.deiconify()
        self.currGui = self.navGUI

    ###########################################################################
    def register_login_emp(self):
        pass

    ###########################################################################
    def register_empVis_back(self):
        self.regEmpVis.withdraw()
        self.navGUI.deiconify()
        self.currGui = self.navGUI

    ###########################################################################
    def register_login_empVis(self):
        pass

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
        self.register = Button(self.adminVisGUI, text="Explore Event", command=self.explore_event).grid(row=4, column=0)
        self.register = Button(self.adminVisGUI, text="View Transit History", command=self.view_transit_history).grid(
            row=5, column=0)

        self.register = Button(self.adminVisGUI, text="Manage User", command=self.manage_user).grid(row=1, column=1)
        self.register = Button(self.adminVisGUI, text="Take Transit", command=self.take_transit).grid(row=2, column=1)
        self.register = Button(self.adminVisGUI, text="Explore Site", command=self.explore_site).grid(row=3, column=1)
        self.register = Button(self.adminVisGUI, text="View Visit History", command=self.view_visit_history).grid(row=4,
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
        self.register = Button(self.manVisGUI, text="Explore Site", command=self.explore_site).grid(row=3, column=0)
        self.register = Button(self.manVisGUI, text="Take Transit", command=self.take_transit).grid(row=4,
                                                                                                    column=0)
        self.register = Button(self.manVisGUI, text="View Visit History", command=self.view_visit_history).grid(row=5,
                                                                                                                column=0)

        self.register = Button(self.manVisGUI, text="Manage Event", command=self.manage_event).grid(row=1, column=1)
        self.register = Button(self.manVisGUI, text="View Site Report", command=self.view_site_report).grid(row=2,
                                                                                                            column=1)
        self.register = Button(self.manVisGUI, text="Explore Event", command=self.explore_event).grid(row=3, column=1)
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

        self.register = Button(self.staffVisGUI, text="Explore Event", command=self.explore_event).grid(row=2, column=1)
        self.register = Button(self.staffVisGUI, text="Explore Site", command=self.explore_site).grid(row=3, column=1)
        self.register = Button(self.staffVisGUI, text="View Visit History", command=self.view_visit_history).grid(row=4,
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
        self.register = Button(self.visitorGUI, text="Explore Event", command=self.explore_event).grid(row=2)
        self.register = Button(self.visitorGUI, text="Explore Site", command=self.explore_site).grid(row=3)
        self.register = Button(self.visitorGUI, text="View Visit History", command=self.view_visit_history).grid(row=4)
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

        self.filter = Button(frame, text="Filter", command=self.filter_take_trans).grid(row=4, column=3)
        self.create = Button(frame, text="Daily Detail", command=self.daily_detail).grid(row=4, column=4)

        frame_tree = Frame(self.site_report)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree,
                            columns=['Date', 'Event Count', 'Staff Count', 'Total Visits', 'Total Revenue ($)'],
                            show='headings')

        tree.heading('Date', text='Date')
        tree.heading('Event Count', text='Event Count')
        tree.heading('Staff Count', text='Staff Count')
        tree.heading('Total Visits', text='Total Visits')
        tree.heading('Total Revenue ($)', text="Total Revenue ($)")
        tree.insert("", "end", values=("1", "2", "3", "4", "6"))
        tree.insert("", "end", values=("4", "5", "6", "7", "8"))
        tree.grid(row=1, column=3)

        frame_under = Frame(self.site_report)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=0, column=0)

    def view_staff(self):
        self.currGui.withdraw()
        self.view_staff = Toplevel()
        self.currGui = self.view_staff
        self.view_staff.title("View / Manage Staff")

        Label(self.view_staff, text="View / Manage Staff").grid(row=0)

        frame = Frame(self.view_staff)
        frame.grid()

        Label(frame, text="Site").grid(row=0, column=0)
        self.site = StringVar()
        choices_type = ['MARTA', 'Bus', 'Bike', 'All']
        self.site.set('All')
        self.popup = OptionMenu(frame, self.site, *choices_type)
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

        self.filter = Button(frame, text="Filter", command=self.filter_take_trans).grid(row=3, column=2)

        frame_tree = Frame(self.view_staff)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree, columns=['Staff Name', '# Event Shifts'],
                            show='headings')

        tree.heading('Staff Name', text='Name')
        tree.heading('# Event Shifts', text='Staff Count')
        tree.insert("", "end", values=("1", "2"))
        tree.insert("", "end", values=("4", "5"))
        tree.grid(row=1, column=3)

        frame_under = Frame(self.view_staff)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=0, column=0)

    def manage_event(self):
        self.currGui.withdraw()
        self.manage_event = Toplevel()
        self.currGui = self.manage_event
        self.manage_event.title("Manage Event")

        Label(self.manage_event, text="Manage Event").grid(row=0)

        frame = Frame(self.manage_event)
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

        self.filter = Button(frame, text="Filter", command=self.filter_take_trans).grid(row=4, column=0)
        self.create = Button(frame, text="Create", command=self.create_event).grid(row=4, column=1)
        self.view = Button(frame, text="View/Edit", command=self.view_edit_event).grid(row=4, column=2)
        self.delete = Button(frame, text="Delete", command=self.filter_take_trans).grid(row=4, column=3)

        frame_tree = Frame(self.manage_event)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree,
                            columns=['Name', 'Staff Count', 'Duration (Days)', 'Total Visits', 'Total Revenue'],
                            show='headings')

        tree.heading('Name', text='Name')
        tree.heading('Staff Count', text='Staff Count')
        tree.heading('Duration (Days)', text='Duration (Days)')
        tree.heading('Total Visits', text='Total Visits')
        tree.heading('Total Revenue', text="Total Revenue")
        tree.insert("", "end", values=("1", "2", "3", "4", "6"))
        tree.insert("", "end", values=("4", "5", "6", "7", "8"))
        tree.grid(row=1, column=3)

        frame_under = Frame(self.manage_event)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=0, column=0)

    def view_edit_event(self):
        self.currGui.withdraw()
        self.view_event = Toplevel()
        self.currGui = self.view_event
        self.view_event.title("View/Edit Event")

        Label(self.view_event, text="View/Edit Event").grid(row=0)

        frame = Frame(self.view_event)
        frame.grid()

        ''' TODO: Change the Labels below to data from SQL. Prepopulate everything else with SQL data'''

        Label(frame, text="Name ").grid(row=0, column=0)
        Label(frame, text="Event Name").grid(row=0, column=1)

        Label(frame, text="Price ($) ").grid(row=0, column=2)
        Label(frame, text="25").grid(row=0, column=3)

        Label(frame, text="Start Date").grid(row=1, column=0)
        Label(frame, text='2019-02-01').grid(row=1, column=1)

        Label(frame, text="End Date").grid(row=1, column=2)
        Label(frame, text="2019-02-01").grid(row=1, column=3)

        Label(frame, text="Minimum Staff Required").grid(row=2, column=0)
        Label(frame, text='4').grid(row=2, column=1)

        Label(frame, text="Capacity").grid(row=2, column=2)
        Label(frame, text='100').grid(row=2, column=3)

        Label(frame, text="Staff Assigned").grid(row=3, column=0)
        list = Listbox(frame, selectmode=MULTIPLE)
        list.insert(0, 'Staff 1')
        list.insert(1, 'Staff 2')
        list.insert(2, 'Staff 3')
        list.grid(row=3, column=1)

        Label(frame, text="Description").grid(row=4, column=0)
        self.description = StringVar()
        self.description_entry = Entry(frame, textvariable=self.description)
        # self.description = Text(frame)
        # self.description.config(borderwidth=5)
        # self.description.insert(END,'description goes here')
        self.description_entry.grid(row=4, column=1)

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

        self.filter = Button(frame, text="Filter", command=self.filter_take_trans).grid(row=6, column=0)
        self.create = Button(frame, text="Update", command=self.filter_take_trans).grid(row=6, column=1)

        frame_tree = Frame(self.view_event)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree, columns=['Date', 'Daily Visits', 'Daily Revenue'],
                            show='headings')

        tree.heading('Date', text='Date')
        tree.heading('Daily Visits', text='Daily Visits')
        tree.heading('Daily Revenue', text='Daily Revenue')
        tree.insert("", "end", values=("1", "2", "3"))
        tree.insert("", "end", values=("4", "5", "6"))
        tree.grid(row=1, column=3)

        frame_under = Frame(self.view_event)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=0, column=0)

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

        Label(frame, text="Description").grid(row=3, column=0)
        self.description = StringVar()
        self.description_entry = Entry(frame, textvariable=self.description)
        # self.description = Text(frame)
        # self.description.config(borderwidth=5)
        # self.description.insert(END,'description goes here')
        self.description_entry.grid(row=3, column=1)

        Label(frame, text="Assign Staff").grid(row=4, column=0)
        list = Listbox(frame, selectmode=MULTIPLE)
        list.insert(0, 'Staff 1')
        list.insert(1, 'Staff 2')
        list.insert(2, 'Staff 3')
        list.grid(row=4, column=1)

        self.back = Button(frame, text="Back", command=self.back_take_trans).grid(row=5, column=0)
        self.create = Button(frame, text="Create", command=self.filter_take_trans).grid(row=5, column=1)

    def view_visit_history(self):
        pass

    def explore_site(self):
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
        choices_type = ['MARTA', 'Bus', 'Bike']
        self.trans_type.set('MARTA')
        self.popup = OptionMenu(frame, self.trans_type, *choices_type)
        self.popup.grid(row=0, column=1)

        Label(frame, text="Contain Site ").grid(row=0, column=2)
        self.destination = StringVar()
        choices = ["Manager", "Staff"]
        self.destination.set("Manager")
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

        self.filter = Button(frame, text="Filter", command=self.filter_take_trans).grid(row=2, column=0)

        frame_tree = Frame(self.view_tran)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree, columns=['Date', 'Route', 'Transport Type', 'Price'],
                            show='headings')

        tree.heading('Date', text='Date')
        tree.heading('Route', text='Route')
        tree.heading('Transport Type', text='Transport Type')
        tree.heading('Price', text='Price')
        tree.insert("", "end", values=("1", "2", "3", "4"))
        tree.insert("", "end", values=("4", "5", "6", "7"))
        tree.grid(row=1, column=3)

        frame_under = Frame(self.view_tran)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=0, column=0)

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

        Label(frame, text="First Name: ").grid(row=0, column=0)
        self.fname = StringVar()
        self.fname_enter = Entry(frame, textvariable=self.fname)
        self.fname_enter.grid(row=0, column=1)

        Label(frame, text="Last Name: ").grid(row=0, column=2)
        self.lname = StringVar()
        self.lname_enter = Entry(frame, textvariable=self.lname)
        self.lname_enter.grid(row=0, column=3)

        Label(frame, text="Username: ").grid(row=1, column=0)
        Label(frame, text='user').grid(row=1, column=1)

        Label(frame, text="Site Name: ").grid(row=1, column=2)
        Label(frame, text="Site").grid(row=1, column=3)

        Label(frame, text="Employee ID: ").grid(row=2, column=0)
        Label(frame, text="123456789").grid(row=2, column=1)

        Label(frame, text="Phone ").grid(row=2, column=2)
        self.phone = IntVar()
        self.phone_enter = Entry(frame, textvariable=self.phone)
        self.phone_enter.grid(row=2, column=3)

        Label(frame, text="Address: ").grid(row=3, column=0)
        self.address = StringVar()
        self.address_enter = Entry(frame, textvariable=self.address)
        self.address_enter.grid(row=3, column=1)

        Label(frame, text="Email: ").grid(row=4, column=0)
        self.email = StringVar()
        self.email_enter = Entry(frame, textvariable=self.email)
        self.email_enter.grid(row=4, column=1)

        self.registerUser = Button(frame, text="Back", command=self.register_emp_back).grid(row=5, column=0)
        self.registerUser = Button(frame, text="Register", command=self.register_login_emp).grid(row=5, column=1)

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
        choices = ["Manager", "Staff"]
        self.type.set("Manager")
        self.popupMenu = OptionMenu(frame, self.type, *choices)
        self.popupMenu.grid(row=0, column=3)

        Label(frame, text="Status ").grid(row=0, column=4)
        self.status = StringVar()
        choices_type = ['Approved', 'Declined', 'Pending', 'All']
        self.status.set('Approved')
        self.popup = OptionMenu(frame, self.status, *choices_type)
        self.popup.grid(row=0, column=5)

        self.filter = Button(frame, text="Filter", command=self.filter_take_trans).grid(row=1, column=0)

        self.approve = Button(frame, text="Approve", command=self.approve_user).grid(row=1, column=1)
        self.decline = Button(frame, text='Decline', command=self.decline_user).grid(row=1, column=2)

        frame_tree = Frame(self.manageUserGui)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree, columns=['Username', 'Email Count', 'User Type', 'Status'],
                            show='headings')

        tree.heading('Username', text='Username')
        tree.heading('Email Count', text='Email Count')
        tree.heading('User Type', text='User Type')
        tree.heading("Status", text='Status')
        tree.insert("", "end", values=("1", "2", "3", "4"))
        tree.insert("", "end", values=("4", "5", "6", "7"))
        tree.grid(row=1, column=3)

        frame_under = Frame(self.manageUserGui)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=0, column=0)

    def approve_user(self):
        pass

    def decline_user(self):
        pass

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
        choices = ["MARTA", "Bus", "Bike"]
        self.trans_type.set("MARTA")
        self.popupMenu = OptionMenu(frame, self.trans_type, *choices)
        self.popupMenu.grid(row=0, column=1)

        Label(frame, text="Route ").grid(row=0, column=2)
        self.route = StringVar()
        self.route_enter = Entry(frame, textvariable=self.route)
        self.route_enter.grid(row=0, column=3)

        Label(frame, text="Contain Site ").grid(row=1, column=0)
        self.site = StringVar()
        choices_type = ['Approved', 'Declined', 'Pending', 'All']
        self.site.set('Approved')
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

        self.filter = Button(frame, text="Filter", command=self.filter_take_trans).grid(row=2, column=0)

        self.create = Button(frame, text="Create", command=self.create_transit).grid(row=2, column=1)
        self.edit = Button(frame, text='Edit', command=self.edit_transit).grid(row=2, column=2)
        self.delete = Button(frame, text='Delete', command=self.delete_transit).grid(row=2, column=3)

        frame_tree = Frame(self.manageTranGui)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree,
                            columns=['Route', 'Transport Type', 'Price', '# Connected Sites', '# Transit Logged'],
                            show='headings')

        tree.heading('Route', text='Route')
        tree.heading('Transport Type', text='Transport Type')
        tree.heading('Price', text='Price')
        tree.heading("# Connected Sites", text='# Connected Sites')
        tree.heading("# Transit Logged", text='# Transit Logged')
        tree.insert("", "end", values=("1", "2", "3", "4", "5"))
        tree.insert("", "end", values=("4", "5", "6", "7", "8"))
        tree.grid(row=1, column=3)

        frame_under = Frame(self.manageTranGui)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=0, column=0)

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

        Label(frame, text="Connected Sites").grid(row=1, column=0)

        list = Listbox(frame, selectmode=MULTIPLE)
        list.insert(0, 'Atlanta Beltline Center')
        list.insert(1, 'Gorden-White Park')
        list.insert(2, 'Inman Park')
        list.grid(row=1, column=1)

        self.registerUser = Button(frame, text="Back", command=self.register_user_back).grid(row=2, column=1)
        self.registerUser = Button(frame, text="Create", command=self.register_login_user).grid(row=2, column=2)

    def edit_transit(self):
        self.manageTranGui.withdraw()
        self.editTransit = Toplevel()
        self.prevGUI = self.currGui
        self.currGui = self.editTransit
        self.editTransit.title("Edit Transit")

        Label(self.editTransit, text="Edit Transit").grid(row=0)

        frame = Frame(self.editTransit)
        frame.grid()

        Label(frame, text="Transport Type").grid(row=0, column=0)
        Label(frame, text="Bus").grid(row=0, column=1)

        Label(frame, text="Route").grid(row=0, column=2)
        self.route = StringVar()
        self.route_enter = Entry(frame, textvariable=self.route)
        self.route_enter.grid(row=0, column=3)

        Label(frame, text="Price").grid(row=0, column=4)
        self.price = IntVar()
        self.price_enter = Entry(frame, textvariable=self.price)
        self.price_enter.grid(row=0, column=5)

        Label(frame, text="Connected Sites").grid(row=1, column=0)

        list = Listbox(frame, selectmode=MULTIPLE)
        list.insert(0, 'Atlanta Beltline Center')
        list.insert(1, 'Gorden-White Park')
        list.insert(2, 'Inman Park')
        list.grid(row=1, column=1)

        self.registerUser = Button(frame, text="Back", command=self.register_user_back).grid(row=2, column=1)
        self.registerUser = Button(frame, text="Edit", command=self.register_login_user).grid(row=2, column=2)

    def delete_transit(self):
        pass

    def manage_site(self):
        self.currGui.withdraw()
        self.manageSiteGui = Toplevel()
        self.currGui = self.manage_site
        self.manageSiteGui.title("Manage Site")

        Label(self.manageSiteGui, text="Manage Site").grid(row=0)

        frame = Frame(self.manageSiteGui)
        frame.grid()

        Label(frame, text="Site ").grid(row=0, column=0)
        self.type = StringVar()
        choices = ["Manager", "Staff", "All"]
        self.type.set("All")
        self.popupMenu = OptionMenu(frame, self.type, *choices)
        self.popupMenu.grid(row=0, column=1)

        Label(frame, text="Manager ").grid(row=0, column=2)
        self.status = StringVar()
        choices_type = ['Approved', 'Declined', 'Pending', 'All']
        self.status.set('All')
        self.popup = OptionMenu(frame, self.status, *choices_type)
        self.popup.grid(row=0, column=3)

        Label(frame, text="Open Everyday ").grid(row=1, column=2)
        self.status = StringVar()
        choices_type = ['Yes', 'No']
        self.status.set('Yes')
        self.popup = OptionMenu(frame, self.status, *choices_type)
        self.popup.grid(row=1, column=3)

        self.filter = Button(frame, text="Filter", command=self.filter_take_trans).grid(row=2, column=0)

        self.create = Button(frame, text="Create", command=self.create_site).grid(row=2, column=1)
        self.edit = Button(frame, text='Edit', command=self.edit_site).grid(row=2, column=2)
        self.delete = Button(frame, text='Delete', command=self.decline_user).grid(row=2, column=3)

        frame_tree = Frame(self.manageSiteGui)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree, columns=['Username', 'Email Count', 'User Type'],
                            show='headings')

        tree.heading('Username', text='Username')
        tree.heading('Email Count', text='Email Count')
        tree.heading('User Type', text='User Type')
        tree.insert("", "end", values=("1", "2", "3"))
        tree.insert("", "end", values=("4", "5", "6"))
        tree.grid(row=1, column=3)

        frame_under = Frame(self.manageSiteGui)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=0, column=0)

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
        self.lname = StringVar()
        self.lname_enter = Entry(frame, textvariable=self.lname)
        self.lname_enter.grid(row=0, column=3)

        Label(frame, text="Address: ").grid(row=1, column=0)
        self.user = StringVar()
        self.username_enter = Entry(frame, textvariable=self.user)
        self.username_enter.grid(row=1, column=1)

        Label(frame, text="Manager: ").grid(row=2, column=0)
        self.password_confirm = StringVar()
        self.password_confirm_enter = Entry(frame, textvariable=self.password_confirm)
        self.password_confirm_enter.grid(row=2, column=1)

        # Label(frame, text="Open Everyday").grid(row=2, column=3)
        self.open = IntVar()
        Checkbutton(frame, text="Open Everyday", variable=self.open).grid(row=2, column=2)

        self.registerUser = Button(frame, text="Back", command=self.register_user_back).grid(row=4, column=1)
        self.registerUser = Button(frame, text="Create", command=self.register_login_user).grid(row=4, column=2)

    def edit_site(self):
        self.manageSiteGui.withdraw()
        self.editSite = Toplevel()
        self.prevGUI = self.currGui
        self.currGui = self.editSite
        self.editSite.title("Edit Site")

        Label(self.editSite, text="Edit Site").grid(row=0)

        frame = Frame(self.editSite)
        frame.grid()

        Label(frame, text="Name: ").grid(row=0, column=0)
        self.fname = StringVar()
        self.fname_enter = Entry(frame, textvariable=self.fname)
        self.fname_enter.grid(row=0, column=1)

        Label(frame, text="Zipcode: ").grid(row=0, column=2)
        self.lname = StringVar()
        self.lname_enter = Entry(frame, textvariable=self.lname)
        self.lname_enter.grid(row=0, column=3)

        Label(frame, text="Address: ").grid(row=1, column=0)
        self.user = StringVar()
        self.username_enter = Entry(frame, textvariable=self.user)
        self.username_enter.grid(row=1, column=1)

        Label(frame, text="Manager: ").grid(row=2, column=0)
        self.password_confirm = StringVar()
        self.password_confirm_enter = Entry(frame, textvariable=self.password_confirm)
        self.password_confirm_enter.grid(row=2, column=1)

        # Label(frame, text="Open Everyday").grid(row=2, column=3)
        self.open = IntVar()
        Checkbutton(frame, text="Open Everyday", variable=self.open).grid(row=2, column=2)

        self.registerUser = Button(frame, text="Back", command=self.register_user_back).grid(row=4, column=1)
        self.registerUser = Button(frame, text="Update", command=self.register_login_user).grid(row=4, column=2)

    ###########################################################################
    def take_transit(self):
        self.currGui.withdraw()
        self.take_tran = Toplevel()
        self.currGui = self.take_transit
        self.take_tran.title("Take Transit")

        Label(self.take_tran, text="Take Transit").grid(row=0)

        frame = Frame(self.take_tran)
        frame.grid()

        Label(frame, text="Contain Site ").grid(row=0, column=0)
        self.destination = StringVar()
        choices = ["Manager", "Staff"]
        self.destination.set("Manager")
        self.popupMenu = OptionMenu(frame, self.destination, *choices)
        self.popupMenu.grid(row=0, column=1)

        Label(frame, text="Transport Type ").grid(row=0, column=2)
        self.trans_type = StringVar()
        choices_type = ['MARTA', 'Bus', 'Bike']
        self.trans_type.set('MARTA')
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

        self.filter = Button(frame, text="Filter", command=self.filter_take_trans).grid(row=1, column=5)

        frame_tree = Frame(self.take_tran)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree, columns=['Route', 'Transport Type', 'Price', '# Connected Sites'],
                            show='headings')

        tree.heading('Route', text='Route')
        tree.heading('Transport Type', text='Transport Type')
        tree.heading('Price', text='Price')
        tree.heading("# Connected Sites", text='# Connected Sites')
        tree.insert("", "end", values=("1", "2", "3", "4"))
        tree.insert("", "end", values=("4", "5", "6", "7"))
        tree.grid(row=1, column=3)

        frame_under = Frame(self.take_tran)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=0, column=0)

        Label(frame_under, text="Transit Date ").grid(row=0, column=2)
        self.date = StringVar()
        self.date_entry = Entry(frame_under, textvariable=self.date)
        self.date_entry.grid(row=0, column=3)

        self.log = Button(frame_under, text="Log Transit", command=self.log_transit).grid(row=0, column=4)

    ###########################################################################
    def filter_take_trans(self):
        pass

    ###########################################################################
    def back_take_trans(self):
        pass

    ###########################################################################
    def log_transit(self):
        pass

    def on_backbutton_clicked(self):
        self.frame()

    def daily_detail(self):
        self.currGui.withdraw()
        self.dailyDetailGUI = Toplevel()
        self.dailyDetailGUI.title("Daily Detail")

        Label(self.dailyDetailGUI, text="Daily Detail").grid(row=0)

        frame = Frame(self.dailyDetailGUI)
        frame.grid()

        frame_tree = Frame(self.dailyDetailGUI)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree, columns=['Event Name', 'Staff Names', 'Visits', 'Revenue ($)'],
                            show='headings')

        tree.heading('Event Name', text='Event Name')
        tree.heading('Staff Names', text='Staff Names')
        tree.heading('Visits', text='Visits')
        tree.heading("Revenue ($)", text='Revenue ($)')
        tree.insert("", "end", values=("1", "2", "3", "4"))
        tree.insert("", "end", values=("4", "5", "6", "7"))
        tree.grid(row=1, column=3)

        frame_under = Frame(self.dailyDetailGUI)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=0, column=0)

    def view_schedule(self):
        self.currGui.withdraw()
        self.view_sched_gui = Toplevel()
        self.view_sched_gui.title("Transit History")

        Label(self.view_sched_gui, text="Transit History").grid(row=0)

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

        self.filter = Button(frame, text="Filter", command=self.filter_take_trans).grid(row=3, column=2)
        self.view_event = Button(frame, text="View Event", command=self.filter_take_trans).grid(row=3, column=4)

        frame_tree = Frame(self.view_sched_gui)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree, columns=['Event Name', 'Site Name', 'Start Date', 'End Date', 'Staff Count'],
                            show='headings')

        tree.heading('Event Name', text='Event Name')
        tree.heading('Site Name', text='Site Name')
        tree.heading('Start Date', text='Start Date')
        tree.heading('End Date', text='End Date')
        tree.heading('Staff Count', text='Staff Count')
        tree.insert("", "end", values=("1", "2", "3", "4", "0"))
        tree.insert("", "end", values=("4", "5", "6", "7", "0"))
        tree.grid(row=1, column=3)

        frame_under = Frame(self.view_sched_gui)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=0, column=0)

    def staff_event_detail(self):
        self.currGui.withdraw()
        self.event_detail = Toplevel()
        self.currGui = self.event_detail
        self.event_detail.title("Event Detail")

        Label(self.event_detail, text="Event Detail").grid(row=0)

        frame = Frame(self.event_detail)
        frame.grid()

        Label(frame, text="Event: ").grid(row=0, column=0)
        self.event = StringVar()
        self.event_enter = Entry(frame, textvariable=self.event)
        self.event_enter.grid(row=0, column=1)

        Label(frame, text="Site: ").grid(row=0, column=2)
        self.site = StringVar()
        self.site_enter = Entry(frame, textvariable=self.site)
        self.site_enter.grid(row=0, column=3)

        Label(frame, text="Start Date: ").grid(row=1, column=0)
        self.start_date_detail = StringVar()
        self.start_date_detail_enter = Entry(frame, textvariable=self.start_date_detail)
        self.start_date_detail_enter.grid(row=1, column=1)

        Label(frame, text="End Date: ").grid(row=1, column=2)
        self.end_date_detail = StringVar()
        self.end_date_detail_enter = Entry(frame, textvariable=self.end_date_detail)
        self.end_date_detail_enter.grid(row=1, column=3)

        Label(frame, text="Duration Days: ").grid(row=1, column=4)
        self.duration_days = StringVar()
        self.duration_days_enter = Entry(frame, textvariable=self.duration_days)
        self.duration_days_enter.grid(row=1, column=5)

        Label(frame, text="Staffs Assigned: ").grid(row=2, column=0)
        self.staff_assigned = StringVar()
        self.staff_assigned_enter = Entry(frame, textvariable=self.staff_assigned)
        self.staff_assigned_enter.grid(row=2, column=1)

        Label(frame, text="Capacity: ").grid(row=2, column=2)
        self.capacity = StringVar()
        self.capacity_enter = Entry(frame, textvariable=self.capacity)
        self.capacity_enter.grid(row=2, column=3)

        Label(frame, text="Price:  ").grid(row=2, column=4)
        self.price = StringVar()
        self.price_enter = Entry(frame, textvariable=self.price)
        self.price_enter.grid(row=2, column=5)

        Label(frame, text="Description:  ").grid(row=3, column=0)
        self.description = StringVar()
        self.description_enter = Entry(frame, textvariable=self.description)
        self.description_enter.grid(row=3, column=1)

        self.registerUser = Button(frame, text="Back", command=self.register_emp_back).grid(row=6, column=1)
        self.registerUser = Button(frame, text="Register", command=self.register_login_emp).grid(row=6, column=2)

    def visit_explore_event(self):
        self.currGui.withdraw()
        self.visit_explore_event = Toplevel()
        self.currGui = self.visit_explore_event
        self.visit_explore_event.title("Explore Event")

        Label(self.visit_explore_event, text="Explore Event").grid(row=0)

        frame = Frame(self.visit_explore_event)
        frame.grid()

        Label(frame, text="Name: ").grid(row=0, column=0)
        self.name = StringVar()
        self.name_enter = Entry(frame, textvariable=self.name)
        self.name_enter.grid(row=0, column=1)

        Label(frame, text="Description: ").grid(row=0, column=2)
        self.desc = StringVar()
        self.desc_enter = Entry(frame, textvariable=self.desc)
        self.desc_enter.grid(row=0, column=3)

        Label(frame, text = "Site Name: ").grid  (row = 1, column = 0)
        self.site_name = StringVar()
        choices = ["MARTA", "Bus", "Bike", "-- ALL --"]
        self.site_name.set("-- ALL --")
        self.popupMenu = OptionMenu(frame, self.site_name, *choices)
        self.popupMenu.grid(row=1, column=1)

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

        frame_tree = Frame(self.visit_explore_event)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree, columns=['Event Name', 'Site Name', 'Ticket Price', 'Tickets Remaining',
                                                 'Total Visits', 'My Visits'],
                            show='headings')

        tree.heading('Event Name', text='Event Name')
        tree.heading('Site Name', text='Site Name')
        tree.heading('Ticket Price', text='Ticket Price')
        tree.heading('Tickets Remaining', text='Tickets Remaining')
        tree.heading('Total Visits', text='Total Visits')
        tree.heading('My Visits', text='My Visits')
        tree.insert("", "end", values=("1", "2", "3", "4", "0", "0"))
        tree.insert("", "end", values=("4", "5", "6", "7", "0", "0"))
        tree.grid(row=4, column=3)

        frame_under = Frame(self.visit_explore_event)
        frame_under.grid()

        self.registerUser = Button(frame, text="Back", command=self.register_emp_back).grid(row=6, column=3)
        self.registerUser = Button(frame, text="Register", command=self.register_login_emp).grid(row=6, column=4)

    def visitor_event_detail(self):
        self.currGui.withdraw()
        self.event_detail = Toplevel()
        self.currGui = self.event_detail
        self.event_detail.title("Event Detail")

        Label(self.event_detail, text="Event Detail").grid(row=0)

        frame = Frame(self.event_detail)
        frame.grid()

        Label(frame, text="Event: ").grid(row=0, column=0)
        self.event = StringVar()
        self.event_enter = Entry(frame, textvariable=self.event)
        self.event_enter.grid(row=0, column=1)

        Label(frame, text="Site: ").grid(row=0, column=2)
        self.site = StringVar()
        self.site_enter = Entry(frame, textvariable=self.site)
        self.site_enter.grid(row=0, column=3)

        Label(frame, text="Start Date: ").grid(row=1, column=0)
        self.start_date_detail = StringVar()
        self.start_date_detail_enter = Entry(frame, textvariable=self.start_date_detail)
        self.start_date_detail_enter.grid(row=1, column=1)

        Label(frame, text="End Date: ").grid(row=1, column=2)
        self.end_date_detail = StringVar()
        self.end_date_detail_enter = Entry(frame, textvariable=self.end_date_detail)
        self.end_date_detail_enter.grid(row=1, column=3)


        Label(frame, text="Ticket Price ($): ").grid(row=2, column=0)
        self.ticket_price = StringVar()
        self.ticket_price_enter = Entry(frame, textvariable=self.ticket_price)
        self.ticket_price_enter.grid(row=2, column=1)

        Label(frame, text="Tickets Remaining: ").grid(row=2, column=2)
        self.tickets_remaining = StringVar()
        self.tickets_remaining_enter = Entry(frame, textvariable=self.tickets_remaining)
        self.tickets_remaining_enter.grid(row=2, column=3)


        Label(frame, text="Description:  ").grid(row=3, column=0)
        self.description = StringVar()
        self.description_enter = Entry(frame, textvariable=self.description)
        self.description_enter.grid(row=3, column=1)

        Label(frame, text="Visit Date:  ").grid(row=4, column=0)
        self.visit_date = StringVar()
        self.visit_date_enter = Entry(frame, textvariable=self.visit_date)
        self.visit_date_enter.grid(row=4, column=1)



        self.registerUser = Button(frame, text="Back", command=self.register_emp_back).grid(row=6, column=1)
        self.registerUser = Button(frame, text="Register", command=self.register_login_emp).grid(row=6, column=2)

    def visitor_explore_site(self):
        self.currGui.withdraw()
        self.explore_site = Toplevel()
        self.currGui = self.explore_site
        self.explore_site.title("Explore Site")

        Label(self.explore_site, text="Explore Site").grid(row=0)

        frame = Frame(self.explore_site)
        frame.grid()

        Label(frame, text="Name: ").grid(row=0, column=0)
        self.site = StringVar()
        choices_type = ['MARTA', 'Bus', 'Bike', 'All']
        self.site.set('All')
        self.popup = OptionMenu(frame, self.site, *choices_type)
        self.popup.grid(row=0, column=1)

        Label(frame, text="Open Everyday: ").grid(row=0, column=2)
        self.site = StringVar()
        choices_type = ['MARTA', 'Bus', 'Bike', 'All']
        self.site.set('All')
        self.popup = OptionMenu(frame, self.site, *choices_type)
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

        self.filter = Button(frame, text="Filter", command=self.filter_take_trans).grid(row=4, column=2)
        self.filter = Button(frame, text="Site Detail", command=self.site_detail).grid(row=4, column=4)
        self.filter = Button(frame, text="Transit Detail", command=self.transit_detail).grid(row=4, column=5)

        frame_tree = Frame(self.explore_site)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree, columns=['Site Name', 'Event Count', 'Total Visits', 'My Visits'],
                            show='headings')

        tree.heading('Site Name', text='Site Name')
        tree.heading('Event Count', text='Event Count')
        tree.heading('Total Visits', text = 'Total Visits')
        tree.heading('My Visits', text = 'My Visits')
        tree.insert("", "end", values=("1", "2", "0", "0"))
        tree.insert("", "end", values=("4", "5", "0", "0"))
        tree.grid(row=1, column=3)

        frame_under = Frame(self.explore_site)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=0, column=0)


    def transit_detail(self):
        self.currGui.withdraw()
        self.trans_detail = Toplevel()
        self.currGui = self.trans_detail
        self.trans_detail.title("Transit Detail")

        Label(self.trans_detail, text="Transit Detail").grid(row=0)

        frame = Frame(self.trans_detail)
        frame.grid()

        Label(frame, text="Site ").grid(row=0, column=0)
        self.site = StringVar()
        self.site_enter = Entry(frame, textvariable=self.site)
        self.site_enter.grid(row=0, column=1)

        Label(frame, text="Transport Type: ").grid(row=0, column=2)
        self.trans_type = StringVar()
        choices_type = ['MARTA', 'Bus', 'Bike', 'All']
        self.trans_type.set('All')
        self.popup = OptionMenu(frame, self.trans_type, *choices_type)
        self.popup.grid(row=0, column=3)

        frame_tree = Frame(self.trans_detail)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree,
                            columns=['Route', 'Transport Type', 'Price', '# Connected Sites'],
                            show='headings')

        tree.heading('Route', text='Route')
        tree.heading('Transport Type', text='Transport Type')
        tree.heading('Price', text='Price')
        tree.heading("# Connected Sites", text='# Connected Sites')
        tree.insert("", "end", values=("1", "2", "3", "4"))
        tree.insert("", "end", values=("4", "5", "6", "7"))
        tree.grid(row=1, column=3)

        frame_under = Frame(self.trans_detail)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=0, column=0)
        Label(frame_under, text="Site ").grid(row=0, column=1)
        self.trans_date = StringVar()
        self.trans_date_enter = Entry(frame_under, textvariable=self.trans_date)
        self.trans_date_enter.grid(row=0, column=2)
        self.log_transit = Button(frame_under, text="Log Transit", command=self.back_take_trans).grid(row=0, column=3)


    def site_detail(self):
        self.currGui.withdraw()
        self.site_detail = Toplevel()
        self.currGui = self.site_detail
        self.site_detail.title("Transit Detail")

        Label(self.site_detail, text="Transit Detail").grid(row=0)

        frame = Frame(self.site_detail)
        frame.grid()

        Label(frame, text="Site ").grid(row=0, column=0)
        self.site = StringVar()
        self.site_enter = Entry(frame, textvariable=self.site)
        self.site_enter.grid(row=0, column=1)

        Label(frame, text="Open Everyday: ").grid(row=0, column=2)
        self.trans_type = StringVar()
        choices_type = ['Yes', 'No', 'All']
        self.trans_type.set('All')
        self.popup = OptionMenu(frame, self.trans_type, *choices_type)
        self.popup.grid(row=0, column=3)

        Label(frame, text="Address ").grid(row=1, column=0)
        self.address = StringVar()
        self.address_enter = Entry(frame, textvariable=self.address)
        self.address_enter.grid(row=1, column=1)

        frame_under = Frame(self.site_detail)
        frame_under.grid()

        Label(frame_under, text="Visit Date ").grid(row=0, column=1)
        self.visit_date = StringVar()
        self.visit_date_enter = Entry(frame_under, textvariable=self.visit_date)
        self.visit_date_enter.grid(row=0, column=2)
        self.log_visit = Button(frame_under, text="Log Visit", command=self.back_take_trans).grid(row=0, column=3)

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=1, column=2)

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

        Label(frame, text="Site ").grid(row=1, column=3)
        self.site = StringVar()
        choices_type = ['Yes', 'No', 'All']
        self.site.set('All')
        self.popup = OptionMenu(frame, self.site, *choices_type)
        self.popup.grid(row=1, column=4)

        Label(frame, text="Start Date").grid(row=2, column=1)
        self.start_date = StringVar()
        self.start_date_enter = Entry(frame, textvariable=self.start_date)
        self.start_date_enter.grid(row=2, column=2)

        Label(frame, text="End Date").grid(row=2, column=3)
        self.end_date = StringVar()
        self.end_date_enter = Entry(frame, textvariable=self.end_date)
        self.end_date_enter.grid(row=2, column=4)

        self.filter = Button(frame, text="Filter", command=self.filter_take_trans).grid(row=3, column=3)

        frame_tree = Frame(self.visit_history_gui)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree, columns=['Date', 'Event Name', 'Site', 'Price'],
                            show='headings')

        tree.heading('Date', text='Date')
        tree.heading('Event Name', text='Event Name')
        tree.heading('Site', text='Site')
        tree.heading('Price', text='Price')
        tree.insert("", "end", values=("1", "2", "3", "4"))
        tree.insert("", "end", values=("4", "5", "6", "7"))
        tree.grid(row=1, column=3)

        frame_under = Frame(self.visit_history_gui)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=0, column=0)





root = Tk()

app = App(root)

root.mainloop()