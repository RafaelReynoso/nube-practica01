# Practica 01 - REYNOSO DAVILA RAFAEL ALEJANDRO

Este proyecto demuestra la implementación del crud de Alumnos en DJANGO y subida a Docker.

## Descripción del Proyecto

Para la realización de esta practica 01, se creó una máquina virtual en AWS EC2. La máquina virtual utilizada ejecuta Ubuntu como sistema operativo y se emplearon las tecnologías de Python (DJANGO).

## Uso del Proyecto en Local

Para utilizar este proyecto en un entorno local, siga los siguientes pasos:

1. **Clonar el repositorio**:

    ```bash
    git clone https://github.com/RafaelReynoso/nube-practica01.git
    ```
    o
     ```bash
    git clone https://github.com/Tecsupsoft/practica01-dsn-RafaelReynoso.git
    ```
    
3. **Abrir la terminal e instalar los requerimientos**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Navegar hasta el directorio del proyecto**:

    ```bash
    cd nube-practica01
    cd practica01
    ```

5. **Iniciar la aplicación**:

    ```bash
    python manage.py runserver
    ```

## Uso del Proyecto con Docker
![image](https://github.com/Tecsupsoft/lab04-microservicios-RafaelReynoso/assets/67761441/60db772b-a8a2-40c9-9d91-edcf7e319af0)


También puede ejecutar este proyecto utilizando Docker. Siga estos pasos:

1. **Buscar mi usuario de DockerHub rafaelreynoso**:

    ```bash
    docker search rafaelreynoso
    ```

2. **Descargar el contenedor llamado "eva01-alumnos-django" con la imagen "rafaelreynoso/eva01-alumnos-django"**:

    ```bash
    docker pull rafaelreynoso/eva01-alumnos-django
    ```
