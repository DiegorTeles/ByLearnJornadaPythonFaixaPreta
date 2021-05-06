def calculo_imc(peso, altura):

  imc = peso / ( altura * altura )

  if imc <= 16:
    print(f'Seu IMC é : {imc:.2f}\n Baixo peso muito grave')

  elif imc >= 16 and imc <= 16.99:
    print(f'Seu IMC é : {imc:.2f}\n Baixo peso grave')

  elif imc >= 17 and imc <= 18.49:
    print(f'Seu IMC é : {imc:.2f}\n Baixo peso')

  elif imc >= 18.50 and imc <= 24.99:
    print(f'Seu IMC é : {imc:.2f}\n Peso normal')

  elif imc >= 25 and imc <= 29.99:
    print(f'Seu IMC é : {imc:.2f}\n Sobrepeso')

  elif imc >= 30 and imc <= 34.99:
    print(f'Seu IMC é : {imc:.2f}\n Obesidade grau I')

  elif imc >= 35 and imc <= 39.99:
    print(f'Seu IMC é : {imc:.2f}\n Obesidade grau II')
    
  else:
    print(f'Seu IMC é : {imc:.2f}\n obesidade mórbida')
    
    
altura = float(input('Qual sua altura em Metros (M)? '))
peso = float(input('Qual seu peso em quilos (KG)? '))

calculo_imc(peso,altura)
