from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    # Verifica se o arquivo já foi processado anteriormente
    for item in instance.data:
        if item["nome_do_arquivo"] == path_file:
            return False  # se ja tiver na fila , volta false
    # se nao tiver na fila , adiciona o arquivo na fila
    file_line = txt_importer(path_file)

    # cria estrutura
    file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_line),
        "linhas_do_arquivo": file_line,
    }

    # insere infos do arq na fila
    instance.enqueue(file)

    # Será validado que ao executar a função process
    # com sucesso deverá mostrar dados via stdout
    sys.stdout.write(str(file))
    return True


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
