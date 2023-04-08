
def get_money():
    valid_input = False
    while not valid_input:
        try:
            money = float(input("Vəsait: "))
            valid_input = True
        except ValueError:
            print("Xəta! Məbləğ daxil et.")
    return money

def set_money(money):
    return round(money, 2)



def film_al(select_film, saat_araligi, meblegg):
    meblegg = set_money(meblegg)
    if select_film == 1:
        if saat_araligi == 1 or saat_araligi == 2:
            fiyat = 12
            if meblegg >= fiyat:
                meblegg -= fiyat
                print("Film uğurla alındı. Qalıq pulunuz:", set_money(meblegg), "AZN")
            else:
                print("Kifayət qədər vəsait yoxdur!")
        else:
            print("Xəta!")
    elif select_film == 2:
        if saat_araligi == 1 or saat_araligi == 2:
            fiyat = 20
            if meblegg >= fiyat:
                meblegg -= fiyat
                print("Film uğurla alındı. Qalıq pulunuz:", set_money(meblegg), "AZN")
            else:
                print("Kifayət qədər vəsait yoxdur!")
        else:
            print("Xəta!")
    elif select_film == 3:
        if saat_araligi == 1 or saat_araligi == 2:
            fiyat = 5
            if meblegg >= fiyat:
                meblegg -= fiyat
                print("Film uğurla alındı. Qalıq pulunuz:", set_money(meblegg), "AZN")
            else:
                print("Kifayət qədər vəsait yoxdur!")
        else:
            print("Xəta!")
    elif select_film == 4:
        if saat_araligi == 1 or saat_araligi == 2:
            fiyat = 13
            if meblegg >= fiyat:
                meblegg -= fiyat
                print("Film uğurla alındı. Qalıq pulunuz:", set_money(meblegg), "AZN")
            else:
                print("Kifayət qədər vəsait yoxdur!")
        else:
            print("Xəta!")
    elif select_film == 5:
        if saat_araligi == 1 or saat_araligi == 2:
            fiyat = 19
            if meblegg >= fiyat:
                meblegg -= fiyat
                print("Film uğurla alındı. Qalıq pulunuz:", set_money(meblegg), "AZN")
            else:
                print("Kifayət qədər vəsait yoxdur!")
    else:
        print("Xəta! Seçdiyiniz film mövcud deyil.")
        exit()


