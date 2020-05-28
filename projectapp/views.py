from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
from django.http import HttpResponse



# Create your views here.
def index(request):
    return render(request,'projectapp/index.html')

def gejala(request):
    return render(request,'projectapp/gejala.html')

def daftarrsrujukan(request):
    return render(request,'projectapp/daftarrsrujukan.html')

def coba(request):
    return render(request,'projectapp/coba.html')

def external(request):
    inp = request.POST.get('param')
    out = run([sys.executable,'C:/Users/GANESHA/Desktop/project/test.py',inp],shell=False,stdout=PIPE)
    text=str(out.stdout)
    text=text[2:]
    text=text[:-5]

    return render(request,'projectapp/coba.html',{'data1':text})

def generate_table(request):

    #Dapatkan input yang dikirim
    post = json.loads(request.POST.get('data',''))

    input_name=post['input_name']
    input_salary=int(post['input_salary'])
    input_multiplier=int(post['input_multiplier'])

    #Jalankan script python mu di sini, sebagai contoh aku bikin script utk buat table aja
    import pandas as pd
    df=pd.DataFrame({"Name":[input_name],
                     "Salary":[input_salary],
                     "Total Salary":[input_salary*input_multiplier]
                    })

    #Untuk mengirim dataframe balik, harus di konversi menjadi json:
    import json

    def ser_df(df):
        df_columns= [{"data":f,"field": f, "title": f} for f in df]
        df_data = df.to_dict('records')
        ser_data={'data': df_data,'columns': df_columns}
        return ser_data

    table=ser_df(df)

    context={'table':table}
    context=json.dumps(context)

    #Kirim balik isi 'context' ke html. Ini akan masuk ke variable 'response' nya
    return HttpResponse(context, content_type="application/json")
