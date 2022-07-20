from random import shuffle


class BetterCode:
    def get_random_alphabet(self):
        j = range(0, 26)
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
