# Usar a imagem oficial do Python como base
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de requisitos e instalar as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos os arquivos necessários para o container
COPY . .

# Expor a porta 5000 (porta padrão do Flask)
EXPOSE 5000

# Comando para rodar o aplicativo Flask
CMD ["python", "app.py"]
