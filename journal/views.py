from django.shortcuts import render
from .models import Org, Actor, InRecord, OutRecord
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
import json
from .forms import inRecForm, markDoneForm, actorsForm, orgsForm
from datetime import date, datetime

# Create your views here.
def journal(request):
    InRecs = InRecord.objects.all()
    actors = Actor.objects.filter(is_active = True)
    return render(request, 'journal.html', { 'actors': actors })

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

    elif jsn == 'act':
        recs = Actor.objects.all()
        data = [
            {
                'pk' : rec.pk,
                'name' : rec.name,
                'surname' : rec.surname,
                'is_active' : rec.is_active,
            }            
            for rec in recs ]

    elif jsn == 'orgs':
        recs = Org.objects.all()
        
    return JsonResponse( { 'data': data } )

def addnewin(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = inRecForm(request.POST)
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
        form = inRecForm(initial = {'rec_num': nextNumRec } )

    return render(request, 'addnewin.html', { 'form': form, 'nums': list(nums) })

def edit(request, editpk=0, typerec='in'):
    '''
    if not editpk:
        print('not edit pk')
        return HttpResponseRedirect('/journal/')
    '''
    
    if request.method == 'POST':
        print('typerec is:', typerec)
        #Редактируем inRecord
        if typerec == 'in':
            form = inRecForm(request.POST)
            if form.is_valid():                                        
                #Добавляем суффикс года
                editData = form.cleaned_data
                InRecord.objects.filter(pk = editpk).update(
                    rec_num = editData['rec_num'],
                    rec_org = editData['rec_org'],
                    out_num = editData['out_num'],
                    out_date = editData['out_date'],
                    rec_desc = editData['rec_desc'],
                    rec_actor = editData['rec_actor'],
                    control_date = editData['control_date'],
                    action_date = editData['action_date'],
                )
                return HttpResponseRedirect('/journal/')
            else:
                print(form.errors.items())
            #Редактируем сотрудника
        elif typerec == 'act':
            form = actorsForm(request.POST)
            if form.is_valid():
                # Новый хлопец
                if form.cleaned_data['pk'] is not None:
                    print('Редактируем сотрудника', form.cleaned_data['surname'], form.cleaned_data['name'], form.cleaned_data['pk'])
                    editRec = Actor.objects.filter(pk = form.cleaned_data['pk']).update(                    
                        name = form.cleaned_data['name'],
                        surname = form.cleaned_data['surname'],
                        is_active = form.cleaned_data['is_active']
                    )
                else:
                    # редактируем старого хлопца
                    print("Добавляем нового сотрудника", form.cleaned_data['surname'], form.cleaned_data['name'])
                
                    newRec = Actor(**form.cleaned_data)
                    newRec.save()
                return HttpResponseRedirect('/journal/')
            else:
                print(form.errors.items())
        else:
            # send back items
            print('typerec is:', typerec)
        
    else:
        editedItem = InRecord.objects.get(pk=editpk)
        form = inRecForm(initial = { 'rec_num': editedItem.rec_num,
                                     'rec_org': editedItem.rec_org,
                                     'out_num': editedItem.out_num,
                                     'out_date': editedItem.out_date,
                                     'rec_desc': editedItem.rec_desc,
                                     'rec_actor': editedItem.rec_actor,
                                     'control_date': editedItem.control_date,
                                     'rec_deal': editedItem.rec_deal,
                                     'action_date': editedItem.action_date })
        return render(request, 'editin.html', { 'form': form, 'pk': editpk })

def delrec(request, typerec='in'):
    if typerec == 'in':
        pks = json.loads(request.body.decode('utf-8'))['data']
        print('Delete this records:', typerec, pks)
        InRecord.objects.filter(pk__in=pks).delete()
    return HttpResponse('null')

def checknum(request, typerec='in'):
    num = json.loads(request.body.decode('utf-8'))['data']
    print('received num:', num)
    if(InRecord.objects.filter(rec_num=num).exists()):
        #print('num exists')
        return JsonResponse( { 'data' : 'ERROR' } )
    else:
        #print('num is NOT exists')
        return JsonResponse( { 'data' : 'OK' } )

def appoint(request):
    if request.method == 'POST':
        recs = json.loads(request.body.decode('utf-8'))['data']
        actor = json.loads(request.body.decode('utf-8'))['actor']
        #print('received data:', recs, 'actor', actor)
        
        InRecord.objects.filter(pk__in=recs).update(rec_actor=actor)
        
        return JsonResponse( { 'data': 'ok' })
    else:
        return JsonResponse( { 'data': 'error' })
    

def markdone(request):
    if request.method == 'POST':
        recs = json.loads(request.body.decode('utf-8'))['data']
        doneDate = datetime.strptime(json.loads(request.body.decode('utf-8'))['doneDate'], '%d.%m.%Y')
        #print('received data:', recs, 'done date:', doneDate)
        
        InRecord.objects.filter(pk__in=recs).update(action_date = doneDate)
        
        return JsonResponse({ 'data': 'ok'})
    else:
        form = markDoneForm()
    
        return render(request, 'markdone.html', { 'form': form })

def loadTableTemplate(request, typerec='in'):
    if typerec == 'in':
        return render(request, 'injournal.html')
    elif typerec == 'out':
        return render(request, 'outtable.html')


def actors(request):

    form = actorsForm()

    return render(request, 'actors.html', { 'form': form })

def orgs(request):

    form = orgsForm()

    return render(request, 'organizations.html', { 'form': form })
