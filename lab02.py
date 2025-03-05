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
            T = min(a1, self.MAX2 - a2)
            uj_allapot = (a1 - T, a2 + T, a3)
            gyerekek.append(("1->2", uj_allapot))


        if a1 != 0 and a3 != self.MAX3:
            T = min(a1, self.MAX3 - a3)
            uj_allapot = (a1 - T, a2, a3 + T)
            gyerekek.append(("1->3", uj_allapot))


        if a2 != 0 and a1 != self.MAX1:
            T = min(a2, self.MAX1 - a1)
            uj_allapot = (a1 + T, a2 - T, a3)
            gyerekek.append(("2->1", uj_allapot))


        if a2 != 0 and a3 != self.MAX3:
            T = min(a2, self.MAX3 - a3)
            uj_allapot = (a1, a2 - T, a3 + T)
            gyerekek.append(("2->3", uj_allapot))


        if a3 != 0 and a1 != self.MAX1:
            T = min(a3, self.MAX1 - a1)
            uj_allapot = (a1 + T, a2, a3 - T)
            gyerekek.append(("3->1", uj_allapot))


        if a3 != 0 and a2 != self.MAX2:
            T = min(a3, self.MAX2 - a2)
            uj_allapot = (a1, a2 + T, a3 - T)
            gyerekek.append(("3->2", uj_allapot))


        return gyerekek



if __name__ == "__main__":
    kancso = kancso_prolema((0,0,8),4)