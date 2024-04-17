class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
    def menu(self):
        k=input("""
        press-1 For Create a new pin
        Press-2 For Change Your pin
        Press-3 For Know Your Balance
        Press-4 For Withdrawl
        Press-5 For Deposite Money
        Press-6 If You Want To Any Type Of Help
        Please Press Button :  """)
         

        if k=='1':
            self.createpin()
        elif k=='2':
           self.changepin()
        elif k=='3':
            self.knowBalance()
        elif k=='4':
            self.withdrawl()
        elif k=='5':
            self.deposite()
        elif k=='6':
            self.help()
        else:
            print("Please Enter Valid Your Input :")


    def createpin(self):
        pin1=input("Enter Your Pin:")
        self.pin=pin1
        amount=int(input("Enter Your Amount:"))
        self.balance=amount
        print("Your pin create Successfully")
        print("Thank You For giving Service")
        self.menu()

    def changepin(self):
        check_pin=input("Enter Your Old Pin : ")
        if check_pin==self.pin:
            change=input("Enter Your New Pin : ")
            self.pin=change
            print("Your Pin Change Successfully")
            print("Thank You For giving Service")
        else:
            print("Please Enter Correct Pin")
            print("Thank You For giving Service")
        self.menu()

    def knowBalance(self):
        pin2=input("Enter Your Pin : ")
        if pin2==self.pin:
            print(f"Your Total Balance = {self.balance}")
            print("Thank You For giving Service")
        else:
            print("Please Enter Your Correct Pin ")
            print("Thank You For giving Service")
        self.menu()

    def withdrawl(self):
        pin3=input("Enter Your Pin : ")
        if pin3==self.pin:
            amount2=int(input("Enter Your For Withdrawl Amount : "))
            if (self.balance >= amount2):
                self.balance=self.balance-amount2
                print("Your Withdrawl Is Successfully")
                print(f"Now Your rest amount = {self.balance}")
                print("Thank You For giving Service")
            else:
                print("You Have No Sufficient Amount ")
                print("Please Enter Sufficient Ammount ")
                print("Thank You For giving Service")
        else:
            print("Please Enter Correct Pin For Successful Withdrawl")
            print("Thank You For giving Service")
        self.menu()
    
    def deposite(self):
        pin4=input("Enter Your Pin : ")
        if pin4==self.pin:
            amount3=int(input("Enter Your Amount For Deposite : "))
            self.balance=amount3+self.balance
            print("Your Deposite Is Successfully")
            print(f"Your Total Current Balance Is {self.balance}")
            print("Thank You For giving Service")
        else:
            print("Please Enter Correct Pin For Deposite")
            print("Thank You For giving Service")
        self.menu()

    def help(self):
        print("""Keep your personal identification number (PIN) just that - personal. Never write it down or share it with anyone - not even family members. It's also a good idea to update your PIN number once a year to keep it fresh.
          1.  Be aware of your surroundings, particularly at night. If you see any suspicious activity, like a person waiting a few feet away or if there aren't any lights around, avoid using that machine and find another in a more public area.
         2.   Bring someone with you when using an ATM. If you can't find a buddy, use an ATM that is located in a public area like a convenience or grocery store. This way, store personnel are there to help and you'll have the video surveillance from both the store and the bank.
         3.   Have your debit card ready to go as you approach the ATM. If you need to search through your purse or wallet, you'll give criminals more of a chance to catch you off guard.
         4.   Use your body to “shield” the ATM keyboard as you enter your PIN. If someone seems to be lingering behind you, walk away and come back later.
        5.    Always take your receipts or transaction records with you. This  will avoid any of your personal information getting into the wrong hands.
        Do not count or visually display any money you received from the ATM. After taking your money out of the ATM, immediately place the cash in your purse or wallet, and count it later.
        6.    If you're using a drive-up ATM, be sure passenger windows are     rolled up and all doors are locked. If you leave your car and walk to the ATM, lock your car. It can also help to turn down the radio so you can be more alert.
        7.    Check the ATM for a card skimmer. A card skimmer is a device attached to the payment terminal of an ATM that is used to steal your card information when inserting your card to withdraw money. You can often spot a card skimmer with your own inspection. If the card reader slot feels loose or is oddly a different color scheme than the bank's branding, or the keyboard doesn't feel right (too thick, buttons don't press easily, etc.), these are often signs that a skimmer is in place.
        8.    If you keep these tips in mind, you'll be more aware of what's going on around you and help eliminate any potential risk to your financial and physical well-being! Our priority is to keep you safe and help you manage your finances, on your terms. Visit one of our convenient branch locations or find an ATM near you.""")
        print("Thank You For giving Service")
        self.menu()


obj=Atm()

