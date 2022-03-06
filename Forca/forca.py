import os
import random
import menu as mn
os.system("cls")

p1=1; q1=3
p2=2; q2=2
p3=2; q3=3
p4=2; q4=4
p5=3; q5=2
p6=3; q6=4


with open('palavra.txt', 'r') as file:
    while True:
        mn.tela_principal()
        print("\n######## BEM VINDO AO JOGO DA FORCA ########")
        res=""
        while res!="s" and res!="n":
            res=input("\nDeseja jogar[s/n]? ")
            res.lower()
        if res=="s":
                file.seek(0,0)
                s=file.readlines()
                tam=len(s)
                linhaAleatoria=random.randrange(0,tam)
                print("linha aleatoria = " + str(linhaAleatoria))
                os.system("pause")
                x=0
                file.seek(0,0)
                while x<tam:
                    if linhaAleatoria==x:
                        palavra=file.readline()
                        break
                    else:
                        palavra=file.readline()
                        x+=1
                
                w=len(palavra)-1
                print()
                print(" - "*w)
           
                tentativaJogador=""
                erros=0
                acertos=0
                letrasChutadas=[]
                letrasAcertadas=[]
                p=""

                while True:
                    mn.tela_principal()
                    if p!="":
                        print(p)
                    else:
                        print(" - "*w)
                    tentativaJogador=input("\nQual letra voce chuta: ")
                    tentativaJogador.lower()
                    while tentativaJogador in letrasChutadas or tentativaJogador=='':
                        mn.tela_principal
                        print("Voce ja tentou essa letra, tente outra letra!")
                        tentativaJogador=input("\nQual letra voce chuta: ")
                        tentativaJogador.lower()
                        
                    if tentativaJogador in palavra and tentativaJogador not in letrasAcertadas:
                        print("\nParabens! Voce acertou")
                        letrasChutadas.append(tentativaJogador)
                        letrasAcertadas.append(tentativaJogador)
                        mn.tela_principal()
                        p=""
                        i=0
                        for s in palavra:
                            if s in letrasAcertadas:
                                p+=s+" "
                            else:
                                p+=" - "
                            i+=1
                            if i==w:
                                break
                        print(p)
                        print("\nLista de letras tentadas: " + str(letrasChutadas))
                        print("Lista de letras acertadas: " + str(letrasAcertadas))
                        os.system("pause")
                        
                        acertos+=palavra.count(tentativaJogador)
                        if acertos==w:
                            mn.tela_principal()
                            print("##### Parabens!!! Voce venceu!!! #####")
                            mn.matriz_forca=mn.redefinir_matriz(mn.matriz_forca)
                            os.system("pause")
                            break
                        continue
                    else:
                        erros+=1
        
                    if erros==1:
                        print("\nVoce errou!")
                        letrasChutadas.append(tentativaJogador)
                        mn.matriz_forca[p1][q1]="O"
                        mn.tela_principal()
                        print(p)
                        print("\n\nLetras chutadas: " + str(letrasChutadas))
                        os.system("pause")
                        continue   
                    elif erros==2:
                        print("\nVoce errou!")
                        letrasChutadas.append(tentativaJogador)
                        mn.matriz_forca[p2][q2]="/"
                        mn.tela_principal()
                        print(p)
                        print("\nLetras chutadas: " + str(letrasChutadas))
                        os.system("pause")
                        continue
                    elif erros==3:
                        print("\nVoce errou!")
                        letrasChutadas.append(tentativaJogador)
                        mn.matriz_forca[p3][q3]="|"
                        mn.tela_principal()
                        print(p)
                        print("\nLetras chutadas: " + str(letrasChutadas))
                        os.system("pause")
                        continue
                    elif erros==4:
                        print("\nVoce errou!")
                        letrasChutadas.append(tentativaJogador)
                        mn.matriz_forca[p4][q4]="\\"
                        mn.tela_principal()
                        print(p)
                        print("\nLetras chutadas: " + str(letrasChutadas))
                        os.system("pause")
                        continue
                    elif erros==5:
                        print("\nVoce errou!")
                        letrasChutadas.append(tentativaJogador)
                        mn.matriz_forca[p5][q5]="/"
                        mn.tela_principal()
                        print(p)
                        print("\nLetras chutadas: " + str(letrasChutadas))
                        os.system("pause")
                        continue
                    elif erros==6:
                        letrasChutadas.append(tentativaJogador)
                        mn.matriz_forca[p6][q6]="\\"
                        mn.tela_principal()
                        print("\n##### Voce Foi enforcado! #####")
                        print(p)
                        print("\nLetras chutadas: " + str(letrasChutadas))
                        os.system("pause")
                        mn.matriz_forca=mn.redefinir_matriz(mn.matriz_forca)
                        break
      
        else:
            break

file.close()