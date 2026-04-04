import datetime

print("🌸 Bem-vinde ao seu Diarinho 💖")
print("-----------------------------")

texto = input("💌 Como você está se sentindo hoje?\n> ")

data = datetime.datetime.now().strftime("%d/%m/%Y")

with open("diario.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{data} - {texto}\n")



print("\n✨ Registrado amore 💕")
print("🌷 Até mais 💖")
