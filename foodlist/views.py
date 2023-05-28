from django.shortcuts import render
import pandas as pd
import os
import openpyxl

def search_view(request):
    if request.method == 'POST':
        sheet_name = request.POST.get('sheet_name')

        df = pd.read_excel('C:\\Users\\jaeyu\\Desktop\\foodlist4.xlsx', sheet_name=sheet_name)

        restaurants = df['식당'].tolist()

        return render(request, 'result.html', {'restaurants': restaurants})
    else:
        return render(request, 'search.html')

