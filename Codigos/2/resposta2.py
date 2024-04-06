def fibonacci(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

def obter_numero():
    return int(input("Informe um número para validar a sequência de Fibonacci: "))

numero_digitado = obter_numero()

if fibonacci(numero_digitado):
    print(f"O número {numero_digitado} pertence à sequência de Fibonacci!! :)")
else:
    print(f"O número {numero_digitado} não pertence à sequência de Fibonacci... :(")