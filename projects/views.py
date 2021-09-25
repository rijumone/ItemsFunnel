from django.http import HttpResponse, Http404
# from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Project


def index(request):
    latest_p_list = Project.objects.order_by('-created_date')[:5]
    # template = loader.get_template('projects/index.html')
    context = {
        'latest_p_list': latest_p_list
    }
    # output = ', '.join([p.label for p in latest_p_list])
    # return HttpResponse(output)
    # return HttpResponse(template.render(context, request))
    return render(request, 'projects/index.html', context)


def detail(request, project_id):
    p = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project': p})


def add(request):
    '''
    1. Add Project to db
    2. Add Funnel to db
    3. Unzip dir_zip
        4. Assign uuids to matched files and write to local dir
        5. Add uuids as Items to db

    '''
    print(request.POST)
    print(request.POST['project_name'])
    return HttpResponse('hn krra hu')
