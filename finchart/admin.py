from django.contrib import admin

# Register your models here.

#========以下をすべて追加(5-2 Admin画面を使いやすくする)========
from .models import Company, Fstatement

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(Fstatement)
class FstatementAdmin(admin.ModelAdmin):
    list_display = ('company', 'fiscal_year')
    list_display_links = ('company',)
