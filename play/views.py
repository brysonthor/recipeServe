# Create your views here.
from django.http import HttpResponse
import datetime
from play.models import ingredient, recipe
try:
	import json
except ImportError:
	import simplejson as json


def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def getIngredients(request):
	ingrList = ['Click Here When Done'] 
	ingr = ingredient.objects.all()
	for x in ingr:
		ingrList.append(x.name)
	addTag = {"ingredients" : ingrList}
	return HttpResponse(json.dumps(addTag))

def getRecipes(request):
	userIng = request.GET['instruments'].split(',')
	allRec = recipe.objects.all()
#	canCook = []
#	for r in allRec:
#		curIngList = r.getIngredientslist()
#		bool test = 0 
#		for i in curIngList:
#			if(!userIng.contains(i)):
#				test = 0
#				break
#			else:
#				test = 1
#		if(i):
#			canCook.add(r)
#	return HttpResponse(json.dumps(canCook))
