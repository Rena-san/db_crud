#### Тестирование БД

- Для подключения к БД mySql в файле config.py необходимо указать следующие параметры:
> HOST
> 
> USER
> 
> PASSWORD
> 
> DB_NAME
> 
> PORT
- Создать окружение:
> python -m venv venv
- Активировать окружение:
> source venv/Scripts/activate
- Установить зависимости:
> pip install -r requirements.txt
- Выполнить команду:
> pytest
