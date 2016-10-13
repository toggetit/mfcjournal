from django.shortcuts import render
from .models import Org, Actor, InRecord, OutRecord
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from .forms import NewInForm
from datetime import date

# Create your views here.
def journal(request):
    outRecs = OutRecord.objects.all()
    return render(request, 'journal.html', { 'outRecs': outRecs })

def jsonrequest(request, jsn='in'):
    if jsn == 'in':
        recs = InRecord.objects.all()
        data = [
            {
                'pk' : rec.pk,
                'rec_num': rec.rec_num,
                'rec_date': rec.rec_date,
                'rec_org': rec.rec_org.org_name,
                'out_num': rec.out_num,
                'out_date': rec.out_date,
                'rec_desc': rec.rec_desc,
                'rec_actor': rec.rec_actor.__str__(),
                'control_date': rec.control_date,
                'rec_deal': rec.rec_deal,
                'action_date': rec.action_date
            }            
            for rec in recs ]
        
    elif jsn == 'out':
        recs = OutRecord.objects.all()
    
    return JsonResponse( { 'data': data } )

def addnewin(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewInForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #Добавляем суффикс года
            newRec = InRecord(**form.cleaned_data)
            newRec.rec_num = str(date.today().year)[2:] + '/' + newRec.rec_num
            newRec.save()
            # redirect to a new URL:
            #return HttpResponse('OK')
            return HttpResponseRedirect('/journal')        
        else:
            # send back items
            print(form.errors.items())
    else:
        # Получаем номера документов, приводим их к int и выделяем из них последний
        # такой геморрой нужен по 2 причинам:
        # 1. Могут быть номера вида 123/1, 123-1
        # 2. Таким образом получится резервировать номера        
        nums = InRecord.objects.all().values_list('rec_num', flat=True)
    
        if len(nums) == 0:
            nextNumRec = 1
        else:
            # Улучшить бы это по-питоньи
            prepared_nums = []
            for num in nums:
                try:
                    prepared_nums.append(int(num[3:]))
                except ValueError:
                    continue
            if len(prepared_nums) == 0:
                prepared_nums.append(0)
            nextNumRec = max(prepared_nums)+1
        # Значение по-умолчанию для вх. док 
        form = NewInForm(initial = {'rec_num': nextNumRec } )

    return render(request, 'addnewin.html', { 'form': form, 'nums': list(nums) })

def delrec(request, typerec='in'):
    pks = json.loads(request.body.decode('utf-8'))['data']
    print('Delete this records', pks)
    InRecord.objects.filter(pk__in=pks).delete()
    return HttpResponse('null')

def checknum(request, typerec='in'):
    num = json.loads(request.body.decode('utf-8'))['data']
    print('received num:', num)
    if(InRecord.objects.filter(rec_num=num).exists()):
        print('num exists')
        return JsonResponse( { 'data' : 'ERROR' } )
    else:
        print('num is NOT exists')
    return JsonResponse( { 'data' : 'OK' } )
