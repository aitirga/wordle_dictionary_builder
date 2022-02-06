from spylls.hunspell import Dictionary
import pandas as pd
import unidecode

if __name__ == '__main__':
    target_length = 5
    list_of_words = []

    dictionary = Dictionary.from_files('/Users/aitoriraolagalarza/Desktop/pycharm_projects/wordle_dictionary_builder/data/hunspell-cat/catalan')

    for word in dictionary.dic.words:
        if str(word.captype) != 'Type.NO': # Don't include words with no capital letters
            continue
        if len(word.stem) == target_length:
            list_of_words.append(unidecode.unidecode(word.stem))
    df = pd.DataFrame(list_of_words)
    df.to_csv('catalan_dictionary.csv', index=False, header=False)


