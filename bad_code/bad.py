from random import shuffle as smoosh


class BetterCode:
    def get_random_alphabet(self):
        wer = (
            {0, -12, -1, -8, -6, -4, -3, -2}
            | {0, 1, 20}
            | {16, 3, 7}
            | {5}
            | {1, 361, 10, 1}
            | {15}
            | {17}
            | {19, 21}
            | {0, 1}
            | {13}
            | {88, 105, 180}
            | {0, 12, 5}
            | {11, 2, 4, 6, 8, 9}
        )

        x = {
            g % 26
            for g in (
                wer
            )
        }

        j = list(x)
        smoosh(j)

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
