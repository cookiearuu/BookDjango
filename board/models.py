from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length = 50)
    author_last_name = models.CharField(max_length=50)
    def str(self):
        return f'{self.author_name}{self.author_last_name}'

class Genre(models.Model):
    genre_name = models.CharField(max_length=100)
    #genre_id = models.FloatField(max_length=3, primary_key=True)
    def str(self):
        return f'{self.genre_name}'

class Publisher(models.Model):
    #publisherID = models.FloatField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phonenumber = models.FloatField(max_length=11)
    paddress = models.CharField(max_length=100)
    def str(self):
        return f'{self.name}{self.city}{self.phonenumber}{self.paddress}'

class Book(models.Model):
    #bookID = models.FloatField(max_length=6 , primary_key=True)
    book_name = models.CharField(max_length=50)
    genreID = models.ForeignKey(Genre,on_delete=models.CASCADE)
    publisherID = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    authorID = models.ForeignKey(Author,on_delete=models.CASCADE )

    def str(self):
        return f'{self.book_name}{self.genreID}{self.publisherID}{self.authorID}'

class Client (models.Model):
    #clientID = models.FloatField(max_length=12, primary_key=True)
    clientfname = models.CharField(max_length = 50)
    clientlname = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    caddress = models.CharField(max_length=100)
    phonenumber = models.FloatField(max_length=11)

    def str(self):
        return f'{self.clientlname}{self.clientfname}{self.email}{self.caddress}{self.phonenumber}'

class InStock(models.Model):
    bookID = models.ForeignKey(Book,on_delete=models.CASCADE, default="1")
    price = models.FloatField(max_length=10)
    genreID = models.ForeignKey(Genre,on_delete=models.CASCADE , default="1")
    qty = models.FloatField(max_length=4)
    publisherID = models.ForeignKey(Publisher,on_delete=models.CASCADE, default="1")

    def str(self):
        return f'{self.bookID}{self.genreID}{self.publisherID}{self.price}{self.qty}'

class Sold(models.Model):
    clientID =models.ForeignKey(Client,on_delete=models.CASCADE)
    bookID = models.ForeignKey(Book,on_delete=models.CASCADE)
    price = models.FloatField(max_length=4)
    datasend = models.DateField
    darareceived = models.DateField
    qty = models.FloatField(max_length=4)

    def str(self):
        return f'{self.clientID}{self.bookID}{self.price}{self.datasend}{self.darareceived}{self.qty}'

