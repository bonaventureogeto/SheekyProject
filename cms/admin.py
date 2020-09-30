from django.contrib import admin

from .models import Customer, Service, Department, Product, ServiceCategory, ServiceSubCategory, Booking, IndexPage


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_no', 'favorite_hairstyle')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone_no')
    list_per_page = 25

admin.site.register(Customer, CustomerAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'service_category', 'service_subcategory', 'staff_assigned')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'price', 'staff_assigned')
    list_per_page = 25

admin.site.register(Service, ServiceAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price')
    list_display_links = ('id', 'product_name')
    search_fields = ('product_name', 'price')
    list_per_page = 25

admin.site.register(Product, ProductAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'department_name')
    list_display_links = ('id', 'department_name')
    search_fields = ('department_name',)
    list_per_page = 25

admin.site.register(Department, DepartmentAdmin)


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_display_links = ('id', 'category_name')
    search_fields = ('category_name',)
    list_per_page = 25

admin.site.register(ServiceCategory, ServiceCategoryAdmin)

class ServiceSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'subcategory_name', 'service_category')
    list_display_links = ('id', 'subcategory_name', 'service_category')
    search_fields = ('subcategory_name', 'service_category')
    list_per_page = 25

admin.site.register(ServiceSubCategory, ServiceSubCategoryAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment_date',  'appointment_time')
    list_display_links = ('id', 'appointment_date', 'appointment_time')
    search_fields = ('appointment_date', 'appointment_time')
    list_per_page = 25

admin.site.register(Booking, BookingAdmin)

class IndexPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone_no', 'location')
    list_display_links = ('id', 'email', 'phone_no', 'location')
    search_fields = ('email', 'phone_no', 'location')
    list_per_page = 25

admin.site.register(IndexPage, IndexPageAdmin)

