class Employee:
    '''doc string to rep any '''
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def info(self):
        print('*'*20)
        print('Employee number:',self.eno)
        print('Employee name:',self.ename)
        print('Employee esal:',self.esal)
        print('Employee eaddr:',self.eaddr)
e1=Employee(100,'Durga',10000,'Hyd')
e2=Employee(200,'Venu',5000,'Hyd')
e1.info()
e2.info()

    
        