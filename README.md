\# Веб-страница Контакты



Простое веб-приложение на Python, которое возвращает HTML-страницу "Контакты" с Bootstrap.



\## Установка и запуск



1\. Установите зависимости:

&#x20;  ```bash

&#x20;  poetry install

2.Запустите сервер:



bash

python src/server.py

Откройте в браузере: http://localhost:8000



Функциональность

GET-запрос → страница "Контакты"



POST-запрос → данные выводятся в консоль



Обработка ошибки 404



text



Сохрани и закрой.



\---



\### Шаг 5: Инициализируй Git и отправь на GitHub



```bash

git init

git add .

git commit -m "init: add web contacts page with server"

git remote add origin https://github.com/alibekovazalina1996-dotcom/web\_contacts.git

git branch -M main

git push -u origin main

