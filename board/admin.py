from django.contrib import admin


from board.models import  Book ,Publisher, Author , Client  , Genre ,Sold ,InStock


# admin.site.register(Book)
# admin.site.register(Publisher)
# admin.site.register(Author)
# admin.site.register(Client)
# admin.site.register(Genre)
# admin.site.register(Sold)
# admin.site.register(InStock)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name','author_last_name')
    list_filter = ()

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','city','phonenumber','paddress')
    list_filter = ()

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre_name']
    list_filter = ()

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name','genreID','publisherID','authorID')
    list_filter = ('genreID','publisherID','authorID')

@admin.register(InStock)
class InStockAdmin(admin.ModelAdmin):
    list_display = ('bookID','price','genreID','qty','publisherID')
    list_filter = ('genreID','publisherID')

@admin.register(Sold)
class SoldAdmin(admin.ModelAdmin):
    list_display = ('clientID','bookID','price','qty')
    list_filter = ()


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('clientfname','clientlname','email','caddress','phonenumber')
    list_filter = ()

