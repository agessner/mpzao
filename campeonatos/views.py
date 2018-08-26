from django.shortcuts import render

from django.http import HttpResponse
from campeonatos.factories import obter_campeonatos_ativos_factory
import ujson 


def index(request):
	obter_campeonatos_ativos = obter_campeonatos_ativos_factory()
	campeonatos = obter_campeonatos_ativos()
	return HttpResponse(ujson.dumps(list(campeonatos), ensure_ascii=False))
