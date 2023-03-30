class Dad():       # Inheritance.. Dad class inherited from Human (abstract class).. so we need to define or implement all abtract methods present in Human class
    sampatti = 'JaminJaydad'
    publicpassword = '1234'         # public attribute
    __accountPass = 'PrivatePassword'   # private attribute when we provide __ double underscore before attribute name
    _childPass = 'protectedPassword'    # protected attribute when we provide _ single underscore before attribute name
    def __init__(self) -> None: # as soon as obejct gets created and before assing to obejct variable in left side
        print("Dad init")

    def bankAccount(self, password):
        if self.__accountPass == password:
            print("account is malamal")
        elif self._childPass ==  password:
            print("Money withdraw limit is 1k per day")
        else:
            print("padhai karo.. pahila number lana then try to access")


    def getPassword(self):  #getter #read only private attribute#   # public method inside we are accessing private attribute
        return self.__accountPass
    
    def setPassword(self, oldPass, newPass):    # setter # to update private attribute in restricted way/ in controlled manner 
        if oldPass == self.__accountPass:
            self.__accountPass = newPass
        else:
            print("Please enter correct password")

class Mom():
    def __init__(self) -> None:
        super().__init__()      #Human init # super points to base class which Human
        print("Mom Cooking")   #Mom Init

    def speak(self):        # abstract method
        print("Speak Hindi")
    
    def walk(self):         # abstract method
        print("slow walk")

class Beta(Dad):
    def __init__(self) -> None:
        super().__init__()  
        print("Beta init")

beta = Beta()
print(beta.sampatti)        #JaminJaydad    # inherited from base class Dad
beta.bankAccount('1234')  #account is malamal

print(beta.publicpassword)    #1234
beta.bankAccount(beta.publicpassword)

## We can not access private attribute of any class outside of that class

#print(beta.__accountPass)    #'Beta' object has no attribute '__accountPass'.
#print(Dad.__accountPass)    #'Dad' has no attribute '__accountPass'.
# dad = Dad()
# print(dad.__accountPass)    #'Dad' has no attribute '__accountPass'.beta.bankAccount('1234')  #account is malamal
beta.bankAccount('PrivatePassword')  #account is malamal

print(beta._childPass)    #'Beta' object has no attribute '__accountPass'.
print(Dad._childPass)    # need to revisit.
dad = Dad()
print(dad._childPass)    # need to revisit.

print(Dad.publicpassword)   #1234
Dad.publicpassword = "mypassword"       # 
print(Dad.publicpassword)