from django.shortcuts import render

# View for the home page, renders the index.html template
def home(request):
    return render(request, 'home/index.html')

# View for the about page, you can render a template if you have an about.html too
def about(request):
    return render(request, 'home/about.html')