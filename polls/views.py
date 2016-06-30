from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Question, Choice
# Create your views here.

#----------------------------------------------------------------------------#
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]
#----------------------------------------------------------------------------#
class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

#----------------------------------------------------------------------------#
class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

#----------------------------------------------------------------------------#
def vote(request, question_id):
	question = Question.objects.get(pk= question_id)
	selected_choice = question.choice_set.get(pk=request.POST['choice'])
	selected_choice.votes += 1
	selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#----------------------------------------------------------------------------#
class SignUpView(generic.CreateView):
	form_class = UserCreationForm
	model = User
	success_url = reverse_lazy('polls:index')
	template_name = 'polls/signup.html'


#----------------------------------------------------------------------------#
class LoginView(generic.FormView):
	form_class = AuthenticationForm
	success_url = reverse_lazy('polls:index')
	template_name = 'polls/login.html'

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)

		if user is not None and user.is_active:
			login(self.request, user)
			return super(LoginView,self).form_valid(form)
		else:
			return self.form_invalid(form)

#----------------------------------------------------------------------------#

class LogoutView(generic.RedirectView):
	url = reverse_lazy('polls:index')

	def get(self, request):
		logout(request)
		return super(LogoutView, self).get(request)

#----------------------------------------------------------------------------#

