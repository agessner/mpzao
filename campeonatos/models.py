from django.db import models


class Campeonato(models.Model):
	criacao = models.DateTimeField(auto_now_add=True)
	ultima_alteracao = models.DateTimeField(auto_now=True)
	excluido = models.BooleanField(default=False)
	nome = models.TextField(max_length=80)


class Rodada(models.Model):
	criacao = models.DateTimeField(auto_now_add=True)
	ultima_alteracao = models.DateTimeField(auto_now=True)
	excluido = models.BooleanField()
	campeonato = models.ForeignKey(to=Campeonato, on_delete=models.PROTECT)
	numero = models.IntegerField()


class Time(models.Model):
	criacao = models.DateTimeField(auto_now_add=True)
	ultima_alteracao = models.DateTimeField(auto_now=True)
	excluido = models.BooleanField()
	nome = models.TextField(max_length=80)
	jogador = models.TextField(max_length=80)


class Jogo(models.Model):
	criacao = models.DateTimeField(auto_now_add=True)
	ultima_alteracao = models.DateTimeField(auto_now=True)
	excluido = models.BooleanField()
	campeonato = models.ForeignKey(to=Campeonato, on_delete=models.PROTECT)
	rodada = models.ForeignKey(to=Rodada, on_delete=models.PROTECT)
	mandante = models.ForeignKey(to=Time, on_delete=models.PROTECT, related_name='mandante')
	vistante = models.ForeignKey(to=Time, on_delete=models.PROTECT, related_name='visitante')
	gols_mandante = models.IntegerField()
	gols_visitante = models.IntegerField()
