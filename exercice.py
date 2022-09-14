#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    texte = list(string)
    if len(texte)%2 == 0:
        return True
    else:
        return False


def remove_third_char(string: str) -> str:
    texte = string[:2] + string[3:]
    return texte


def replace_char(string: str, old_char: str, new_char: str) -> str:
    texte = ""
    for i in range(len(string)):
        if string[i] == old_char:
            texte += new_char
        else:
            texte += string[i]
    return texte


def get_number_of_char(string: str, char: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == char:
            count += 1
    return count


def get_number_of_words(sentence: str, word: str) -> int:
    count = 0
    texte = sentence.split()
    for i in range(len(texte)):
        if texte[i] == word:
            count += 1
    return count


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans '{chaine}' est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
