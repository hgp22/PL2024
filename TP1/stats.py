import sys

entradas = 0
modalidades = []
aptos = 0
idades = []

sys.stdin.readline() # ignorar a primeira linha

for line in sys.stdin:
    entradas += 1
    item = line.split(',')
    idades.append(int(item[5]))
    
    if item[12] == "true\n":
        aptos += 1
        
    if item[8] not in modalidades:
        modalidades.append(item[8])

modalidades.sort()

aptos = (aptos/entradas)*100
n_aptos = 100 - aptos

faixa_etaria = [0] * 21
for i in idades:
    faixa_etaria[i//5] += 1

##
print("--Resultados--", '\n',
      "Lista Ordenada de Modalidades:", modalidades, '\n',
      "Percentagem de atletas aptos e inaptos:", aptos, n_aptos, '\n'
      "Distribuicao por Faixa etarias:")
for i, faixa in enumerate(faixa_etaria):
    print(f'[{i*5}-{(i*5)+4}] = {faixa}')
##  
