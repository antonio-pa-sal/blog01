from django.contrib import admin
from .models import * #Importar todos los modelos

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',   
                       'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body1')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Web)
admin.site.register(RedesSociales)
admin.site.register(Contact)
admin.site.register(Subscriber)
