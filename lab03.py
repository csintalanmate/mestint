class Hanoi:
    def __init__(self,ke,c):
        self.kezde = ke
        self.cel = c


    def celteszt(self, allapot):
        return allapot == self.cel


    def rakovetkezo(self, a):
        gyerekek = []

        for melyiket in range(0,3):
            for hova in ['P', 'Q', 'R']:
                alkalmazhato = True
                if a[melyiket] != hova:
                    for i in range(0, melyiket):
                        if a[i] != a[melyiket] and a[i] != hova:
                            pass                #üres utasítás
                        else:
                            alkalmazhato = False
                            break
                else:
                    alkalmazhato = False

                if alkalmazhato:
                    tmp = list(a)
                    tmp[melyiket] = hova
                    uj_allapot = tuple(tmp)
                    gyerekek.append(("operator", uj_allapot))
                    #gyerekek.append((f"{melyiket}->{hova}", uj_allapot))               ez a hazi


        return gyerekek



if __name__ == "__main__":
    h = Hanoi(('P', 'P', 'P'), ('R', 'R', 'R'))