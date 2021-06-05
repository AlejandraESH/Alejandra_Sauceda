from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
Prestamos = [
    {
        'monto': '1000',
        'tasa': '5',
        'plazo':'10',
        'cuota':'500',
        'total':'1500'
    }
]
def index(request):
    if (request.method == 'POST'):
        monto = int(request.POST.get('monto'))
        tasa = int(request.POST.get('tasa'))
        plazo = int(request.POST.get('plazo'))

        r = tasa / 100 / 12

        n = plazo * 12

        c = (monto * r) / (1 - (1 + r) ** -n)
        
        t = n * c

        cuota = c
        total = t 

        Prestamos.append({
            'monto': monto,
            'tasa':tasa,
            'plazo':plazo,
            'cuota':cuota,
            'total': total,
            
        })

        ctx = {
            'Prestamos': Prestamos
        }
        # return HttpResponse('El participante ha sido registrado')
        return render(request,'Prestamos/index.html', ctx)    
    else:
        ctx = {
            'Prestamos': Prestamos
        }
        # return HttpResponse('El participante ha sido registrado')
        return render(request,'Prestamos/index.html', ctx)