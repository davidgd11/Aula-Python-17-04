opcao = int(input("Escolha a opção desejada de 1 a 5: "))

match opcao:
    case 1:
        print("Voce optou pela alternativa 1")
            
    case 2:
        print("Voce optou pela alternativa 2 ")
        
    case 3:
        print("Voce optou pela alternativa 3")
    
    case 4:
        print("Voce optou pela alternativa 4")
        
    case 5:
        print("Voce optou pela alternativa 5")
        
    case _:
        print("Opção inválida")
        
        
São Paulo - plataforma 1 
Rio de Janeiro - plataforma 2
Curitiba - plataforma 3
Brasília - plataforma 4
Florianópolis - plataforma 5


print("""Olhe aqui os destinos: 
     (1) São Paulo; \n 
     (2) Rio de Janeiro; \n 
     (3) Curitiba; \n 
     (4) Brasília; \n
     (5) Florianópolis. \n """)
 plataforma = int(input("Qual é o seu destino? (Digite o número de 1 a 5): "))

#Utilizar números para minimizar as chances de erro na hora da digitação

match plataforma:
    case 1:
        print("Vá para a plataforma 1")
        
    case 2:
        print("Vá para a plataforma 2")
        
    case 3:
        print("Vá para a plataforma 3")
        
    case 4:
        print("Vá para a plataforma 4")
        
    case 5:
        print("Vá para a plataforma 5")
        
    case _:
        print("Opção inválida")
        
            
        
print("""Dê uma olha em nosso ótimos vinhos!
      (1) Casa Valduga Gran R$ 160,00. \n
      (2) Casa Silva Gran Terrois Los Carménère R$130,00. \n
      (3) Chocalan Origen Viogner R$ 180,00. \n
      (4) Miolo Demi-sec Reserva especial 2005 R$ 90,00. \n
      (5) Casa Silva Terrois Cabernet Savignon R$ 100,00.\n """)
      
   
vinho = int (input("Qual vinho você deseja escolher? (Digite o número pré estabelecido no menu de opções.): " ))

match vinho:
    case 1:
        print("Casa Valduga Gran R$ 160,0.")
    
    case 2:
        print("Casa Silva Gran Terrois Los Carménère R$130,00.")
    
    case 3:
        print("Chocalan Origen Viogner R$ 180,00.")
    
    case 4:
        print("Miolo Demi-sec Reserva especial 2005 R$ 90,00.")
    
    case 5:
        print("Casa Silva Terrois Cabernet Savignon R$ 100,00.")
    
    case _:
        print("Opção inválida!")
        
        
num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))

print("""Observe os tipos de operações póssíveis:
                (1) Soma \n
                (2) Subtração \n
                (3) Divisão \n 
                (4) Multiplicação \n """)
                
calculo = int(input("Digite a opção que você deseja executar: "))

match calculo:
    case 1: 
        soma = (num1 + num2)
        print("A soma entre %d e %d é igual à: %d" %(num1, num2, soma))
        
    case 2:
        print(int(num1 - num2))
        
    case 3:
        print(int(num1 / num2))
        
    case 4:
        print(int(num1 * num2))
