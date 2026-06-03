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
        if user_input==1:
            pass
        elif user_input==2:
            pass
        elif user_input==3:
            pass
        elif user_input==4:
            pass
        else:
            exit()
obj=chatbook()
    