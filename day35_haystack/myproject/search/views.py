from django.shortcuts import render
from haystack.query import SearchQuerySet

# Create your views here.
def search_view(request):
    query = request.GET.get('q')
    results = []
    
    if query:
        print(query)
        results = SearchQuerySet().filter(text=query)
        print(results)
        
    context = {'results': results}
    return render(request, 'myapp/search_results.html', context)