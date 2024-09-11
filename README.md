# TICS - Treino Inteligente de Contadores

Este projeto é uma aplicação web desenvolvida em Flask para o gerenciamento e acompanhamento de treinamentos no jogo Valorant. A aplicação permite que o usuário visualize e acompanhe os treinamentos através de contadores que podem ser incrementados e resetados.

## Funcionalidades

- Exibição dos treinamentos com contadores dinâmicos
- Incremento e reset dos contadores para cada exercício do treinamento
- Interface amigável com design inspirado em cores do Valorant
- Dados de treinamento salvos e carregados a partir de um arquivo JSON

### Funcionalidades Futuras

- Adicionar, atualizar ou remover treinamentos diretamente na interface
- Sistema de login para separar os treinamentos por usuários

## Estrutura do Projeto

O projeto é composto pelos seguintes componentes:

1. **Backend:**
   - **Flask** é usado para gerenciar as rotas e a lógica do servidor.
   - Os dados dos treinamentos são armazenados e gerenciados em um arquivo JSON (`trainings/trainings.json`).

2. **Frontend:**
   - Interface web desenvolvida com HTML e CSS, renderizada pelo Flask.
   - Contadores dinâmicos são gerados para cada exercício de treinamento.

3. **Docker:**
   - Dockerfile para criar um container com Python 3.9.
   - Docker Compose para facilitar a execução do projeto em um ambiente isolado.

## Requisitos

- Python 3.9
- Flask
- Docker e Docker Compose

## Instalação

### Clonando o Repositório

```bash
git clone https://github.com/seu-usuario/tics-counter.git
cd tics-counter
```

### Usando Docker

1. **Build e execução do container:**

```bash
docker-compose up --build
```

2. Acesse a aplicação no seu navegador através da URL: [http://localhost:5000](http://localhost:5000)

### Sem Docker

1. **Instalar as dependências:**

```bash
pip install -r requirements.txt
```

2. **Executar o servidor:**

```bash
python app.py
```

3. Acesse a aplicação no seu navegador através da URL: [http://localhost:5000](http://localhost:5000)

## Arquivos

- **Dockerfile**: Define o ambiente de execução com Python 3.9 e Flask.
- **docker-compose.yml**: Configura a execução do container e define os volumes para persistência dos dados.
- **app.py**: Arquivo principal da aplicação Flask que gerencia as rotas e a lógica do backend.
- **trainings/trainings.json**: Arquivo que armazena os dados dos treinamentos e contadores.
- **templates/index.html**: Interface HTML que exibe os treinamentos e botões de controle.
- **static/css/styles.css**: Estilos da interface.

## Como Usar

1. **Incrementando um contador**: Clique no botão "Incrementar" ao lado do exercício para aumentar o contador.
2. **Resetando um contador**: Use o botão "Resetar" para reiniciar o contador de um exercício específico.
3. **Resetando todos os contadores**: Use o botão "Resetar todos os contadores" para reiniciar todos os exercícios de um treinamento.

## Melhorias Futuras

- Adição de funcionalidades para criar e editar treinamentos diretamente na interface.
- Integração de um sistema de autenticação para gerenciar treinamentos específicos por usuário.

---

**Autor:** Arthur (Noctiz) Paes Leme Stiegler
**Licença:** Não possui licença
