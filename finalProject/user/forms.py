from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User
# first_name=models.CharField(max_length=200)
#     last_name=models.CharField(max_length=200)
#     email=models.CharField(max_length=255, unique=True)
#     password=models.CharField(max_length=150)
#     phone_number=models.CharField(max_length=10)
#     city=models.CharField(max_length=45)
#     gender=models.CharField(max_length=10,default="")
#     rule_type=models.ForeignKey(Rule,related_name='users_in_this_rule', on_delete=models.CASCADE)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)
# 'first_name','last_name','email','password','phone_number','city','gender'