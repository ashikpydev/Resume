from django.db import models

# Create your models here.
class Aboutme(models.Model):
    name = models.CharField(max_length=50, blank = True, null = True)
    photo = models.ImageField(blank = True, null = True)
    cover_photo = models.ImageField(blank = True, null = True)
    designation = models.CharField(max_length=50, blank = True, null = True)
    about_me = models.TextField(blank = True, null = True)
    age = models.IntegerField(blank = True, null = True)
    email = models.CharField(max_length=50, blank = True, null = True)
    skype = models.CharField(max_length=50, blank = True, null = True)
    address = models.TextField(blank = True, null = True)
    phone = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return self.name

class Level(models.Model):
    level = models.IntegerField()

    def __str__(self):
        return str(self.level)

class Skills(models.Model):
    name = models.CharField(max_length =250)
    level = models.ForeignKey(Level, on_delete = models.CASCADE )

    def __str__(self):
        return self.name

class Experience(models.Model):
    position = models.CharField(max_length=50, blank = True, null = True)
    institute_name = models.CharField(max_length=50, blank = True, null = True)
    start_date = models.DateField(blank = True, null = True)
    end_date = models.DateField(blank = True, null = True)
    description = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.position
    
class Refference(models.Model):
    name = models.CharField(max_length=50, blank = True, null = True)
    image = models.ImageField(blank = True, null = True)
    position = models.CharField(max_length=50, blank = True, null = True)
    institute = models.CharField(max_length=50, blank = True, null = True)
    review = models.TextField(blank = True, null = True)
    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    image = models.ImageField(blank = True, null = True)
    project_url = models.CharField(blank = True, null = True, max_length=50)
    title =  models.CharField(blank = True, null = True, max_length=50)
    overview = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(blank = True, null = True, max_length=50)
    institute = models.CharField(blank = True, null = True, max_length=50)
    join_date = models.DateField(blank = True, null = True)
    graduation_date = models.DateField(blank = True, null = True)
    description = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.degree
    
class Contact(models.Model):
    name = models.CharField(blank = True, null = True, max_length=50)
    email = models.EmailField(blank = True, null = True, max_length=254)
    message = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name
    