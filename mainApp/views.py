from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum, F

from mainApp.models import MainView, Keywords, News
from mainApp.forms import MainViewForm

def main(request):
	main_list = MainView.objects.all()
	keywords = Keywords.objects.all()
	# keywords = Keywords.objects.filter()

	query = request.GET.get("q")
	if query:
		main_list = main_list.filter(main_service__icontains = query)
	paginator = Paginator(main_list, 4)

	page = request.GET.get('page')
	try:
		services_list = paginator.page(page)
	except PageNotAnInteger:
		services_list = paginator.page(1)
	except EmptyPage:
		services_list = paginator.page(paginator.num_pages)

	form = MainViewForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		return redirect('/')

	context = {'services_list': services_list, 'keywords': keywords, 'form':form}
	return render(request, 'mainApp/homePage.html', context)

def about(request):
	return render(request, 'mainApp/about.html')

def show_singlpages(request, show_main_id):
	args = {}
	args.update(csrf(request))
	args['services_lists'] = get_object_or_404(MainView, id = show_main_id)
	return render(request, 'mainApp/singlPages.html', args)

def keywords(request, k_id):
	keywords = Keywords.objects.all()
	args = {}
	args['keywords'] = Keywords.objects.all()
	args['keyws'] = Keywords.objects.get(id = k_id)
	args['services_list'] = MainView.objects.filter(keywords__name__exact = args['keyws'])
	return render(request, 'mainApp/keypage.html', args)

def news(request):
	news_m = News.objects.all()
	context = {'news_m':news_m}
	return render(request, 'mainApp/test.html', context)

def show_news(request, news_id):
	args = {}
	args.update(csrf(request))
	args['news_list'] = get_object_or_404(News, id = news_id)
	return render(request, 'mainApp/news.html', args)

def addlikes(request, news_id):
	news = get_object_or_404(News, id = news_id)
	news.likes += 1
	news.save()
	return redirect('/news/%s' %news_id)
