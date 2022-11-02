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
2. Создайте ssl сертификат и ключ для домена `localhost` при помощи утилиты mkcert
    ```
    mkcert localhost
    ```
3. В папке с проектом создайте файл `.env` и добавьте в него пути до сгенерированных выше файлов
    ```
    SSL_CERTIFICATE=...
    SSL_CERTIFICATE_KEY=...
    ```
4. Запросить .env файл у разработчика

5. Собрать образы и запустить их 
    ```
    docker-compose up --build -d
    ```
6. Создать супер юзера
   ```
   docker exec pj-parser-backend python manage.py createsuperuser
   ```
   
8. Админка проекта будет доступна по ссылке
    ```
    https://localhost/admin/
    ```
   
