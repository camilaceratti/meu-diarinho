import tkinter as tk
from tkinter import messagebox
import datetime
import os

def salvar():
    texto = entrada.get("1.0", tk.END).strip()

    if texto == "":
        messagebox.showwarning("ops", "como você está se sentindo?")
        return

    pasta = "historico"
    os.makedirs(pasta, exist_ok=True)

    data_arquivo = datetime.datetime.now().strftime("%d-%m-%Y")
    caminho_arquivo = os.path.join(pasta, f"{data_arquivo}.txt")

    with open(caminho_arquivo, "a", encoding="utf-8") as f:
        f.write(texto + "\n")

    entrada.delete("1.0", tk.END)
    messagebox.showinfo("🌸 meu diarinho", "registrado\naté mais 💖")

janela = tk.Tk()
janela.title("🌸 meu diarinho")
janela.geometry("420x420")
janela.configure(bg="#ffd6e7")

titulo = tk.Label(
    janela,
    text="Bem-vinda ao seu diarinho 💖",
    bg="#ffd6e7",
    font=("Arial", 16)
)
titulo.pack(pady=15)

subtitulo = tk.Label(
    janela,
    text="Como você está se sentindo?",
    bg="#ffd6e7",
    font=("Arial", 11)
)
subtitulo.pack(pady=5)

entrada = tk.Text(
    janela,
    height=10,
    width=35,
    font=("Arial", 11)
)
entrada.pack(pady=10)

botao = tk.Button(
    janela,
    text="Salvar",
    command=salvar,
    bg="#ff8fb1",
    fg="white",
    font=("Arial", 11)
)
botao.pack(pady=10)

janela.mainloop()
