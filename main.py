def is_antipalindrome(n):
    '''
    Determina daca un numar dat n este antipalindrom
    :param n: nr. intreg
    :return: True daca n este antipalindrom si False in caz contrar
    '''

    n = abs(n)
    nr_cifre = 0
    copie_n = n

    # Determinam numarul de cifre ale lui n
    while copie_n != 0:
        nr_cifre = nr_cifre + 1
        copie_n = copie_n // 10
    copie_n = n
    invers = 0

    # Aflam inversul lui n
    while copie_n != 0:
        invers = invers * 10 + copie_n % 10
        copie_n = copie_n // 10
    i = nr_cifre // 2

    # Comparam cifrele
    while i != 0:
        if n % 10 == invers % 10:
            return False
        i = i - 1
        n = n // 10
        invers = invers // 10
    return True


def test_is_antipalindrome():
    assert is_antipalindrome(-20) == True
    assert is_antipalindrome(4) == True
    assert is_antipalindrome(7) == True
    assert is_antipalindrome(33) == False
    assert is_antipalindrome(45) == True
    assert is_antipalindrome(454) == False
    assert is_antipalindrome(458) == True
    assert is_antipalindrome(777) == False
    assert is_antipalindrome(2783) == True
    assert is_antipalindrome(2773) == False
    assert is_antipalindrome(2783) == True
    assert is_antipalindrome(234453) == False


def get_base_2(n: str):
    '''
    Transforma un numar dat din baza 10 in baza 2
    :param n: Sir de numere
    :return: Numarul n in baza 2
    '''

    numar = ""
    if int(n) < 0:
        numar = "Numar incorect!"
    elif n == "0":
        numar = "0"
    else:
        while int(n) != 0:
            numar = str(int(n) % 2) + numar
            n = str(int(n) // 2)
    return numar


def test_get_base_2():
    assert get_base_2("-14") == "Numar incorect!"
    assert get_base_2("0") == "0"
    assert get_base_2("1") == "1"
    assert get_base_2("3") == "11"
    assert get_base_2("9") == "1001"
    assert get_base_2("75") == "1001011"
    assert get_base_2("123") == "1111011"


def is_palindrome(n):
    '''
    Determină dacă un număr dat este palindrom.
    :param n: numarul ce urmaeza sa fie verificat
    :return: True daca numarul este palindrom si False in caz contrar
    '''
    n = abs(n)
    copie_n = n
    invers = 0

    # Aflam inversul lui n
    while copie_n != 0:
        invers = invers * 10 + copie_n % 10
        copie_n = copie_n // 10

    # Comparam cifrele
    while n != 0:
        if n % 10 != invers % 10:
            return False
        n = n // 10
        invers = invers // 10
    return True


def test_is_palindrome():
    assert is_palindrome(7) == True
    assert is_palindrome(55) == True
    assert is_palindrome(454) == True
    assert is_palindrome(4564) == False


def main():
    RunMain = True
    while RunMain:
        print('1. Determinare daca numarul este antipalindrom (problema 7). ')
        print('2. Transforma un numar dat din baza 10 in baza 2 ( problema 8).')
        print('3. Găsește ultimul număr prim mai mic decât un număr dat (problema 1). ')
        print('x. Iesire')
        optiune = input('Alegeti o optiune: ')
        if optiune == '1':
            nr = int(input('Numarul care doriti sa se verifice: '))
            if is_antipalindrome(nr):
                print(f'Numarul {nr} este antipalindrom!')
            else:
                print(f'Numarul {nr} nu este antipalindrom!')
        elif optiune == '2':
            nr = int(input('Numarul din baza 10 care doriti sa fie transformat in baza 2: '))
            print(f'Numarul {nr} este echivalent cu {get_base_2(nr)} in baza 2.')
        elif optiune == '3':
            nr = int(input('Numarul care dirti sa aflati ca este palindrom este: '))
            if is_palindrome(nr):
                print(f'Numarul {nr} este palindrom!')
            else:
                print(f'Numarul {nr} nu este palindrom!')
        elif optiune == 'x':
            break
        else:
            RunMain = False


test_is_antipalindrome()
test_get_base_2()
test_is_palindrome()
main()
