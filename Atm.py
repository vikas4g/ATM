class Atm:
    def __init__(self):
        #use of Abstraction we hide data members with private keyword ( __ )
        self.__pin=""
        self.__blance=0
        self.menu()
    def menu(self):
        print(""" 
              ********** Wellcome *********
              How whould you like to proced
              1 press 1 to create pin
              2 press 2 to deposite
              3 press 3 to withdraw
              4 press 4 to check blance 
              5 press 5 to exit""")
        choice=input("enter : ")
        if choice=="1":
            self.create_pin()
        elif choice=="2":
            self.deposite()
        elif choice=="3":
            self.withdraw()
        elif choice=="4":
            self.check_blance()
        else:
            print("thank you : your exit")
    
    def create_pin(self):
        self.pin=input("enter your pin : ")
        print("pin set succesfuly")
        self.menu()
    
    def deposite(self):
        temp = input("enter pin : ")
        if temp==self.pin:
            amount=int(input("enter amount : "))
            self.blance=self.blance+amount
            print("deposit succesfuly")
        else:
            print("invalid pin")
        self.menu()   
    
    def withdraw(self):
        temp = input("enter pin : ")
        if temp==self.pin:
            amount=int(input("enter amount : "))
            if amount<self.blance:
                self.blance = self.blance - amount
                print("succesfully withdraw")
            else:
                print("infissient blance")
        else:
            print("invalide pin")
        self.menu()

    def check_blance(self):
        temp = input("enter pin : ")
        if temp==self.pin:
          print(self.blance)
        else:
            print("invaild pin")
            
        self.menu()
        
# vikas = Atm()
harsh = Atm()
harsh.blance()
