from mall import Mall
from deniz_mall import DenizMall
from ganja_mall import GanjaMall
from genclik_mall import GanjlikMall
from irmisekkiz import IyirmisekkizMall
from aygun_mall import Aygunmoll
from human import worker, musteri
from money import film_al
from movie import *

print("""
Kim giriş edir?:

İşçi - 1
Müştəri - 2

"""

)
try:
    person_selection = int(input("Seç: "))
    if person_selection == 1:
        print(worker.Person1())
    elif person_selection == 2:
        print(musteri.Person2())
    else:
        print("Xəta: Qaqam nağaysan aa!")
        exit()
except ValueError:
    print("Xəta: Rəqəm daxil edin. Hərf yox!")
    exit()



print("""
Getmək istədiyiniz ticarət mərkəzini seçin!

Dəniz Mall : 1
Gəncə Mall : 2
Gənclik Mall : 3
28 Mall : 4
Aygün Mall : 5

""")

deniz_mall = DenizMall("Bakı", "4", "7")
ganja_mall = GanjaMall("Gəncə", "5", "6")
ganjlik_mall = GanjlikMall("Gənclik ", "4", "7")
irmisekkiz_mall = IyirmisekkizMall("28 may", "5", "6")
aygun_mol = Aygunmoll("Bakıxanov", "3", "5")



try:
    select_mall = int(input("Mall seç: "))
    if select_mall == 1:
        deniz_mall.enter_time(int(input("Giriş saatınız: ")))
        deniz_mall.your_age(int(input("Yaşınız: ")))
        deniz_mall.vaccine(input("Karonavirus Vaksinasiyaniz var? (B/X): "))
        print(deniz_mall.information())
    elif select_mall == 2:
        ganja_mall.enter_time(int(input("Giriş saatınız: ")))
        your_age = int(input("Yaşınız: "))
        ganja_mall.vaccine(input("Karonavirus Vaksinasiyaniz var? (B/X): "))
        print(ganja_mall.information())    
    elif select_mall == 3:
        ganjlik_mall.enter_time(int(input("Giriş saatınız: ")))
        ganjlik_mall.your_age(int(input("Yaşınız: ")))
        ganjlik_mall.vaccine(input("Karonavirus Vaksinasiyaniz var? (B/X): "))
        print(ganjlik_mall.information())
    elif select_mall == 4:
        irmisekkiz_mall.enter_time(input("Giriş saatınız: "))
        irmisekkiz_mall.your_age(int(input("Yaşınız: ")))
        irmisekkiz_mall.vaccine(input("Karonavirus Vaksinasiyaniz var? (B/X): "))
        print(irmisekkiz_mall.information())
    elif select_mall == 5:
        aygun_mol.enter_time(int(input("Giriş saatınız: ")))
        aygun_mol.your_age(int(input("Yaşınız: ")))
        aygun_mol.vaccine(input("Karonavirus Vaksinasiyaniz var? (B/X): "))
        print(aygun_mol.information())
    else:
        print(f'{select_mall} dənə mol görmürsən axı məni yorma :/')
        exit()
except ValueError:
    print("Xəta: Rəqəm daxil edin. Hərf yox!")
    exit()
    

print("""
İzləmək istədiyiniz filmi seç!
    Budur bizim filmlərimiz:
 - - - - - - - - - - - - - - -

Təhminə - 1
Komedi Xana - 2
Bozbash Pictuers - 3
Yuxu - 4
Bizim Cəbiş Müəllim - 5

""")
tehmine = Tehmine(
    "Təhminə", 
    1994, 8.8, 
    "Drama", 
    "2 saat 22 dəqiqə", 
    "Cristopher Nolan", 
    Hours("10", "12", "12", "14"), 
    12)
#  - - - -
komedixana = Komedixana(
    "Komedi Xana", 
    2020, 6.5, 
    "Komedi", 
    "1 saat", 
    "Ənvər Abbas", 
    Hours("10", "12", "12", "14"), 
    20)
#  - - - -
bozbashh = Bozbashh(
    "Bozbash Pictuers", 
    2011, 3.9, 
    "Gülməli", 
    "45 dəq", 
    "İlkin Həsənli", 
    Hours("10", "12", "12", "14"), 
    5)
#  - - - -
yuxu = Yuxu(    
    "Yuxu", 
    2001, 8.4, 
    "Komedi", 
    "1 saat 19 dəqiqə", 
    "Fikrət Əliyev", 
    Hours("10", "12", "12", "14"), 
    13)
