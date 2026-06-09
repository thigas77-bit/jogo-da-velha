# 🎮 Jogo da Velha (Tic-Tac-Toe)

Um jogo da velha feito em Python, jogável direto no terminal. O projeto oferece dois modos de jogo: partida entre dois jogadores ou duelo contra uma inteligência artificial desafiadora.

---

## 🕹️ Modos de Jogo

- **Jogador vs Jogador** — dois jogadores se alternam no mesmo terminal, cada um escolhendo sua posição no tabuleiro.
- **Jogador vs I.A 🤖** — enfrente uma inteligência artificial que analisa o estado do jogo a cada rodada e toma decisões estratégicas para vencer ou bloquear as suas jogadas.

---

## 🧠 Como a I.A funciona

A I.A não joga de forma aleatória. Ela segue uma hierarquia de prioridades a cada turno:

1. **Vencer imediatamente** — se houver uma jogada que complete três em linha, ela executa.
2. **Bloquear o adversário** — se o jogador humano estiver prestes a vencer, a I.A bloqueia.
3. **Ocupar o centro** — posição estrategicamente mais vantajosa do tabuleiro.
4. **Ocupar um canto vazio** — segunda posição mais forte estrategicamente.
5. **Qualquer posição disponível** — como último recurso.

---

## 🔄 Lógica e Estrutura do Código

O jogo é construído em cima de um **loop principal** que mantém a partida em andamento até que haja um vencedor ou empate. A cada iteração do loop:

- O tabuleiro é exibido atualizado na tela.
- O jogador da vez realiza sua jogada (humano digita a posição; I.A calcula a melhor jogada).
- O código verifica todas as **8 combinações vencedoras** possíveis (3 linhas, 3 colunas e 2 diagonais).
- Se nenhuma combinação for formada e não houver espaços vazios, o jogo termina em empate.
- O turno então passa para o outro jogador, e o loop recomeça.

A validação de jogadas garante que o jogador não possa escolher uma posição já ocupada ou fora do intervalo de 1 a 9, exibindo mensagens de erro apropriadas em cada caso.

---

## 🚀 Como executar

Você precisa ter o **Python 3** instalado na sua máquina.

```bash
python jogo_da_velha.py
```

Siga as instruções exibidas no terminal para escolher o modo de jogo e começar a partida.

---

## 📐 Numeração do Tabuleiro

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

---

## 🛠️ Tecnologias

- **Python 3**
- Biblioteca padrão `random` (usada pela I.A para desempate entre posições equivalentes)
