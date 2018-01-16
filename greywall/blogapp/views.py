from django.shortcuts import render
from blogapp.models import Article

# Create your views here.
def blog(request):
    context = {}
    article_list = Article.objects.all()
    context['article_list'] = article_list
    index_page = render(request, 'blog.html', context)
    return index_page