import random
import textwrap
import time
from rich.console import Console

# ============================================================================
# ALIEN: O SÉTIMO PASSAGEIRO - JOGO DETETIVE
# ============================================================================
# Personagens:
# - Piloto: Vector
# - Biólogo: Logan (SEMPRE CULPADO)
# - Engenheiro: Rodrigo
# - Médico: Adalberto
# - Cozinheiro: Jonathan
# - Chefe de Segurança: Peçanha (VÍTIMA)
# ============================================================================

def centralizar_texto(console, texto, largura=155, estilo="white", justify="center"):
    """Centraliza o texto na tela."""
    console.print(textwrap.fill(texto, width=largura), justify=justify, style=estilo)

def mostrar_mapa(console):
    """Exibe o mapa da nave espacial."""
    mapa = (
        "MAPA DA NAVE\n"
        "+" + "-" * 75 + "+\n"
        "|   Cabine          |  Ala de Segurança   | Ala Biológica       |\n"
        "|-------------------|---------------------|---------------------|\n"
        "|   Motores         |                     | Ala Médica          |\n"
        "|-------------------|  Área Central       |---------------------|\n"
        "|   Cozinha         |                     | Ala de Recreação    |\n"
        "+" + "-" * 75 + "+\n"
    )
    console.print(mapa, style="bold", justify="center")

def mostrar_titulo(console):
    """Exibe o título do jogo."""
    console.print("\n\n+-----------------------------------------------------+", style="bold green", justify="center")
    console.print("|  ALIEN: O SÉTIMO PASSAGEIRO - MISTÉRIO NA NAVE     |", style="bold green", justify="center")
    console.print("+-----------------------------------------------------+\n", style="bold green", justify="center")

def aleatorizar_cenario():
    """Retorna um número aleatório entre 1 e 3."""
    return random.randint(1, 3)

def definir_tripulantes_fixos():
    """
    Retorna tripulantes com os nomes e papeis fixos.
    """
    vitima = "Chefe de Segurança (Peçanha)"
    piloto = "Piloto (Vector)"
    biologo = "Biólogo (Logan)"
    engenheiro = "Engenheiro (Rodrigo)"
    medico = "Médico (Adalberto)"
    cozinheiro = "Cozinheiro (Jonathan)"
    assassino = "biologo"

    return vitima, piloto, biologo, engenheiro, medico, cozinheiro, assassino

def obter_fase_alien(acao):
    """Retorna a fase do alien baseado na ação atual (1-10)."""
    if acao <= 1:
        return 1
    elif acao <= 3:
        return 2
    elif acao <= 6:
        return 3
    elif acao <= 9:
        return 4
    else:
        return 5

def descricao_fase_alien(fase):
    """Retorna descrição narrativa da fase do alien."""
    descricoes = {
        1: {
            "emoji": "🌱",
            "titulo": "FASE 1: ALIEN RECÉM-NASCIDO",
            "descricao": "O alien ainda está se adaptando ao novo ambiente.",
            "risco": "🟢 RISCO BAIXO",
            "chance": 10,
            "mensagem": "O alien está escondido. Você ainda tem tempo!"
        },
        2: {
            "emoji": "🐛",
            "titulo": "FASE 2: ALIEN EM CRESCIMENTO",
            "descricao": "O alien começa a explorar a nave.",
            "risco": "🟡 RISCO MÉDIO",
            "chance": 30,
            "mensagem": "Você ouve sons estranhos pelos corredores..."
        },
        3: {
            "emoji": "👁️",
            "titulo": "FASE 3: ALIEN ADOLESCENTE",
            "descricao": "O alien se torna predador.",
            "risco": "🟠 RISCO ALTO",
            "chance": 50,
            "mensagem": "🚨 ALARME! Sistemas de comunicação derrubados!"
        },
        4: {
            "emoji": "🦑",
            "titulo": "FASE 4: ALIEN ADULTO",
            "descricao": "O alien domina a nave.",
            "risco": "🔴 RISCO CRÍTICO",
            "chance": 80,
            "mensagem": "A nave inteira tremendo. O alien está em toda parte!"
        },
        5: {
            "emoji": "💀",
            "titulo": "FASE 5: ALIEN MADURO",
            "descricao": "O alien praticamente venceu.",
            "risco": "💀 RISCO TERMINAL",
            "chance": 95,
            "mensagem": "O alien já dominou metade da nave. VOCÊ ESTÁ FORA DO TEMPO!"
        }
    }
    return descricoes.get(fase, descricoes[1])

