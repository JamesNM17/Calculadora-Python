import tkinter as tk
from calculadora_model import CalculadoraModel


class CalculadoraView:
    def __init__(self):
        self.model = CalculadoraModel()

        self.janela = tk.Tk()
        self.janela.title("Calculadora")
        self.janela.geometry("300x400")
        self.janela.configure(bg="#1e1e1e")

        self.expressao = ""

        self.display = tk.Entry(
            self.janela,
            font=("Arial", 18),
            justify="right",
            bg="#2d2d2d",
            fg="white",
            bd=10
        )
        self.display.pack(fill="both", padx=10, pady=10)

        self.criar_botoes()

    def criar_botoes(self):
        botoes = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        frame = tk.Frame(self.janela, bg="#1e1e1e")
        frame.pack()

        linha = 0
        coluna = 0

        for botao in botoes:
            tk.Button(
                frame,
                text=botao,
                width=5,
                height=2,
                font=("Arial", 14),
                bg="#3a3a3a",
                fg="white",
                command=lambda b=botao: self.clique(b)
            ).grid(row=linha, column=coluna, padx=5, pady=5)

            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1

        tk.Button(
            self.janela,
            text="C",
            font=("Arial", 14),
            bg="#ff5555",
            fg="white",
            command=self.limpar
        ).pack(fill="both", padx=10, pady=10)

    def clique(self, valor):
        if valor == "=":
            resultado = self.model.calcular(self.expressao)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, resultado)
            self.expressao = str(resultado)
        else:
            self.expressao += valor
            self.display.insert(tk.END, valor)

    def limpar(self):
        self.expressao = ""
        self.display.delete(0, tk.END)

    def iniciar(self):
        self.janela.mainloop()