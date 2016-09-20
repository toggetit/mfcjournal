from django.shortcuts import render
from .models import Org, Actor, InRecord, OutRecord
from django.http import JsonResponse

from .forms import NewInForm

# Create your views here.
def journal(request):
    outRecs = OutRecord.objects.all()
    return render(request, 'journal.html', { 'outRecs': outRecs })

def json(request, jsn='in'):
    if jsn == 'in':
        recs = InRecord.objects.all()
        data = [
            { 'rec_num': rec.rec_num,
              'rec_date': rec.rec_date,
              'rec_org': rec.rec_org.org_name,
              'out_num': rec.out_num,
              'out_date': rec.out_date,
              'rec_desc': rec.rec_desc,
              'rec_actor': rec.rec_actor.__str__(),
              'control_date': rec.control_date,
              'rec_deal': rec.rec_deal,
              'action_date': rec.action_date }            
            for rec in recs ]
        
    elif jsn == 'out':
        recs = OutRecord.objects.all()
    
    return JsonResponse( { 'data': data }, safe=False )

def testform(request):
    form = NewInForm()
    return render(request, 'testform.html', { 'form': form })
