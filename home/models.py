from django.db import models

# Create your models here.
class Contact(models.Model):
    Pending = 'Pending'
    Completed = 'Completed'
    Attended = 'Attended'

    STATUS = [
        (Pending,'Pending'),
        (Completed, 'Completed'),
        (Attended, 'Attended'),
    ]

    full_name = models.CharField(max_length= 70)
    email = models.EmailField()
    message = models.TextField()
    status = models.CharField(max_length=100, choices= STATUS, default= 'Pending')
    when_sent = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'


class Category(models.Model):
    name = models.CharField(max_length= 50)
    img = models.ImageField(upload_to= ('img'),default= '')
    slug = models.SlugField(default='-')
    description = models.CharField(max_length= 100)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    imgr = models.ImageField(upload_to = 'Product', default= 'prouct.jpg')
    slug = models.SlugField(default = '-')
    price = models.FloatField()
    max_quantity = models.IntegerField()
    min_quantity = models.IntegerField()
    description = models.TextField()
    shoes = models.BooleanField()
    bag = models.BooleanField()
    perfume = models.BooleanField()
    cloth = models.BooleanField()
    uploaded = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    

