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
    # ve se tem elementos na fila
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return

    # Em caso de sucesso de remoção
    path_file = instance.data[0]["nome_do_arquivo"]
    instance.dequeue()
    print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return

    if position < 0 or position >= len(instance):
        print("Posição inválida", file=sys.stderr)
        return

    file = instance.data[position]
    print(file)
