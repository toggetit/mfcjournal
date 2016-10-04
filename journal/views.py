from django.shortcuts import render
from .models import Org, Actor, InRecord, OutRecord
from django.http import JsonResponse, HttpResponseRedirect

from .forms import NewInForm

# Create your views here.
def journal(request):
    outRecs = OutRecord.objects.all()
    return render(request, 'journal.html', { 'outRecs': outRecs })

def json(request, jsn='in'):
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
            # process the data in form.cleaned_data as required
            newRec = InRecord(**form.cleaned_data)
            newRec.save()
            # redirect to a new URL:                        
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
        # Улучшить бы это по-питоньи
        prepared_nums = []
        for num in nums:
            try:
                prepared_nums.append(int(num))
            except ValueError:
                continue
        # Значение по-умолчанию для вх. док 
        form = NewInForm(initial={'rec_num': max(prepared_nums)+1})

    return render(request, 'addnewin.html', { 'form': form })
