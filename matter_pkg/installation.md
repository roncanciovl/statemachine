# Environments

Desde el terminal de VS code envie el siguiente comando. Despues de enviado le debe aparecer una ventana preguntando si quiere vincular este environment al workspace actual, selecciones Si.

```shell script
python -m venv .env
```

Al crear el environment se crea una carpeta .robotenv dentro del workspace con algunos Scripts, entre ellos se crea un link al ejecutable de python del sistema operativo: .robotenv\Scripts\python.exe. En esa carpeta tambien se guardaran las bibliotecas (libraries) necesarias para el proyecto.

## Luego se debera activar el environment para instalar los paquetes

Envie primero este comando para habilitar permisos, toda la linea es el comando

```shell script
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
Comando para activar el environment:

```shell script
.env\Scripts\activate
```
Luego de activarlo deberá aparecer al lado izquierdo entre parentesis el nombre del environment activo. 

```shell script
(.env) C:\Users\username\
```

Si se cierra este terminal y se abre otro nuevo, es necesario activar el environment otra vez:

```shell script
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.env\Scripts\activate
```

## Por ultimo se instalan los paquetes en el environment (.robotenv)

```shell script
python -m pip install --upgrade pip
```
Si en este punto le aparece el siguiente WARNING o un error, la instalación requiere unas configuraciones adicionales. En caso contrario salte al siguiente comando.

```shell script
WARNING: pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
```
Probablemente su environment tomó una preinstalación del interpretador de Python de Anaconda o de alguna otra preninstalación, y su environment no encuentra el camino o PATH a algunas "libraries" necesarias.

La solución es agregar el PATH C:\\...\anaconda3\Library\bin a las variables de entorno del sistema operativo. Note que los ... depende de cada computador, normalmente la carpeta que necesitamos se encuentra en este camino o PATH C:\Users\username\anaconda3\Library\bin pero deberá verificarlo en su computador. 

Pasos:

1. Cierre VScode
2. Agregue este PATH a través de "Editar la variables de entorno del sistema" (busqueda de windows). No olvide al final darle aceptar a todas la ventanas. https://parzibyte.me/blog/2017/12/21/agregar-directorio-path-windows/
3. Abra de nuevo VScode
4. Habilite los permisos para activar el environment desde un terminal
5. Active el environment
6. Verifique el cambio, enviando el comando de instalación anterior: python -m pip install --upgrade pip


Siguiente comando:


```shell script
pip install -r requirements.txt
```


## Anotaciones adicionales. No son necesarias en la instalación


El archivo .gitignore se ha configurado para evitar que el environment se guarde en el repositorio. Adicionando la siguiente linea dentro en el archivo: .robotenv

En caso de instalar nuevos paquetes, se require actualizar el archivo de requerimientos de paquetes

```shell script
pip freeze > requirements.txt
```
