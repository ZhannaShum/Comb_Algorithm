Задача 1434 - https://acm.timus.ru/problem.aspx?space=1&num=1434

Данный код представляет собой реализацию алгоритма поиска кратчайшего пути между 
двумя вершинами в графе. Для решения задачи используется алгоритм обхода в ширину (BFS).

Изначально импортируется deque из модуля collections (deque представляет собой 
двустороннюю очередь, которая используется для эффективной реализации BFS).

Затем создается список S размером 1001, каждый элемент которого является пустым списком.

Класс Node представляет собой узел графа, имеющий три атрибута:

1) v: Вершина посещена или нет (тип bool).
2) s: Список связанных с ним остановок (тип list).
3) p: Родительская вершина (тип Node или None, если нет родителя).

Создается список nodes размером 100001, каждый элемент которого является экземпляром класса Node.

Далее считываются значения N и M, где N - количество остановок, 
а M - количество автобусных маршрутов. Для каждой из N остановок считывается 
список остановок, которые соединены с данной остановкой. Добавление связей 
между узлами происходит в двойном цикле.

Затем считываются значения a и b, представляющие начальную и конечную вершины.

Инициализируется очередь Q с вершиной a. Алгоритм BFS начинает работу с вершины 
a и обходит граф в ширину, пока очередь Q не станет пустой. 
В процессе обхода вершин обновляются их атрибуты: v (посещена) и p (родительская вершина).

После завершения алгоритма BFS, если вершина b не посещена, значит, путь не найден, 
и выводится -1. В противном случае вычисляется и выводится длина кратчайшего пути, 
а затем сам путь, полученный обратным проходом от вершины b к вершине a, используя родительские ссылки.