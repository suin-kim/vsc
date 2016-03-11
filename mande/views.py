from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Job, Volunteer
from .forms import SignupForm

def home(request):
    return render(request, 'mande/home.html')

class IndexView(generic.ListView):
    template_name = 'mande/index.html'
    context_object_name = 'latest_job_list'

    def get_queryset(self):
        """Return the last five published jobs."""
        return Job.objects.order_by('-pub_date')[:5]


def detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    print ("start")
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            job.new_volunteer = form.save()
            return HttpResponse("thanks")
            print("yes")
    else:
        form = SignupForm()
        print ("a")
    #volunteer = job.volunteer_set
    #form = SignupForm(request.POST)
    #if request.method == 'POST':
    #    if form.is_valid():
    #        volunteerform.save()
    return render(request, 'mande/detail.html', {'job' : job,'n' : range(1,13)})

def results(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'mande/results.html', {'job' : job})

#def vote(request, job_id):
#    job = get_object_or_404(Job, pk=job_id)
#    try:
#        selected_choice = job.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
#        # Redisplay the job voting form.
#        return render(request, 'mande/results.html', {
#            'job': job,
            #'error_message': "You didn't select a choice.",
#        })
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
#        return HttpResponseRedirect(reverse('mande:results', args=(job.job_id,)))
