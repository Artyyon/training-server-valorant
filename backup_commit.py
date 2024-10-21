import subprocess
import datetime
import os


# Obtém o diretório atual (onde o script está localizado)
repo_dir = os.path.dirname(os.path.abspath(__file__))


# Obtém a data e hora atual
now = datetime.datetime.now()
commit_message = f"Atualização automática: {now.strftime('%Y-%m-%d %H:%M:%S')}"


# Comando para adicionar alterações
add_command = ['git', 'add', '.']


# Comando para fazer o commit
commit_command = ['git', 'commit', '-m', commit_message]


# Comando para fazer push
push_command = ['git', 'push']


# Executa os comandos
try:
    subprocess.run(add_command, cwd=repo_dir, check=True)
    subprocess.run(commit_command, cwd=repo_dir, check=True)
    subprocess.run(push_command, cwd=repo_dir, check=True)
    print("Backup commit e push realizados com sucesso.")

except subprocess.CalledProcessError as e:
    print(f"Erro ao realizar commit ou push: {e}")
