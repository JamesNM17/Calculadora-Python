class CalculadoraModel:
    def calcular(self, expressao):
        try:
            # Avalia a expressão matemática
            resultado = eval(expressao)
            return resultado
        except ZeroDivisionError:
            return "Erro: divisão por zero"
        except:
            return "Erro"