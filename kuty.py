
class Kutya:

    def __init__(self):

        self.kor = 1

    def csere(self):

        self.kor = 10

class Nemetjuhasz(Kutya):

    def csere(self):

        self.kor=self.kor+1

        return self.kor

def main():

    obj = Nemetjuhasz()

    print(obj.csere())

main()