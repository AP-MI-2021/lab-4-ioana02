def show_menu():
    print("1.Citire a doua multimi de numere intregi sub forma de doua liste")
    print("2.Afisarea celor doua liste daca au acelasi numar de elemente pare")
    print("3.Afisarea unei liste care reprezinta intersectia listelor citite")
    print("4.Afisare palindroame")
    print("5.citire a treia lista")
    print("x. exit")

def citire_multime1():
    lst1 = []
    lst_str = input("Dati numerele din lista: "))
    lst_str_split = lst_str.split("")
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst1


def citire_multime2():
    lst2 = []
    lst_str = input("Dati numerele din lista: "))
    lst_str_split = lst_str.split("")
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst2


def elemente_pare1(lst1):
    """
         calculeaza numarul de elemente pare din prima lista
         param lst1: lista in care cauta
         return: numarul de elemente pare
        """
    for num in lst1:
        if num%2 == 0:
            k=k+1
        else:
            return None
    return k
def test_elemente _pare1():
    assert elemente_pare1([2, 3, 4, 5]) == 2
    assert elemente_pare1([]) is None
    assert elemente_pare_1([3, 5, 7]) is None


def elmente_pare2(lst2):
    """
     calculeaza numarul de elemente pare din prima lista
     param lst2: lista in care cauta
     return: numarul de elemente pare
    """
    for num in lst2:
        if num%2 == 0:
            h=h+1
        else:
            return None
    return h
def test_elemente_pare2():
    assert elemente_pare2([4, 6, 8, 3]) ==3
    assert elemente_pare2([]) is None
    assert elemente_pare2([1, 3, 7]) is None


def egalitate_pare(k, h):
    """
         Verifica daca cele doua multimi au acelasi numar de elemente pare
         param k:nr de elmente pare din prima multime
         param h:nr de elemente pare din a doua multime
         return: True daca ambele multimi au acelasi nr de elmente pare si False daca nu au
    """
    if k==h:
        return True
    else:
        return False


def lista3(lst1, lst2):
    """
       Creaza o lista cu elementele comune
        param lst1: lista 1
        param lst2: lista2
        return: lista cu elementele comune
    """
    result = []
    ok=0
    for i in lst1:
        if i == lst2:
            ok=1
    if ok == 1:
        result = lst2
    return result
def test_lista3():
    assert lista3([1,3,7],[2, 4, 3, 7]) == [3, 7]
    assert lista3([1, 2, 3],[4, 5, 6]) is None
    assert lista3([],[]) == []


def show_lista3(lst):
    result = lista3()
    print(f'Lista 3 este: {result}')


def is_palindrome(n):
        """
         Aratati daca un numar este palindrom sau nu
         param n: numar intreg
         return:True daca n este palindrom sau False daca nu este
        """
        copie = n
        oglindit = 0
        while n > 0:
            oglindit = oglindit * 10 + n % 10
            n = n // 10
        if copie == oglindit:
            return True
        return False

def test_is_palindrome(n):
    assert is_palindrome(1) == True
    assert is_palindrome(2345) == False
    assert is_palindrome(121) == True
    assert is_palindrome(333) == True
    assert is_palindrome(55342) == False



def main():
    lst= []
    while True:
        show_menu()
        option= input("Dati un numar: ")
        if option== "1":
            lst1 = citire_multime1()
            lst2 = citire_multime2()
        elif option== "2":
            egalitate_pare()
        elif option== "3":
            show_lista3(lst)
        elif option== "4":

        elif option== "5":

        elif option== "x":
            break
        else:
            print("introdu alt numar")

if_name_== "_main_":
    test_
    test_
    test_
    test_
    test_
    main()
