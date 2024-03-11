def exists_word(word, instance):
    list = []  # Lista para armazenar info palavra em cada arquivo

    for item in instance.data:
        file_name = item["nome_do_arquivo"]
        file_line = item["linhas_do_arquivo"]

    list_file = []  # Lista para armazenar info palavra em cada arquivo

    for line_iterable, line in enumerate(file_line, start=1):
        if word.lower() in line.lower():  # case insensitive
            list_file.append(
                {"linha": line_iterable}
            )  # Adiciona a linha onde a palavra foi encontrada

    if list_file:
        list.append(
            {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": list_file,
            }
        )
    return list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
