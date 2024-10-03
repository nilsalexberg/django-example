from django.shortcuts import render, redirect
from .forms import ContactForm
from django.views import View

# Create your views here.
class ContactView(View):
  def get(self, request):
    context = {
      'form': ContactForm()
    }

    if 'message' in request.session:
      message = request.session['message']
      del request.session['message']
      context['message'] = message

    return render(request, 'contact/index.html', context)
  
  def post(self, request):
    form = ContactForm(request.POST)

    if not form.is_valid():
      context = {
        'form': form
      }
      return render(request, 'contact/index.html', context)

    form.save()

    request.session['message'] = 'Mensagem enviada com sucesso!'

    return redirect('/contato/')