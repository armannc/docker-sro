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

<img width="1600" height="899" alt="WhatsApp Image 2026-10-25 at 18 56 10" src="https://github.com/user-attachments/assets/102f03b6-b023-485d-966e-d8b7f6ea9568" />

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

## 7. Docker Hub

Docker Hub-та тіркелдім (`armanakmurat`) және үш image жүктедім:

```bash
docker login
docker tag my-html-site armanakmurat/my-html-site:latest
docker push armanakmurat/my-html-site:latest
```

Профиль: https://hub.docker.com/u/armanakmurat

| Image | Сипаттама |
|-------|-----------|
| armanakmurat/my-html-site | nginx сайты |
| armanakmurat/my-db-image | `students` кестесі бар PostgreSQL 18 |
| armanakmurat/my-html-site-2 | busybox негізіндегі екінші сайт |

<img width="1907" height="1023" alt="image" src="https://github.com/user-attachments/assets/d8b185ed-c192-4a15-a237-9767ddc098f0" />

## 8. Бәрін Docker Compose арқылы іске қосу

Сайт, дерекқор және приложение бір `docker-compose.yml` арқылы көтеріледі (image-дер Docker Hub-тан тартылады):

```bash
git clone https://github.com/armannc/docker-sro.git
cd docker-sro
docker compose up -d
```

Тексеру (іске қосқаннан кейін 10 секундтай күту керек):

- `docker compose ps`: 3 контейнер `Up` болуы керек
- http://localhost:8080 сайт
- http://localhost:5000/students приложение, БД-дан деректі оқиды

Тоқтату: `docker compose down`
