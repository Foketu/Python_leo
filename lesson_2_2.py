# valid string for all brackets v2.2

class Validator:
    def __init__(self, open_br, close_br):
        self.open_br = open_br
        self.close_br = close_br

    def is_valid(self, line):
        """ search bracket '(', ')'"""
        count = 0
        for symbol in line:
            if symbol == self.open_br:
                count += 1
            elif symbol == self.close_br:
                count -= 1
                if count < 0:
                    return False
        return count == 0

open_br = input('Insert open bracket: ')
close_br = input('Insert close bracket: ')
valid = Validator(open_br, close_br)

assert(valid.is_valid('(){}'))
assert(valid.is_valid('({})'))
assert(valid.is_valid('({()})'))

assert(not valid.is_valid('(}'))
assert(not valid.is_valid('({)}'))
assert(not valid.is_valid('((()})'))

print ('Correct!')