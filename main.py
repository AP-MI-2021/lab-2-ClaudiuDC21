'''
def is_antipalindrome(n):
    nr_cifre = 0
    copie_n = n
    while copie_n != 0:
        nr_cifre = nr_cifre + 1
        copie_n = copie_n // 10
    copie_n = n
    invers = 0
    while copie_n != 0:
        invers = invers * 10 + copie_n % 10
        copie_n = copie_n // 10
    i = nr_cifre // 2
    while i != 0:
        if n % 10 == invers % 10:
            return False
        i = i - 1
    return True
def test_is_antipalindrome():
    assert is_antipalindrome(2783) == True
    assert is_antipalindrome(2773) == False
    assert is_antipalindrome(458) == True
    assert is_antipalindrome(454) == False
'''
def get_base_2(n: str):
    numar = " "
    while n != 0:
        rest = n % 2
        numar = numar + rest
        n = n // 10
    return numar

def main():
'''    while True:
            print('1.Determinare daca numarul este antipalindrom (problema 7). ')
            optiune = input('Alegeti o optiune: ')
            if optiune == '1':
                nr= int(input('Numarul care doriti sa se verifice: '))
                if is_antipalindrome(nr):
                    print('Numarul dat este antipalindrom!')
                else:
                    print('Numarul dat nu este palindrom!')

    test_is_antipalindrome()
    '''
    n = int(input("Dati numarul: "))
    p= get_base_2(n)
    print(p)
main()