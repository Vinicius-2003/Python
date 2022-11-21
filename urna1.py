def cadastro_cand(f,g,p,part):
    pref = list()
    gov = list()
    pres = list()
    while True:
        cargo = input('A qual cargo ele disputará : ').upper()
        if cargo == 'PREFEITO':
            nome = input('Digite o nome do candidato : ').upper()
            pref.append(nome)
            num = int(input('Digite o número : '))
            pref.append(num)
            partido = input('Digite a qual partido ele pertence : ').upper()
            pref.append(partido)
            part.append(partido)
            pref.append(0)
            f.append(pref)
            pref = list()
            continuar = input('Deseja continuar ? : ').upper()
            if continuar == 'SIM':
                continue
            else:
                break
        elif cargo == 'GOVERNADOR':
            nome = input('Digite o nome do candidato : ').upper()
            gov.append(nome)
            num = int(input('Digite o número : '))
            gov.append(num)
            partido = input('Digite a qual partido ele pertence : ').upper()
            gov.append(partido)
            part.append(partido)
            gov.append(0)
            g.append(gov)
            gov = list()
            continuar = input('Deseja continuar ? : ').upper()
            if continuar == 'SIM':
                continue
            else:
                break
        elif cargo == 'PRESIDENTE':
            nome = input('Digite o nome do candidato : ')
            pres.append(nome)
            num = int(input('Digite o número : '))
            pres.append(num)
            partido = input('Digite a qual partido ele pertence : ').upper()
            pres.append(partido)
            part.append(partido)
            pres.append(0)
            p.append(pres)
            pres = list()
            continuar = input('Deseja continuar ? : ').upper()
            if continuar == 'SIM':
                continue
            else:
                break

prefeitos = list()
governadores = list()
presidentes = list()
partido = list()

def pessoa(listapessoa):
    while True:
        print(partido)
        nome = input('Insira seu nome : ').upper()
        cpf = input('Insira seu cpf : ')
        listaaux = list()
        listaaux.append(nome)
        listaaux.append(cpf)
        for i in range(3):
            listaaux.append(False)
        listapessoa.append(listaaux)
        continuar = input('Deseja continuar ? : ').upper()
        if continuar == 'SIM':
            continue
        else:
            break

eleitores = list()


def votar(b,n,e,tot):
    for y in e:
        print('É a vez de {}|{} votar!'.format(y[0],y[1]))
        print('Ordem de votação : PREFEITO / GOVERNADOR / PRESIDENTE')
        podeBreak1 = False
        podeBreak2 = False
        podeBreak3 = False 
        if y[2] == False:
            if len(prefeitos) != 0:
                while True:
                    if podeBreak1 == True:
                        break
                    num1 = int(input('Digite o número do Prefeito : '))
                    for p in prefeitos:
                        if num1 == -1:
                            confirma = input('Seu voto foi marcado branco. confirma? (sim/não): ').upper()
                            if confirma =='SIM':
                                print('Seu voto foi confirmado {}!'.format(y[0]))
                                b[0] +=1
                                tot[0] += 1
                                print(tot)
                                y[2] = True
                                podeBreak1 = True
                                break
                        elif num1 ==-2:
                            confirma = input('Seu voto foi marcado nulo. confirma? (sim/não): ').upper()
                            if confirma =='SIM':
                                print('Seu voto foi confirmado {}!'.format(y[0]))
                                n[0] +=1
                                y[2] = True
                                tot[0] += 1
                                podeBreak1 = True
                                break
                        if p[1] == num1:
                            confirma = input('{} esse é o seu candidato? (sim/ não) : '.format([p])).upper()
                            if confirma =='SIM':
                                y[2] = True
                                p[3] += 1
                                tot[0] += 1
                                print(tot)
                                print('Seu voto foi confirmado {}!'.format(y[0]))
                                podeBreak1 = True
                                break
            else:
                print('\033[0;31mNão há nenhum Prefeito cadastrado!\033[m')
        else:
            print('\033[0;32mEssa pessoa já votou!!\033[m')
        if y[3] == False:
            if len(governadores) != 0:
                while True:
                    if podeBreak2 == True:
                        break
                    num2 = int(input('Digite o número do Governador : '))
                    for g in governadores:
                        if num2 == -1:
                            confirma = input('Seu voto foi marcado branco. confirma? (sim/não): ').upper()
                            if confirma =='SIM':
                                print('Seu voto foi confirmado {}!'.format(y[0]))
                                b[1] +=1
                                y[3] = True
                                tot[1] += 1
                                print(tot[1])
                                podeBreak2 = True
                                break
                        elif num2 == -2:
                            confirma = input('Seu voto foi marcado nulo. confirma? (sim/não): ').upper()
                            if confirma =='SIM':
                                print('Seu voto foi confirmado {}!'.format(y[0]))
                                n[1] += 1
                                y[3] = True
                                tot[1] += 1
                                podeBreak2 = True
                                break
                        if g[1] == num2:
                            confirma = input('{} esse é o seu candidato? (sim/ não) : '.format([g])).upper()   
                            if confirma == 'SIM':
                                y[3] = True
                                g[3] += 1
                                tot[1] += 1
                                print(tot)
                                print('Seu voto foi confirmado {}!'.format(y[0]))
                                podeBreak2 = True
                                break
            else:
                print('\033[0;31mNão há nenhum Governador cadastrado!\033[m')
        else:
            print('\033[0;32mEssa pessoa já votou!!\033[m')
        if y[4] == False:
            if len(presidentes) != 0:
                while True:
                    if podeBreak3 == True:
                        break
                    num3 = int(input('Digite o número do Presidente : '))
                    for pres in presidentes:
                        if num3 == -1:
                            confirma = input('Seu voto foi marcado branco. confirma? (sim/não): ').upper()
                            if confirma =='SIM':
                                print('Seu voto foi confirmado {}!'.format(y[0]))
                                b[2] +=1
                                y[4] = True
                                tot[2] += 1
                                podeBreak3 = True
                                break
                        elif num3 ==-2:
                            confirma = input('Seu voto foi marcado nulo. confirma? (sim/não): ').upper()
                            if confirma =='SIM':
                                print('Seu voto foi confirmado {}!'.format(y[0]))
                                n[2] +=1
                                y[4] = True
                                tot[2] += 1
                                podeBreak3 = True
                                break
                        else:
                            if pres[1] == num3:
                                confirma = input('{} esse é o seu candidato? (sim/ não) : '.format([pres])).upper()   
                                if confirma == 'SIM':
                                    y[4] = True
                                    pres[3] += 1
                                    tot[2] += 1
                                    print(tot)
                                    print('Seu voto foi confirmado {}!'.format(y[0]))
                                    podeBreak3 = True
                                    break
            else:
                print('\033[0;31mNão há nenhum Presidente cadastrado!\033[m')
        else:
            print('\033[0;32mEssa pessoa já votou!!\033[m')

