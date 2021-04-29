from django.shortcuts import render
import requests


# Create your views here.
def sp(request):
    url = ' https://guarded-bayou-44144.herokuapp.com'
    response = requests.request("GET", url)
    result = response.json()
  #  print(result)
    name = []
    ranking = []
    location = []
    info = []
    #q = 'Princeton University'
    for i in range(len([result][0])):
        # print([result][0][i]['schoolName'])
        name.append([result][0][i]['schoolName'])
        ranking.append([result][0][i]['schoolRanking'])
        location.append([result][0][i]['locatation'])
        info.append([result][0][i]['schoolInfo'])


    print(info)

    schoollist = zip(name,ranking,location, info)


    return render(request, 'test/test.html',context={"schoolInfo":schoollist})
