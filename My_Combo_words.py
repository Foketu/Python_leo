# for fun. take two different words. Half from first word and half from second word

class Words:
    def __init__(self, w_1, w_2):
        self.w_1 = w_1
        self.w_2 = w_2

    def fist_w(self):
        """Half from first word """
        temp_w1 = self.w_1[:self.get_w(self.w_1)]
        return temp_w1

    def second_w(self):
        """Half from second word"""
        temp_w2 = self.w_2[self.get_w((self.w_2)):]
        return temp_w2

    def get_w(self, w):
        """Determine word length"""
        count_letter_w = len(w)
        half_letter_w = count_letter_w // 2
        return half_letter_w

    def summ_w(self):
        return (self.fist_w() + self.second_w())

w_1 = input('Input first word: ')
w_2 = input('Input second word: ')
words_1 = Words(w_1, w_2)
words_2 = Words(w_2, w_1)
print('var. №1 is: ' + words_1.summ_w())
print('var. №2 is: ' + words_2.summ_w())

#_________________________Simple______________________
# w_1 = input('input word 1 ')
# w_2 = input('input word 2 ')
# count_letter_w_1 = len(w_1)
# count_letter_w_2 = len(w_2)
# half_letter_w_1 = count_letter_w_1 // 2
# half_letter_w_2 = count_letter_w_2 // 2
# temp_w1 = w_1[:half_letter_w_1]
# temp_w2 = w_2[half_letter_w_2:]
# print(temp_w1 + temp_w2)
