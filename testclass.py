class user:
    name= ""
    email= ""
    password= ""
    login= False

    def __init__(self, name,email,password):
        self.name = name
        self.email= email
        self.password= password

    def login(self):
        email = input(" Enter Email: ")
        password= input("Enter Password: ")

        if email == self.email and password == self.password:
            login= True
            print(" Welcome")
        else:
            print(" Login Failed")

        def logout(self):
            login= False
            print(" Logged Out")


user1= user("tuhin","tuhinbabu@gmail.com","123")



user1.login()











Hello= input()