# 🍄 Super Mario - Interface Animada em Pygame

> Projeto prático desenvolvido durante o **1º período da graduação** para a disciplina **INF1034 - Práticas de Programação**.

---

## 📌 Sobre o Projeto

Este projeto consiste em uma interface gráfica interativa e animada desenvolvida em **Python** utilizando a biblioteca **Pygame**. A aplicação recria o visual clássico do universo de **Super Mario Bros**, implementando:

- **Menu interativo** com botões gráficos e controle de reprodução de áudio.
- **Cenário dinâmico** composto por múltiplos elementos em camadas (background com montanhas repetidas, canos, blocos de chão e nuvens).
- **Animação contínua** da nuvem com movimentação oscilatória suave calculada com base no delta time (`dt`).
- **Sistema de áudio** integrado utilizando o mixer do Pygame, com execução de trilha sonora temática e efeitos sonoros clássicos (som de *1-Up*).
- **Interação multimodal** (suporte a ações por mouse e teclas de atalho).

---

## 🎮 Funcionalidades e Controles

A aplicação opera em dois estados principais: a **Tela de Menu** e o **Cenário Animado do Mario**.

### 1. Menu Inicial (Tela de Controle)
Exibe ícones interativos e as instruções de atalho:
- **Cogumelo 1-Up (`1up.png`)**:
  - **Clique com Botão Esquerdo**: Reproduz o efeito sonoro clássico de vida extra (`1up.mp3`).
  - **Clique com Botão Direito**: Interrompe a reprodução do som.
- **Super Cogumelo (`super.png`)**:
  - **Clique com Botão Esquerdo**: Inicia a trilha sonora tema (`super.mp3`) e transiciona para o cenário animado.
  - **Clique com Botão Direito**: Interrompe a música e retorna à tela de repouso.

### 2. Controles por Teclado
Você pode controlar a trilha sonora e o estado da tela a qualquer momento através das teclas:

| Tecla | Ação | Descrição |
| :---: | :--- | :--- |
| <kbd>I</kbd> | **Iniciar** | Toca a trilha sonora e exibe o cenário animado |
| <kbd>P</kbd> | **Pausar** | Pausa a música e retorna ao menu |
| <kbd>R</kbd> | **Retomar / Resume** | Despausa a música e volta ao cenário |
| <kbd>S</kbd> | **Parar / Stop** | Encerra a música e retorna ao menu inicial |

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3](https://www.python.org/)**: Linguagem de programação principal.
- **[Pygame](https://www.pygame.org/)**: Biblioteca para desenvolvimento gráfico 2D, renderização de superfícies, taxa de quadros (60 FPS) e manipulação de áudio (`pygame.mixer`).

---

## 📁 Estrutura de Arquivos

```text
mario/
├── 1up.mp3                 # Efeito sonoro de 1-Up (vida extra)
├── 1up.png                 # Sprite do cogumelo 1-Up
├── super.mp3               # Trilha sonora clássica do Super Mario
├── super.png               # Sprite do Super Cogumelo
├── mario_background.png    # Sprite das montanhas de fundo
├── mario_cloud.png         # Sprite da nuvem animada
├── mario_ground.png        # Bloco de textura do chão
├── mario_pipe.png          # Sprite do cano verde clássico
├── mario_jogo.py           # Código-fonte principal da aplicação
└── README.md               # Documentação do projeto
