from django.http import HttpResponse

def index(request):
	return HttpResponse("<ul><li><a href='polls'>Polls?</a><li><a href='calci'>Calculator?</a></ul>")
