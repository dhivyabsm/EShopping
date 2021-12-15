from django.contrib import admin
from Shop.models import Customer, Item, Purchase, Cart


# Register your models here.
@admin.action(description='Buy Item')
def Buy(ModelAdmin,request,queryset):
    print('1111',queryset)
    for i in queryset:
        Purchase.objects.get_or_create(purchase_id=1,purchase_details='bought',item=i.item,user=i.user)
        i.delete()
    queryset.update()
    

class Itemadmin(admin.ModelAdmin):
    list_display = ['item_id', 'item_name', 'item_desc', 'item_price']


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['item','purchase_id', 'purchase_details']


class CartAdmin(admin.ModelAdmin):
    list_display = ['item', 'item_quantity', 'user','get_price','total']
    actions = [Buy,]

    def get_price(self,obj):
        return obj.item.item_price
    get_price.short_description = 'Price'

    def total(self,obj):
        return obj.item.item_price * obj.item_quantity



class Customeradmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_name', 'user_mobile_number', 'address', 'item','purchase']


admin.site.register(Customer, Customeradmin)
admin.site.register(Item, Itemadmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Cart, CartAdmin)
