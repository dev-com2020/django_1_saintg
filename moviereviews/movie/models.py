from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


"""
-- Logowanie do powłoki PostgreSQL (zazwyczaj `psql`)
sudo -u postgres psql

-- Tworzenie bazy danych
CREATE DATABASE your_db_name;

-- Tworzenie użytkownika
CREATE USER your_db_user WITH PASSWORD 'your_password';

-- Nadanie uprawnień
GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;

-- Zakończenie sesji
\q
ps -f -u postgres

185.237.15.14

"""