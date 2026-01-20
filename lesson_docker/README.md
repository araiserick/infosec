# Задание 1. Образы и контейнеры Docker

скриншот вывода результатов команды ifconfig (на Kali Linux) или ip a (на Ubuntu);

![](image.png)

скриншот вывода результатов команды sudo docker pull bash;

![](image-1.png)

скриншот вывода результатов команды sudo docker run -it bash;

![alt text](image-2.png)

скриншот вывода результатов команды sudo docker stop names; ( он итак остановился после выхода, потому что не указал ключик -d для работы контейнера в фоновом режиме)

![alt text](image-3.png)

скриншот вывода результатов команды sudo docker rm names;

![](image-4.png)

скриншот вывода результатов команды sudo docker rmi repository;

![alt text](image-5.png)

скриншот вывода результатов команды sudo docker ps -a;

![alt text](image-6.png)

скриншот вывода результатов команды sudo docker image ls.( у меня были уже скачаны контейнеры)
скриншот вывода результатов команды whoami и cat /etc/*release* (в контейнере);
![alt text](image-7.png)

# Задание 2. Bash в Docker

скриншот вывода результатов команды sudo docker run –rm -it bash;

![](image-8.png)

скриншот вывода результатов команды whoami и cat /etc/*release* (в контейнере);

![alt text](image-9.png)

скриншот вывода результатов команды ls -la / (в контейнере);

![alt text](image-10.png)

скриншот вывода результатов команды whoami и cat /etc/*release* (в основной системе);

![alt text](image-11.png)

скриншот вывода результатов команды ls -la / (в основной системе).

![alt text](image-12.png)

# Задание 3. Dockerfile

скриншот вывода содержимого файла скрипта cat my_bash_1.sh

![alt text](image-13.png)

скриншот вывода содержимого файла Dockerfile cat Dockerfile;


![alt text](image-14.png)

скриншот результатов сборки образа sudo docker build -t image_bash_1 .

![alt text](image-15.png)

скриншот результатов запуска контейнера sudo docker run –rm image_bash_1

![alt text](image-16.png)

скриншот результатов запуска скрипта в основной системе ./my_bash_1.sh 

![alt text](image-17.png)

# Задание 4. Docker-compose

скриншот вывода содержимого подготовленного вами файла index.html, содержащий ваше Ф.И.О.;

![alt text](image-18.png)

скриншот вывода содержимого подготовленного вами файла docker-compose.yml;

![alt text](image-19.png)

скриншот результатов запуска подготовленной вами связки контейнеров;

![alt text](image-20.png)

скриншот первоначальной титульной страницы Nginx при подключении браузером к контейнеру;

![alt text](image-21.png)

скриншот вашего варианта титульной страницы Nginx при подключении браузером к контейнеру, содержащий ваше Ф.И.О.;

![alt text](image-22.png)

скриншот вывода результатов команды остановки связки контейнеров.

![alt text](image-23.png)