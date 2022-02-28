import random
from time import sleep

lista = [('47589283749','Natalia'),
         ('63564286842','Iolanda'),
         ('66538826927','Vera'),
         ('73687683798','Camila'),
         ('63658163791','Leo'),
        ('66538826927','Lucas'),
         ('73687683798','Leone'),
         ('63658163791','Lorenzo'),
        ('73687683798','Vivi'),
         ('63658163791','Marcelo')
         ]

num_cadeiras = len(lista)-1

while len(lista)>1:
  print('Música tocando ....')
  sleep(1)
  print('Música para ....')
  sleep(1)
  print('Jogadores se movimentam...')
  sleep(3)
  #sortear alguém para sair do jogo
  random.shuffle(lista)
  print(f'O jogador {lista.pop()[1]} saiu do jogo') #retirando o último nome da lista

  #num_cadeiras -=1

print(f'O Jogador(a) {lista[0][1]} venceu!!')