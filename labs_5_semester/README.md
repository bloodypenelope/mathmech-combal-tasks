# A. lab 1

| Ограничение времени | 1 секунда |
| ------------------- | --------- |
| Ограничение памяти  | 64.0 Мб   |
| Ввод                | in.txt    |
| Вывод               | out.txt   |

Построить минимальное связывающее дерево заданного множества точек на плоскости в прямоугольной метрике (d(M,N)=|XM-XN|+|YM-YN|).

Метод решения: алгоритм Ярника-Прима-Дейкстры.

### Формат ввода

Множество точек на плоскости, заданное парами координат(x,y). N - количество точек. Далее построчно координаты точек.

### Формат вывода

Минимальное связывающее дерево, заданное в виде списков смежностей. Для каждой точки исходного множества указать порядковые номера точек, смежных с ней. Список начинать с новой строки, точки внутри списка упорядочить по возрастанию номеров. Каждый список заканчивается 0. В последней строке файла записать вес.

### Пример

| Ввод                                    | Вывод                                       |
| --------------------------------------- | ------------------------------------------- |
| 5<br>1 2<br>3 6<br>-1 -2<br>4 4<br>3 10 | 3 4 0<br>4 5 0<br>1 0<br>1 2 0<br>2 0<br>18 |

# B. lab 2

| Ограничение времени | 1 секунда |
| ------------------- | --------- |
| Ограничение памяти  | 64.0 Мб   |
| Ввод                | in.txt    |
| Вывод               | out.txt   |

Построить максимальный поток f в заданной сети.

Метод решения: алгоритм Форда-Фалкерсона.

### Формат ввода

Сеть, заданная матрицей пропускных способностей.

N - количество вершин. Далее построчно расположена матрица пропускных способностей размерности NxN. В предпоследней и последней строках файла записаны источник s и сток t.

### Формат вывода

Матрица f, расположенная построчно. В последней строке файла записать величину потока |f|.

### Пример

| Ввод                                                    | Вывод                                         |
| ------------------------------------------------------- | --------------------------------------------- |
| 4<br>0 1 1 0<br>0 0 1 1<br>0 0 0 1<br>0 0 0 0<br>1<br>4 | 0 1 1 0<br>0 0 0 1<br>0 0 0 1<br>0 0 0 0<br>2 |

# C. lab 3

| Ограничение времени | 1 секунда |
| ------------------- | --------- |
| Ограничение памяти  | 64.0 Мб   |
| Ввод                | in.txt    |
| Вывод               | out.txt   |

N предприятий выпускают товары народного потребления. Известна мощность предприятий по выпуску товаров (a<sub>i</sub> - единиц в день, i = 1, ..., n).<br>
По системе автодорог, связывающих эти предприятия и базу, эти товары попадают на базу. Известно максимальное количество товаров (единиц в день), которые могут быть перевезены от i-го к j-му предприятию или базе С<sub>ij</sub> (i = 1, ..., n; j = 1, ..., n + 1).<br>
Какое максимальное количество товаров (единиц в день) может принять база?

### Формат ввода

В первой строке число n. Во второй - n чисел a<sub>i</sub>. В следующих n строках по n + 1 числу в каждой - матрица С<sub>ij</sub>.

### Формат вывода

Одно число - максимальное количество товаров, принимаемое базой за день.
