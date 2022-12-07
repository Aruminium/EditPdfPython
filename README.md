## how to use

step1 git clone

```terminal
$ git clone https://github.com/Aruminium/EditPdfPython
$ cd EditPdfPython
```

step2 docker compose

```
$ docker compose build
$ docker compose up -d
$ docker ps
CONTAINER ID ...省略
96bae4353519
$ docker exec -it 96bae4353519 /bin/bash
myuser@96bae4353519:~/app$ -ここから先はコンテナ内
```

step3 run python script

```terminal
myuser@96bae4353519:~/app$ python ExcelPdfConverter.py
javaldx: Could not find a Java Runtime Environment!
Please ensure that a JVM and the package libreoffice-java-common
is installed.
If it is already installed then try removing ~/.config/libreoffice/4/user/config/javasettings_Linux_*.xml
Warning: failed to read path from javaldx
convert /home/myuser/app/files/sample.xlsx -> /home/myuser/app/files//sample.pdf using filter : calc_pdf_Export
Overwriting: /home/myuser/app/files//sample.pdf
myuser@96bae4353519:~/app$ 
```
