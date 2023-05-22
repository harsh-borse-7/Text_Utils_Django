from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('textarea','default')
    removepunc=request.POST.get('Removepunc','off')
    capitalize=request.POST.get('Capitalize','off')
    removespace=request.POST.get('RemoveSpace','off')
    charcount=request.POST.get('CharCount','off')
    result=""
    
    
    if(removepunc=='on'):
        result=""
        punc='''[!\"#\$%&\'\(\)\*\+,-\./:;<=>\?@\[\\\]\^_`{\|}~]'''
        for i in djtext:
            if i not in punc:
                result=result+i
        djtext=result
        
    
    if(capitalize=='on'):
        result=""
        for i in djtext:
            result=result+i.upper()
        djtext=result
        
    if(charcount=='on'):
            count=0 
            for i in djtext:
                if(i!=" "):
                    count=count+1

            result=result+f" & the Length of string is {count}"
           

    if not (capitalize=='on' or removepunc=='on' or charcount=='on'):
        result="Please Select Operation"
    
    if result=="":
        result="Please Enter String"
    dict1={'result':result}
    
    return render(request,'index.html',dict1)      