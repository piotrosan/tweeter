# Instalacja

1. Pobranie danych do katalogu
2. Wprowadzenie poprawnej konfiguracji do połączenia z tweeterem w pliku settings, parametry poniżej
CONSUMER_API_KEY = ''
CONSUMER_API_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET_KEY = ''
2. Uruchomienie docker-compose up
3. Zalogowanie się do powłoki systemu do kontenera
docker ps -> szukamy id kontenera aplikacji
docker exec -it <id kontenera> bash
4. Uruchomienie migracji django
python manage.py migrate
plik bazy jest wyżucony do tmp systemu linux także po zamknieci dokera nadal
będzie działać ale po restarcie systemu już nie
5. Aplikacja działa pod adresem 72.20.0.10 na porcie 8000




