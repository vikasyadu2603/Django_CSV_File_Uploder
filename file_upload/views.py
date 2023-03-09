from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FileDetails,CsvFile
from .serializers import  GetSerializer
import pandas  as pd
# Create your views here.

class FileUploadAPI(APIView):                
    
    
        #Create an api endpoint using django rest framework which does the following:
        #(1)- Parses an uploaded CSV file
        #(2)- Inserts the rows into a table   
  
    def post(self, request, format=None):
        file =request.FILES['file']
        csv_obj=CsvFile.objects.create(file=file)
        df=pd.read_csv(csv_obj.file ,delimiter=',')
        csv_list=df.values
        for listValue in csv_list:
            FileDetails.objects.create(
                first_name=listValue[0],
                last_name=listValue[1],
                email=listValue[2],
                gender=listValue[3],
                phone=listValue[4],
            )
        return Response({"status": "success"})
        
    def get(self,request,pk=None,format=None):
            
            '''Create another api endpoint which does the following:
                Given the column name and sort order: ascending/descending, return the top 50 rows after sorting as json
            '''
            
            get_data=FileDetails.objects.all().order_by('first_name')[:50]
            serializer=GetSerializer(get_data, many=True)
            return Response(serializer.data) 
    

   
