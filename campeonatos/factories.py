import functools
from campeonatos.gateways import obter_campeonatos_ativos_do_bd
from campeonatos.core.obter_campeonatos_ativos import obter_campeonatos_ativos


def obter_campeonatos_ativos_factory():
	return functools.partial(
		obter_campeonatos_ativos,
		obter_campeonatos_ativos_do_bd=obter_campeonatos_ativos_do_bd
	)
