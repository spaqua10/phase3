from tkinter import *
from tkinter import ttk, messagebox



class App:

    ###########################################################################
    # this function pulls up the initial gui, of the initial log in window

    def __init__(self, master):
        self.currGui = None
        self.prevGUI = None
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

        self.new5 = Button(master, text = "Staff-Visit Fun", command = self.staff_visitor_functionality)
        self.new5.grid(row = 14)

        self.new6 = Button(master, text = "Visitor", command = self.visitor_functionality)
        self.new6.grid(row = 15)

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
        self.navGUI = Toplevel()
        self.currGui = self.navGUI
        self.navGUI.title("User Functionality")

        Label(self.navGUI, text="User Functionality").grid(row=1)

        frame = Frame(self.navGUI)
        frame.grid()


        self.register = Button(self.navGUI, text="Take Transit", command=self.take_transit).grid(row=2)
        self.register = Button(self.navGUI, text="View Transit History", command=self.view_transit_history).grid(row=3)
        self.register = Button(self.navGUI, text="Back", command=self.register_employee).grid(row=4)

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
        self.register = Button(self.manVisGUI, text="View Site Report", command=self.view_site_report).grid(row=2, column=1)
        self.register = Button(self.manVisGUI, text="Explore Event", command=self.explore_event).grid(row=3, column=1)
        self.register = Button(self.manVisGUI, text="View Transit History", command=self.view_transit_history).grid(row=4, column=1)
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
        self.register = Button(self.staffOnlyGUI, text="View Transit History", command=self.view_transit_history).grid(row=5)
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

        self.register = Button(self.staffVisGUI, text="Explore Event", command=self.explore_event).grid(row=2, column = 1)
        self.register = Button(self.staffVisGUI, text="Explore Site", command=self.explore_site).grid(row=3, column = 1)
        self.register = Button(self.staffVisGUI, text="View Visit History", command=self.view_visit_history).grid(row=4, column = 1)
        self.register = Button(self.staffVisGUI, text="Back", command=self.staff_vis_back).grid(row=5, column = 1)

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
    def view_schedule(self):
        pass

    def view_site_report(self):
        pass

    def view_staff(self):
        pass

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

        Label(frame, text="Duration Range").grid(row = 2, column = 0)
        self.duration_lower = StringVar()
        self.duration_lower_enter = Entry(frame, textvariable=self.duration_lower)
        self.duration_lower_enter.grid(row = 2, column = 1)

        Label(frame, text=" -- ").grid(row = 2, column = 2)
        self.duration_upper = StringVar()
        self.duration_upper_enter = Entry(frame, textvariable=self.duration_upper)
        self.duration_upper_enter.grid(row = 2, column = 3)

        Label(frame, text="Total Visits Range").grid(row = 2, column = 4)
        self.visits_lower = StringVar()
        self.visits_lower_enter = Entry(frame, textvariable=self.visits_lower)
        self.visits_lower_enter.grid(row = 2, column = 5)

        Label(frame, text=" -- ").grid(row = 2, column = 6)
        self.visits_upper = StringVar()
        self.visits_upper_enter = Entry(frame, textvariable=self.visits_upper)
        self.visits_upper_enter.grid(row = 2, column = 7)

        Label(frame, text="Total Revenue Range").grid(row = 3, column = 0)
        self.revenue_lower = StringVar()
        self.revenue_lower_enter = Entry(frame, textvariable=self.revenue_lower)
        self.revenue_lower_enter.grid(row = 3, column = 1)

        Label(frame, text=" -- ").grid(row = 3, column = 2)
        self.revenue_upper = StringVar()
        self.revenue_upper_enter = Entry(frame, textvariable=self.revenue_upper)
        self.revenue_upper_enter.grid(row = 3, column = 3)

        self.filter = Button(frame, text="Filter", command=self.filter_take_trans).grid(row=4, column=0)
        self.create = Button(frame, text="Create", command=self.filter_take_trans).grid(row=4, column=1)
        self.view = Button(frame, text="View/Edit", command=self.filter_take_trans).grid(row=4, column=2)
        self.delete = Button(frame, text="Delete", command=self.filter_take_trans).grid(row=4, column=3)


        frame_tree = Frame(self.manage_event)
        frame_tree.grid()

        tree = ttk.Treeview(frame_tree, columns=['Name', 'Staff Count', 'Duration (Days)', 'Total Visits', 'Total Revenue'],
                            show='headings')

        tree.heading('Name', text='Name')
        tree.heading('Staff Count', text='Staff Count')
        tree.heading('Duration (Days)', text='Duration (Days)')
        tree.heading('Total Visits', text='Total Visits')
        tree.heading('Total Revenue', text="Total Revenue")
        tree.insert("", "end", values=("1", "2", "3", "4", "6"))
        tree.insert("", "end", values=("4", "5", "6", "7", "8" ))
        tree.grid(row=1, column=3)

        frame_under = Frame(self.manage_event)
        frame_under.grid()

        self.back = Button(frame_under, text="Back", command=self.back_take_trans).grid(row=0, column=0)

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

        Label(frame, text="End Date").grid(row = 1, column = 4)
        self.end_date = StringVar()
        self.end_date_enter = Entry(frame, textvariable=self.end_date)
        self.end_date_enter.grid(row = 1, column = 5)

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

        tree = ttk.Treeview(frame_tree, columns=['Route', 'Transport Type', 'Price', '# Connected Sites', '# Transit Logged'],
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
        self.price_enter.grid(row = 0, column = 5)

        Label(frame, text="Connected Sites").grid(row = 1, column = 0)

        list = Listbox(frame, selectmode=MULTIPLE)
        list.insert(0, 'Atlanta Beltline Center')
        list.insert(1, 'Gorden-White Park')
        list.insert(2, 'Inman Park')
        list.grid(row=1, column = 1)

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
        Label(frame, text="Bus").grid(row = 0, column = 1)

        Label(frame, text="Route").grid(row=0, column=2)
        self.route = StringVar()
        self.route_enter = Entry(frame, textvariable=self.route)
        self.route_enter.grid(row=0, column=3)

        Label(frame, text="Price").grid(row=0, column=4)
        self.price = IntVar()
        self.price_enter = Entry(frame, textvariable=self.price)
        self.price_enter.grid(row = 0, column = 5)

        Label(frame, text="Connected Sites").grid(row = 1, column = 0)

        list = Listbox(frame, selectmode=MULTIPLE)
        list.insert(0, 'Atlanta Beltline Center')
        list.insert(1, 'Gorden-White Park')
        list.insert(2, 'Inman Park')
        list.grid(row=1, column = 1)

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
        self.delete = Button(frame, text='Delete', command = self.decline_user).grid(row = 2, column = 3)

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

        #Label(frame, text="Open Everyday").grid(row=2, column=3)
        self.open = IntVar()
        Checkbutton(frame, text = "Open Everyday", variable = self.open).grid(row = 2, column = 2)



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

root = Tk()

app = App(root)

root.mainloop()
