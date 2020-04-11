#Anthony Bernardo Kamers - 19204700

class Matematica:
    def primo(self, numero):
        qtdDivisivel = 0

        for i in range(1, numero+1):
            if numero % i == 0:
                qtdDivisivel += 1

        if qtdDivisivel == 2:
            print("Primo")
        else:
            print("Não é primo")

    def fatorial(self, numero):
        def fat(numero):
            if numero == 0 or numero == 1:
                return 1
            else:
                return numero * fat(numero-1)

        return fat(numero)

    def fibonacci(self, numero):
        def fib(numero):
            if numero <= 1:
                return numero
            else:
                return fib(numero-1) + fib(numero-2)
        
        return fib(numero)

    def fibonarial(self, numero):
        x = self.fibonacci(numero)
        y = self.fatorial(x)
        return y

#mat = Matematica()
#mat.primo(23)
# x = mat.fatorial(5)
# print(x)
# y = mat.fibonacci(6)
# print(y)
# z = mat.fibonarial(5)
# print(z)