from mall import Mall
class Hours:
    def __init__(self, seans1_start_time, seans1_end_time, seans2_start_time, seans2_end_time):
        self.seans1_start_time = seans1_start_time
        self.seans1_end_time = seans1_end_time
        self.seans2_start_time = seans2_start_time
        self.seans2_end_time = seans2_end_time
        
    def __str__(self):
        return "Seans 1: {} - {} : Seans 2: {} - {}".format(self.seans1_start_time, self.seans1_end_time, self.seans2_start_time, self.seans2_end_time)


class Movie:
    def __init__(self, name, year, imdb, genre, duration, directory, hours, price):
        self.name = name
        self.year = year
        self.imdb = imdb
        self.genre = genre
        self.duration = duration
        self.directory = directory
        self.hours = hours 
        self.price = price

    def name_film(self, name):
        print(name)


    def year_info(self):
        if self.year >= 2000:
            print("Fİlm yenidir")
        else:
            print("Fİlm köhnədir")

    def imdb_film(self):
        try:
            imdb = int(self.imdb)
            if imdb >= 9:
                print("Film qiymətləndirilir - A+")
            elif imdb >= 8:
                print("Film qiymətləndirilir - A")
            elif imdb >= 7:
                print("Film qiymətləndirilir - B")
            elif imdb >= 6:
                print("Film qiymətləndirilir - C")
            elif imdb >= 5:
                print("Film qiymətləndirilir - D")
            else:
                print("Film qiymətləndirilir - F")
        except ValueError:
            print("IMDB reytinqi etibarlı deyil.")

    
    def genre_film(self, genre):
        print(genre)

    def duration_film(self, duration):
        print(duration)

    def directory_film(self, directory):
        print(directory)

    def hours_film(self, hours):
        print(hours)

class Tehmine(Movie):
    def __init__(self, name, year, imdb, genre, duration, directory, hours, price):
        super().__init__(name, year, imdb, genre, duration, directory, hours, price)

    def info_film(self):
        return"""
        Adı: {}
        -
        İli: {}
        -
        IMDB: {}
        -
        Janr: {}
        -
        Müddət: {}
        -
        Film rejissoru: {}
        -
        {}
        -
        Qiymət: {} AZN
        """.format(self.name, self.year, self.imdb, self.genre, self.duration, self.directory, self.hours, self.price)




class Komedixana(Movie):
    def __init__(self, name, year, imdb, genre, duration, directory, hours, price):
        super().__init__(name, year, imdb, genre, duration, directory, hours, price)
    def info_film(self):
        return"""
        Adı: {}
        -
        İli: {}
        -
        IMDB: {}
        -
        Janr: {}
        -
        Müddət: {}
        -
        Film rejissoru: {}
        -
        {}
        -
        Qiymət: {} AZN
        """.format(self.name, self.year, self.imdb, self.genre, self.duration, self.directory, self.hours, self.price)
class Bozbashh(Movie):
    def __init__(self, name, year, imdb, genre, duration, directory, hours, price):
        super().__init__(name, year, imdb, genre, duration, directory, hours, price)
    def info_film(self):
        return"""
        Adı: {}
        -
        İli: {}
        -
        IMDB: {}
        -
        Janr: {}
        -
        Müddət: {}
        -
        Film rejissoru: {}
        -
        {}
        -
        Qiymət: {} AZN
        """.format(self.name, self.year, self.imdb, self.genre, self.duration, self.directory, self.hours, self.price)
class Yuxu(Movie):
    def __init__(self, name, year, imdb, genre, duration, directory, hours, price):
        super().__init__(name, year, imdb, genre, duration, directory, hours, price)
    def info_film(self):
        return"""
        Adı: {}
        -
        İli: {}
        -
        IMDB: {}
        -
        Janr: {}
        -
        Müddət: {}
        -
        Film rejissoru: {}
        -
        {}
        -
        Qiymət: {} AZN
        """.format(self.name, self.year, self.imdb, self.genre, self.duration, self.directory, self.hours, self.price)
class Bizimcebismellim(Movie):
    def __init__(self, name, year, imdb, genre, duration, directory, hours, price):
        super().__init__(name, year, imdb, genre, duration, directory, hours, price)
    def info_film(self):
        return"""
        Adı: {}
        -
        İli: {}
        -
        IMDB: {}
        -
        Janr: {}
        -
        Müddət: {}
        -
        Film rejissoru: {}
        -
        {}
        -
        Qiymət: {} AZN
        """.format(self.name, self.year, self.imdb, self.genre, self.duration, self.directory, self.hours, self.price)