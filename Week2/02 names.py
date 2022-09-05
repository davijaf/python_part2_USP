names = ["Helena", "Alice", "Laura", "Manuela", "Sophia", "Isabella", "Luísa", "Heloísa",
        "Cecília", "Maitê", "Eloá", "Elisa", "Liz", "Júlia", "Maria Luísa", "Valentina",
        "Maria Alice", "Lívia", "Antonella", "Lorena", "Ayla", "Isis", "Maria Júlia",
        "Maya", "Maria Clara", "Esther", "Giovanna", "Lara", "Sarah", "Beatriz", "Aurora",
        "Mariana", "Maria Cecília", "Olívia", "Maria Helena", "Isadora", "Luna", "Catarina",
        "Melissa", "Maria Eduarda", "Lavínia", "Agatha", "Emanuelly", "Maria", "Alícia", "Rebeca",
        "Ana Clara", "Yasmin", "Clara", "Marina", "Ana Júlia", "Ana Luísa", "Isabelly", "Ana Laura",
        "Rafaela", "Ana Liz", "Stella", "Gabriela", "Vitória", "Allana", "Mirella", "Milena",
        "Bella", "Ana", "Nicole", "Emilly", "Maria Vitória", "Mariah", "Clarice", "Letícia", "Laís",
        "Maria Liz", "Bianca", "Melina", "Jade", "Ana Beatriz", "Maria Fernanda", "Betina",
        "Maria Valentina", "Maria Laura", "Heloíse", "Maria Isis", "Zoenovo", "Louise", "Malu",
        "Melinda", "Ana Cecília", "Ana Lívia", "Ana Vitória", "Maria Heloísa", "Chloe", "Maria Flor",
        "Pietra", "Pérola", "Ana Sophia", "   Maria Elisa   ", "Gabrielly", "Larissa", "Maria Eloá", "Eduarda"]

def shortName(names):
    short = names[0]
    for name in range(len(names)):
        if len(names[name].replace(" ", "")) <= len(short.replace(" ", "")):
            short = names[name].lower()
    print(short)

shortName(names)