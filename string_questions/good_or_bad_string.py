

def isGoodOrBadString(string):
    voewls = 'aeiou'
    consonantes = 'bcdfghjklmnpqrstvxwyz'
    count_vogals = 0
    count_consonts = 0
    for character in string:
        if character in voewls:
            count_vogals += 1
            if count_vogals >= 5:
                return False
        else:
            count_vogals = 0

        if character in consonantes:
            count_consonts += 1
            if count_consonts >= 3:
                return False
        else:
            count_consonts = 0

    return True


assert False == isGoodOrBadString('goeiuop')
assert True == isGoodOrBadString('teacher')
assert False == isGoodOrBadString('phnomenal')