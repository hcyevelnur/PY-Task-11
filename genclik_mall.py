from mall import Mall

class GanjlikMall(Mall):
    def __init__(self, location, floor, hall_count):
        self.location = location
        self.floor = floor
        self.hall_count = hall_count

    def information(self):
        return"""
    Salam! Gənclik Mola Xoş Gəldin!
    -
    Ünvan: {}
    -
    Mərtəbə: {}
    -
    Zal sayı: {}
""".format(self.location, self.floor, self.hall_count)