class CalculadoraModel:
    def calcular(self, expressao):
        try:
            resultado = eval(expressao)
            return resultado
        except ZeroDivisionError:
            return "Erro: divisão por zero"
        except:
            return "Erro"
