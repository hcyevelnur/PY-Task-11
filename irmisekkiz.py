from mall import Mall

class IyirmisekkizMall(Mall):
    def __init__(self, location, floor, hall_count):
        self.location = location
        self.floor = floor
        self.hall_count = hall_count


    def information(self):
        return"""
    Salam! 28 Mala Xoş Gəldin!
    -
    Ünvan: {}
    -
    Mərtəbə: {}
    -
    Zal sayı: {}
    """.format(self.location, self.floor, self.hall_count)
    