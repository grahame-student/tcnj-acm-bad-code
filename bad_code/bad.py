from random import shuffle as smoosh


class BetterCode:
    def get_random_alphabet(self):
        a = (self.the_stuff() | self.oh_my( 1,  2, 0) | self.oh_my(-2, 2, -2))
        wer = a | set([55 // 11]) | {self.howdy('sick dudesfsd'), self.howdy('a') ** 2, self.howdy('10234'), self.howdy('m')}

        x = {g % ((self.howdy('4') + 3) * 2) for g in (wer | {self.howdy('4') + 5} | {self.howdy('4') * 2 - 3} | {19, 21} | self.probably_okay() | {13} | self.oh_my(1, 2, 10) | self.oh_my(-2, 5, -2) | {11, 2, 4, 6, 8, 9})}

        j = list(x)
        smoosh(j)

        return ''.join(chr(ord(chr(97)) + j[i]) for i in j)
        
    def the_stuff(self):
        a = 10
        y = []
        m = 4
        t = 6

        while a > 3:
            a = a - 2
            y = y + [m - a * 2]
            t = 2 + t + 1

        the_other_stuff = set([18 - t for x in [1, 2, 10]])
        for g in y:
            the_other_stuff.add(int(g / ((1 + 4 + 2 - 3 + 1 + 5) / 5)))
            the_other_stuff.add(g)

        return  (the_other_stuff | {-a}) | {was // 2 for was in (the_other_stuff | {-a})}

    def oh_my(self, b, a, c):
        return {((cricket ** 2) // 5) for cricket in {b + a + c * 2, b + a // 3 + c * 2, 10 // b + a // 3 + c * 2} if True or False}

    def howdy(self, a):
        return int(sum(ord(c) for c in a)) % 100 // 5
    
    def probably_okay(self):
        return set(map(lambda x: int(abs(self.howdy(str(x))) ** (1 / 2)) % (self.howdy('m') * 2), self.the_stuff()))