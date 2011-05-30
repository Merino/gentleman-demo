#
# Field Demo Gentleman
#   Default fields
#       - AutoField
#       - BigintegerField
#       - BooleanField
#       - Charfield
#       - CommaSepratedIntegerField
#       - DateField
#       - DateTimeField
#       - DecimalField
#       - EmailField
#       - FileField
#       - FilePathField
#       - FloatField
#       - ImageField
#       - IntegerField
#       - IPAdressField
#       - NullBooleanField
#       - PositiveIntegerField
#       - PositiveSmallIntegerField
#       - TextField
#       - TimeField
#       - URLField
#       - XMLField
#
#   Custom fields
#       - SourceField
#       - RichtextField
#       - ValutaField
#       - TimeZoneField
#       - IP6AddressField
#
#

from django.contrib import admin
from code.fieldsapp.models import DefaultField, CustomField, Teacher, Boss, Student

class DefaultFieldAdmin(admin.ModelAdmin):
    pass
    
class CustomFieldAdmin(admin.ModelAdmin):
    pass
    
class StudentInlineAdmin(admin.TabularInline):
    model = Student
    extra = 0

class RelationAdmin(admin.ModelAdmin):
    raw_id_fields = ('boss',)
    
    inlines = [
        StudentInlineAdmin,
    ]
    
admin.site.register(DefaultField, DefaultFieldAdmin)
admin.site.register(CustomField, CustomFieldAdmin)
admin.site.register(Teacher, RelationAdmin)