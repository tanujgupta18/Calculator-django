from django.shortcuts import render

def Addition(num1,num2):
    result = int(num1) + int(num2)
    return result
 
def Subtract(num1,num2):
    result = int(num1) - int(num2)
    return result
 
def Multiply(num1,num2):
    result = int(num1) * int(num2)
    return result
 
def Divide(num1,num2):
    result = int(num1) / int(num2)
    return result
 
def home(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        if 'add' in request.POST:
            result = Addition(num1,num2)
            return render(request,'index.html',{'result':result})
        
        if 'sub' in request.POST:
            result = Subtract(num1,num2)
            return render(request,'index.html',{'result':result})
 
        if 'div' in request.POST:
            result = Divide(num1,num2)
            return render(request,'index.html',{'result':result})
 
        if 'mul' in request.POST:
            result = Multiply(num1,num2)
            return render(request,'index.html',{'result':result})
    return render(request,'index.html')