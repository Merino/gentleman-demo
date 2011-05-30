#
# Fieldset Demo Gentleman
#   Fieldset collapse
#       - normal
#       - close
#       - open
#       
#   Fieldset Width
#       - column 2
#       - column 3
#       - column 4

from django.contrib import admin
from code.fieldsetapp.models import Column, Collapse, Action

class ColumnAdmin(admin.ModelAdmin):
    
    actions = ()
    
    fieldsets = (
             ('Colum Basic', {
                 'fields': ('column01', 'column02')
             }),
             ('Colum 1 of 2', {
                 'classes': ('column1of2',),
                 'fields': ('columnA1', 'columnA2', 'columnA3', 'columnA4', 'columnA5')
             }),
             ('Colum 2 of 2', {
                 'classes': ('column2of2',),
                 'fields': ('columnB1', 'columnB2', 'columnB3', 'columnB4', 'columnB5')
             }),
             ('Colum 1 of 3', {
                 'classes': ('column1of3',),
                 'fields': ('columnC1', 'columnC2', 'columnC3', 'columnC4', 'columnC5')
             }),
             ('Colum 2 of 3', {
                 'classes': ('column2of3',),
                 'fields': ('columnD1', 'columnD2', 'columnD3', 'columnD4', 'columnD5')
             }),
             ('Colum 3 of 3', {
                  'classes': ('column3of3',),
                  'fields':('columnE1', 'columnE2', 'columnE3', 'columnE4', 'columnE5')
              }),
              ('Colum with cells', {
                    'classes': ('',),
                    'fields':('columnFA1', ('columnFB1', 'columnFB2'), ('columnFC1', 'columnFC2', 'columnFC3'))
              }),
              ('Colum 1 of 2 with cells', {
                   'classes': ('column1of2',),
                   'fields': ('columnGA1', ('columnGB1', 'columnGB2'))
               }),
               ('Colum 2 of 2 with cells', {
                   'classes': ('column2of2',),
                   'fields': ('columnHA1', ('columnHB1', 'columnHB2'))
               }),
         )

class CollapseAdmin(admin.ModelAdmin):
    fieldsets = (
             ('Collpase Open', {
                 'classes': ('collapse',),
                 'fields': ('fieldsetA1', 'fieldsetA2', 'fieldsetA3')
             }),
             ('Collapse Close', {
                 'classes': ('collapse',),
                 'fields': ('fieldsetB1', 'fieldsetB2', 'fieldsetB3')
             }),
             ('Collapse None', {
                 'classes': ('',),
                 'fields': ('fieldsetC1', 'fieldsetC2', 'fieldsetC3')
             })
         )
         
class ActionAdmin(admin.ModelAdmin):
    
    action = ()
    
    fieldsets = (
            ('Action A', {
                'classes': ('',),
                'fields': ('actionA1', 'actionA2', 'actionA3')
            }),
            ('Action A', {
                'classes': ('',),
                'fields': ('actionB1', 'actionB2', 'actionB3')
            }),
         )
    
admin.site.register(Column, ColumnAdmin)
admin.site.register(Collapse, CollapseAdmin)
admin.site.register(Action, ActionAdmin)