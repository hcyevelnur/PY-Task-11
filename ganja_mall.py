from mall import Mall

class GanjaMall(Mall):
    def __init__(self, location, floor, hall_cout):
        self.location = location
        self.floor = floor
        self.hall_count = hall_cout
    def information(self):
        return"""
    Salam! Gəncə Mola Xoş Gəldin!
    -
    Ünvan: {}
    -
    Mərtəbə: {}
    -
    Zal sayı: {}
""".format(self.location, self.floor, self.hall_count)