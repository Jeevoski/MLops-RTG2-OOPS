class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()

    def menu(self):
        user_input=input("""welcome to chatbook,how would you like to proceed
                        1.press 1 to signup
                        2.press 2 to sign in
                        3.press 3 to post
                        4.press 4 to chat
                        5.press any key to signout""")
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.mypost()
        elif user_input=="4":
            pass
        else:
            exit()

    def signup(self):
        email=input("please enter your email")
        pwd = input("please enter your password")
        self.username=email
        self.password=pwd
        print("you have signed in successfully")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input("enter your email/username here -> ")
            pwd = input("enter your password here -> ")

        if self.username == uname and self.password == pwd:
            print("You have signed in successfully !!")
            self.loggedin = True
        else:
            print("please input correct credentials..")

        print("\n")
        self.menu()
    def mypost(self):
        if self.loggedin==True:
            txt=input("enter the content for the post")
            print(f"the post is uploaded{txt}")
        else:
            print("please sign in to post")
        print("\n")
        self.menu()

obj=chatbook()



    