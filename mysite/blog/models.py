from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class ModeloBase(models.Model):
    STATUS_ACTIVATED = (
        ('activated', 'Activated'),
        ('desactivated', 'Desactivated')
    )
    id = models.AutoField(primary_key = True)
    status = models.CharField('Estado', max_length=15,
                            choices=STATUS_ACTIVATED,
                            default='activated')
    created = models.DateField('Fecha de Creación',auto_now = False, auto_now_add = True)
    modificated = models.DateField('Fecha de Modificación',auto_now = True, auto_now_add = False)
    deleted = models.DateField('Fecha de Eliminación',auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True

class Category(ModeloBase):
    name = models.CharField('Nombre de la Categoría', max_length = 100, unique = True)
    reference_image = models.ImageField('Imagen de referencia',upload_to = 'categoria/')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Author(ModeloBase):
    name = models.CharField('Nombre',max_length = 100)
    surname = models.CharField('Apellidos',max_length = 120)
    email = models.EmailField('Correo Electrónico', max_length = 200)
    description = models.TextField('Descripción')
    reference_image = models.ImageField('Imagen de perfil', null = True, blank = True, upload_to = 'autores/')
    web = models.URLField('Web', null = True, blank = True)
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return '{0},{1}'.format(self.surname,self.name)

class Post(ModeloBase):
    STATUS_PUBLICATED = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    STATUS_FEATURED = (
        ('normal', 'Normal'),
        ('featured', 'Featured')
    )
    STATUS_PROMOTED = (
        ('normal', 'Normal'),
        ('promoted', 'Promoted')
    )

    title = models.CharField('Título del Post',max_length = 150, unique = True)
    slug = models.CharField('Slug', max_length = 150, unique = True)
    reading = models.IntegerField('Tiempo de lectura (nº entero)', default=10)
    description = models.TextField('Descripción')
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    body1 = RichTextField()
    reference_image1 = models.ImageField('Imagen Referencial 1', upload_to = 'imagenes/', max_length = 255)
    body2 = RichTextField(blank=True)
    reference_image2 = models.ImageField('Imagen Referencial 2', upload_to = 'imagenes/', max_length = 255, blank=True)
    body3 = RichTextField(blank=True)
    reference_image3 = models.ImageField('Imagen Referencial 3', upload_to = 'imagenes/', max_length = 255, blank=True)
    quoted = models.CharField('Introduce cita literal',max_length = 250, null = True, blank=True)
    publish = models.DateField('Fecha de Publicación', default=timezone.now)
    publicated = models.CharField('Publicado', max_length=15,
                            choices=STATUS_PUBLICATED,
                            default='draft')
    featured = models.CharField('Destacado', max_length=15,
                            choices=STATUS_FEATURED,
                            default='normal')
    promoted = models.CharField('Promocionado', max_length=15,
                            choices=STATUS_PROMOTED,
                            default='normal')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

class Web(ModeloBase):
    us = models.TextField('Nosotros')
    phone = models.CharField('Teléfono', max_length = 10)
    email = models.EmailField('Correo Electrónico', max_length = 200)
    address = models.CharField('Dirección', max_length = 200)

    class Meta:
        verbose_name = 'Web'
        verbose_name_plural = 'Webs'

    def __str__(self):
        return self.us

class RedesSociales(ModeloBase):
    facebook = models.URLField('Facebook')
    twitter = models.URLField('Twitter')
    instagram = models.URLField('Instagram')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.facebook

class Contact(ModeloBase):
    name = models.CharField('Nombre', max_length = 100)
    surname = models.CharField('Apellidos', max_length = 150)
    email = models.EmailField('Correo Electrónico', max_length = 200)
    subject = models.CharField('Asunto', max_length = 100)
    message = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.subject

class Subscriber(ModeloBase):
    email = models.EmailField('Correo Electrónico', max_length = 200)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email
