from django.http import JsonResponse


def home_page(request):
    name = ['prikshit' , 'rajesh',  'suraj']
    return JsonResponse(name , safe=False)