def mostrar_texto_cenario(console, cenario, vitima):
    """Exibe a descrição do cenário."""
    if cenario == 1:
        texto = (
            f"Em uma manhã tensa na nave Prodigy, a tripulação acordou com uma notícia chocante: "
            f"o {vitima} foi encontrado morto na ala de segurança. O corpo apresentava "
            f"ferimentos estranhos e substâncias incomuns. O alien conseguiu um hospedeiro e agora se esconde "
            f"na nave. Quem sabotou a ala de segurança e permitiu que isso acontecesse?\n"
        )
    elif cenario == 2:
        texto = (
            f"Durante a noite na nave Prodigy, gritos ecoaram pelos corredores. O {vitima} "
            f"foi encontrado na ala de segurança com marcas de ataque brutal. A sabotagem foi clara: alguém "
            f"desativou os sistemas de contenção. O alien está à solta. Quem é o responsável?\n"
        )
    else:
        texto = (
            f"No silêncio da madrugada espacial, o {vitima} foi descoberto próximo aos "
            f"tanques de espécimes biológicos, com sinais de envenenamento. O alien usou o corpo como hospedeiro "
            f"e desapareceu na nave. Quem tinha acesso às substâncias letais e sabotou a segurança?\n"
        )
    centralizar_texto(console, texto)

def definir_dicas(cenario, vitima, piloto, biologo, engenheiro, medico, cozinheiro):
    """
    as 10 dicas/proposições.
    """
    if cenario == 1:
        dica_principal = f"O {vitima} foi encontrado com substâncias incomuns no corpo."
        dicas = [
            f"P1: {vitima} encontrado com substâncias incomuns.",
            f"P2: Os hematomas não causaram a morte e o {cozinheiro} estava na sala de recreação.",
            f"P3: Se o {medico} estava na cozinha, então o {piloto} estava na ala de segurança.",
            f"P4: O {medico} tinha uma rixa com o {vitima}.",
            f"P5: O {{piloto}} foi o último a ver o {{vitima}} vivo.",
            f"P6: Se o {{piloto}} não estava na ala de segurança, então o {{biologo}} matou o {{vitima}}.",
            f"P7: O {{cozinheiro}} estava na sala de recreação durante o incidente.",
            f"P8: Se as substâncias incomuns são de origem biológica, apenas {{biologo}} ou {{medico}} teriam acesso.",
            f"P9: O {{medico}} estava na cozinha durante o período do assassinato.",
            f"P10: Se o {{medico}} estava na cozinha, então ele não poderia estar na ala de segurança."
        ]
    elif cenario == 2:
        dica_principal = f"O {vitima} morreu após um ataque com marcas de luta."
        dicas = [
            f"P1: {{vitima}} apresenta marcas de ataque brutal.",
            f"P2: Os hematomas não causaram a morte e {{cozinheiro}} estava na recreação.",
            f"P3: Se {{medico}} estava na cozinha, então {{piloto}} estava na ala de segurança.",
            f"P4: {{medico}} tinha uma rixa com {{vitima}}.",
            f"P5: {{piloto}} foi o último a ver {{vitima}} vivo.",
            f"P6: Se {{piloto}} não estava na segurança, então {{biologo}} sabotou.",
            f"P7: {{cozinheiro}} estava na sala de recreação durante o incidente.",
            f"P8: Acesso aos sistemas: apenas {{biologo}} tinha conhecimento total.",
            f"P9: {{medico}} estava na cozinha durante o período do assassinato.",
            f"P10: Se {{medico}} estava na cozinha, então não poderia estar na segurança."
        ]
    else:
        dica_principal = f"O {vitima} morreu por envenenamento com substâncias biológicas."
        dicas = [
            f"P1: {{vitima}} foi encontrado com envenenamento.",
            f"P2: Hematomas não causaram morte e {{cozinheiro}} estava na recreação.",
            f"P3: Se {{medico}} estava na cozinha, então {{piloto}} estava na ala de segurança.",
            f"P4: {{medico}} tinha rixa com {{vitima}}.",
            f"P5: {{piloto}} último a ver {{vitima}} vivo.",
            f"P6: Se {{piloto}} não estava na segurança, então o {{biologo}} matou.",
            f"P7: {{cozinheiro}} estava na recreação durante incidente.",
            f"P8: Toxinas: apenas {{biologo}} e {{medico}} têm acesso.",
            f"P9: {{medico}} estava na cozinha durante assassinato.",
            f"P10: {{medico}} estava cozinha → não pode estar em segurança simultaneamente."
        ]

    dicas_expandidas = []
    for dica in dicas:
        dica_expandida = dica.format(
            vitima=vitima,
            piloto=piloto,
            biologo=biologo,
            engenheiro=engenheiro,
            medico=medico,
            cozinheiro=cozinheiro
        )
        dicas_expandidas.append(dica_expandida)

    return dica_principal, dicas_expandidas

