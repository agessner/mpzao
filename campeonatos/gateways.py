from campeonatos.models import Campeonato


def obter_campeonatos_ativos_do_bd():
	return Campeonato.objects.filter(excluido=False)