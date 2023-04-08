from mall import Mall

class Aygunmoll(Mall):
    def __init__(self, location, floor, hall_count):
        self.location = location
        self.floor = floor
        self.hall_count = hall_count

    def information(self):
        return"""
    Salam! Aygün Mola Xoş Gəldin!
    -
    Ünvan: {}
    -
    Mərtəbə: {}
    -
    Zal sayı: {}
""".format(self.location, self.floor, self.hall_count)