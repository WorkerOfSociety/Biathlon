from random import randint
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("              Biathlon")

print("         a hit or miss game")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("You got 5 shots")
targetsAll = [False,False,False,False,False,False,False,False,False,False]
counter = 0
n=0
def checkTurn(n):
    if n%2==0:
        return True
    else:
        return False
def printtargetsAll(n):
    print("1 2 3 4 5")
    for i in range(n,n+5):
        if targetsAll[i]:
            print("O", end="")
        else:
            print("*", end="")
        print(" ", end="")
    print("\n")

        
    
poäng =[0,0]

for i in range(10):
    if checkTurn(counter):
        n=0
        text = "A"
    else:
        n=5
        text = "B"
    hit = "tjena mittbean"
    while not (type(hit) == int):            
        try:
            hit = int(input(f"Spelare {text}, Aim nr {i//2+1} at target: "))
        except ValueError:
            print("Vilken måltavla är det?")
    if not randint(0,3)==0:
        if targetsAll[hit-1+n]:
            print("Den träffade du ju redan")
        else:
            print("Den var snygg!")
            poäng[checkTurn(counter)] += 1
        targetsAll[hit-1+n] = True
    else:
        print("Du suger")
    counter+=1
    printtargetsAll(n)


print(f"Spelare A träffade {poäng[1]} Måltavlor av 5 och spelare B träffade {poäng[0]} Måltavlor av 5")