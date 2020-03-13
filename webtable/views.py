from django.shortcuts import render, redirect
from .form import TestForm
from .models import InfoModelForm
from .form import InfoModelFormAdd

def index(request):
    my_dict = {
    'insert_something':"views.pyのinsert_something部分です。",
    'name':'Bashi',
    'form':TestForm(),
    'insert_forms':'初期値',
    }
    if (request.method == 'POST'):
        my_dict['insert_forms'] = '文字列:' + request.POST['text'] + '<br>整数型:' + request.POST['num']
        my_dict['form'] = TestForm(request.POST)

    return render(request,'webtable/index.html',my_dict)

def info(request):
    infodata = InfoModelForm.objects.all()
    infodata2 = InfoModelForm.objects.values()
    my_dict2 = {
        'title':'テスト',
        'val':infodata,
        'val2':infodata2,
    }

    return render(request, 'webtable/info.html', my_dict2)

def create(request):
    if (requst.method == 'POST'):
        obj = InfoModelForm()
        info = InfoModelFormAdd(request.POST, instance=obj)
        info.save()
        return redirect(to='/info')
    modelform_dict = {
    'title':'modelformテスト',
    'form':InfoModelFormAdd(),
    }
    return render(request, 'webtable/create.html', modelform_dict)

def update(request, num):
    obj = InfoModelForm.objects.get(id=num)

    if(request.method == 'POST'):
        info = InfoModelFormAdd(request.POST, instance=obj)
        info.save()
        return redirect(to='/info')
    update_dict = {
    'title' :'登録情報更新画面',
    'id':num,
    'form':InfoModelFormAdd(instance=obj),
    }

    return render(request, 'webtable/update.html',update_dict)

def delete(request, num):
    obj = InfoModelForm.objects.get(id=num)
    if (request.method == 'POST'):
        obj.delete()
        return redirect(to='/info')
    delete_dict = {
        'title':'削除確認',
        'id':num,
        'obj':obj,
    }
    return render(request, 'webtestapp/delete.html',delete_dict)
