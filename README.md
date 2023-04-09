В заданном лабиринте найти путь между двумя данными узлами.

Метод решения: Поиск в ширину.

Формат ввода:
В первой строке число N — количество строк в лабиринте. 
Во второй строке число M — количество столбцов в лабиринте. 
Далее построчно расположен сам лабиринт. 
Затем располагаются координаты источника и цели в формате X Y, 
где X — номер строки, Y — номер столбца. Нумерация строк и столбцов начинается с единицы.

Формат вывода:
В случае отсутствия пути в файл результатов необходимо записать "N". 
При наличии пути "Y" и далее весь путь. 
Маршрут должен начинаться координатами источника и заканчиваться координатами цели. 
Каждый шаг записывается с новой строки в формате X Y, где X — номер строки, Y — номер столбца. 
Нумерация строк и столбцов начинается с единицы.