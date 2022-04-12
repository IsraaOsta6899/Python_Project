from django.contrib import admin

# Register your models here.
from user.models import User , Animal , Category , Rule

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    pass