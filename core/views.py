from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, CreateView
from .models import Testimonial, ContactMessage, HeroSlide
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hero_slides'] = HeroSlide.objects.filter(is_active=True)
        try:
            from portfolio.models import Project
            context['featured_projects'] = Project.objects.filter(is_featured=True)[:6]
        except ImportError:
            context['featured_projects'] = []
            
        context['testimonials'] = Testimonial.objects.all()[:4]
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'

class PriceView(TemplateView):
    template_name = 'core/price.html'

class ContactView(CreateView):
    model = ContactMessage
    form_class = ContactForm
    template_name = 'core/contact.html'
    success_url = '/contact/'

    def form_valid(self, form):
        response = super().form_valid(form)
        obj = self.object
        types = {
            'residential': 'Turar-joy interyeri',
            'commercial': 'Tijorat interyeri',
            'architecture': 'Arxitektura',
            'other': 'Boshqa',
        }
        text = (
            "🔔 <b>Yangi murojaat!</b>\n\n"
            f"👤 <b>Ism:</b> {obj.name}\n"
            f"📞 <b>Telefon:</b> {obj.phone}\n"
            f"🏠 <b>Loyiha turi:</b> {types.get(obj.project_type, obj.project_type)}\n"
            f"📐 <b>Maydon:</b> {obj.area or '—'} m²\n"
            f"📍 <b>Manzil:</b> {obj.address or '—'}"
        )
        from .telegram import send_telegram
        send_telegram(text)
        messages.success(self.request, "Xabaringiz muvaffaqiyatli yuborildi! Tez orada siz bilan bog'lanamiz.")
        return response
