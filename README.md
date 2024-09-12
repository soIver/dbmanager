## Инструкция по использованию менеджера:
1. Скачать [архив](https://github.com/soIver/dbmanager/releases/download/v1.0.0/dbmanager.zip) и распаковать его.
2. Запустить приложение менеджера (соединение с БД установится автоматически).
3. Ввести ифнормацию в поле ввода согласно соответствующему шаблону (см. Шаблоны ввода).
4. Нажать на кнопку соответствующей операции.
5. В случае успеха в окне вывода появится соответствующее сообщение.


## Шаблоны ввода:
1. Создать таблицу: 
    > имя_таблицы: имя_атрибута1 формат_атрибута1, имя_атрибута2 формат_атрибута2, ... , имя_атрибутаn формат_атрибутаn
2. Добавить запись: 
    > имя_таблицы: значение_атрибута1, значение_атрибута2, ... , значение_атрибутаn

Если атрибут имеет текстовый формат, заключите его значение в двойные скобки.

3. Считать таблицу: 
    > имя_таблицы
4. Обновить запись: 
    > имя_таблицы: имя_атрибута1 = значение_атрибута1, имя_атрибута2 = значение_атрибута2, ... ; ключевой_атрибут = значение_ключевого_атрибута
5. Удалить запись: 
    > имя_таблицы: ключевой_атрибут = значение_ключевого_атрибута
