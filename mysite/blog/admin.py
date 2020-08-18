from django.contrib import admin
from .models import * #Importar todos los modelos

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Web)
admin.site.register(RedesSociales)
admin.site.register(Contact)
admin.site.register(Subscriber)
