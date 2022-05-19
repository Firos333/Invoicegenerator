from django.db.models import Count
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.contrib.auth.decorators import user_passes_test
# from .models import client_details,District,Taluk
from datetime import datetime, timedelta

@login_required(login_url="/login/")
def index(request):
    # total_apps = client_details.objects.all().count()
    # selected_apps = client_details.objects.filter(is_approved=True).count()
    # procesing_apps = client_details.objects.filter(is_approved=False,is_declined=False).count()
    # rejected_apps = client_details.objects.filter(is_declined=True).count()
    # today_count = client_details.objects.filter(created_date=datetime.today().strftime('%Y-%m-%d')).count()
    # yesterday_count = client_details.objects.filter(created_date=(datetime.today()- timedelta(1)).strftime('%Y-%m-%d')).count()
    
    # high_dist = client_details.objects.values_list('district').annotate(district_count=Count('district')).order_by('-district_count')[0]
    
    # taluk_count = client_details.objects.values('taluk','district').annotate(the_count=Count('taluk')).order_by('-the_count')
    # dec_inc = today_count-yesterday_count
    

    # context = {'total_apps':total_apps,'selected_apps':selected_apps,
    #             'rejected_apps':rejected_apps,'procesing_apps':procesing_apps,
    #             'taluk_count':taluk_count,'today_count':today_count,'yesterday_count':yesterday_count,
    #             'dec_inc':dec_inc,'high_dist':high_dist,

    #             }
    # context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render({}, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))



# @login_required(login_url="/login/")
# @user_passes_test(lambda u: u.is_staff)
def apply(request):
  
    context = {}
    html_template = loader.get_template( 'tables.html' )
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def requests(request):

    

    html_template = loader.get_template('request.html')
    return HttpResponse(html_template.render(context, request))





@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def applications(request):

   

    context = {}
    html_template = loader.get_template('filter_appli.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def filter(request):


    context = {}
    html_template = loader.get_template('filter_application.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def cardsall(request):

    context = {}
    html_template = loader.get_template('table_cards.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def cardsselected(request):

    html_template = loader.get_template('table_cards.html')
    return HttpResponse(html_template.render({}, request))

@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def cardsrejected(request):

   
    html_template = loader.get_template('table_cards.html')
    return HttpResponse(html_template.render({}, request))

@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def cardsprocessing(request):

    html_template = loader.get_template('table_cards.html')
    return HttpResponse(html_template.render({}, request))


@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def dated(request):

   

    context = {}
    html_template = loader.get_template('filter_date.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def filter_district(request):

  
    context = {}
    html_template = loader.get_template('filter_district.html')
    return HttpResponse(html_template.render(context, request))