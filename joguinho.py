import os
from turtle import clear

player = {
    "nome": "Py", 
    "x": 0, 
    "y": 0
}

def andar(direcao): 
    if direcao == "d":
        player['x'] += 1
    elif direcao == "a":
        player["x"] -= 1
    elif direcao == "w":
        player['y'] -= 1
    elif direcao == "s":
        player['y'] += 1
        
while True:
    os.system('clear')
    
    print("----------------------------")
    for y in range(5):
        print("\n")
        for x in range(10):
            if player['x'] == x and player['y'] == y:
                print("🏃", end="")
            else:
                print("🟩", end="")
    print("----------------------------")
    
    direcao = input("Proxima direção (w,s,d,a): ")
    
    if direcao in ["w", "s", "d", "a"]:
        andar(direcao)
    else:
        print("Direção inválida. Use 'w', 's', 'd', ou 'a'.")
    
    
    