import os
import sys
import django
from django.core.files import File
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from portfolio.models import Category, Project
from core.models import Testimonial

def populate():
    # Superuser
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        print("Superuser created: admin / admin")

    # Categories
    categories = ['Hard Surface', 'Characters', 'Environments']
    for cat in categories:
        Category.objects.get_or_create(name=cat)
    print("Categories created")

    # Projects
    cat1 = Category.objects.get(name='Hard Surface')
    if not Project.objects.filter(title='Sci-Fi Mech').exists():
        Project.objects.create(
            title='Sci-Fi Mech',
            category=cat1,
            description='<p>High-poly Sci-Fi Mech design created in Maya and ZBrush.</p>',
            is_featured=True,
            views=150,
            likes=45
        )
    print("Sample projects created")

    # Testimonial
    if not Testimonial.objects.filter(client_name='John Doe').exists():
        Testimonial.objects.create(
            client_name='John Doe',
            company='Game Studios Inc',
            content='Amazing 3D artist. Delivered high-quality assets on time!',
            rating=5
        )
    print("Sample testimonials created")

if __name__ == '__main__':
    populate()
