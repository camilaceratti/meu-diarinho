import tkinter as tk
from tkinter import messagebox
import datetime

def salvar():
    texto = entrada.get("1.0", tk.END).strip()

    if texto == "":
        messagebox.showwarning("ops", "escreve alguma coisa 💖")
        return

    data = datetime.datetime.now().strftime("%d/%m/%Y")

    with open("diario.txt", "a", encoding="utf-8") as f:
        f.write(f"{data} - {texto}\n")

    entrada.delete("1.0", tk.END)
    messagebox.showinfo("💌", "salvo")

# janela
janela = tk.Tk()
janela.title("🌸 diarinho")

# tamanho
janela.geometry("400x400")

# cor de fundo (rosinha)
janela.configure(bg="#ffc0cb")

# título
titulo = tk.Label(janela, text="🌸 diarinho 💖", bg="#ffc0cb", font=("Arial", 16))
titulo.pack(pady=10)

# caixa de texto
entrada = tk.Text(janela, height=10, width=35)
entrada.pack(pady=10)

# botão
botao = tk.Button(janela, text="💌 salvar", command=salvar, bg="#ff69b4", fg="white")
botao.pack(pady=10)

janela.mainloop()
