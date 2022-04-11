idd = []
qtd20_30 = 0
qtdm_media = 0

for i in range(5):
  idd.append(int(input("Digite um número: ")))
  if idd[i] >=20 and idd[i] <=30:
    qtd20_30 +=1
media = sum(idd) / 5
for i in range (5):
  if idd[i] > media:
    qtdm_media += 1
print("A quantidade de pessoas com idade maior que a média é:", qtdm_media)
print("A média das idades é: ",media)
print("A menor idade é:", min(idd))
print("A quantidade de pessoas com idade entre 20 e 30 anos é: ", qtd20_30)