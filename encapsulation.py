class Dad():
    sampati = 'Jaminjaydad'
    publicpassword = '1234'
    __accountPass = 'PrivatePassword'
    _childPass = 'ProtectedPassword'
    def __init__(self) -> None:
        print("Dad init")

    def bankAccount(self, password):
        if self.__accountPass == password:
            print("account is malamal")
        elif self._childPass == password:
         print("Money withdrawn limit is 1k per day")
        else:
            print("Padhai karo")
    
    
    def getPassword(self):
        return self.__accountPass

    def setPassword(self, oldPass, newPass):
        if oldPass == self.__accountPass:
            self.__accountPass = newPass
        else:
            print("Please enter valid password")


class Beta(Dad):
    def __init__(self) -> None:
        super().__init__()
        print("Beta init")

beta = Beta()
print(beta.sampati)
beta.bankAccount('1234')

print(beta.publicpassword)
beta.bankAccount(beta.publicpassword) 

print(beta._childPass)    #'Beta' object has no attribute '__accountPass'.
print(Dad._childPass)    # need to revisit.
dad = Dad()
print(dad._childPass)

print(Dad.publicpassword)   #1234
Dad.publicpassword = "mypassword"       # 
print(Dad.publicpassword)