from django.contrib import admin
from .models import Movie, Genre, HashTag, Review, Sort

# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(HashTag)
admin.site.register(Review)
admin.site.register(Sort)