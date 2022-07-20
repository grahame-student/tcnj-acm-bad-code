from random import shuffle


class BetterCode:
    def get_random_alphabet(self):        
        x = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}
        j = list(x)
        shuffle(j)
        return "".join(chr(ord(chr(97)) + j[i]) for i in j)

    def the_stuff(self):
        return {0, -12, -1, -8, -6, -4, -3, -2}

    def oh_my(self, b, a, c):
        return {
            ((cricket**2) // 5)
            for cricket in {b + a + c * 2, b + a // 3 + c * 2, 10 // b + a // 3 + c * 2}
            if True or False
        }

    def howdy(self, a):
        return int(sum(ord(c) for c in a)) % 100 // 5

    def probably_okay(self):
        return {0, 1}
