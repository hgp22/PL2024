entradas = 0
modalidades = []
aptos = 0
idades = []

f = open("emd.csv", "r")

f.readline() # ignorar a primeira linha

for line in f:
    entradas += 1
    item = line.split(',')
    idades.append(int(item[5]))
    
    if item[12] == "true\n":
        aptos += 1
        
    if item[8] not in modalidades:
        modalidades.append(item[8])
f.close()

modalidades.sort()

aptos = (aptos/entradas)*100
n_aptos = 100 - aptos

faixa_etaria = [0] * 21
print(idades)
for i in idades:
    faixa_etaria[i//5] += 1

##
print("--Resultados--", '\n',
      "Lista Ordenada de Modalidades:", modalidades, '\n',
      "Percentagem de atletas aptos e inaptos:", aptos, n_aptos, '\n'
      "Distribuicao por Faixa etarias:")
i = 0
while i < len(faixa_etaria):
    a = i * 5
    print(f'[{a}-{a+4}] = {faixa_etaria[i]}')
    i += 1
##  
