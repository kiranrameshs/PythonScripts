from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from result_list import result_list
from .models import *
from rest_framework.views import APIView
from Reports import Reports

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class ChartsPageView(TemplateView):
    template_name = 'charts.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ResultPageView(TemplateView):
    template_name = 'result.html'

class UpdatePageView(TemplateView):
    template_name = 'update.html'

'''
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'results.html',{'bu':v_bu, 'proj':v_project})
        #return render(request, 'charts.html', {"customers": 10})
'''
'''
def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 23, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)
'''
def submit(request):
    v_bu=request.POST["bu"]
    v_project=request.POST["project"]
    v_board=request.POST["board"]
    start_tag=request.POST["tag1"]
    end_tag=request.POST["tag2"]
    print (v_bu)
    print (v_project)
    print (v_board)
    obj_result_list = result_list()
    results = obj_result_list.get_table_data(v_bu,v_project,v_board,start_tag,end_tag)
    print("results is ",str(results))
    objTCContoler = Reports()
    objTCContoler.send_email(results['rdd'],results['ordd'],results['str_kloc'])
    print("mail sent")
    testlink_data = results['testlink']
    keys = getdictkey(results['testlink'])
    args = {'bu':results['bu'],'proj':results['proj'],'board':results['board'],'start_date':results['start_date'],'end_date':results['end_date'],'str_kloc':results['str_kloc'],'rdd':results['rdd'],'ordd':results['ordd'],'td':results['td'],'od':results['od'],'testlink':testlink_data,'keys':keys};
    return render(request,'result.html',args)
    #return render(request,'result.html',{'bu':v_bu, 'proj':v_project, 'board':v_board})
'''
    labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
    default_items = [5, 23, 2, 3, 12, 2]
    data = {
            "labels": labels,
            "default": default_items,
    }
    return render(request,'charts.html',data)
'''
def getdictkey(dictionary):
    return dictionary.keys()
def get_charts(request):
    v_bu=request.POST["bu"]
    print (v_bu)
    labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
    default_items = [5, 23, 2, 3, 12, 2]
    data = {
            "labels": labels,
            "default": default_items,
    }
    return render(request,'charts_result.html',data)

def update(request):
    print ("Updating results...")
    return render(request,'update_result.html')

