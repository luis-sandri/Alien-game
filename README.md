# 👽 Alien: O Sétimo Passageiro - Mistério na Nave Prodigy

> Um projeto acadêmico interdisciplinar unindo Lógica Proposicional, Dedução Matemática e Programação em Python.

![Status do Projeto](https://img.shields.io/badge/Status-Finalizado-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Focus](https://img.shields.io/badge/Foco-Lógica%20%26%20Algoritmos-orange)

## 📋 Sobre o Projeto

Este projeto foi desenvolvido em 2 dias como parte de uma atividade acadêmica para demonstrar a aplicação prática da **Lógica Proposicional** na resolução de problemas complexos.

O cenário é um jogo de mistério no estilo "Detetive", ambientado em uma nave espacial onde um tripulante foi assassinado e um alienígena está à solta. O objetivo é utilizar pistas (premissas lógicas) para deduzir quem é o sabotador antes que o alien domine a nave.

## 🚀 Funcionalidades

O projeto é dividido em duas partes principais:

1.  **O Jogo Interativo (`alien_jogo.py`):**
    * Um *text-adventure* rodando no terminal.
    * Interface visual rica utilizando a biblioteca `rich`.
    * Sistema de fases (o alien evolui com o tempo).
    * Mecânica de coleta de pistas aleatórias e dedução.

2.  **Validação Lógica (`alien_tabelas_verdade.py`):**
    * Uso da biblioteca `truth-table-generator` (`ttg`).
    * Demonstração matemática da culpabilidade do suspeito através de Tabelas Verdade.
    * Formalização das premissas narrativas em expressões lógicas.

## 📖 O Enredo (Contexto)

Em uma missão da empresa Prodigy, seis tripulantes viajam rumo a um planeta habitável. A nave transporta espécimes extraterrestres na ala de segurança. Na manhã seguinte ao jantar, o **Chefe de Segurança Peçanha** é encontrado morto com ferimentos estranhos.

Alguém sabotou a nave, permitindo que um alien escapasse e usasse o corpo do chefe como hospedeiro.

**Os Suspeitos:**
* **Vector (Piloto):** Último a ver o chefe vivo.
* **Logan (Biólogo):** Especialista em espécimes, acesso a toxinas.
* **Rodrigo (Engenheiro):** Conhecimento técnico dos sistemas.
* **Adalberto (Médico):** Tinha uma rixa com o chefe.
* **Jonathan (Cozinheiro):** Estava na área de recreação.

## 🧠 Fundamentação Lógica

A solução do mistério não é aleatória; ela segue uma dedução lógica rigorosa baseada em premissas.

**Exemplo de Dedução do Projeto:**
* **Premissa 1:** O médico estava na cozinha ($D$).
* **Premissa 2:** Se o médico estava na cozinha, então o piloto estava na ala de segurança ($D \rightarrow E$).
* **Premissa 3:** Se o piloto não estava na ala de segurança, o biólogo é o assassino ($\neg E \rightarrow H$).
* **Fato:** As substâncias encontradas são biológicas e apenas o Biólogo ou Médico teriam acesso ($I \rightarrow (H \lor D)$).

Através de *Modus Ponens*, *Silogismo Disjuntivo* e análise de Tabela Verdade, o algoritmo prova que **o Biólogo (Logan)** é o único cenário logicamente possível para o sabotador.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **[Rich](https://github.com/Textualize/rich):** Para formatação visual no terminal (cores, tabelas, painéis).
* **[truth-table-generator (ttg)](https://github.com/chicolucio/truth-table-generator):** Para geração e validação das tabelas verdade.

## ⚠️ Disclaimer / Nota Legal
**Este projeto é uma obra de ficção desenvolvida para fins exclusivamente educacionais e acadêmicos.**

O enredo e a ambientação são inspirados na franquia de filmes Alien, mas os personagens (Peçanha, Vector, Logan, etc.) e a trama específica deste jogo são criações originais dos autores para ilustrar problemas de Lógica Computacional. Este projeto não possui fins lucrativos e não tem afiliação com os detentores dos direitos autorais da franquia.


## 📦 Como Rodar o Projeto

### Pré-requisitos
Certifique-se de ter o Python instalado. Em seguida, instale as dependências necessárias executando o comando abaixo no terminal:

```bash
pip install rich truth-table-generator
```

## 👨‍🎓 Autores
Projeto desenvolvido por:
* Luís Gustavo Pazin Sandri
* Renan Cassou Rodrigues
* João Pedro Gadens Mosson
* Victor de Oliveira Medeiros
