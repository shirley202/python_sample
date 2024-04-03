from django.shortcuts import render
from .models import Article # --- 1
 
 
def index(request):
    articles = Article.objects.all() # --- 2
    params = {    # --- 3
        'articles': articles,
    }
    return render(request, 'blog/index.html', params) # --- 4