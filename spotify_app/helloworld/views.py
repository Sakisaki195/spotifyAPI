from django.shortcuts import render

def index(request):
    print(request)
    print("ジェバンニが一晩でやってくれました")
    return render(request, 'helloworld/index.html')