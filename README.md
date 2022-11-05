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
5. Создайте свой телеграм-канал (!!!Обязательно сделайте его публичным и задайте юзернейм!!!) для теста. Добавьте
   в `.env` файл юзернейм вашего канала
    ```
    CHANNEL=...
    ```
6. Создайте приложение в телеграмме через https://my.telegram.org/apps
7. Возьмите полученные api_id и api_hash и положите в `.env` файл
   ```
   API_ID=...
   API_HASH=...
   ```
8. Собрать образы и запустить их
     ```
     docker-compose up --build -d
     ```
9. Авторизируйтесь в телеграмме с помощью команды и полученных ранее `api_id` и `api_hash`:
   ```
   docker exec -it pj-parser-backend python authenticate.py  --id {api_id} --hash {api_hash}
   ```
   Далее понадобиться ввести номер телефона и код из телеграмма.
10. Перегазрузите собранные образы:
    ```
    docker-compose restart
    ```
11. Создайте супер юзера. Достаточно указать username и password
    ```
    docker exec -it pj-parser-backend python manage.py createsuperuser
    ```
12. Админка проекта будет доступна по ссылке
     ```
     https://localhost/admin/
     ```
13. По данному адресу будут доступны записи, полученные из вашего телеграм канала
    ```
    https://localhost/admin/posts/rawpost/
    ```