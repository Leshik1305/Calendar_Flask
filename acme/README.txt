curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2000-01-02|title|text"
```

### получение всего списка заметок

curl http://127.0.0.1:5000/api/v1/calendar/
```

### получение заметки по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/
```

### обновление текста заметки по идентификатору / ID == 1 /  
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2000-01-03|title2|new text1"
```

### удаление заметки по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
```


## пример исполнения команд с выводом

```
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2000-01-02|title|text"
new id: 1

Пробуем создать заметку с тем же числом:
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2000-01-02|title|text"
failed to CREATE with: Another event already exists on the date: 2000-01-02


Пробуем создать заметку с длинным текстом:
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2000-01-07|title|t111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111114ext"
failed to CREATE with: Text length > MAX: 200

curl http://127.0.0.1:5000/api/v1/calendar/
1|2000-01-02|title|text

curl http://127.0.0.1:5000/api/v1/calendar/1/
1|2000-01-02|title|text

curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2000-01-03|title2|new text1"
updated

curl http://127.0.0.1:5000/api/v1/calendar/1/
1|2000-01-03|title|new text

Пробуем обновить заметку, внеся слишком длинный заголовок.
 curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2010-01-11|loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong title|text"
failed to UPDATE with: Title length > MAX: 30

 curl http://127.0.0.1:5000/api/v1/note/1/ -X DELETE
deleted

 curl http://127.0.0.1:5000/api/v1/note/
-- пусто --