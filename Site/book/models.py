from django.db import models
from django.urls import reverse

class Category(models.Model):

    name = models.CharField("Категория", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.url})

class Author(models.Model):

    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание Автора")
    image = models.ImageField("Фотография", upload_to="authors/")
    year = models.SmallIntegerField('Дата рождения', default=1970)
    worth = models.PositiveIntegerField('Состояние', default=100000)
    date = models.CharField('Годы жизни', max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author_itself", kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Izdan(models.Model):

    name = models.CharField("Издательство", max_length=50)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"

class Book(models.Model):

    image = models.ImageField("Картина книги", upload_to="books/")
    category = models.ManyToManyField(Category, related_name="category_of_book")
    name = models.CharField("Название книги", max_length=150, db_index=True)
    description = models.TextField("Описание Книги")
    year = models.PositiveSmallIntegerField('Год издания', default=2016)
    author = models.ManyToManyField(Author, related_name='book_author')
    izdan = models.ManyToManyField(Izdan,  related_name="published_by")
    pages = models.PositiveSmallIntegerField("Страницы", default=300)
    cover = models.TextField("Переплет", max_length=10)
    isbn = models.SmallIntegerField("ISBN")
    slug = models.SlugField(max_length=130, unique=True, db_index=True)
    price = models.PositiveSmallIntegerField('Цена', default=10)
    stock = models.PositiveIntegerField('В наличии шт')
    available = models.BooleanField(default=True)
    created = models.DateTimeField('Создан',auto_now_add=True)
    updated = models.DateTimeField('Обновлен',auto_now=True)

    def get_absolute_url(self):
        return reverse("books:book_itself", kwargs={"slug": self.slug})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        
class RatingStar(models.Model):

    value = models.SmallIntegerField("Значение",default=0)
    
    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"

class Rating(models.Model):

    ip = models.CharField('IP адрес',max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Звезда")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")

    def __str__(self):
        return f'{self.star} - {self.book}'

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):

    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Комментарий",max_length=500)
    parent = models.ForeignKey('self', verbose_name="Родитель", blank=True, null=True, on_delete=models.SET_NULL)
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.book}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
