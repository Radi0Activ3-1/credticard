'''
Homework22
Name:Drake Pierce-Demksi
github link: 
'''
def mask_creditcard(string):
    return '*' * (len(string) - 4) + string[-4:]


def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in string if char not in vowels)


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest22.py'))