from mall import Mall

class DenizMall(Mall):
    def __init__(self, location, floor, hall_count):
        self.location = location
        self.floor = floor
        self.hall_count = hall_count
    def information(self):
        return"""
    Salam! Dəniz Mola Xoş Gəldin!
    -
    Ünvan: {}
    -
    Mərtəbə: {}
    -
    Zal sayı: {}
    """.format(self.location, self.floor, self.hall_count)