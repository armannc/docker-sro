# Docker СРО

nginx контейнеріндегі статикалық HTML бет. Контейнер хост операциялық жүйесінің ядросын пайдаланады, сондықтан әрқайсысына бөлек ОЖ керек виртуалды машинадан жеңілірек.

## 1. Docker-ді тексеру

```bash
docker --version
# Docker version 29.7.2, build a7dcaa6
```

## 2. Образды жинау

```bash
docker build -t my-html-site .
```

## 3. Образды тексеру

```bash
docker images
```

```
IMAGE                 ID             DISK USAGE   CONTENT SIZE
my-html-site:latest   dcfa1225d58f   102MB        28.8MB
```

## 4. Контейнерді іске қосу

```bash
docker run -d -p 8080:80 --name my-site my-html-site
docker ps
```

```
CONTAINER ID   IMAGE          STATUS          PORTS                  NAMES
916579a2a5c5   my-html-site   Up 9 seconds    0.0.0.0:8080->80/tcp   my-site
```

## 5. Нәтиже

Сайт http://localhost:8080 мекенжайында қолжетімді.

<img width="1192" height="666" alt="image" src="https://github.com/user-attachments/assets/83a3ae7e-8721-42b9-90e2-d8622427a16f" />
## 6. PostgreSQL контейнері

Сайттың орнына дерекқор көтердім (postgres:18). Порт 5433, себебі 5432 жергілікті PostgreSQL-де бос емес.

```bash
docker run -d --name my-db -e POSTGRES_PASSWORD=secret -p 5433:5432 postgres:18
docker ps
```

```
CONTAINER ID   IMAGE         STATUS         PORTS                    NAMES
e085814a4500   postgres:18   Up 5 minutes   0.0.0.0:5433->5432/tcp   my-db
```

Контейнер ішінен тексеру:

```bash
docker exec -it my-db psql -U postgres
```

```sql
CREATE TABLE students (id SERIAL PRIMARY KEY, name TEXT);
INSERT INTO students (name) VALUES ('Arman');
SELECT * FROM students;
```

```
 id | name
----+-------
  1 | Arman
```

pgAdmin4 арқылы `localhost:5433` мекенжайымен қосылдым:

<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/6852e173-dfd1-4728-9908-c424d0178c70" />
Терминалдағы нәтиже:

<img width="1465" height="556" alt="image" src="https://github.com/user-attachments/assets/26573e72-2c12-4b2d-8dd3-9f224ab62937" />
