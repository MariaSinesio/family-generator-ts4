import random 
import json


with open("character.json", "r", encoding="utf-8") as c:
    character = json.load(c)

print("------- The Sims Generator -------")

print("Escolha o gênero do seu primeiro sim")

def generate_sim(gender):

# Se o gender for masculino, a estrutura que conter a chave masculine será usada
    if gender not in character:
        return "Genêro não encontrado, digite algo válido"

    first_name = random.choice(character[gender])
    last_name = random.choice(character["surnames"])
    attributes = random.choice(character["attributes"]["personalities"])
    sexualities = random.choice(character["attributes"]["sexualities"])
    age_bk = random.choice(character["attributes"]["age bucket"]) 

# Como se fosse um template, um embed do Discord
    message = (f"♡~(≧ω≦)~ ━━━★ Seu sim prontinho ★━━━ ~(≧ω≦)~♡\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
               f"Nome do seu sim é {first_name} {last_name}\n"
               f"Sexualidade: {sexualities}\n"
               f"Personalidade: {attributes}\n"
               f"Faixa etária: {age_bk}\n"
               f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    return message

user = input("Qual será o gênero do seu sim?(female/masculine):\n").strip().lower()
print(generate_sim(user))