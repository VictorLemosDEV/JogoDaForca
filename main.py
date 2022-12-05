import random
import re
palavras = []

with open("palavrasboas.txt", mode = "r") as file:
  for x in file.readlines():
    pos = x.find(" ")
    palavras.append(x[:pos])


resposta = random.choice(palavras)

acertos = {}

def checar_resposta(chute):
#Checar se alguma letra do chute está na palavra certa

  nAcertos = 0

  string = []
  for x in resposta:
    string.append( "_ ")
  

  for x,y in enumerate(resposta):
    if y in chute:
      nAcertos += 1
      if y in acertos:
        acertos[y].append(x)
      else:
        acertos[y] = [x]


  for x,y in acertos.items(): #("a", [2,3,4])
    for z in y:
      string[z] = x

  if chute == "":
      return "".join(string), 100
  
      
  return "".join(string), nAcertos
  
      
    
  
  

def forca6():
  print("┏━━━━━┓")
  print("┃     ┃")
  print("┃")
  print("┃")
  print("┃")
  print("┃")
  print("┗━━━")
  print("")
  print("")

def forca5():
  print("┏━━━━━┓")
  print("┃     ┃")
  print("┃     ☹")
  print("┃")
  print("┃")
  print("┃")
  print("┗━━━")
  print("")
  print("") 

def forca4 ():
  print("┏━━━━━┓")
  print("┃     ┃")
  print("┃     ☹")
  print("┃     |")
  print("┃")
  print("┃")
  print("┗━━━")
  print("")
  print("") 

def forca3 ():
  print("┏━━━━━┓")
  print("┃     ┃")
  print("┃     ☹")
  print("┃     |")
  print("┃     /")
  print("┃")
  print("┗━━━")
  print("")
  print("") 

def forca2 ():
  print("┏━━━━━┓")
  print("┃     ┃")
  print("┃     ☹")
  print("┃     |")
  print("┃     /\\")
  print("┃")
  print("┗━━━")
  print("")
  print("") 

def forca1 ():
  print("┏━━━━━┓")
  print("┃     ┃")
  print("┃     ☹")
  print("┃    /|")
  print("┃     /\\")
  print("┃")
  print("┗━━━")
  print("")
  print("") 

def forca0 () :
  print("┏━━━━━┓")
  print("┃     ┃")
  print("┃     ☹")
  print("┃    /|\\")
  print("┃     /\\")
  print("┃")
  print("┗━━━")
  print("")
  print("") 
def gameover ():
  print("╔══════════════════╗")
  print("║                  ║")
  print("║    𝕘𝕒𝕞𝕖 𝕠𝕧𝕖𝕣     ║")
  print("║                  ║")
  print("║   𝕧𝕔 𝕖́ 𝕠𝕥𝕒́𝕣𝕚𝕠    ║")
  print("╚══════════════════╝")
  print(f"a resposta era {resposta}")
def youwin ():
  print("     ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
  print("    ⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛")
  print("    ⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛")
  print("   ⬛⬜⬛⬛⬛⬜⬛⬛⬛⬛⬜⬜⬜⬜⬛")
  print("   ⬛⬜⬜⬛⬛⬜⬜⬜⬛⬛⬜⬛⬛⬜⬜⬛")
  print("    ⬛⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬛⬛⬜⬛")
  print("    ⬛⬜⬜⬛⬛⬜⬜⬜⬛⬛⬛⬜⬛⬜⬛")
  print("    ⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬜⬜⬜⬛")
  print("    ⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬜⬜⬛")
  print("   ⬛⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬛")
  print("   ⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛")
  print("   ⬛⬜⬜⬜⬜⬜⬜⬛⬛⬛")
  print("    ⬛⬛⬛⬛⬛⬛")
  print(" ")
  print("    You win")
  
  
tentativasRestantes = 6
tentativas = 0
def Atualizar(chute):
  nAcertos = None
  global tentativasRestantes
  global tentativas
  
  

  if tentativasRestantes == 6:
    resultado, nAcertos = checar_resposta(chute)
    
    
    
    print("")
    print("")
  elif tentativasRestantes == 5:
    
    resultado, nAcertos = checar_resposta(chute)
    
    
    print("")
    print("")
  elif tentativasRestantes == 4:
    
    resultado, nAcertos = checar_resposta(chute)
    
    
    print("")
    print("")
  elif tentativasRestantes == 3:
    
    resultado, nAcertos = checar_resposta(chute)
    
    
    print("")
    print("")
  elif tentativasRestantes == 2:
    
    resultado, nAcertos = checar_resposta(chute)
    
    
    print("")
    print("")
  elif tentativasRestantes == 1:
    
    resultado, nAcertos = checar_resposta(chute)
    
    
    print("")
    print("")
  elif tentativasRestantes == 0:
    
    resultado, nAcertos = checar_resposta(chute)
    
    
    print("")
    print("")
  

  
  if nAcertos == 0 and tentativasRestantes != 0:
    tentativasRestantes -= 1

  tentativas += 1
  
  
    
  
  
  

funcoes = {0: forca0, 1: forca1, 2: forca2, 3: forca3, 4: forca4, 5:forca5, 6:forca6}







while True:
  if "_" not in checar_resposta("")[0]:
    funcoes[tentativasRestantes]()
    youwin()
    break
  
  
  if tentativasRestantes == 0:
    forca0()
    print(checar_resposta("")[0])
    gameover()
    break
  elif tentativasRestantes < 6:
    
    funcoes[tentativasRestantes]()
    print(checar_resposta("")[0])
    chute=input("escreva uma letra\n")
    Atualizar(chute)
  else:
    
    forca6()
    print(checar_resposta("")[0])
    chute=input("escreva uma letra\n")
    Atualizar(chute)
    
  
