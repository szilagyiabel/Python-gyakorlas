class Egy:

    def getMethodt1(self):

        print(" getMethod of Egy called ")

class Ketto(Egy):

    def getMethod(self):

        print(" getMethod of Ketto called ")

class Harom(Egy):

    def getMethod(self):

        print(" getMethod of Harom called ")

class Negy(Ketto,Harom):

    def getMethod2(self):

        print(" getMethod of Negy called ")        

obj=Negy()

obj. getMethod()