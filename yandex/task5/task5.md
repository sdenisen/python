Ограничение запросов [2 балла]
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	3 секунды	256Mb	стандартный ввод	стандартный вывод
Golang 1.14.4 + network	2 секунды	256Mb
Python 3.7 + network + requests	5 секунд	256Mb
GNU c++ 11 + network + libcurl + json	2 секунды	256Mb
Слава только-только устроился в Яндекс.Маркет и получил первое задание: написать компонент, отвечающий за ограничение запросов пользователей к сервису.
Характеристики компонента — лимит запросов на пользователя, лимит запросов на сервис и продолжительность интервала (
d
u
r
a
t
i
o
n
), за который учитываются запросы. Запрос к сервису, поступивший в момент времени 
t
i
m
e
, отклоняется, если он удовлетворяет хотя бы одному из двух условий:

Если в промежутке времени 
[
t
i
m
e
−
d
u
r
a
t
i
o
n
,
t
i
m
e
]
 от данного пользователя было принято к выполнению не меньше пользовательского лимита запросов — должен возвращаться код ошибки «Too Many Requests».
Если в промежутке времени 
[
t
i
m
e
−
d
u
r
a
t
i
o
n
,
t
i
m
e
]
 суммарно от всех пользователей было принято к выполнению не меньше сервисного лимита запросов — должен возвращаться код ошибки «Service Unavailable».
Условия проверяются последовательно друг за другом, пока не будет найдено первое условие, которому запрос удовлетворяет. Если запрос не удовлетворяет ни одному условию, то он выполняется. Пока что Слава еще не до конца погрузился в разработку и внутренние технологии, поэтому решил написать прототип, а вы можете помочь Славе.

Формат ввода
Программа получает на вход строку с тремя числами, разделенными пробелами: 
u
s
e
r
L
i
m
i
t
 (
1
≤
u
s
e
r
L
i
m
i
t
≤
5
⋅
1
0
4
) — лимит запросов на пользователя, 
s
e
r
v
i
c
e
L
i
m
i
t
 (
1
≤
s
e
r
v
i
c
e
L
i
m
i
t
≤
5
⋅
1
0
4
) — лимит запросов на сервис, 
d
u
r
a
t
i
o
n
 (
1
≤
d
u
r
a
t
i
o
n
≤
1
0
9
) — промежуток времени в миллисекундах, за который учитываются запросы для расчета лимитов.
В следующих строках поступают описания запросов. Каждый запрос представлен двумя разделенными пробелом числами: 
t
i
m
e
 (
1
≤
t
i
m
e
≤
1
0
9
) — время поступления запроса, 
u
s
e
r
I
d
 (
1
≤
u
s
e
r
I
d
≤
1
0
9
) — идентификатор пользователя, выполнившего запрос.
Входные данные завершаются строкой с числом 
−
1
. Гарантируется, что все времена в описании запросов не убывают, а количество запросов не превышает 
5
⋅
1
0
4
.
Тестирующая система даст прочитать очередной запрос только после записи в стандартный вывод ответа на предыдущий запрос (не забудьте после вывода запроса сделать flush).

Формат вывода
Для каждого запроса необходимо вывести один из трех кодов ответа HTTP:
2
0
0
 — если запрос будет выполнен.
4
2
9
 — если запрос будет отклонен из-за превышения лимита запросов пользователем.
5
0
3
 — если запрос будет отклонен из-за превышения сервисного лимита запросов.
Не забывайте о том, что ваша программа должна сбрасывать буфер вывода после вывода строчки с тайм-аутом. Для сброса буфера вывода можно использовать fflush(stdout) в C++, System.out.flush() в Java, stdout.flush() в Python.



Пример
Ввод	Вывод
2 5 5
1 100
1 100
2 100
2 200
2 300
2 400
2 500
3 500
5 200
6 100
7 200
-1
200
200
429
200
200
200
503
503
503
429
200