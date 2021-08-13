from django.db import models
from django.db.models import Model, CharField

# Create your models here.
# class name should match model name, usually is singular and


class Artist(Model):
    name = models.CharField(max_length=100, default='NA')
    img = CharField(max_length=500)
    # charfield will automaitcally make input, text field will make textarea when auto generate forms
    bio = models.TextField(max_length=500)
    verified_artist = models.BooleanField(default=False)
    # this will be checkbox and based on default, it will have default checked
    created_at = models.DateTimeField(auto_now_add=True)
    # this will auto create this

    def __str__(self):
        return self.name
        # override string method for printing

    class Meta:
        ordering = ['name', 'created_at']
# python3 manage.py makemigrations
# run this when you make or change model
# only one person needs to make the models and run migration, need to code out models together then migrate
# then run
# python3 manage.py migrate
# \dt ignore sequences