#  - - - -
bizimcebismellim = Bizimcebismellim(    
    "Bizim Cəbiş Müəllim", 
    1969, 8.6, 
    "Maraqlı", 
    "1 saat 13 dəq", 
    "Hasan Seyidbaylı", 
    Hours("10", "12", "12", "14"),    
    19)
#  - - - -

try:
    select_film = int(input("Seç: "))
    if select_film == 1:
        print(tehmine.info_film())
        tehmine.year_info()
        print("Dram filmidir")
        tehmine.imdb_film()
    elif select_film ==2:
        print(komedixana.info_film())
        komedixana.year_info()
        print("Komedi filmidir")
        komedixana.imdb_film()
    elif select_film ==3:
        print(bozbashh.info_film())
        bozbashh.year_info()
        print("Komedi filmidir")
        bozbashh.imdb_film()
    elif select_film ==4:
        print(yuxu.info_film())
        yuxu.year_info()
        print("Tammetrajlı bədii filmdir")
        yuxu.imdb_film()
    elif select_film ==5:
        print(bizimcebismellim.info_film())
        bizimcebismellim.year_info()
        print("Dram, Komedi, Savaş")
        bizimcebismellim.imdb_film()
    else:
        print(f'{select_film} qədər film yoxdur.')
        exit()
except ValueError:
    print("Nagaysan qaqam :/ Ancaq 1-5 arası seçim et.")
    exit()

print("""
Seans saatlarini sec!
 - - - - - - - - - - - - - - -
1) 10 - 12
2) 12 - 14

""")
try:
    saat_araligi = int(input("Seç: "))
    if select_film == 1:
        if saat_araligi == 1:
            print("Təhminə filmi mövcud seans: 10 - 12")
            print("Filmin mövcud qiyməti: 12 AZN")
        elif saat_araligi == 2:
            print("Təhminə filmi mövcud seans: 12 - 14")
            print("Filmin mövcud qiyməti: 12 AZN")
        else:
            print("Xəta!")
            exit()
    elif select_film == 2:
        if saat_araligi == 1:
            print("Komedi Xana filmi mövcud seans: 10 - 12")
            print("Filmin mövcud qiyməti: 20 AZN")
        elif saat_araligi == 2:
            print("Komedi Xana filmi mövcud seans: 12 - 14")
            print("Filmin mövcud qiyməti: 20 AZN")
        else:
            print("Xəta!")
            exit()
    elif select_film == 3:
        if saat_araligi == 1:
            print("Bozbash Pictuers filmi mövcud seans: 10 - 12")
            print("Filmin mövcud qiyməti: 5 AZN")
        elif saat_araligi == 2:
            print("Bozbash Pictuers filmi mövcud seans: 12 - 14")
            print("Filmin mövcud qiyməti: 5 AZN")
        else:
            print("Xəta!")
            exit()
    elif select_film == 4:
        if saat_araligi == 1:
            print("Yuxu filmi mövcud seans: 10 - 12")
            print("Filmin mövcud qiyməti: 13 AZN")
        elif saat_araligi == 2:
            print("Yuxu filmi mövcud seans: 12 - 14")
            print("Filmin mövcud qiyməti: 13 AZN")
        else:
            print("Xəta!")
            exit()
    elif select_film == 5:
        if saat_araligi == 1:
            print("Bizim Cəbiş Müəllim filmi mövcud seans: 10 - 12")
            print("Filmin mövcud qiyməti: 19 AZN")
        elif saat_araligi == 2:
            print("Bizim Cəbiş Müəllim filmi mövcud seans: 12 - 14")
            print("Filmin mövcud qiyməti: 19 AZN")
        else:
            print("Xəta!")
            exit()
except ValueError:
    print("Xəta!")
    exit()

print("Siz seçilmiş filimin biletini almaq istədiyinizə əminsinizsə (B\X) seçin.")


alll_filmi = input("Seç: ")
if alll_filmi == "B":
    pass
elif alll_filmi == "X":
    print("Siz alış etmədiniz!")
    exit()
else:
    print("Nagaysan qaqam :/ Ancaq B-X seçimi et.")
    exit()


try:
    meblegg = int(input("Vəsait girin: "))
except:
    print("Yalnız qiymət daxil edə bilərsən!")
    exit()
    
film_al(select_film, saat_araligi, meblegg)







