from django.shortcuts import render
from ..forms import ContactForm

def create(request):

    if request.method == 'POST':
        context = {
            'form': ContactForm(data=request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context=context,
        )

    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context=context,
    )
