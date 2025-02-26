#3 kancsó probléma
class kancso_prolema:
    def __init__(self, ke, c):
        self.kezdo = ke
        self.cel = c
        self.MAX1 = 3
        self.MAX2 = 5
        self.MAX3 = 8


    def celteszt(self, a):
        return a[1] == self.cel or a[2] == self.cel


    def rakovetkezo(self, a):
        a1,a2,a3 = a
        gyerekek = []

        if a1 != 0 and a2 != self.MAX2:



if __name__ == "__main__":
    kancso = kancso_prolema((0,0,8),4)