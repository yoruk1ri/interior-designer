from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.db.models import F
from .models import Project, Category

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'projects'
    paginate_by = 9

    def get_queryset(self):
        queryset = Project.objects.all().order_by('-created_at')
        category_slug = self.request.GET.get('category')
        search_query = self.request.GET.get('q')
        
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_category'] = self.request.GET.get('category', '')
        context['search_query'] = self.request.GET.get('q', '')
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'

    def get_object(self):
        obj = super().get_object()
        # Increment views
        obj.views = F('views') + 1
        obj.save(update_fields=['views'])
        obj.refresh_from_db()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = Project.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id).order_by('-created_at')[:3]
        return context

def like_project(request, pk):
    if request.method == 'POST':
        project = get_object_or_404(Project, pk=pk)
        project.likes = F('likes') + 1
        project.save(update_fields=['likes'])
        project.refresh_from_db()
        return JsonResponse({'status': 'ok', 'likes': project.likes})
    return JsonResponse({'status': 'error'}, status=400)
