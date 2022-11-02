# Запуск проекта парсера pj-parser

## Необходимое ПО
* Docker
* docker-compose
* mkcert
* git

## Установка
1. Клонируйте репозиторий 
    ```
    git clone https://github.com/yarvod/pj-parser.git
    ```
2. Запросить .env файл у разработчика
3. Создайте ssl сертификат и ключ для домена `localhost` при помощи утилиты mkcert
    ```
    mkcert localhost
    ```
4. В папке с проектом создайте файл `.env` и добавьте в него пути до сгенерированных выше файлов
    ```
    SSL_CERTIFICATE=...
    SSL_CERTIFICATE_KEY=...
    ```
5. Создайте своего телеграм бота для теста через https://t.me/BotFather

7. Создайте свой канал для теста и добавте туда своего бота

8. Собрать образы и запустить их 
    ```
    docker-compose up --build -d
    ```
9. Создать супер юзера
   ```
   docker exec pj-parser-backend python manage.py createsuperuser
   ```
   
10. Админка проекта будет доступна по ссылке
     ```
     https://localhost/admin/
     ```