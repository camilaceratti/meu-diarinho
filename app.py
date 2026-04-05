tema_escuro = False
def alternar_tema():
    global tema_escuro
    tema_escuro = not tema_escuro

    if tema_escuro:
        # ROSA ESCURO 🌙
        janela.config(bg="#2b1b24")
        titulo.config(bg="#2b1b24", fg="#ffd6e7")
        entrada.config(bg="#3a2430", fg="white", insertbackground="white")

    else:
        # ROSA CLARO 🌸
        janela.config(bg="#ffe4ec")
        titulo.config(bg="#ffe4ec", fg="#b03060")
        entrada.config(bg="white", fg="black", insertbackground="black")
      
botao_tema = tk.Button(janela, text="Tema", command=alternar_tema)
botao_tema.pack(pady=5)
