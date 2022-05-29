class Validator:

    verifications = {'is_int': None,
                     'is_in_range': None,
                     'negative_range': None,
                     'negative_to_positive_index': None
                     }

    MESSAGES = ['!!!ERROR!!! Индекс элемента должен быть числовым значением',
                '!!!ERROR!!! Указанный индекс элемента не обнаружен',
                '',
                '']

    def __init__(self, length=None, index=None):
        self.index = index
        self.length = length
        self.verifications = {'is_int': None,
                     'is_in_range': None,
                     'negative_range': None,
                     'negative_to_positive_index': None
                     }

    def is_int(self):
        if type(self.index) == int:
            return True
        return False

    def is_in_range(self):
        if self.index in range(self.length):
            return self.index
        return False

    def is_in_negative_range(self):
        negative_set = [i * (-1) for i in range(1, self.length + 1)]
        if self.index in negative_set:
            return True
        return False

    def negative_to_positive_index(self):
        positive_index = self.length + self.index
        return positive_index


def verification(**kwargs):
    val = Validator(**kwargs)
    if val.is_int():
        val.verifications['is_int'] = True
        if val.index < 0:
            val.verifications['negative_range'] = val.is_in_negative_range()
            val.verifications['negative_to_positive_index'] = val.negative_to_positive_index()
        else:
            val.verifications['is_in_range'] = val.is_in_range()
    else:
        val.verifications['is_int'] = False

    if not val.verifications['is_int']:
        print(Validator.MESSAGES[0])
    if val.verifications['is_in_range'] or val.verifications['is_in_range'] == 0:
        return val.verifications['is_in_range']
    elif val.verifications['is_in_range'] == None:
        pass
    else:
        print(Validator.MESSAGES[1])
    if val.verifications['negative_range']:
        return val.verifications['negative_to_positive_index']
    elif val.verifications['negative_range'] == None:
        pass
    else:
        print(Validator.MESSAGES[1])


