from django.db import models
from django.contrib import admin
from django.shortcuts import render
from skilltest.models.test_session import TestSessionInfo, TestSessionItems

# Register your models here.


#@admin.register(models.Model)
class CombinedAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        model1 = TestSessionInfo.objects.all()
        model2 = TestSessionItems.objects.all()

        context = {
            'model1': model1,
            'model2': model2,
        }

        return render(request, 'combined_admin.html', context)