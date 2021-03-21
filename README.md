# Mvideo
Web Api. Стек технологий: python-3.8, flask-1.1.2.

generate_sort_csv.py - скрипт, который считывает данные с исходного файла, сортирует по алфавиту и записывает в файл - zadanie.csv.(Скрипт работает ~300 секунд)

main.py - главный файл, который запускается. Перед запуском происходит задержка, потому что в массив записываются данные с файла zadanie.csv.
В url передается параметр sku - именование товара и необязательный параметр rank(Степень "близости"). Выводит список всех рекомендаций по этому товару.
Для поиска товара использовался алгоритм бинарного поиска, сложность которого = O(log n). Среднее время на ответ ~30 мс.

### Команды для запуска в Windows

```
git clone https://github.com/prostomusa/Mvideo.git
cd Mvideo
python -m venv env
env\Scripts\activate.bat
pip install flask==1.1.2
python main.py
```

### Команды для запуска в Linux

```
git clone https://github.com/prostomusa/Mvideo.git
cd Mvideo
python -m venv env
source env/bin/activate
pip install flask==1.1.2
python main.py
```

### Ссылка на файлы CSV:
[https://cloud.mail.ru/public/34bt/uU48ZxQBW]

### Ссылка на документацию API:
[https://documenter.getpostman.com/view/7641548/TVmMgdL1]
