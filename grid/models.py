from django.db import models
from django.urls import reverse

CHOICES = (
    (True, 'Посетил(а)'),
    (False, 'Не посетил(а)'),
)


class Positions(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=500)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    slug = models.SlugField(unique=True)
    steck = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('visit', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employee'


class Visits(models.Model):
    date = models.DateField(auto_created=False)
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    visited = models.BooleanField(choices=CHOICES)
    time_start = models.TimeField(blank=True, null=True)
    time_end = models.TimeField(blank=True, null=True)
    reason = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'Сотрудник {self.user.name} {self.date}'

    class Meta:
        ordering = ['-date']
        db_table = 'visit'

