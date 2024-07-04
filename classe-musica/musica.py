class Musica:

    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
    
    def listar_musicas():
        for musicas in Musica.musicas:
            print(f'{musicas.nome} | {musicas.artista} | {musicas.duracao}')

imagine_dragons_beliver = Musica('Beliver', 'Imagine Dragons', 3.37)
twenty_one_pilots_stressed_out= Musica('Stressed out', 'Twenty one Pilots', 3.46)
artic_monkeys_arabela = Musica('Arabela', 'Artic Monkeys', 4.11)

Musica.listar_musicas()
