from django.db import models

# Create your models here.


def path_and_rename(instance, filename):
    upload_to = 'uploads/products/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(id_generator(), ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(id_generator(), ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class coffee(models.Model):
    id = models.AutoField(primary_key=True, max_length=11)
    code = models.CharField(max_length=10)
    nama = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=500)
    gambar = models.ImageField(upload_to=path_and_rename)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=18, decimal_places=2)
    categories = models.ForeignKey('Category', related_name='to_products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama


class Category(models.Model):
    id = models.AutoField(primary_key=True, max_length=11)
    name = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
