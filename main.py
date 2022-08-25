import os

ru = "Russian.txt"
eng = "English.txt"


def append_to_file(name: str, word: str):

    with open(name, 'a', encoding="utf-8") as new_file:
        new_file.write(word)


if __name__ == "__main__":

    if os.path.isfile(eng) and os.path.isfile(ru):
        os.remove(eng)
        os.remove(ru)

    with open("PythonTest.txt", encoding="utf-8") as file:
        f = file.readlines()

        for elem in f[33:]:
            tab_index = elem.rfind('\t')

            for i in elem[:tab_index].split(';'):

                if i.startswith(' '):
                    append_to_file(eng, f"{i[1:]}\n")
                else:
                    append_to_file(eng, f"{i}\n")

            for i in elem[tab_index:].replace('\t', '').split(';'):

                if i.endswith('\n'):
                    if i.startswith(' '):
                        append_to_file(ru, f"{i[1:]}")
                    else:
                        append_to_file(ru, f"{i}")
                else:
                    if i.startswith(' '):
                        append_to_file(ru, f"{i[1:]}\n")
                    else:
                        append_to_file(ru, f"{i}\n")