from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
#from django.template import RequestContext, loader
#from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
import logging
from polls.models import Poll, Choice
from rest_framework.response import Response
from rest_framework.views import APIView

class IndexView(generic.ListView):
   template_name= 'polls/index1.html'
   context_object_name= 'latest_poll_list'

   def get_queryset(self):
      return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
   model=Poll
   template_name='polls/details.html'
   def get_queryset(self):
      return Poll.objects.filter(pub_date__lte=timezone.now())

class ResultView(generic.DetailView):
   model=Poll
   template_name='polls/results.html'


class Index_SPA(generic.TemplateView):
    template_name = 'polls/index.html'

class GetQuestions(APIView):
    def get(self, request, format=None):
        polls = Poll.objects.values('questions', 'id')
        return Response({"data": polls})


"""def index(request):
   #return HttpResponse("Hello, world. You are at the poll index.")
   latest_poll_list=Poll.objects.order_by('-pub_date')[:5]
   #template=loader.get_template('polls/index1.html')
   #context=RequestContext(request, {'latest_poll_list': latest_poll_list})
   context={'latest_poll_list': latest_poll_list}
   #return HttpResponse(template.render(context))
   return render(request, 'polls/index1.html', context)

def detail(request,poll_id):
   poll=get_object_or_404(Poll,pk=poll_id)
   return render(request,'polls/details.html', {'poll': poll}) """

def vote(request, poll_id):
   p=get_object_or_404(Poll, pk=poll_id)
   try:
      selected_choice=p.choice_set.get(pk=request.POST['choice'])
   except(KeyError, Choice.DoesNotExist):
      return render(request, 'polls/details.html', {'poll':p, 'error_message': "You didn't select a choice.",})
   else:
      selected_choice.votes+=1
      selected_choice.save()
      return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))   


"""def results(request, poll_id):
   poll=get_object_or_404(Poll, pk=poll_id)
   return render(request,'polls/results.html', {'poll': poll}) """

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'D:/mysite//debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


