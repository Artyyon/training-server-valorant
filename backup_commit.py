import subprocess
import datetime
import os
import asyncio


# Obtém o diretório atual (onde o script está localizado)
repo_dir = os.path.dirname(os.path.abspath(__file__))


async def get_branch_name():
    """Obtém o nome da branch atual do repositório."""
    try:
        branch_name = await asyncio.create_subprocess_exec(
            'git', 'rev-parse', '--abbrev-ref', 'HEAD',
            cwd=repo_dir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, _ = await branch_name.communicate()
        return stdout.decode().strip()
    except Exception:
        return "unknown_branch"


async def check_git_status():
    """Verifica se há alterações pendentes no repositório Git."""
    process = await asyncio.create_subprocess_exec(
        'git', 'status', '--porcelain',
        cwd=repo_dir,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, _ = await process.communicate()

    # Se stdout estiver vazio, não há mudanças para commit
    return bool(stdout.strip())


async def run_git_command(command):
    """Executa comandos Git de forma assíncrona."""
    process = await asyncio.create_subprocess_exec(
        *command,
        cwd=repo_dir,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()

    if process.returncode != 0:
        print(f"Erro ao executar {' '.join(command)}:\n{stderr.decode()}")
        return False
    else:
        print(stdout.decode())
        return True


async def main():
    """Função principal assíncrona."""
    branch_name = await get_branch_name()

    # Verifica se há alterações antes de prosseguir
    has_changes = await check_git_status()
    if not has_changes:
        print(f"Nenhuma alteração detectada. O repositório já está atualizado na branch '{branch_name}'.")
        return  # Encerra o script sem tentar commit/push

    now = datetime.datetime.now()
    commit_message = f"[{branch_name}] Automatic data saving: {now.strftime('%Y-%m-%d %H:%M:%S')}"

    # Lista de comandos Git
    git_commands = [
        ['git', 'add', '.'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push']
    ]

    # Executa cada comando sequencialmente
    for command in git_commands:
        success = await run_git_command(command)
        if not success:
            print("Erro ao executar o comando. Interrompendo o processo.")
            return  # Para a execução em caso de erro

    # Aguarda tempo suficiente para garantir que tudo foi enviado antes de encerrar
    print("Aguardando o processo ser finalizado...")
    await asyncio.sleep(5)  # Aguarde 5 segundos para garantir sincronização com o Git

    print(f"Backup commit e push realizados com sucesso na branch '{branch_name}'.")


# Executa apenas se o script for chamado diretamente
if __name__ == "__main__":
    asyncio.run(main())
