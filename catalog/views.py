from django.shortcuts import render

# Create your views here.

from .models import Tags, ChineseName, EnglishName, Location, Source, Principal, Reagent, ReagentInstance

def index(request):
    # Generate counts of some of the main objects
    num_reagent=Reagent.objects.all().count()
    num_instance=ReagentInstance.objects.all().count()
    # Available Reagents (status = 'a')
    num_instance_available=ReagentInstance.objects.filter(status__exact='a').count()
    num_instance_nerverused=ReagentInstance.objects.filter(status__exact='n').count()
    num_principal=Principal.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_reagent':num_reagent,'num_instance':num_instance,'num_instance_available':num_instance_available,'num_instance_neverused':num_instance_nerverused,'num_principal':num_principal},
    )
    
from django.views import generic

class ReagentListView(generic.ListView):
    model = Reagent
    paginate_by = 30
    
class ReagentDetailView(generic.DetailView):
    model = Reagent
    
class ReagentInstanceListView(generic.ListView):
    model = ReagentInstance
    paginate_by = 30
    
class ReagentInstanceDetailView(generic.DetailView):
    model = ReagentInstance
    
class PrincipalListView(generic.ListView):
    model = Principal
    paginate_by = 30
    
class PrincipalDetailView(generic.DetailView):
    model = Principal
    
class LocationListView(generic.ListView):
    model = Location
    paginate_by = 30
    
class LocationDetailView(generic.DetailView):
    model = Location
    
class SourceListView(generic.ListView):
    model = Source
    paginate_by = 30
    
class SourceDetailView(generic.DetailView):
    model = Source
    
class ChineseNameListView(generic.ListView):
    model = ChineseName
    paginate_by = 30
    
class ChineseNameDetailView(generic.DetailView):
    model = ChineseName

    
class EnglishNameListView(generic.ListView):
    model = EnglishName
    paginate_by = 30
    
class EnglishNameDetailView(generic.DetailView):
    model = EnglishName