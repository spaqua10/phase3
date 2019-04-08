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
				passwd="savirahe",
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

            frame = Frame(self.navGUI)
            frame.grid()

            self.register = Button(self.navGUI, text="User Only", command = self.register_user).grid(row=1)
            self.register = Button(self.navGUI, text="Visitor Only", command = self.register_visitor).grid(row=2)
            self.register = Button(self.navGUI, text="Employee Only", command = self.register_employee).grid(row=3)
            self.register = Button(self.navGUI, text="Employee-Visitor", command = self.register_employee).grid(row=4)
            self.register = Button(self.navGUI, text="Back", command = self.back).grid(row=5)

###########################################################################
    def login(self):
        pass


###########################################################################
    def register_user(self):
        pass

###########################################################################
    def register_visitor(self):
        pass

###########################################################################
    def register_employee(self):
        pass

###########################################################################
    def back(self):
        self.navGUI.withdraw()
        self.firstGUI.deiconify()


root = Tk()

app = App(root)


root.mainloop()
