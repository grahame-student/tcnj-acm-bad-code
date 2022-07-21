from deprecated import deprecated
from random import shuffle


class BetterCode:
    def get_random_alphabet(self):
        j = list(range(0, 26))
        shuffle(j)
        return "".join(chr(ord("a") + j[i]) for i in j)

    @deprecated(reason="This method is deprecated and will be removed in a future version")
    def the_stuff(self):
        return {0, -12, -1, -8, -6, -4, -3, -2}

    @deprecated(reason="This method is deprecated and will be removed in a future version")
    def oh_my(self, b, a, c):
        values = {b + a + c * 2, b + a // 3 + c * 2, 10 // b + a // 3 + c * 2}
        return {
            ((value**2) // 5)
            for value in values
        }

    @deprecated(reason="This method is deprecated and will be removed in a future version")
    def howdy(self, a):
        return int(sum(ord(c) for c in a)) % 100 // 5

    @deprecated(reason="This method is deprecated and will be removed in a future version")
    def probably_okay(self):
        return {0, 1}
