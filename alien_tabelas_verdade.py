import ttg

print("="*80)
print("TABELAS VERDADE - ALIEN: O OITAVO PASSAGEIRO")
print("="*80)

# Cenário 1: Substâncias incomuns no corpo
# Proposições:
# p: O chefe de segurança foi encontrado com substâncias incomuns
# m: O médico estava na cozinha
# s: O piloto estava na ala de segurança
# b: O biólogo é o assassino
# c: O cozinheiro estava na sala de recreação
# r: O médico tinha rixa com o chefe de segurança
# a: Substâncias são de origem biológica

print("\n--- CENÁRIO 1: Substâncias Incomuns ---")
print("Proposições:")
print("p: Chefe encontrado com substâncias incomuns")
print("m: Médico estava na cozinha")
print("s: Piloto estava na ala de segurança")
print("b: Biólogo é o assassino")
print("c: Cozinheiro estava na sala de recreação")
print("r: Médico tinha rixa com chefe")
print("a: Substâncias são de origem biológica")
print("\nFórmula: (p and m and s and c and a) => b")

answer1 = ttg.Truths(
    ["p", "m", "s", "b", "c", "r", "a"],
    ["(p and m and s and c and a) and b"],
    ints=False,
)
print(answer1)
print(f"\nValores que satisfazem: {answer1.valuation()}")

# Cenário 2: Ataque com marcas de luta
# Proposições:
# a: Chefe foi atacado com marcas de luta
# b: Biólogo sabotou a segurança
# p: Piloto estava na cabine
# f: Engenheiro tinha ferimentos
# m: Médico estava ausente da ala médica
# c: Chefe foi atacado na ala de segurança
# s: Biólogo tinha conhecimento dos sistemas

print("\n\n--- CENÁRIO 2: Ataque com Marcas de Luta ---")
print("Proposições:")
print("a: Chefe foi atacado com marcas de luta")
print("b: Biólogo sabotou a segurança")
print("p: Piloto estava na cabine")
print("f: Engenheiro tinha ferimentos")
print("m: Médico estava ausente")
print("c: Ataque foi na ala de segurança")
print("s: Biólogo conhecia sistemas de contenção")
print("\nFórmula: (a and p and f and c and s) => b")

answer2 = ttg.Truths(
    ["a", "b", "p", "f", "m", "c", "s"],
    ["(a and p and f and c and s) and b"],
    ints=False,
)
print(answer2)
print(f"\nValores que satisfazem: {answer2.valuation()}")

# Cenário 3: Envenenamento com substâncias biológicas
# Proposições:
# e: Chefe morreu envenenado
# b: Biólogo tinha acesso a toxinas
# p: Piloto estava na cabine
# m: Médico estava na ala médica
# c: Cozinheiro estava na cozinha
# t: Biólogo tinha conhecimento sobre toxinas
# a: Veneno era da ala biológica

print("\n\n--- CENÁRIO 3: Envenenamento ---")
print("Proposições:")
print("e: Chefe morreu envenenado")
print("b: Biólogo é o assassino")
print("p: Piloto estava na cabine")
print("m: Médico estava na ala médica")
print("c: Cozinheiro estava na cozinha")
print("t: Biólogo tinha conhecimento sobre toxinas")
print("a: Veneno era da ala biológica")
print("\nFórmula: (e and p and m and c and t and a) => b")

answer3 = ttg.Truths(
    ["e", "b", "p", "m", "c", "t", "a"],
    ["(e and p and m and c and t and a) and b"],
    ints=False,
)
print(answer3)
print(f"\nValores que satisfazem: {answer3.valuation()}")

print("\n" + "="*80)
print("ANÁLISE COMPLETA")
print("="*80)
print("\nEm todos os cenários, quando todas as premissas são verdadeiras,")
print("o Biólogo (Logan) é identificado como o sabotador/assassino.")
print("\nA lógica proposicional demonstra que:")
print("- Cenário 1: Substâncias biológicas + presença do médico na cozinha => Biólogo")
print("- Cenário 2: Sabotagem dos sistemas + conhecimento técnico => Biólogo")
print("- Cenário 3: Envenenamento + acesso a toxinas biológicas => Biólogo")
