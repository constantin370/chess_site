# chess tournament
## О проекте
Project chess tournament
## Установка
- Клонируйте проект из гитхаба:\
`git@github.com:constantin370/chess_site.git`
- Создайте и активируйте виртуальное окружение:\
`python -m venv venv`\
`source venv/Scripts/activate`
- Установите зависимости из файла requirements.txt:\
`pip install -r requirements.txt`
`poetry install`
- Перейдите в каталог с файлом manage.py, примените миграции:\
`cd core/`\
`python manage.py migrate`
- Запустите сервер:\
`python manage.py runserver`
## Авторы
* Константин Мурадян
