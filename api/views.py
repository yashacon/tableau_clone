from django.http import HttpResponse
from .models import *
from django.db.models import Sum
import os,sys
from pathlib import Path
import csv 

from rest_framework.views import APIView
from rest_framework.response import Response
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.

class fetch(APIView):
    def get(self, request):
        #getting year and stat query
        stat = request.GET.get('stat', '')
        year = request.GET.get('year', '')

        #getting objects with year same as query
        order=Orders.objects.all().filter(Year=year)

        ### Grouping data on the basis of info required ###

        # monthly stats for the year
        yearly=order.values('month').order_by().annotate(monthly_stat=Sum(stat))
        yearly=sorted(yearly,key=lambda x:x['monthly_stat'],reverse=True)

        # segment stats for the year
        segment=order.values('Segment').order_by().annotate(segment_stat=Sum(stat))
        segment=sorted(segment,key=lambda x:x['segment_stat'],reverse=True)

        # category stats for the year
        category=order.values('Category').order_by().annotate(category_stat=Sum(stat))
        category=sorted(category,key=lambda x:x['category_stat'],reverse=True)

        # sub-category stats for the year
        sub_category=order.values('Sub_category').order_by().annotate(subcategory_stat=Sum(stat))
        sub_category=sorted(sub_category,key=lambda x:x['subcategory_stat'],reverse=True)

        # region stats for the year
        region=order.values('Region').order_by().annotate(region_stat=Sum(stat))
        region=sorted(region,key=lambda x:x['region_stat'],reverse=True)

        # state stats for the year
        state=order.values('State').order_by().annotate(state_stat=Sum(stat))
        state=sorted(state,key=lambda x:x['state_stat'],reverse=True)

        # city stats for the year
        city=order.values('City').order_by().annotate(city_stat=Sum(stat))
        city=sorted(city,key=lambda x:x['city_stat'],reverse=True)

        context={
            'yearly':yearly,
            'segment':segment,
            'category':category,
            'sub_category':sub_category,
            'region':region,
            'state':state,
            'city':city
        }
        return Response(context,status=200)



###------------Method to load Database from CSV File-------------###
def load_data(request):
    csv_filepathname=os.path.join(BASE_DIR,'Sample - Superstore.xls - Orders.csv')          #path to CSV File
    djangoproject_path=BASE_DIR                                                              #path to django project
    sys.path.append(djangoproject_path)
    dataReader = csv.reader(open(csv_filepathname,encoding="utf8"), delimiter=',', quotechar='"') 
    for row in dataReader:                                                                    #Iterating through CSV row-wise
        if row[0] != 'Row ID': 
            order=Orders()
            order.ID=row[0]
            order.Order_ID=row[1]
            order.Order_Date=row[2]
            order.Ship_Date=row[3]
            order.Ship_Mode=row[4]
            order.Customer_ID=row[5]
            order.Customer_Name=row[6]
            order.Segment=row[7]
            order.Country=row[8]
            order.City=row[9]
            order.State=row[10]
            order.Postal_Code=row[11]
            order.Region=row[12]
            order.Product_ID=row[13]
            order.Category=row[14]
            order.Sub_category=row[15]
            order.Product_Name=row[16]
            order.Sales=row[17]
            order.Quantity=row[18]
            order.Discount=row[19]
            order.Profit=row[20]
            order.Year=row[2][-4:]
            
            if row[2][-7]=='/':
                order.month=row[2][-6]                                             
            else:
                order.month=row[2][-7:-5]
            order.save()                                                                          #saving in database
            print(row[0])
    return HttpResponse('success')
    