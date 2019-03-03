# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    fields = ('name', 'description', 'price', 'quantity', 'published_on')
    list_display = ('name', 'description', 'price', 'quantity', 'published_on')
