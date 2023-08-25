#IMC Calc

print("Calculadora de IMC")
print ("Bem - vindo")

#Entrada de dados
peso = float(input("Digite seu peso(kg): "))
altura = float(input("Digite sua altura(m): "))


#Cálculo IMC
IMC = round(peso / altura **2)

if IMC < 18.5:
    print(f"Seu IMC é {IMC:.2f}. Você está abaixo do peso.")

elif IMC >= 18.5 and IMC < 25:
    print(f"Seu IMC é {IMC:.2f}. Você está com peso normal.") 
   
elif IMC >=25 and IMC < 30:
    print(f"Seu IMC é {IMC:.2f}. Você está com sobrepeso.")

else:
    print(f"Seu IMC é {IMC:.2f}. Você está com obesidade.")