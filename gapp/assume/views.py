from django.shortcuts import render
from django.http import HttpResponse
from gnewsclient import gnewsclient
from .models import *
import datetime
from django.core.mail import send_mail

# Create your views here.
def index(request):
    lan = "hindi"

    client = gnewsclient.NewsClient(language=lan,
                                    location='india',
                                    topic='agriculture',
                                    max_results=3)

    news_list = client.get_news()
    item1 = news_list[0]
    item2 = news_list[2]
    item3 = news_list[2]
    paramas = {"news1": item1['title'], "news2": item2['title'], "news3": item3['title']}
    return render(request,'assume/index.html',paramas)

#about page
def about(request):
    return render(request,'assume/about.html')
#signup page
def signup(request):
    return render(request,'assume/signup.html')
#login page
def login(request):
    return render(request,'assume/login.html')

#admin loggin
def alog(request):
    return render(request,'assume/alogg.html')

#admin loggin verification
def alogin(request):
    global var
    password=request.POST.get("psw")
    username=request.POST.get("uname")
    value = admin_data.objects.get(username = username)
    var = value
    if password == value.psw:
        paramas={"name":value.name,"loc":value.location,"state":value.state}
        return render(request,'assume/crop.html',paramas)
    else:
        return HttpResponse("<h1>return back and try again !!!<h1>")

#user login verification
def ulogin(request):
    passwordg=request.POST.get("psw")
    unameg=request.POST.get("uname")
    uvalue=user_data.objects.get(username=unameg)
    if uvalue.psw == passwordg:
        tod = datetime.date.today()
        t = tod - datetime.timedelta(days=3)
        tod = tod.strftime("%Y-%m-%d")
        t = t.strftime("%Y-%m-%d")
        detail = Crop.objects.all().filter(state=uvalue.state)
        detail = detail.filter(location=uvalue.location)
        detail = detail.filter(date__range=[t, tod]).order_by('-date')
        params = {"lsr": detail, "loc": uvalue.location, "state": uvalue.state}
        return render(request, 'assume/search.html', params)
    else:
        return HttpResponse("YOU ENTERED  WRONG VALUES PLEASE RETURN BACK ")


# crop detail entered by admin at specific location
def crop(request):
    cropg = request.POST.get('crop').lower()
    priceg = request.POST.get('price')
    next = request.POST.get('next')
    qry = Crop(crop_name = cropg, price = priceg,location = var.location,state = var.state)
    qry.save()
    if next == "next crop":
        params = {'name': var.name, 'loc': var.location, 'state': var.state}
        return render(request,'assume/crop.html',params)
    else:
        mail_man()
        return index(request)


#home page--
def home(request):
    return index(request)

#search page
def search(request):
    location = request.POST.get('loc').lower()
    state = request.POST.get('state').lower()
    tod = datetime.date.today()
    t = tod-datetime.timedelta(days=3)
    tod = tod.strftime("%Y-%m-%d")
    t = t.strftime("%Y-%m-%d")
    state=state.replace(' ','')
    detail = Crop.objects.all().filter(state=state)
    detail = detail.filter(location=location)
    detail = detail.filter(date__range=[t,tod]).order_by('-date')
    params = {"lsr":detail, "loc":location, "state":state}
    return render(request,'assume/search.html',params)

# user sign in database
def usign(request):

    nameg=(request.POST.get('nm'))
    emailg = (request.POST.get('email'))
    pswg = (request.POST.get('psw'))
    addg = (request.POST.get('address')).lower().replace(" ","")
    count=0
    for i in addg:
        if i == "-" :
            break
        count = count+1
    disttg=addg[:count]
    stateg=addg[count+1:]
    qry = user_data(name=nameg,username=emailg,psw=pswg,location=disttg,state=stateg)
    qry.save()
    return index(request)


# data base connection for queries
def contact(request):
    mail = request.POST.get('email')
    suggestions =request.POST.get('sug')
    qry = suggestion(username=mail,text=suggestions)
    qry.save()
    return render(request, 'assume/about.html')

# mail sending code--
#mail send after admin enter in location
def mail_man():
    lst=[]
    lemail=[]
    tod = datetime.date.today()
    detail = Crop.objects.all().filter(state=var.state)
    detail = detail.filter(location=var.location)
    detail = detail.filter(date = tod)

    message =  f"Updated price of crop at mandi {var.location}, {var.state} is \n"
    for i in detail:
        msg = f"{i.crop_name} ----> {i.price} \n"
        lst.append(msg)
    for i in lst:
        message += i
    sub = "mandi today updated rate of crop"
    e_list = user_data.objects.all().filter(state = var.state)
    e_list = e_list.filter(location = var.location)
    for i in e_list:
        lemail.append(str(i.username))
    send_mail(sub,message,'prashantchandel2103@gmail.com',lemail,fail_silently=True)

