# We don't need code for this

namevalbase = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
        }

namevalteens = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
        }

namevaltens = {
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        }



onethrunine = sum ( len(x) for x in namevalbase.values() )

tenthrunineteen = sum ( len(x) for x in namevalteens.values() )

# For each X0 - X9...
# X appears 10 times
# onethrunine appears ocne
twentythru99 = sum ( 10 * len(x) + onethrunine for x in namevaltens.values() )

onethru99 = onethrunine + tenthrunineteen + twentythru99

# For each X00-X99...
# X appears 100 times
# 'hundred' appears 100 times
# 'and' appears 99 times
# onethru99 appears once
hundredthru999 = sum ( len(x) * 100 + len('hundred') * 100 + len('and') * 99 + onethru99 for x in namevalbase.values() )

total = onethru99 + hundredthru999 + len('onethousand')

print (str(total))
