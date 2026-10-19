# Docker СӨЖ

nginx контейнеріндегі статикалық HTML бет.
Контейнер хост операциялық жүйесінің ядросын пайдаланады, сондықтан әрқайсысына бөлек ОЖ керек виртуалды машинадан жеңілірек.

## 1. Docker-ді тексеру
```
arman@DESKTOP-6SCBB5A:~$ docker --version
Docker version 29.7.2, build a7dcaa6
```

## 2. Образды жинау
```
arman@DESKTOP-6SCBB5A:~/docker-sro$ docker build -t my-html-site .
 => [1/2] FROM docker.io/library/nginx:alpine
 => [2/2] COPY index.html /usr/share/nginx/html/index.html
 => => naming to docker.io/library/my-html-site:latest
```

## 3. Образды тексеру
```
arman@DESKTOP-6SCBB5A:~/docker-sro$ docker images
IMAGE                 ID             DISK USAGE   CONTENT SIZE
my-html-site:latest   dcfa1225d58f   102MB        28.8MB
```

## 4. Контейнерді іске қосу
```
arman@DESKTOP-6SCBB5A:~/docker-sro$ docker run -d -p 8080:80 --name my-site my-html-site
916579a2a5c59c9cbae27c1815381df45a6bc7f7f918f82a7e8725930f3e64e1

arman@DESKTOP-6SCBB5A:~/docker-sro$ docker ps
CONTAINER ID   IMAGE          STATUS         PORTS                  NAMES
916579a2a5c5   my-html-site   Up 9 seconds   0.0.0.0:8080->80/tcp   my-site
```

## 5. Нәтиже
Сайт http://localhost:8080 мекенжайында қолжетімді.

<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/c6745e73-ae42-4f4e-b3b7-262f7227164c" />
