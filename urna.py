# Criando uma urna eletrônica 

print("O Brasil tem um grave problema quando falamos em política, porém podemos ter ações que podem melhorar alguns dos fatores.")
print("A primeira que teremos é criar um algoritmo base para a Urna Eletrônica. Nesse algoritmo teremos apenas 3 candidatos:")

print("11 - Vincent Vega;")
print("22 - Jules Winfield;")
print("33 - Marsellus Wallace")
print(" ")
eleitores = int(input("Informe a quantidade de eleitores participantes da eleição: "))
voto1 = 0 # Vincent
voto2 = 0 # Jules
voto3 = 0 # Marsellus
tentativa = 5
total = 0

while total < eleitores:
  eleicao = int(input("Digite aqui o número do seu candidato: "))
  if eleicao == 11:
    voto1 += 1
    total += 1
  elif eleicao == 22:
    voto2 += 1
    total += 1
  elif eleicao == 33:
    voto3 += 1
    total += 1
  elif total == eleitores:
    break 

  while eleicao != 11 and eleicao != 22 and eleicao != 33 and tentativa > 0: 
    tentativa -= 1
    print(f"Opção inválida. Digite novamente o número do seu candidato ({tentativa} tentativa(s) restantes).")
    eleicao = int(input("Digite aqui o número do seu candidato: "))
    if eleicao == 11:
      voto1 += 1
      total += 1
      tentativa = 5
    elif eleicao == 22:
      voto2 += 1
      total += 1
      tentativa = 5
    elif eleicao == 33:
      voto3 += 1
      total += 1
      tentativa = 5
      continue

      
perc1 = (voto1 / eleitores) * 100 # Percentual Vincent Vega
perc2 = (voto2 / eleitores) * 100 # Percentual Jules Winfield
perc3 = (voto3 / eleitores) * 100 # Percentual Marsellus Wallace

print(" ")
print(f"O percentual do candidato Vincent Vega foi de: {perc1} %.")
print(f"O percentual do candidato Jules Winfield foi de: {perc2} %.")
print(f"O percentual do candidato Marsellus Wallace foi de: {perc3} %.")
print(" ")

if perc1 == perc2 and perc3 > perc1 and perc3 > perc2:
  print(f"Vicent Vega e Jules Winfield tiveram a mesma porcentagem de votos ({perc1}) %.")
  print(f"O vencedor foi Marsellus Wallace, com {perc3} % dos votos")
elif perc1 == perc3 and perc2 > perc1 and perc2 > perc3:
  print(f"Vincent Vega e Marsellus Wallace tiveram a mesma porcentagem de votos ({perc3}) %.")
  print(f"O vencedor foi Jules Winfield, com {perc2} % dos votos")
elif perc2 == perc3 and perc1 > perc2 and perc1 > perc3:
  print(f"Jules Winfield e Marsellus Wallace tiveram a mesma porcentagem de votos ({perc2}) %.")
  print(f"O vencedor foi Vincent Vega, com {perc1} % dos votos")
else:
  if perc1 == perc2 and perc3 < perc1 and perc3 < perc2:
    print(f"Vicent Vega e Jules Winfield empataram na disputa com ({perc1}) %.")
  elif perc1 == perc3 and perc2 < perc1 and perc2 < perc3:
    print(f"Vincent Vega e Marsellus Wallace tempataram na disputa com ({perc3}) %.")

  elif perc2 == perc3 and perc1 < perc2 and perc1 < perc3:
    print(f"Jules Winfield e Marsellus Wallace empataram na disputa com ({perc2}) %.")
  else:
    if perc1 > perc2 and perc1 > perc3:
      print(f"O candidato vencedor foi: Vincent Vega.")
    elif perc2 > perc1 and perc2 > perc3:
      print(f"O candidato vencedor foi: Jules Wincent.")
    elif perc3 > perc1 and perc3 > perc2:
      print(f"O candidato vencedor foi: Marsellus Wallace.")
