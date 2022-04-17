
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
from user.models import User , Animal , Category , Rule

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Rule)
class RuleInline(admin.ModelAdmin):
    model=Rule
class UserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    
    list_display = ('email','rule_type')
    list_filter = ('email','rule_type')
    fieldsets = (
        (None, {'fields': ('email','first_name','last_name','password','phone_number','city','gender')}),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','first_name','last_name','phone_number','city','gender' )}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User,UserAdmin)
