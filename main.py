import json

class Library():
    "bu sinif ögrenci kayit icin olusturulan classdir."    
    def __init__(self, name, surname, age, **kwargs):
        self.name = name 
        self.surname = surname 
        self.age = age  


        for key, value in kwargs.items():
            setattr(self, key, value)
l = Library("Akif", "Yildiz", "17", numara = 200)
l = Library("Recep", "Öztürk", "29", numara = 201)
l = Library("Deniz", "Tas", "45", numara = 203)

class Borrow_Book():
    "burada kayit olan kisi kitap ödünc aliyor"
    def __init__(self, book, date, **kwargs):
        self.book = book
        self.date = date
    

        for key, value in kwargs.items():
            seta
