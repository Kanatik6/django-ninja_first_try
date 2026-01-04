from django.db import models
from slugify import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Иконка категории (emoji или код)")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text="Порядок отображения")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            counter = 1

            # Проверяем существование слага и добавляем номер если нужно
            while Category.objects.filter(slug=slug).exists():
                slug = f"{slugify(self.name)}-{counter}"
                counter += 1

            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['order', 'name']


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    images = models.JSONField(default=list, blank=True, help_text="Список URL фотографий")
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            counter = 1

            # Проверяем существование слага и добавляем номер если нужно
            while Product.objects.filter(slug=slug).exists():
                slug = f"{slugify(self.name)}-{counter}"
                counter += 1

            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
