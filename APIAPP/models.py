from django.db import models

# Create your models here.


# construction model
class construction(models.Model):
    type = models.CharField()
    completed = models.BooleanField()
    title = models.CharField(primary_key=True)
    details = models.CharField()
    location = models.CharField()
    year = models.DateField(auto_now_add=True,blank=True)
    company = models.CharField()
    size = models.IntegerField()
    # features = models.ForeignKey(feature,related_name='item', on_delete=models.CASCADE)
    # image = models.ForeignKey(Image,related_name='item', on_delete=models.CASCADE)

    def __str__(self):
        return f'a {self.title} | {self.year} '


# feature model and foreign key in construction model
class feature(models.Model):
    construction = models.ForeignKey(construction, related_name='features', on_delete=models.CASCADE)
    keyfeature1 = models.CharField(blank=True)
    def __str__(self):
        return f'{self.keyfeature1} - {self.construction.title}'

# image model and foreign key in construction
class Image(models.Model):
    construction = models.ForeignKey(construction, on_delete=models.CASCADE,related_name='image')
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return  self.construction.title

# a many to one model

# contact model
class contact(models.Model):
    fullname = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=254,blank=True)
    number = models.IntegerField(blank=True)
    subject = models.CharField(blank=True)
    state = models.CharField(blank=True)
    projecttype= models.CharField(blank=True)
    budget = models.IntegerField(blank=True)
    duration = models.CharField(blank=True)
    discription = models.TextField(blank=True)
    
    def __str__(self):
        return self.fullname

        # the related name must be the same in your serialisers