from itertools import combinations


class TestStringClass:
    def __init__(self, str):
        self.str = str

    def test_String_length(self):
        length = len(self.str)
        return length

    def test_str_list(self):
        characters = list(self.str)
        return characters


class TestPairsPossible(TestStringClass):

    def test_Possible_pairs(self):
        lis = TestStringClass.test_str_list(self)
        groups = 2
        combos = [
            x for x in combinations(lis, groups)
        ]
        print(*combos)
        return combos


class TestSearchCommonElements:

    def __init__(self, a, b):
        self.StringClass_string = a
        self.PossiblePair_string = b
        self.common_list = list()

    def test_find_common(self):
        dict = {}

        for ele in self.StringClass_string:
            if ele in self.PossiblePair_string:
                if ele in dict:
                    continue
                else:
                    dict[ele] = 1

        for key in dict:
            self.common_list.append(key)

        return self.common_list


class TestEqualSumPairs:
    def __init__(self, str):
        self.str = str

    def test_str_list(self):
        characters = list(self.str)
        return characters

    def test_Possible_pairs(self):
        lis = TestStringClass.test_str_list(self)
        groups = 2
        combos = [
            x for x in combinations(lis, groups)
        ]
        print(*combos)
        return combos

    def test_Possible_pairs(self):
        lis = TestStringClass.test_str_list(self)
        groups = 2
        combos = [
            x for x in combinations(lis, groups)
        ]
        print(*combos)
        return combos

    def test_print_equal_sum_pairs(self, lis):

        dict1 = {}

        for pair in lis:
            pairs_list = list(pair)
            sum = 0
            for num in pairs_list:
                sum = sum + int(num)

            if sum in dict1:
                dict1[sum] = dict1[sum] + 1
            else:
                dict1[sum] = 1

        for key in dict1:
            if dict1[key] == 1:
                print(key, end=" ")


def test_StringClass():
    obj = TestStringClass("12314532")
    print("length of the string is:")
    print(obj.test_String_length())
    print("String converted into list are")
    print(obj.test_str_list())



def test_Search():
    obj = TestStringClass("12314532")
    Demo = TestPairsPossible("1357357")
    obj1 = TestSearchCommonElements(obj.str, Demo.str)
    print("Common Elements are:")
    print(obj1.test_find_common())


def test_Equal():
    Demo = TestPairsPossible("1357357")
    lis = Demo.test_Possible_pairs()
    obj2 = TestEqualSumPairs("12314532")
    print("Equal sum pairs are:")
    obj2.test_print_equal_sum_pairs(lis)