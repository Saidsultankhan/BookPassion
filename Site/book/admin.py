from django.contrib import admin

from .models import Rating,RatingStar,Reviews,Izdan,Author,Category,Book


admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
admin.site.register(Izdan)
admin.site.register(Category)
admin.site.register(Book)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (('name', 'date', 'worth', 'description', 'image'))




admin.site.site_title = 'Салам Алейкум!'
admin.site.site_header = 'Салам Алейкум!'