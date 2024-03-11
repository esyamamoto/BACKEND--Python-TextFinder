import os
import sys


def txt_importer(path_file):
    # existe ou nao?
    if not os.path.exists(path_file):
        print(
            f"Arquivo {path_file} não encontrado", file=sys.stderr
        )  # stderr:objeto - fluxo de saída - padrão para mensagens de erro
        return []

    # Caso a extensão nao seja .txt
    if not path_file.endswith("txt"):
        print("Formato inválido", file=sys.stderr)
        return []

    # abre o arquivo e le
    with open(path_file, "r") as file:
        lines = file.read().splitlines()  # le as linhas e divide em uma lista
        return lines
