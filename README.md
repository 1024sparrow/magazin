# magazin

# Скачивание
```git clone https://github.com/1024sparrow/magazin
cd magazin
git checkout travis
```

# Разворачивание сервера

```
$ pipenv install --dev <-- создаём виртуальное окружение, версию python-а и зависимотей pipenv берёт из Pipfile
$ pipenv shell <-- входим в созданное виртуальное окружение
(magazin-...) $ pytest <-- тестирование. Правила тестирования берутся из setup.cfg
(magazin-...) $ ./manage migrate <-- генерируем БД
(magazin-...) $ ./manage.py runserver 8080 <-- запускаем сервер. Номер порта указывается, чтобы не было конфликта с Apache, если таковой запущен. Если ваш localhost свободен для вещания, номер порта можно не указывать.
```
Остановить сервер - <Ctrl> + <C>
Выйти из виртуального окружения - <Ctrl> + <D>

# Работа с магазином (клиентская часть)
Адреса в браузере:
* localhost:8080 <-- магазин
* localhost:8080/admin <-- админка магазина
* localhost:8080/api <-- api магазина для доступа, например, из SPA-версии сайта или мобильного приложения
