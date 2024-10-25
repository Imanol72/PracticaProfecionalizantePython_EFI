#Modelo de python y sistema operativo
FROM python:alpine3.19 

#Copia todo lo que esta a la altura del docker file. Copia todo lo del directorio en el contenedor
COPY . /first_docker_b  

#Setea el directorio de trabajo en el contenedor 
WORKDIR /first_docker_b

#Corre comandos
RUN pip install --upgrade pip
RUN pip install -r requeriments.txt

#Exxpone puerto
EXPOSE 5000

#ENTRYPOINT [ "python" ]

#CMD [ "app.py" ]

ENV FLASK_APP=app/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["sh","run.sh"]