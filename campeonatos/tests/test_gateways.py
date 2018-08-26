from django.test import TestCase
from campeonatos.models import Campeonato
from campeonatos.gateways import obter_campeonatos_ativos_do_bd

class ObterCampeonatoAtivoTestCase(TestCase):
	def test_obtem_apenas_campeonatos_ativos(self):
		campeonato_ativo = Campeonato.objects.create(nome='Campeonato')
		campeonato_excluido = Campeonato.objects.create(nome='Campeonato Excluido', excluido=True)

		campeonatos = obter_campeonatos_ativos_do_bd()

		self.assertEqual(1, len(campeonatos))
		self.assertEqual(campeonato_ativo, campeonatos[0])
