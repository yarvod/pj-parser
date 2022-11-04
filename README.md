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
2. Запросите `.env` файл у разработчика и положить в корневую папку с проектом
3. Создайте ssl сертификат и ключ для домена `localhost` при помощи утилиты mkcert
    ```
    mkcert localhost
    ```
4. В папке с проектом в `.env` файл добавьте пути до сгенерированных выше файлов
    ```
    SSL_CERTIFICATE=...
    SSL_CERTIFICATE_KEY=...
    ```
5. Создайте своего телеграм бота для теста через https://t.me/BotFather. Положите токен бота в `.env` файл
   ```
   TOKEN=...
   ```
6. Создайте свой телеграм-канал (!!!Обязательно сделайте его публичным и задайте юзернейм!!!) для теста и добавте туда
   своего бота как администратора. Добавте в `.env` файл юзернейм вашего канала
    ```
    CHANNEL=...
    ```
7. Создайте приложение в телеграмме через https://my.telegram.org/apps
8. Возьмите полученные api_id и api_hash и положите в `.env` файл
   ```
   API_ID=...
   API_HASH=...
   ```
9. Собрать образы и запустить их
    ```
    docker-compose up --build -d
    ```
10. Создать супер юзера. Достаточно указать username и password
    ```
    docker exec -it pj-parser-backend python manage.py createsuperuser
    ```
11. Админка проекта будет доступна по ссылке
     ```
     https://localhost/admin/
     ```