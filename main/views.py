from django.http import HttpResponse
from django.shortcuts import render
from .workwithhash import Hashing,deHashUPH


def indexview(request):
    if request.method == "POST":
        hash_value = request.POST['hash_value']
        hash_type = request.POST['hash_type']
        hash_types = ['md5','sha1','sha224','sha256','sha512']
        if str(hash_type).lower() not in hash_types:
            return HttpResponse(f"<h1>{hash_type} is not found!</h1>")
        else:
            hashed_word = Hashing(hashtype=hash_type,hash_value=hash_value)
            return render(request,'index.html',{'answer':hashed_word,'hashtype':hash_type,'word':hash_value,'home_page':'active'})
    else:
        return render(request,'index.html',{'home_page':'active'})

def dehashview(request):
    if request.method == "POST":
        hashed = request.POST['hashed']
        words = request.POST['words']
        r_words = str(words).split(" ")
        answer = deHashUPH(wlist=r_words,hash_code=hashed)
        return render(request,'dehash.html',{'hashtype':answer[0],'hashvalue':answer[1],'hashed':hashed,'dehash_page':'active'})
    else:
        return render(request,'dehash.html',{'dehash_page':'active'})
