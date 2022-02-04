import random

#Prints para dar contexto ao jogo e definir regras
#Utilizando a tabela ANSI, nativa do Python para utilizar o negrito
print("Olá,\n")
print("Dois cachorros, Bob e Rex avistaram um gato e resolveram pega-lo.")
print("Para isso resolveram apostar na sorte, com um dado para ver quem chegaria no gato primeiro")
print("Temos uma linha reta com dois cachorros, Bob e Rex, no fim desta linha está Oli, o gato.")
print("Esta linha possuí 10 blocos de tijolo, Bob e Rex iniciam no bloco 1 e Oli está no bloco 20")
print('O "dado" que irão jogar possuí a forma geométrica de um Decágono e por isso tem 10 lados\n')
print("\033[;1mRegras:\033[0;0m")
print("1. Bob e Rex jogam o dado juntos na primeira vez, se cair a mesma posição, eles devem jogar de novo")
print("2. Quem estiver com a maior posição joga o dado primeiro na próxima vez")
print("3. Se chegarem juntos, isso iniciará uma briga entre eles e Oli irá fugir")
print("4. Se em algum momento os dois pararem no mesmo bloco, jogará o que na primeira rodada tirou um maior número")
print("5. Eles avançam juntos, então podem chegar juntos dependendo da posição que estiverem")
print("Exemplo: Se o Rex estiver na posição 19 e o Bob na posição 11, o rex tira 1 e o Bob 9 então eles chegam juntos na mesma rodada na posição de Oli (posição 20)")
print("Vamos ver quem ganha esta corrida!\n\n")

print("Início do jogo!")
def game(): #Inicio da função
    oli = 20 #Posição do gato(Oli) permanece em 20
    bob = random.randint(1, 10) #"Jogada do 'dado'", random de 1 a 10
    first_bob = bob #Copia o valor inicial da primeira jogada de rex para a variável first_bob, seguindo a regra 4 definida por mim
    rex = random.randint(1, 10) #"Jogada do 'dado'", random de 1 a 10
    first_rex = rex #Copia o valor inicial da primeira jogada de rex para a variável first_rex, seguindo a regra 4 definida por mim

    rounds = 1 #Rounds inicia como 1, pois já teve a primeira jogada de dado

    if bob != rex: #Se bob diferente de rex (cumprindo a regra número 1 definida por mim)
        print(f'\033[1mBOB tirou o número {bob} na primeira jogada do dado \nREX tirou o número {rex} na primeira jogada do dado \nPosição fixa de OLI que está se alimentando: {oli}\033[0m\n\n')

        while True: #Loop infinito até alguém vencer ou empatar
            rounds = rounds + 1  # Conta mais uma rodada

            if (bob == oli) and (bob != rex):
                print(f"\nNúmero de rodadas necessárias: {rounds}")
                print("Bob pegará o gato")
                break  # Encerra o programa

            elif (rex == oli) and (rex != bob):
                print(f"\nNúmero de rodadas necessárias: {rounds}")
                print("Rex pegará o gato")
                break  # Encerra o programa

            elif (rex == oli) and (bob == oli):  # Se rex e bob estiverem na posição de OLI juntos, Oli foge
                print(f"\nNúmero de rodadas necessárias: {rounds}")
                print("\033[91mBob e Rex chegaram ao mesmo tempo, eles irão brigar e portando Oli conseguirá fugir.\033[0m")
                break #Encerra o programa

            if (bob > rex) or (first_bob > first_rex): #Se bob estiver na frente de rex ou a primeira jogada de bob tiver sido que a de rex, bob joga primeiro
                print(f"\nRodada número: {rounds}")
                new_randon_bob = random.randint(1, 10) #Um "randon" novo para cada jogada, por isso uma nova variável
                bob = bob + new_randon_bob #Soma o número de bob a variável nova
                if bob >= oli: #Se bob maior ou igual a oli (chegou ou passou da posição de oli)
                    bob = oli #Número de bob setado para o número que oli está, para que vença na verificação acima e também para que o print abaixo não fique em uma posição superior a que OLI está
                print(f'Bob conquistou mais {new_randon_bob} blocos e já conseguiu chegar na posição {bob}')

                #Vez de rex jogar
                new_randon_rex = random.randint(1, 10) #Um "randon" novo para cada jogada, por isso uma nova variável
                rex = rex + new_randon_rex #Soma o número de rex a variável nova
                if rex >= oli: #Se rex maior ou igual a oli (chegou ou passou da posição de oli)
                    rex = oli #Número de rex setado para o número que oli está, para que vença na verificação acima e também para que o print abaixo não fique em uma posição superior a que OLI está
                print(f'Rex conquistou mais {new_randon_rex} blocos e já conseguiu chegar na posição {rex}')

                continue #Volta ao início do loop

            #Seguindo a mesma lógica do loop acima, mas se rex for maior do que bob ou a sua primeira jogada tiver sido maior do que a de bob
            elif (rex > bob) or (first_rex > first_bob):
                print(f"\nRodada número: {rounds}")
                new_randon_rex = random.randint(1, 10)
                rex = rex + new_randon_rex

                if rex >= oli:
                    rex = oli
                print(f'Rex conquistou mais {new_randon_rex} blocos e já conseguiu chegar na posição {rex}')

                new_randon_bob = random.randint(1, 10)
                bob = bob + new_randon_bob
                if bob >= oli:
                    bob = oli
                print(f'Bob conquistou mais {new_randon_bob} blocos e já conseguiu chegar na posição {bob}')
            continue

    else: #Se os dados caíram na mesma posição na primeira jogada, executa novamente a função game (reinicia as jogadas)
        game()


#Programa principal
game()