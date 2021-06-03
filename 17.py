# Number letter counts

word_table = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'onehundred',
    1000: 'onethousand',
}

def decode_number(x: int):
    # thousand = int(x / 1000)
    hundred = int(x / 100 % 10)
    ten = int(x / 10 % 10)
    one = x % 10
    ten_one = x % 100
    # print(hundred, ten, one)
    word = ''
    if x == 1000:
        print(word_table[x])
        return len(word_table[x])
    if hundred > 0:
        word += word_table[hundred] + ' hundred'
        if ten != 0 or one != 0:
            word += ' and '
    if ten_one in word_table.keys():
        word += word_table[ten_one]
    else:
        if ten > 0:
            word += word_table[ten * 10] + '-'
        if one > 0:
            word += word_table[one]
    print(word)
    word = word.replace(' ', '')
    word = word.replace('-', '')
    return len(word)


def calc_all():
    return sum([decode_number(i) for i in range(1, 1001)])

"""
# tests
print(decode_number(123))
print(decode_number(243))
print(decode_number(52))
print(decode_number(4))
print(decode_number(1000))
"""

print(calc_all())