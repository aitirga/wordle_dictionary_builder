from spylls.hunspell import Dictionary

if __name__ == '__main__':
    target_length = 5
    list_of_words = []
    sample_word = 'anar'


    h = Dictionary.from_files('/Users/aitoriraolagalarza/Desktop/pycharm_projects/wordle_dictionary_builder/data/hunspell-cat/catalan')
    # print(h.dic.words[10000].stem)
    # print(h.lookup('anava'))
    list = h.lookuper.produce_affix_forms('menjar')

    for element in list:
        print(element)

    # dictionary_words = h.dic.words
    # for word in dictionary_words:
    #     print(word.flags)
    #     # if len(word.stem) == target_length:
    #     #     list_of_words.append(word.stem)
    #
    # print(list_of_words)


