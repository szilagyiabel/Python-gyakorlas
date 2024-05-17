class Alma:
    def __init__(self, x):
        self.x = x

    def count(self, x):
        self.x = x + 1

class ZoldAlma(Alma):
    def __init__(self, y=0):
        super().__init__(3)  # Javítottuk a szülő osztály konstruktorának meghívását
        self.y = y

    def count(self):
        self.y += 1

def main():
    obj = ZoldAlma()
    obj.count()
    print(obj.x, obj.y)

main()