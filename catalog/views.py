from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.

from .models import Tags, ChineseName, EnglishName, Location, Source, Principal, Reagent, ReagentInstance


def index(request):
    # Generate counts of some of the main objects
    num_reagent = Reagent.objects.all().count()
    num_instance = ReagentInstance.objects.all().count()
    # Available Reagents (status = 'a')
    num_instance_available = ReagentInstance.objects.filter(
        status__exact='a').count()
    num_instance_nerverused = ReagentInstance.objects.filter(
        status__exact='n').count()
    num_principal = Principal.objects.count(
    )  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={
            'num_reagent': num_reagent,
            'num_instance': num_instance,
            'num_instance_available': num_instance_available,
            'num_instance_neverused': num_instance_nerverused,
            'num_principal': num_principal
        },
    )


def update_runout(request, id):
    try:
        reagent_instance = ReagentInstance.objects.get(id=id)
    except ReagentInstance.DoesNotExist:
        return HttpResponse("Invalid ID")

    reagent_instance.status = 'r'
    reagent_instance.save()

    return HttpResponse("Status changed to 'r'")


def update_neverused(request, id):
    try:
        reagent_instance = ReagentInstance.objects.get(id=id)
    except ReagentInstance.DoesNotExist:
        return HttpResponse("Invalid ID")

    reagent_instance.status = 'n'
    reagent_instance.save()

    return HttpResponse("Status changed to 'n'")


def update_occupied(request, id):
    try:
        reagent_instance = ReagentInstance.objects.get(id=id)
    except ReagentInstance.DoesNotExist:
        return HttpResponse("Invalid ID")

    reagent_instance.status = 'o'
    reagent_instance.save()

    return HttpResponse("Status changed to 'o'")


def update_available(request, id):
    try:
        reagent_instance = ReagentInstance.objects.get(id=id)
    except ReagentInstance.DoesNotExist:
        return HttpResponse("Invalid ID")

    reagent_instance.status = 'a'
    reagent_instance.save()

    return HttpResponse("Status changed to 'a'")


def get_data_by_id(request, id):
    try:
        obj_list = ReagentInstance.objects.filter(id__icontains=id)
        results = []
        for obj in obj_list:
            data = {
                "id": str(obj.id),
                "reagent": obj.reagent.name,
                "register_date": str(obj.register_date),
                "name": obj.name,
                "principal": obj.principal.__str__(),
                "location": obj.location.name,
                "status": obj.status,
                "note": obj.note,
                # 其他属性
            }
            results.append(data)
        # print("Get Data:", results)
        response = JsonResponse({"results": results},
                                json_dumps_params={'ensure_ascii': False})
        response['content-type'] = 'application/json; charset=utf-8'

        # response = HttpResponse(results,
        #                         content_type='application/json; charset=utf-8')
        return response
    except ReagentInstance.DoesNotExist:
        # 处理不存在ID的情况
        return JsonResponse({"error": "Object not found."}, status=404)


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