total = [0,0,0]
votoembranco = [0,0,0]
votonulo = [0,0,0]


def apurar_resulpref(prefeitos):
    for i in range(len(prefeitos)-1):
        for j in range(i+1, len(prefeitos)):
            if prefeitos[i][3]< prefeitos[j][3]:
                prefeitos[i],prefeitos[j] = prefeitos[j],prefeitos[i]
    for a in range(len(prefeitos)):
        print('-=-'*30)
        print('\033[0;34mRanking de Prefeitos!\033[m')
        print('{}: {} | {} | Total de votos: {} ' .format(a+1,prefeitos[a][0],prefeitos[a][2],prefeitos[a][3]))
        print('-=-'*30)
        print('Total de votos = {}'.format(total[0]))
        print('-=-'*30)
        print('Total de brancos = {}'.format(votoembranco[0]))
        print('-=-'*30)
        print('Total de nulos = {}'.format(votonulo[0]))
        
        
def apurar_resulgov(governadores):
    for i in range(len(governadores)-1):
        for j in range(i+1, len(governadores)):
            if governadores[i][3]< governadores[j][3]:
                governadores[i],governadores[j] = governadores[j],governadores[i]
    for a in range(len(governadores)):
        print('-=-'*30)
        print('\033[0;34mRanking de Governadores!\033[m')
        print('{}: {} | {} | Total de votos: {} ' .format(a+1,governadores[a][0],governadores[a][2],governadores[a][3]))
        print('-=-'*30)
        print('Total de votos = {}'.format(total[1]))
        print('-=-'*30)
        print('Total de brancos = {}'.format(votoembranco[1]))
        print('-=-'*30)
        print('Total de nulos = {}'.format(votonulo[1]))
        
        
def apurar_resulpres(presidentes):
    for i in range(len(presidentes)-1):
        for j in range(i+1, len(presidentes)):
            if presidentes[i][3]< presidentes[j][3]:
                presidentes[i],presidentes[j] = presidentes[j],presidentes[i]
    for a in range(len(presidentes)):
        print('-=-'*30)
        print('\033[0;34mRanking de Presidentes!\033[m')
        print('{}: {} | {} | Total de votos: {} ' .format(a+1,presidentes[a][0],presidentes[a][2],presidentes[a][3]))
        print('-=-'*30)
        print('Total de votos = {}'.format(total[2]))
        print('-=-'*30)
        print('Total de brancos = {}'.format(votoembranco[2]))
        print('-=-'*30)
        print('Total de nulos = {}'.format(votonulo[2]))

organizar_partido = list()

def estatisticas(eleitores,partido):
    eleitores.sort()
    for i in range(len(eleitores)):
        print(eleitores[i][0:2])
    for c in range(len(partido)-1):
        for d in range(c+1,len(partido)+1):
            partido.sort()
            print(partido)



while True:
    menu = print('''
    1. Cadastrar Candidatos
    2. Cadastrar Eleitores
    3. Votar
    4. Apurar Resultados
    5. Relatório e Estatísticas
    6. Encerrar''')
    menu_escolha = int(input('Digite o valor desejado : '))
    if menu_escolha == 1:
        cadastro_cand(prefeitos,governadores,presidentes,partido)
        print(prefeitos)  
        print(governadores)
        print(presidentes)
    elif menu_escolha == 2:
        pessoa(eleitores)
        print(eleitores)
    elif menu_escolha == 3:
        votar(votoembranco,votonulo,eleitores,total)
    elif menu_escolha == 4:
        apurar_resulpref(prefeitos)
        apurar_resulgov(governadores)
        apurar_resulpres(presidentes)
    elif menu_escolha == 5:
        estatisticas(eleitores,partido)
    elif menu_escolha == 6:
        break