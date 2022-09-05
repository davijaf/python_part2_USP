names = [" helena", "Alice", "Laura", "Manuela", "Sophia", "Isabella", "Luísa", "Heloísa",
        "Cecília", "Maitê", " eloá", "Elisa", "Liz", "Júlia", "Maria Luísa", "Valentina",
        "Maria Alice ", "Lívia", "Antonella", "lorena", "Ayla", "Isis", "Maria Júlia",
        "Maya", "Maria Clara", "Esther", "Giovanna", "Lara", "Sarah", "Beatriz", "Aurora",
        "mariana", "Maria Cecília", "olívia", "Maria Helena", "Isadora", "Luna", "Catarina",
        "Melissa", " Maria Eduarda", "lavínia", "agatha", "emanuelly", "Maria", "Alícia", "Rebeca",
        "Ana Clara", "Yasmin", "Clara", "Marina", "Ana Júlia", "Ana Luísa", "Isabelly", "Ana Laura",
        "Rafaela", "Ana Liz", "stella", "Gabriela", "Vitória", "Allana", "Mirella", "Milena",
        "Bella", "Ana", "Nicole", "Emilly", "Maria Vitória", "Mariah", "Clarice", "Letícia", "Laís",
        "Maria Liz", "Bianca", "Melina", "Jade", "Ana Beatriz", "Maria Fernanda", " betina",
        "Maria Valentina", "Maria Laura", "Heloíse", "maria Isis", "Zoenovo", "Louise", "Malu",
        "Melinda", "Ana Cecília", "Ana Lívia", "ana Vitória", "Maria Heloísa", "chloe", "Maria Flor",
        "Pietra", "Pérola", "Ana Sophia", "   Maria Elisa   ", " Gabrielly", "larissa", "Maria Eloá", "Eduarda"]

names_sorted = []

for name in range(len(names)):
    names_sorted.append(names[name].strip().capitalize())
names_sorted = sorted(names_sorted)
lowerName = names_sorted[0]
print(names_sorted)
print("The first name is :", lowerName)