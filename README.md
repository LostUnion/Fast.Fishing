<h1>Fast.Fishing</h1>

<b>Данный скрипт оптимизирует и ускоряет поиск информации по звонку.</b>

<h3>Запуск программы</h3>

Скрипт запускается из командной строки с указанием одного аргумента:
```
py main.py -c [call_id]
```

При первом запуске программы, будет создана локальная база данных, а также будет запрошены логин и пароль от личного кабинета.
После ввода валидных логина и пароля, программа продолжит свое выполнение.

***После успешного завершения работы программы, будет сформирован документ с расширением .xlsx, в котором будут указаны все данные по искомому звонку.***

<h3>!ВАЖНО! Для работы скрипта необходимо соединение с выделенным сервером VPN.</h3>

---

<h3>Установка зависимостей</h3>

Установить зависимости, необходимые для работы скрипта, можно командой:

```
pip install -r requirements.txt
```
Скрипт готов к работе.

---

<div align="center">

Libraries in this project

[![Python](https://img.shields.io/badge/Python-3.12-brightgreen?logo=python&color=orange)](https://www.python.org/downloads/) [![Requests](https://img.shields.io/badge/Requests-2.31-brightgreen?logo=Requests&color=green)](https://requests.readthedocs.io/en/latest/)

<i>Version 1.0.1 | Release Date: January 10, 2024</i>
</div>