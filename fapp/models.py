from django.db import models
from django.contrib.auth.models import User

class Register(User):
    age=models.IntegerField()
    img=models.ImageField(upload_to="image", default="")
    date=models.DateField(auto_now=True)

class UserPosts(models.Model):
    name=models.CharField(max_length=20)
    img=models.ImageField(upload_to="image", default="")
    description=models.TextField(max_length=200)
    date=models.DateField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, default="")

    class Meta:
        db_table="user_posts"

class Interaction(models.Model):
    comment=models.TextField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    userp=models.ForeignKey(UserPosts,on_delete=models.CASCADE,default="")

    class Meta:
        db_table="interaction"


from django import forms
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model=Register
        fields=['username','first_name','last_name','email','age','img']

class UPostsForm(forms.ModelForm):
    class Meta:
        model=UserPosts
        fields=['name','img','description']