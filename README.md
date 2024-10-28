# Документация
Документация api:


```
http://localhost:8000/docs
```


# Запуск проекта

1. Клонируйте репозиторий:

```
git clone https://github.com/iMaanick/qr_generator.git
```

2. При необходимости установить Poetry ```pip install poetry```

3. Запустить виртуальное окружение ```poetry shell```

4. Установить зависимости ```poetry install```

5. Для запуска выполните:
```
uvicorn --factory app.main:create_app --host localhost --port 8000
```

# Функциональность

1. Страница включает в себя поле ввода ссылки, кнопку `Update Link`, текущую ссылку и QR код.
2. QR код статичный, не меняется в процессе.
3. В поле ввода пользователь вводит ссылку, которую хочет увидеть при сканировании QR кода. Чтобы перенастроить QR код на новую ссылку пользователь нажимает на кнопку обновления.
4. В поле с текущей ссылкой отображается ссылка, которую откроет QR код в данный момент. Пока пользователь не ввел ссылку, работает дефолтная ссылка https://renident.ru/ .

# О проекте
1. FastAPI для разработки RESTful API
2. Poetry для управления зависимостями