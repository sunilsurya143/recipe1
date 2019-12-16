from django.db import models

# Create your models here.

class Login(models.Model):
    first_name=models.CharField(max_length=50,blank=False)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    username=models.CharField(primary_key=True,max_length=100)
    password=models.CharField(max_length=100)
    repassword=models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Recipe(models.Model):
    recipe_name=models.CharField(max_length=100)
    cook_name=models.CharField(max_length=100)
    recipe_ingrediants=models.TextField()
    recipe_process=models.TextField()


    def __str__(self):
        return  self.recipe_name
