# I have created this file - Avinash Joshi
from distutils.spawn import spawn
from os import remove
from re import purge
from ssl import Purpose
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    # return HttpResponse('Hello')
    return render(request,'Desgining.html')

def analyze(request):
    djtext=request.GET.get('text','default')
    removepuncuation=request.GET.get('removepunc','off')
    uppercase=request.GET.get('uppercase','off')
    space=request.GET.get('spaceremover','off')
    newlineremover=request.GET.get('removenewline','off')
    count=request.GET.get('countword','off')

    counter=0
    analyze=djtext
    Purpose=''
    if(removepuncuation!='off'):
        analyze=''
        pancuations='''!()-[]{};:'"\,<>./?@#^&_~'''
        for char in djtext:
            if char not in pancuations:
                analyze=analyze+char
        print(analyze)
        Purpose='Pancuations removed'
        djtext=analyze

    if(uppercase!='off'):
        analyze=djtext.upper()
        djtext=analyze
        print(djtext)
        Purpose=Purpose+'Uppercase'

    if(space!='off'):
        analyze=""
        for index,char in enumerate(djtext):
            if(index<len(djtext)-1 and not(djtext[index]==' ' and djtext[index+1]==' ')):
                analyze=analyze+char
        djtext=analyze
        print(analyze)
        Purpose=Purpose+'Removed Extra Space'

    if(newlineremover!='off'):
        analyze=''
        for index,char in enumerate(djtext):
            if(char!='\n'):
                analyze=analyze+char 
        djtext=analyze 
        print(djtext)       

    if(count!='off'):
        for char in djtext:
            if(char!='\n'):
                counter+=1
            else:
                counter+=-1                
        param={'purpose':Purpose,'analyzed_text':analyze,'counter':counter}
        return render(request,'Analyze.html',param)

    param={'purpose':Purpose,'analyzed_text':analyze}
    return render(request,'Analyze.html',param)

    # return HttpResponse('Hello')

# def analyze(request):
#     djtext=request.GET.get('text','default')
#     removepunc=request.GET.get('removepunc','off')
#     upper=request.GET.get('uppercase','off')
#     space=request.GET.get('spaceremover','off')
#     newline=request.GET.get('removenewline','off')
#     count=request.GET.get('countword','off')
#     print(djtext)
#     print(removepunc)
#     print(upper)
#     print(space)
#     print(newline)
#     print(count)
    
#     analyze=''
#     analyzed=''
#     text=''
#     if(count!='off'):
#         character=0
#         alphabet=0
#         word=0
#         for index,char in enumerate(djtext):
#             if not(len(djtext)>index+1 and (djtext[index]==' 'and djtext[index+1]==' ')):
#                 analyze=analyze+char
#                 # print(analyze)
#         djtext=analyze    
#         if(djtext[0]==' '):
#             djtext=djtext[1:]
#             # print("0",djtext)
#         if(djtext[-1]==' '):
#             djtext=djtext[:-1]
#             # print("1",djtext) 
#         print('1',djtext)           
#         # for char in djtext:
#         #     if(djtext!='\n'):
#         #         text=text+char
    
#         for index,char in enumerate(djtext):
#             if(char=='\r' and djtext[index+1]==' '):
#                 continue
#             if(char=='\r' and djtext[index+1]!=' '):
#                 char=' '
#                 text=text+' '
#                 continue
#             if(char!='\n'):
#                 text=text+char
#                 print(text)
#                 character+=1
#                 if char!=' ':
#                     alphabet+=1
#                 if char==' ':
#                     word+=1
#         if(character>0):
#             word+=1                
#         param={'purpose':'Count the letter','text':text,'analyzed_text':{'character':character,'alphabets':alphabet,'words':word}}
#         return render(request,'Analyze.html',param)

              
#     if(newline!='off'):
#         for char in djtext:
#             if char!='\n':
#                 analyze=analyze+char
#                 print(analyze)
#         print(analyze)                
#         params={'purpose':'Remove New Line','analyzed_text':analyze}        
#         return render(request,'Analyze.html',params)


#     if(space!='off'):
#         for index,char in enumerate(djtext):
#             if not(len(djtext)>index+1 and djtext[index]==' 'and djtext[index+1]==' '):
#                 analyze=analyze+char
#         print(analyze)                
#         params={'purpose':'Extra Space Removed','analyzed_text':analyze}
#         return render(request,'analyze.html',params)


#     if(upper!='off' and removepunc!='off'):
#         djtext=djtext.upper()
#         pancuations='''!()-[]{};:'"\,<>./?@#^&_~'''
#         analyzed=''
#         for char in djtext:
#             if char not in pancuations:
#                 analyzed=analyzed+char
#         params={'purpose':'Upper-case Removed Panctuations','analyzed_text':analyzed}
#         return render(request,'analyze.html',params)

#     elif(upper!='off'):
#         djtext=djtext.upper()
#         params={'purpose':'Uppercase','analyzed_text':djtext}
#         return render(request,'Analyze.html',params)
            
#     elif(removepunc!='off'):
#         pancuations='''!()-[]{};:'"\,<>./?@#^&_~'''
#         analyzed=''
#         for char in djtext:
#             if char not in pancuations:
#                 analyzed=analyzed+char
#         params={'purpose':'Removed Panctuations','analyzed_text':analyzed}
#         return render(request,'analyze.html',params)
#     # else         
#     else:
#         return HttpResponse("Error")    
    # return HttpResponse("Hello")

# # def index(request):
# #     param={'name':"Avinash",'place':'Mars'}
# #     return render(request,'index.html',param)

# # def removepunc(request):
# #     djtext=request.GET.get('text','default')
# #     print(djtext)
# #     return HttpResponse('Remove Puncuation')
#     # return render(request,'index.html')

# # def button(request):
#     # f=open('button.html')
#     # data=f.read()
#     # return HttpResponse("dragon Rage\n"data)

# f=open("D:\\VScode\\Python\\Django\\Textutils\\textutils\\textutils\\button.txt")
# data=f.read()

# # def index(request):
#     # return HttpResponse(f"{data}<br/>hello Avinash")

# def txtfile(request):
#     f=open("D:\\VScode\\Python\\Django\\Textutils\\textutils\\textutils\\one.txt",'r')    
#     data1=f.read()
#     return HttpResponse(f"{data}<br/>{data1}")

# def about(request):
#     return HttpResponse(f"{data}<br/>Avinash You are in about")

# def html(requst):
#     return HttpResponse(f'{data}<br/><h1>Dragon Range</h1> Dragon Rage')

# def link(request):
#     return HttpResponse(f'{data}<br/><a href="https://www.youtube.com/">Youtube</a>')

# f=open("D:\\VScode\\Python\\Django\\Textutils\\textutils\\textutils\\one.txt",'r')
# print(f.read())    