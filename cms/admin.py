from django.contrib import admin

from .models import Customer, Service, ServiceCategory, ServiceSubCategory, Booking, SheekyHub, ContactUs, AboutUs


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
    list_display = ('id', 'suggested_time')
    list_display_links = ('id', 'suggested_time')
    search_fields = ('suggested_time',)
    list_per_page = 25

admin.site.register(Booking, BookingAdmin)

class SheekyHubAdmin(admin.ModelAdmin):
    list_display = ('id', 'latest_youtube_video_link')
    list_display_links = ('id', 'latest_youtube_video_link')
    list_per_page = 25

admin.site.register(SheekyHub, SheekyHubAdmin)

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone_no', 'location')
    list_display_links = ('id', 'email')
    search_fields = ('location', 'email', 'phone_no')
    list_per_page = 25

admin.site.register(ContactUs, ContactUsAdmin)

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_us', 'staff_name', 'staff_description')
    list_display_links = ('id', 'about_us')
    search_fields = ('staff_name', 'staff_description')
    list_per_page = 25

admin.site.register(AboutUs, AboutUsAdmin)
