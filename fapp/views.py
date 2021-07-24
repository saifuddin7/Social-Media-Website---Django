from typing import ContextManager
from django.db.models.query import InstanceCheckMeta
from django.shortcuts import render,redirect
from .models import Register,User,UserForm,UserPosts,UPostsForm,Interaction
from django.contrib.auth import login,logout,authenticate

def home(request):
    return render(request,'login.html')

def index(request):
    uid=request.session.get('uid')
    
    sp=UserPosts.objects.all()
    po_name=set()
    for i in sp:
        po_name.add(i.name)

    context={'po_name':po_name,'sp':sp}
    return render(request,'userView.html',context)

def register(request):
    if request.method=='POST':
        reg=UserForm(request.POST,request.FILES)
        reg.save()
        return redirect('/')
    else:
        reg=UserForm
        context={'reg':reg}
        return render(request,'form.html',context)

def login_view(request):
    
    if request.method=='POST':
        uname=request.POST.get('username')
        passw=request.POST.get('password')
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            
            sp=UserPosts.objects.all()
            po_name=set()
            for i in sp:
                po_name.add(i.name)
            context={'po_name':po_name,'sp':sp}
            return render(request,'userView.html',context)
        else:
            context={'msg':'Invalid Username and Password'}
            return render(request,'login.html',context)
    else:
        return render(request,'login.html')
        

def user_posts(request):
    if request.method=='POST':
        i=UserPosts()
        uid=request.session.get('uid')
        i.name=request.POST.get('name')
        i.img=request.FILES.get('img')
        i.description=request.POST.get('description')
        i.user=User.objects.get(id=uid)
        i.save()
        return redirect('/user_posts')
    else:
        reg=UPostsForm
        context={'reg':reg}
        return render(request,'form.html',context)

def show_posts(request):
    uid=request.session.get('uid')
    regi=Register.objects.filter(id=uid)
    sp=UserPosts.objects.all()
    context={'sp':sp,'regi':regi}
    return render(request,'userView.html',context)
    


def logout_view(request):
    logout(request)
    return redirect('/login')

def delete_post(request):
    u_id=request.GET.get('id')
    usr=UserPosts.objects.get(id=u_id)
    usr.delete()
    return redirect('/profile')

def edit_profile(request):
    uid=request.GET.get('id')
    r=UserPosts.objects.get(id=uid)
    if request.method=='POST':
        reg=UPostsForm(request.POST,request.FILES,instance=r)
        reg.save()
        return redirect('/profile')
    else:
        reg=UPostsForm(instance=r)
        context={'reg':reg}
        return render(request,'form.html',context)

def edit_reg(request):
    uid=request.GET.get('id')
    r=Register.objects.get(id=uid)
    if request.method=='POST':
        reg=UserForm(request.POST,request.FILES,instance=r)
        reg.save()
        return redirect('/profile')
    else:
        reg=UserForm(instance=r)
        context={'reg':reg}
        return render(request,'form.html',context)
  

def my_profile(request):
    uid=request.session.get('uid')
    regi=Register.objects.filter(id=uid)
    usrp=UserPosts.objects.filter(user=uid)
    context={'regi':regi,'usrp':usrp}
    return render(request,'profile.html',context)

def sort_by_name(request):
    data=request.GET.get('data')
    sp=UserPosts.objects.filter(name=data)
    po_name=set()
    for i in UserPosts.objects.all():
        po_name.add(i.name)
    context={'sp':sp,'po_name':po_name}
    return render(request,'userView.html',context)


def comments(request):
    uid=request.session.get('uid')
    global pid
    pid=request.GET.get('pid')
    
    sp=UserPosts.objects.filter(id=pid)
    inc=Interaction.objects.filter(userp_id=pid)
    if request.method=='POST':
        i=Interaction()
        i.comment=request.POST.get('comment')
        i.user=User.objects.get(id=uid)
        i.userp=UserPosts.objects.get(id=pid)
        i.save()
        context={'sp':sp,'inc':inc}
        return render(request,'comment.html',context)
    else:
            
        context={'sp':sp,'inc':inc}
        return render(request,'comment.html',context)

def delete_cmnt(request):
    iid=request.GET.get('id')
    commnt=Interaction.objects.get(id=iid)
    commnt.delete()
    
    #to redirect to comment page and view post and other comments
    #as we were passing pid with comment, while using redirect it was not taking pid only comment hence need to use render
    sp=UserPosts.objects.filter(id=pid)
    inc=Interaction.objects.filter(userp_id=pid)
    context={'sp':sp,'inc':inc}
    return render(request,'comment.html',context)

    
        
   
    
   









