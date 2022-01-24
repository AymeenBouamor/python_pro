#..................ses........................#
def saisie():
    e={}
    e["num"]=int(input("Donner le numéro : "))
    e["nom"]=(input("Donner le nom : "))
    e["serv"]=(input("Donner le service : "))
    while True:
        e["sit"]=(input("Donner la situation: "))
        if e["sit"]in["c","C","p","P"]:
            break
    while True:
        e["sal"]=int(input("Donner le salaire: "))
        if 800<=e["sal"]<=2000:
            break
    return(e)
def affiche(e):
    print("Donner le numéro : ",e["num"])
    print("Donner le nom : ",e["nom"])
    print("Donner le service : ",e["serv"])
    print("Donner la situation : ",e["sit"])
    print("Donner le salaire : ",e["sal"])
def mieuxpaye(e1,e2):
    if e1["sal"]>e2["sal"]:
        affiche(e1)
    elif e2["sal"]>e1["sal"]:
        affiche(e2)
    else:
        print("meme salaire")
        
employe={"num":int,"nom":str,"serv":str,"sit":str,"sal":int}
emp1=employe
emp2=employe
emp1=saisie()
emp2=saisie()
print("---------------Salaire le plus élève---------------")
mieuxpaye(emp1,emp2)




