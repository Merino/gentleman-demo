from django.contrib import admin
from django.db import models
from code.demo.models import Customer, Order


from gentleman.widgets import SourceWidget, RichTextWidget

class OrderInlineAdmin(admin.TabularInline):
    model = Order

class CustomerAdmin(admin.ModelAdmin):
    
    #save_on_top = True
    list_per_page = 2
    search_fields = ('name',)
    
    
    
    fieldsets = (
            ('Naam', {
                'classes': ('column1of2',),
                'fields': ('name', 'address_admin1', 'address_admin2')
            }),
            ('Adres', {
                'classes': ('column2of2',),
                'fields': ('address_admin_zipcode', 'address_admin_city', 'address_admin_country')
            }),
            ('Adres', {
                'classes': ('',),
                'fields': ('description', 'source')
            }),
            ('Date & Time', {
                'classes': ('',),
                'fields': ('field_time', 'field_date', 'field_datetime')
            })
        )
        
    inlines = [
        OrderInlineAdmin,
    ]


admin.site.register(Customer, CustomerAdmin)

class OrderAdmin(admin.ModelAdmin):
    
    #save_on_top = True
    list_per_page = 2
    
    raw_id_fields = ('customer',)
    
    
    list_display = ('number','colored_state')
    
    
    def colored_state(self, obj):
        return '<span class="state draft %s">%s</span>' % (obj.status, obj.status)
    colored_state.allow_tags = True
    
admin.site.register(Order, OrderAdmin)