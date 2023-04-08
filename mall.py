class Mall:
    def __init__(self, DenizMall, GanjaMall, GanjlikMall, IyirmisekkizMall, Aygunmoll):
        self.DenizMall = DenizMall
        self.GanjaMall = GanjaMall
        self.GanjlikMall = GanjlikMall
        self.IyirmisekkizMall = IyirmisekkizMall
        self.Aygunmoll = Aygunmoll

    def enter_time(self, time):
        if 8 <= int(time) <= 23:
            print("Mola giriş saatı açıqdır")
        else:
            print("Moll Bağlıdır!")
            exit()

    def your_age(self, age):
        if age >= 18:
            print("Mola giriş yaşınız uyğundur")
        else:
            print("Mola giriş yaşınız uyğun deyildir!")
            exit()


    def vaccine(self, vaccine):
        try:
            if vaccine == "B":
                print("Siz peyvənd olunmusunuz")
            else:
                print("Siz peyvənd olunmamısınız!")
                exit()
        except ValueError:
            print("Yanlış veri girdiniz!")









