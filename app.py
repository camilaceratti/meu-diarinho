import tkinter as tk
from tkinter import messagebox
import datetime
import os
import random
import subprocess

tema_escuro = False

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
    label_contador.config(text="Caracteres: 0")
    messagebox.showinfo("🌸 meu diarinho", "registrado\naté mais 💖")


def alternar_tema():
    global tema_escuro
    tema_escuro = not tema_escuro

    if tema_escuro:
        janela.config(bg="#2b1b24")
        frame_principal.config(bg="#2b1b24")
        frame_esquerda.config(bg="#2b1b24")
        frame_centro.config(bg="#2b1b24")
        frame_direita.config(bg="#2b1b24")

        titulo.config(bg="#2b1b24", fg="#ffd6e7")
        subtitulo.config(bg="#2b1b24", fg="#ffd6e7")
        entrada.config(bg="#3a2430", fg="white", insertbackground="white")
        label_contador.config(bg="#2b1b24", fg="#ffd6e7")
        label_humor.config(bg="#2b1b24", fg="#ffd6e7")
    else:
        janela.config(bg="#ffd6e7")
        frame_principal.config(bg="#ffd6e7")
        frame_esquerda.config(bg="#ffd6e7")
        frame_centro.config(bg="#ffd6e7")
        frame_direita.config(bg="#ffd6e7")

        titulo.config(bg="#ffd6e7", fg="black")
        subtitulo.config(bg="#ffd6e7", fg="black")
        entrada.config(bg="white", fg="black", insertbackground="black")
        label_contador.config(bg="#ffd6e7", fg="black")
        label_humor.config(bg="#ffd6e7", fg="black")


def mostrar_humor():
    label_humor.config(text=random.choice(humores))


def ver_historico():
    pasta = "historico"
    os.makedirs(pasta, exist_ok=True)
    subprocess.Popen(f'explorer "{pasta}"')


def contar_caracteres(event=None):
    texto = entrada.get("1.0", tk.END)
    label_contador.config(text=f"Caracteres: {len(texto) - 1}")


# JANELA
janela = tk.Tk()
janela.title("🌸 meu diarinho")
janela.geometry("700x420")
janela.configure(bg="#ffd6e7")

# TÍTULO
titulo = tk.Label(
    janela,
    text="Bem-vinda ao seu diarinho 💖",
    bg="#ffd6e7",
    font=("Segoe Print", 16, "bold")
)
titulo.pack(pady=15)

# FRAME PRINCIPAL
frame_principal = tk.Frame(janela, bg="#ffd6e7")
frame_principal.pack(pady=20)

frame_esquerda = tk.Frame(frame_principal, bg="#ffd6e7")
frame_esquerda.grid(row=0, column=0, padx=20)

frame_centro = tk.Frame(frame_principal, bg="#ffd6e7")
frame_centro.grid(row=0, column=1, padx=20)

frame_direita = tk.Frame(frame_principal, bg="#ffd6e7")
frame_direita.grid(row=0, column=2, padx=20)

# ESQUERDA - BOTÃO TEMA
botao_tema = tk.Button(
    frame_esquerda,
    text="Tema",
    command=alternar_tema
)
botao_tema.pack(pady=20)

# CENTRO - SUBTÍTULO
subtitulo = tk.Label(
    frame_centro,
    text="Como você está se sentindo?",
    bg="#ffd6e7",
    font=("Segoe Print", 11)
)
subtitulo.pack(pady=5)

# ENTRADA
entrada = tk.Text(
    frame_centro,
    height=10,
    width=35,
    font=("Segoe Print", 11)
)
entrada.pack(pady=10)
entrada.bind("<KeyRelease>", contar_caracteres)

# CONTADOR
label_contador = tk.Label(
    frame_centro,
    text="Caracteres: 0",
    bg="#ffd6e7",
    font=("Segoe Print", 10)
)
label_contador.pack()

# BOTÃO SALVAR
botao_salvar = tk.Button(
    frame_centro,
    text="Salvar",
    command=salvar,
    bg="#ff8fb1",
    fg="white",
    font=("Segoe Print", 11)
)
botao_salvar.pack(pady=10)

# DIREITA - HUMOR DO DIA
humores = ["😊 Feliz", "😴 Cansada", "🤔 Pensativa", "💪 Motivada", "🌈 Leve"]

label_humor = tk.Label(
    frame_direita,
    text="",
    bg="#ffd6e7",
    font=("Segoe Print", 11)
)
label_humor.pack(pady=5)

botao_humor = tk.Button(
    frame_direita,
    text="Humor do dia",
    command=mostrar_humor,
    bg="#ffc0cb"
)
botao_humor.pack(pady=5)

botao_historico = tk.Button(
    frame_direita,
    text="Ver histórico",
    command=ver_historico,
    bg="#ffc0cb"
)
botao_historico.pack(pady=5)

janela.mainloop()
