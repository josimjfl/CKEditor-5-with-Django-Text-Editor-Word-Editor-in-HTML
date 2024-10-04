from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Article

def index(request):
    """View for the index page that handles comments."""
    if request.method == 'GET':
    	obj = Article.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the comment
            return redirect('index')  # Redirect to the same page after saving
    else:
        form = CommentForm()

    comments = Article.objects.all()  # Get all comments to display on the index page
    return render(request, 'news/index.html', {'form': form, 'obj': obj})
