import acs, mb

exited = False

connectors = []

"""Here is a custom class for creating custom command managers."""

class Receiver:
    def __init__(self, catchphrase, descr="default description"):
        self.catchphrase = catchphrase
        self.descr = descr
    
    def connect(self,system):
        system.append(self)
    
    def on_called(self):
        pass

class Remover(Receiver):

    def on_called(self):
        print("Please enter a mode you want to remove alphabet/digit-set: ")
        answer = input().lower()
        if answer[0] == "a":
            for i in range(len(acs.abcs)):
                print(i, "-", acs.abcs[i])
            acs.abcs.pop(int(input("Enter the index of the alphabet: ")))
            print("Alphabet Removed. Awaiting further command: ")
        elif answer[0] == "d":
            for i in range(len(acs.digits)):
                print(i, "-", acs.digits[i])
            acs.digits.pop(int(input("Enter the index of the digit-set: ")))
            print("Digit-set Removed. Awaiting further command. ")

mbadder = Receiver("addmb", "initiates the adding system for the mb language.")
mbd = Receiver("mb", "initiates the mb encoding console.")
def mbdf():
    mb.main()
mbd.on_called = mbdf
mbd.connect(connectors)
def adder():
    print("You are trying to add an alphabet to mb.")
    abc = input("Please enter the alphabet in a long string.")
    mb.add_abc(abc)
mbadder.on_called = adder
mbadder.connect(connectors)
remover = Remover("removeacs", "initiates the removing system for the language acs.")
remover.connect(connectors)
while not exited:
    answer = input("Command: ")
    if answer == "exit":
        exited = True
    elif answer == "acs":
        acs.main()
    elif answer == "addacs":
        mode = input("Alphabet or digit-set? ").lower()
        if mode[0] == "a":
            abc = input("Please enter the alphabet in a long string: ")
            acs.add_abc(abc)
            print("Alphabet has been registered.")
        elif mode[0] == "d":
            digitset = []
            for i in range(5):
                digitset.append(input(f"Enter the char for {i}: "))
            acs.add_digits(digitset)
            print("Digit-set has been registered.")
    elif answer == "help":

        print("Default commands are:\n")
        print("""
exit - exits the whole thing.
acs - launches the acs language.
addacs - initiates the adding interface of the acs language.
help - you just typed this command.
""")

        print("Customly added extensions (receivers):\n")

        for i in connectors:
            print(i.catchphrase, "-", i.descr)
        print("\n")
    else:
        for i in connectors:
            if answer == i.catchphrase:
                i.on_called()

