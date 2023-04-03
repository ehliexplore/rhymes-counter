

def line():
    print('~' * 80)


lyrics = """Talvez eu to vivendo em transe
Tipo um mês só queimando blunt
Tipo um ano olhando pra estante
Tipo uma década no mesmo rasante
Porque o tempo é uma flecha e eu não sinto essa Terra girando
Porque o tempo é uma flecha e eu não sinto essa Terra girando
Talvez eu to vivendo em transe
Tipo um mês só queimando blunt
Tipo um ano olhando pra estante
Tipo uma década no mesmo rasante
Porque o tempo é uma flecha e eu não sinto essa Terra girando
Porque o tempo é uma flecha e eu não sinto essa Terra girando

Eu tava sentado pensando
Coisas que eu faço girando
Novo rap, novo ano
Corações de quem eu amo
Bebidas a noite na cidade
Batalhas e luas e planos
Vivências em turmas e bandos
Ciência e rua e danos

Talvez eu to vivendo em transe
Quando emoção e pressão é constante
Quando eu to de roupa velha elegante
Quando acelera meu fluxo de sangue
Porque o tempo é uma flecha e eu não sinto essa Terra girando
Porque o tempo é uma flecha e eu não sinto essa Terra girando
Talvez eu to vivendo em transe
Quando emoção e pressão é constante
Quando eu to de roupa velha elegante
Quando acelera meu fluxo de sangue
Porque o tempo é uma flecha e eu não sinto essa Terra girando
Porque o tempo é uma flecha e eu não sinto essa Terra girando"""

lyrics_clean = lyrics.replace('\n', ' ')
words = lyrics_clean.split(' ')
print(words)

option = str(input('Enter a letter to see all words ending with it: ')).lower()[0]

rhymes = list(filter(lambda string: string[-1:] == f'{option}', words))

cont = 0
for w in rhymes:
    if len(w) == 1:
        pass
    else:
        print(w)
        cont += 1
line()
print(f'The letter {option} are used to finish words {cont} times')
line()


