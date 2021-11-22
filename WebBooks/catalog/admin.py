from django.contrib import admin

from .models import Authors, Book, Genre, Language, Status, BookInstance

# admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)


# admin.site.register(BookInstance)


@admin.register(Authors)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('lastName', 'firstName', 'dateOfBirth', 'dateOfDeath')
    fields = ['firstName', 'lastName', ('dateOfBirth', 'dateOfDeath')]


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'dueBack', 'id')
    list_filter = ('status', 'dueBack')

    fieldsets = (
        ('Экземпляр книги', {'fields': ('book', 'imprint', 'invNum')}),
        ('Статус и окончание его действия', {'fields': ('status', 'dueBack', 'borrower')})
    )
