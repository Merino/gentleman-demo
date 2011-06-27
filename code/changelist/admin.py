from django.contrib import admin
from code.changelist.models import BasicChangelist

class BasicChangelistAdmin(admin.ModelAdmin):
    
    list_display = ('fieldA','fieldB','fieldC','fieldD1','get_link_field','get_multi_row')
    
    def get_link_field(self, obj):
        
        spliter = ''
        row_email = ''
        row_phone = ''
        
        if obj.fieldD2 and obj.fieldB:
            spliter = '<br />' 
        
        if obj.fieldD2:
            row_email = '<a href="mailto:%s">email mij</a>' % obj.fieldD2
        
        if obj.fieldB:
            row_phone = '<a href="tel:%s">tel</a>' % obj.fieldB
        
        return "%s %s %s" % (row_email, spliter, row_phone)
    get_link_field.allow_tags = True
    
    def get_multi_row(self, obj):
        return "%s <br /> %s" % (obj.fieldD1, obj.fieldD2)
    get_multi_row.allow_tags = True
    
admin.site.register(BasicChangelist, BasicChangelistAdmin)