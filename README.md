==== Projekt: Problem plecakowy 2D ====

==== Autorzy ====
Wojciech Piszczek (145401) 
Martyna Jędrzejczyk(145374)

==== Streszczenie ====
Autorzy projektu zaprojektowali i zaimplementowali algorytmy w języku Python rozwiązania problemu plecakowego w 2D. Przedstawione zostały dwa algorytmy: zachłanny oraz brute-force. Algorytm i wyniki zwizualizowano za pomocą biblioteki pygame. 

== Słowa kluczowe: ==
  *Problem plecakowy [[https://pl.wikipedia.org/wiki/Problem_plecakowy]]


==== Metodyka pracy grupowej ====
  - Wybranie tematu projektu: Problem plecakowy 2D.
  - Wstępne określenie szczegółów projektu i dobór odpowiednich algorytmów.
  - Plan realizacji projektu:
    * Utworzenie wizualizacji projektu za pomocą biblioteki Pygame. 
    * Implementacja algorytmu zachłannego, 
    * Implementacja algorytmu brute-force,
    * Testowanie i ulepszanie kodu,
    * Pomiar czasu wykonywania się obu algorytmów dla różnych instancji oraz przedstawienie wyników na wykresach.
  - Prezentacja projektu.
======= Wprowadzenie =======
===== Opis problemu =====
Problem plecakowy 2D to rozszerzenie problemu plecakowego. Przedmioty umieszczane w plecaku są prostokątami z wartością, plecak jest kwadratem. Problem polega na umieszczeniu w plecaku takich przedmiotów, że sumaryczna wartość plecaka jest największa. 
Zakładamy, że każdy kolejny przedmiot wkładany do plecaka zostaje umieszczony tak, aby stykał się z dowolnym wierzchołkiem innego przedmiotu znajdującego się w plecaku oraz nie nachodził na inne przedmioty. Przedmiotów nie można obracać.

===== Dane wejściowe =====
    * ''N'' - liczba przedmiotów wkładanych do plecaka 
    * ''boxes'' - lista przedmiotów wczytywana z klawiatury lub losowana, przy czym każdy przedmiot posiada szerokość, wysokość oraz wartość

=== Losowy generator danych wejściowych ===
Dane wejściowe losowane są za pomoca funkcji ''random_Boxes()'' :

<code python>
def random_Boxes():
    l = []
    for i in range(N):
        a = random.randint(1,10) * CHANGE
        b = random.randint(1,10) * CHANGE
        c = random.randint(1,10)
        d = random.choice(colors)
        l.append(Box(a,b,c,d))
    return l
</code>
''CHANGE'' - zmienna używana do przeskalowania rozmiarów przedmiotów

== Przykładowe wygenerowane dane wejściowe: ==
<code python>
Pudełko nr 0: szerokosc 200.0 wysokosc 200.0 wartosc 8
Pudełko nr 1: szerokosc 140.0 wysokosc 20.0 wartosc 8
Pudełko nr 2: szerokosc 20.0 wysokosc 120.0 wartosc 2
Pudełko nr 3: szerokosc 200.0 wysokosc 80.0 wartosc 3
Pudełko nr 4: szerokosc 160.0 wysokosc 80.0 wartosc 4
Pudełko nr 5: szerokosc 160.0 wysokosc 80.0 wartosc 10
Pudełko nr 6: szerokosc 80.0 wysokosc 40.0 wartosc 9
</code>  

==== Wybór technologii ====
  * Python 3.8
  * biblioteka Pygame

======= Opis działania algorytmów =======
===== Algorytm zachłanny =====

  - Posortowanie przedmiotów malejąco względem stosunku wartości do powierzchni danego przedmiotu
  - Przechodzenie w pętli przez listę przedmiotów, jeżeli przedmiot może być umieszczony w plecaku, umieszczenie go w wolnym miejscu. Jeżeli przedmiot się nie mieści w żadnym miejscu, nie zostaje umieszczony w rozwiązaniu.

<code python>
def greedy(boxes, container):
    boxes.sort(key=lambda x: x.wage, reverse=True)
    first_box = boxes.pop(0)
    first_box.x = container.x
    first_box.y = container.y
    boxes_in = [first_box]
    suma = first_box.value
    update_greedy(container, boxes_in, boxes, suma)
    i = 0 
    while len(boxes)>i>=0:
        flaga1 = 0
        box = boxes[i]
        coords_list = coords(boxes_in)
        for coord in coords_list: #wstawiamy normalnie lewym gornym
            box.x = coord[0]
            box.y = coord[1]
            if box.check_place(container, boxes_in):
                boxes_in.append(box)
                boxes.remove(box)
                flaga1 = 1
                suma += box.value
                update_greedy(container, boxes_in, boxes, suma)
                break
            
        if flaga1 == 0: #wstawiamy lewym dolnym
            for coord in coords_list:
                box.x = coord[0]
                box.y = coord[1] - box.height
                if box.check_place(container, boxes_in):
                    boxes_in.append(box)
                    boxes.remove(box)
                    flaga1 = 1
                    suma += box.value
                    update_greedy(container, boxes_in, boxes, suma)
                    break
        
        if flaga1 == 0: #wstawiamy prawym gornym
            for coord in coords_list:
                box.x = coord[0] - box.width
                box.y = coord[1]
                if box.check_place(container, boxes_in):
                    boxes_in.append(box)
                    boxes.remove(box)
                    flaga1 = 1
                    suma += box.value
                    update_greedy(container, boxes_in, boxes, suma)
                    break
                
        if flaga1 == 0: #wstawiamy prawym dolnym
            for coord in coords_list:
                box.x = coord[0] - box.width
                box.y = coord[1] - box.height
                if box.check_place(container, boxes_in):
                    boxes_in.append(box)
                    boxes.remove(box)
                    flaga1 = 1
                    suma += box.value
                    update_greedy(container, boxes_in, boxes, suma)
                    break

        if flaga1 == 0:
            i = i+1
    return
</code>

=== Przykładowa instancja dla $N=20$ : ===
<code python>
Pudełko nr 0: szerokosc 60.0 wysokosc 80.0 wartosc 10
Pudełko nr 1: szerokosc 140.0 wysokosc 200.0 wartosc 6
Pudełko nr 2: szerokosc 80.0 wysokosc 60.0 wartosc 6
Pudełko nr 3: szerokosc 20.0 wysokosc 120.0 wartosc 2
Pudełko nr 4: szerokosc 100.0 wysokosc 180.0 wartosc 3
Pudełko nr 5: szerokosc 200.0 wysokosc 100.0 wartosc 2
Pudełko nr 6: szerokosc 80.0 wysokosc 120.0 wartosc 2
Pudełko nr 7: szerokosc 80.0 wysokosc 120.0 wartosc 4
Pudełko nr 8: szerokosc 20.0 wysokosc 20.0 wartosc 5
Pudełko nr 9: szerokosc 140.0 wysokosc 40.0 wartosc 6
Pudełko nr 10: szerokosc 80.0 wysokosc 200.0 wartosc 1
Pudełko nr 11: szerokosc 60.0 wysokosc 180.0 wartosc 6
Pudełko nr 12: szerokosc 60.0 wysokosc 20.0 wartosc 7
Pudełko nr 13: szerokosc 160.0 wysokosc 20.0 wartosc 7
Pudełko nr 14: szerokosc 100.0 wysokosc 20.0 wartosc 10
Pudełko nr 15: szerokosc 200.0 wysokosc 180.0 wartosc 4
Pudełko nr 16: szerokosc 200.0 wysokosc 160.0 wartosc 2
Pudełko nr 17: szerokosc 60.0 wysokosc 160.0 wartosc 8
Pudełko nr 18: szerokosc 120.0 wysokosc 160.0 wartosc 3
Pudełko nr 19: szerokosc 180.0 wysokosc 100.0 wartosc 4
</code>

== Rozwiązanie: ==
{{ :ok20:pr015:p145374:zachlanny.png |algorytm zachłanny}}
Po lewej stronie widoczny jest plecak z przedmiotami wybranymi do rozwiązania, po prawej stronie znajdują się przedmioty, które nie zostały wybrane.
Czas wykonywania się algorytmu: 0.09109s. 

===== Algorytm brute-force =====
  - Wyznaczenie każdego możliwego umieszczenia przedmiotów w plecaku poprzez tworzenie wszystkich permutacji ułożeń przedmiotów w liście z użyciem algorytmu Dijkstry.
  - Jeżeli dane rozwiązanie jest lepsze od najlepszego, ustawienie rozwiązania jako najlepsze.
Funkcja ''perm(t, max)'' wyznacza następnik permutacyjny listy ''t'' o długości ''max''.
<code python>
def perm(t, max):
    tab = t
    # wyznaczanie pierwszego od prawej elementu 
    # mniejszego niz jego sasiad z prawej strony
    i = max - 1
    while i>0 and tab[i-1].value >= tab[i].value:
        i -= 1
    # wyznaczanie elementu wiekszego od znalezionego
    if i > 0:
        j = max
        while j > 0 and tab[j-1].value <= tab[i-1].value:
            j -= 1
    # zamiana miejscami dwoch znalezionych wyzej elementow
    if i > 0 and j > 0:
        k = tab[i-1]
        tab[i-1] = tab[j-1]
        tab[j-1] = k
    # odbicie lustrzane szeregu elementow od indeksu i+1 do konca tablicy
    i += 1
    j = max
    while i < j:
        k = tab[i-1]
        tab[i-1] = tab[j-1]
        tab[j-1] = k
        i += 1
        j -= 1
    return tab
</code>
<code python>    
def brute_force(boxes, container):
    best_list = []
    best_coords = []
    best_sum = 0
    best_number = 0
    best_left = []
    end = False
    for j in range(factorial(N)):
        number = j + 1
        perm(boxes,N)
        boxes1 = boxes.copy()
        first_box = boxes1.pop(0)
        first_box.x = container.x
        first_box.y = container.y
        boxes_in = [first_box]
        suma = first_box.value
        update_brute(container, boxes_in, boxes1, suma, number, end)
        i = 0
        while len(boxes1)>i>=0:
            flaga4 = 0
            box = boxes1[i]
            coords_list = coords(boxes_in)
            for coord in coords_list: #wstawiamy normalnie lewym gornym
                box.x = coord[0]
                box.y = coord[1]
                if box.check_place(container, boxes_in):
                    boxes_in.append(box)
                    boxes1.remove(box)
                    flaga4 = 1
                    suma += box.value
                    update_brute(container, boxes_in, boxes1, suma,number, end)
                    break
                
            if flaga4 == 0: #wstawiamy lewym dolnym
                for coord in coords_list:
                    box.x = coord[0]
                    box.y = coord[1] - box.height
                    if box.check_place(container, boxes_in):
                        boxes_in.append(box)
                        boxes1.remove(box)
                        flaga4 = 1
                        suma += box.value
                        update_brute(container, boxes_in, boxes1, suma,number, end)
                        break
            
            if flaga4 == 0: #wstawiamy prawym gornym
                for coord in coords_list:
                    box.x = coord[0] - box.width
                    box.y = coord[1]
                    if box.check_place(container, boxes_in):
                        boxes_in.append(box)
                        boxes1.remove(box)
                        flaga4 = 1
                        suma += box.value
                        update_brute(container, boxes_in, boxes1, suma,number, end)
                        break
                    
            if flaga4 == 0: #wstawiamy prawym dolnym
                for coord in coords_list:
                    box.x = coord[0] - box.width
                    box.y = coord[1] - box.height
                    if box.check_place(container, boxes_in):
                        boxes_in.append(box)
                        boxes.remove(box)
                        flaga4 = 1
                        suma += box.value
                        update_brute(container, boxes_in, boxes, suma,number, end)
                        break

            if flaga4 == 0:
                i = i+1
        if suma > best_sum:
            best_sum = suma
            best_list = boxes_in.copy()
            best_coords = copy_coords(boxes_in)
            best_number = number
            best_left = boxes1
    for i in range(len(best_list)):
        best_list[i].x = best_coords[i][0]
        best_list[i].y = best_coords[i][1]

    end = True
    number = best_number 
    update_brute(container, best_list, best_left, best_sum, best_number, end)
</code>

=== Przykładowa instancja dla $N$ = 6: ===
<code python>
Pudełko nr 0: szerokosc 200.0 wysokosc 200.0 wartosc 10
Pudełko nr 1: szerokosc 160.0 wysokosc 160.0 wartosc 2
Pudełko nr 2: szerokosc 180.0 wysokosc 160.0 wartosc 3
Pudełko nr 3: szerokosc 180.0 wysokosc 140.0 wartosc 2
Pudełko nr 4: szerokosc 140.0 wysokosc 180.0 wartosc 8
Pudełko nr 5: szerokosc 180.0 wysokosc 160.0 wartosc 3
</code>
== Rozwiązanie: ==
{{ :ok20:pr015:p145374:bruteforce.png |algorytm brute-force}}
Po lewej stronie widoczny jest plecak z przedmiotami wybranymi do rozwiązania, po prawej stronie znajdują się przedmioty, które nie zostały wybrane.
Czas wykonywania się algorytmu: 8.9s. 

======= Testy i wykresy =======

Wykresy przedstawiają uśrednione czasy działania algorytmów dla różnych instancji otrzymane poprzez $10$-krotne wykonanie algorytmu dla tego samego $N$.

{{ :ok20:pr015:p145374:w-bruteforce.png |algorytm brute-force}}
{{ :ok20:pr015:p145374:w-zachlanny.png |algorytm zachlanny}}
{{ :ok20:pr015:p145374:w-porownanie.png |porownanie wynikow}}

======= Wnioski końcowe =======
===== Analiza złożoności =====
=== Algorytm zachłanny ===
Przejście poprzez wszystkie $N$ przedmiotów oraz w najgorszym przypadku sprawdzenie wszystkich możliwych miejsc umieszczenia danego przedmiotu (jest ich $4N$, ponieważ dopasowujemy przedmioty do wierzchołków przedmiotów znajdujących się w plecaku) daje złożoność rzędu  $O(N^2)$.
=== Algorytm brute-force ===
Algorytm polega na sprawdzeniu wszystkich $N!$ permutacji przedmiotów w liście oraz próbie włożenia przedmiotów do plecaka na $4N$ możliwości dla każdej z tych permutacji. Składa się to na złożoność rzędu $O(N \cdot N!)$.
===== Podsumowanie =====

Algorytm zachłanny jest znacznie szybszy od algorytmu brute-force, jednak nie zawsze znajduje optymalne rozwiązanie. Algorytm brute-force zawsze znajduje rozwiązanie najlepsze, jednak próba uruchomienia go dla $N$ większego niż 8 daje długi czas oczekiwania, który drastycznie rośnie wraz ze wzrostem $N$. 
==== Uwagi oceniającego projekt ====

==== Link do repozytorium projektu ====


