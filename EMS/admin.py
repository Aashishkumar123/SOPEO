from django.contrib import admin
from EMS.models import add,Employee
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


admin.site.register(add)
admin.site.register(Employee)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        ('User Information', {'fields': ('email', 'password', 'first_name', 'last_name',)}),
        ('User Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'user_permissions')}),
        ('User Type', {'fields': ('account_type',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
