from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _






class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    ,first_name,last_name,phone_number,city,gender,rule_type
    """
    def create_user(self, email,password,first_name,last_name,phone_number,city,gender,rule_type,**extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        # user.set_first_name(first_name)
        # user.set_last_name(last_name)
        # user.set_phone_number(phone_number)
        # user.set_city(city)
        # user.set_gender(gender)
        # user.set_rule_type(rule_type)
        user.rule_type=Rule.objects.get(id=1)
        
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self,email,password,**extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        defultRule= 1;
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('first_name', "israa")
        extra_fields.setdefault('last_name', "usta")
        extra_fields.setdefault('phone_number', 'defultRule')
        extra_fields.setdefault('city', 'defultRule')
        extra_fields.setdefault('gender', 'defultRule')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('rule_type', 'user')
        
        



        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        return self.create_user(email,password, **extra_fields)