def main():
    """Função principal do jogo com sistema de fases."""

    while True:
        console = Console()

        vitima, piloto, biologo, engenheiro, medico, cozinheiro, assassino = definir_tripulantes_fixos()
        cenario = aleatorizar_cenario()

        opcoes_acusacao = {
            "piloto": piloto,
            "biologo": biologo,
            "engenheiro": engenheiro,
            "medico": medico,
            "cozinheiro": cozinheiro
        }

        pistas_encontradas = []
        alien_found = False
        jogo_vencido = False

        dica_principal, dicas = definir_dicas(cenario, vitima, piloto, biologo, engenheiro, medico, cozinheiro)

        mostrar_titulo(console)
        time.sleep(0.5)
        mostrar_mapa(console)
        time.sleep(0.5)
        mostrar_texto_cenario(console, cenario, vitima)
        time.sleep(0.5)

        acao_count = 1
        chance_de_sucesso = 0.99
        pistas_encontradas.append(dica_principal)
        passar_tempo_usado = 0

        # Loop principal
        while not alien_found:
            fase_atual = obter_fase_alien(acao_count)
            info_fase = descricao_fase_alien(fase_atual)

            # Exibe informações da fase
            console.print(f"\n{info_fase['emoji']} {info_fase['titulo']}", style="bold red")
            console.print(f"   {info_fase['risco']}", style="bold yellow")
            console.print(f"   {info_fase['mensagem']}", style="bold cyan")

            console.print("\n--- PISTAS COLETADAS ---", style="bold yellow")

            for pista in pistas_encontradas:
                time.sleep(0.3)
                print(f"✓ {pista}")

            if fase_atual == 5:
                console.print("\n💀 FASE TERMINAL! VOCÊ DEVE FAZER UMA ACUSAÇÃO AGORA!", style="bold red")
                acao = input("\n1. Confrontar o sabotador\n\nEscolha: ").strip()
            else:
                console.print("\n--- AÇÕES DISPONÍVEIS ---", style="bold cyan")
                time.sleep(0.3)
                acao = input("1. Investigar\n2. Confrontar o sabotador\n3. Passar tempo\n\nEscolha: ").strip()

            # Ação 1: Investigar
            if acao == '1' and fase_atual != 5:
                time.sleep(0.5)
                console.print("\n🔍 Investigando a nave...", style="bold cyan")
                time.sleep(1)

                if random.random() < chance_de_sucesso:
                    dicas_disponiveis = [dica for dica in dicas if dica not in pistas_encontradas]
                    if dicas_disponiveis:
                        nova_dica = random.choice(dicas_disponiveis)
                        pistas_encontradas.append(nova_dica)
                        console.print(f"\n✅ Pista encontrada: {nova_dica}", style="bold green")
                    else:
                        console.print("\n⚠️ Não há mais pistas para serem encontradas.", style="bold yellow")
                else:
                    alien_found = True
                    console.print("\n❌ O ALIEN TE ENCONTROU!", style="bold red")
                    console.print("   Você foi incapacitado enquanto investigava!", style="bold red")

                chance_de_sucesso -= 0.15
                acao_count += 1

            # Ação 2: Confrontar
            elif acao == '2' or (acao == '1' and fase_atual == 5):
                time.sleep(0.5)
                console.print("\n--- ACUSAÇÃO FINAL ---", style="bold yellow")
                resposta = input(
                    "\nQuem você acha que é o sabotador?\n"
                    "(piloto, biologo, engenheiro, medico, cozinheiro): "
                ).strip().lower()

                if resposta in opcoes_acusacao:
                    time.sleep(0.5)
                    console.print(f"\n🎯 Você confrontou o {opcoes_acusacao[resposta]}!", style="bold")

                    if resposta == assassino:
                        # VITÓRIA
                        console.print("\n" + "="*70, style="bold green")
                        console.print("✅ VOCÊ ENCONTROU O SABOTADOR! PARABÉNS!", style="bold green")
                        console.print("="*70, style="bold green")
                        console.print(f"\nO {biologo} sabotou a ala de segurança!", style="bold green")
                        console.print("Permitiu que o alien escapasse e usasse o corpo do chefe como hospedeiro!", style="bold green")

                        jogo_vencido = True
                        alien_found = True

                        # Pontuação baseada na fase
                        if fase_atual == 1:
                            pontuacao = 1000
                            mensagem = "🌱 VITÓRIA PERFEITA - Alien ainda era fraco!"
                        elif fase_atual == 2:
                            pontuacao = 500
                            mensagem = "🐛 VITÓRIA EXCELENTE - Investigação rápida!"
                        elif fase_atual == 3:
                            pontuacao = 250
                            mensagem = "👁️ VITÓRIA BOA - Análise meticulosa!"
                        else:
                            pontuacao = 100
                            mensagem = "🦑 VITÓRIA NO LIMITE - Conseguiu na hora H!"

                        console.print(f"\n{mensagem}", style="bold green")
                        console.print(f"Pontuação: {pontuacao:.2f}", style="bold yellow")
                    else:
                        # DERROTA - Culpado errado
                        console.print("\n" + "="*70, style="bold red")
                        console.print("❌ VOCÊ ESTAVA ERRADO!", style="bold red")
                        console.print("="*70, style="bold red")
                        console.print(f"\nO {opcoes_acusacao[resposta]} protestou sua inocência!", style="bold red")
                        console.print("\nEnquanto você o interrogava, o alien atacou indiscriminadamente!", style="bold red")
                        console.print(f"\nO VERDADEIRO SABOTADOR era o {biologo}!", style="bold red")
                        console.print("\n😢 A tripulação foi dizimada. Fim de jogo!", style="bold red")
                        break
                else:
                    console.print("\n⚠️ Essa não é uma opção válida.", style="bold red")

            # Ação 3: Passar tempo
            elif acao == '3' and fase_atual != 5:
                if passar_tempo_usado >= 3:
                    console.print("\n⚠️ Você já usou o máximo de 3 vezes a ação Passar tempo!", style="bold red")
                    continue
                passar_tempo_usado += 1
                acao_count += 1
                chance_de_sucesso -= 0.05
                console.print("\n⏰ O tempo passa...", style="bold cyan")

                dicas_disponiveis = [dica for dica in dicas if dica not in pistas_encontradas]
                if dicas_disponiveis:
                    nova_dica = random.choice(dicas_disponiveis)
                    pistas_encontradas.append(nova_dica)
                    console.print(f"\n📬 Você recebeu uma transmissão: {nova_dica}", style="bold green")
                else:
                    console.print("\n⚠️ Não há mais informações disponíveis.", style="bold yellow")
            else:
                console.print("\n⚠️ Ação inválida. Tente novamente.", style="bold red")

        if not jogo_vencido:
            console.print(f"\nO sabotador era o {biologo}!", style="bold red")

        console.print("\n" + "="*70)
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            console.print("\nObrigado por jogar! Boa sorte na próxima investigação!", style="bold cyan")
            break

if __name__ == "__main__":
    main()
