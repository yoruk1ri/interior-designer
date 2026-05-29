from django.contrib import admin
from .models import ContactMessage, Testimonial, HeroSlide

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'order', 'is_active')
    list_editable = ('order', 'is_active')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'project_type', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at', 'project_type')
    search_fields = ('name', 'phone', 'address')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('client_name', 'company')
