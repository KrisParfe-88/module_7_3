class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = [*file_names]

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                for line in file:
                    new_line = line.lower()
                    for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        if i in new_line:
                            new_line = new_line.replace(i, '')
                    all_words.setdefault(name, []).extend(new_line.split())
        return all_words

    def find(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():
            dict_[name] = words.index(word.lower()) + 1
        return dict_

    def count(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():
            dict_[name] = words.count(word.lower())
        return dict_


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
