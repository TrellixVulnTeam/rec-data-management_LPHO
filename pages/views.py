from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import json
from .forms import *
from .queries import *
from pages.entry_scripts.data_entry_script import *
from pages.entry_scripts.date_entry_script import *
from django.db.models import Max


#Index View -----------------------------------
def index(request):
    request.session['current_chartset'] = ChartSet.objects.latest('id').id
    chart_list = []
    for x in Chart.objects.filter(chart_set_id=request.session.get('current_chart')):
        chart_list.append(x)
    request.session['current_datasets'] = []
    request.session['current_titles'] = []
    label_list = []
    value_list = []
    title_list = []
    chart_number = len(Chart.objects.filter(chart_set_id=request.session.get('current_chartset')))
    chartset_dict = chartset_to_json(ChartSet.objects.latest('id'))
    chartset_json = json.dumps(chartset_dict)
    # return_chartset = json.loads(chartset_dict)
    return render(request, 'pages/index.html', {'json': chartset_json, 'chart_number':range(chart_number)})

def create_chartset_index(request):
    new_chart_set = ChartSet()
    new_chart_set.save()
    request.session['current_chartset'] = ChartSet.objects.latest('id').id
    return HttpResponseRedirect('/data-visualizer/dashboard')

#Chart Creation View -----------------------------------
def chartcreation(request):
    query = ''
    chart_form = ChartCreationForm()
    if request.META.get('HTTP_REFERER') == 'http://127.0.0.1:8000/data-visualizer/dashboard/':
            chart = Chart(chart_set_id=ChartSet.objects.latest('id').id)
            chart.save()
            request.session['current_chart'] = Chart.objects.latest('id').id
    elif request.META.get('HTTP_REFERER') == 'http://127.0.0.1:8000/data-visualizer/data-selection/':
        if request.method == "POST":
            dataset_form = DatasetForm(request.POST)
            if dataset_form.is_valid():
                graph = Graph(id=Graph.objects.latest('id').id + 1, chart_id=Chart.objects.latest('id').id, unit=dataset_form.cleaned_data['units'], 
                    facility=dataset_form.cleaned_data['facility'], area=dataset_form.cleaned_data['area'], start_date=dataset_form.cleaned_data['start_date'], 
                    end_date=dataset_form.cleaned_data['end_date'], gender=dataset_form.cleaned_data['gender'], year=dataset_form.cleaned_data['year'], 
                    month=dataset_form.cleaned_data['month'], week=dataset_form.cleaned_data['week'], day_of_month=dataset_form.cleaned_data['day_of_month'], 
                    day_of_week=dataset_form.cleaned_data['day_of_week'], time=dataset_form.cleaned_data['time'], )
                graph.save()
                query_dicts = Query().query_every_day(graph)
                for single_dictionary in query_dicts:
                    for data_object in query_dicts[single_dictionary]:
                        graph.data.add(data_object)
                graph.save()
                return HttpResponseRedirect('/data-visualizer/chart-creation')
            else:
                dataset_form = DatasetForm()
    return_query = chartset_to_json(ChartSet.objects.latest('id'))
    label_list = ['1', '2', '3']
    value_list = [1, 2, 3]
    title_list = ['yes', 'no']
    return render(request, 'pages/chart-creation.html', {'variable':return_query, 'chart_form':chart_form, 'labels':label_list, 'values':value_list, 'titles':title_list})

#Data Selection View -----------------------------------
def dataselection(request):

    dataset_form = DatasetForm()
    return render(request, 'pages/data-selection.html', {'dataset_form':dataset_form})


#Additional Methods -----------------------------------
def date_creation_loop(start, end):
    flag = True
    while (flag):
        if (start == end):
            flag = False
        date = DateEntryScript(start)
        date.create_date()
        start += timedelta(days=1)

def create_label(graph):
    dates =  str(graph.start_date.month) + '/' + str(graph.start_date.day) + '/' + str(graph.start_date.year) + '-'
    dates =  dates + str(graph.end_date.month) + '/' + str(graph.end_date.day) + '/' + str(graph.end_date.year)
    facility = ''
    facility_list = Query().replace_characters(graph.facility)
    for x in facility_list:
        facility += x + ':'
    area = ''
    area_list = Query().replace_characters(graph.area)
    for x in area_list:
        area += x + ':'
    return dates + ', ' + facility + ', ' + area

def create_dates():
    start = datetime(2016, 1, 1)
    end = datetime(2020, 12, 31)
    date_creation_loop(start, end)

def chartset_to_json(chartset):
    query = Chart.objects.filter(chart_set_id=chartset.id)
    chart_list = []
    index = 0
    for chart in query:
        chart_list.append(chart_to_json(chart, index))
        index+=1
    return {'chartset':chart_list}

def chart_to_json(chart, passed_index):
    query = Graph.objects.filter(chart_id=chart.id)
    graph_list = []
    index = 0
    for graph in query:
        graph_list.append(graph_to_json(graph, index))
        index+=1
    return {'charts':graph_list, 'title':chart.title, 'type':chart.type}

def graph_to_json(graph, passed_index):
    graph_values = Query().sort_results(graph)
    data_list = []
    index = 0
    for data in graph_values:
        data_list.append(data_to_json(data, graph_values[data]))
        index+=1
    return {'graph':data_list, 'color':graph.color}

def data_to_json(key, value):
    return {'data':{key:value}}