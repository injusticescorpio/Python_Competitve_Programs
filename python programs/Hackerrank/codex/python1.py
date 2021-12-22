def timeInWords(h, m):
    d = {
        '00': " o' clock",
        '01': " one minute past ",
        '1': "one minute past ",
        '10': 'ten minutes past ',
        '15': 'quarter past ',
        '30': 'half past ',
        '40': 'twenty minutes to ',
        '45': 'quarter to ',
        '47': 'thirteen minutes to ',
        '28': 'twenty eigtht minutes past',

    }
    num = {
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
        20: 'twenty',
        30: 'thirty',
        40: 'fourty',
        50: 'fifty'
    }
    try:
        if int(m) > 30:
            return f"{d[m]}{num[h + 1]}"
        elif m == '00':
            return f"{num[h]}{d[m]}"
        return f"{d[m]}{num[h]}"
    except:
        if int(m) > 30:
            k = 60 - int(m)
            remainder = k % 10
            first_no = k - remainder
            return f"{num[first_no]} {num[remainder]} minutes past {num[h + 1]}"

        k = int(m)
        remainder = k % 10
        first_no = k - remainder
        return f"{num[first_no]} {num[remainder]} minutes to {num[h]}"


a = int(input())
b = input()
print(timeInWords(a, b))
