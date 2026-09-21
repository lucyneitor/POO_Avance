# POO - Avance de Clases

**Autor:** Luz Estefanía Castillo Olate

**Formato:** Documentación en Markdown

## 1. Configuración e Inicio con Git

### Clonar un repositorio

```
git clone <url_repo> .

```

**Explicación:**
Este comando descarga y vincula el repositorio remoto a tu equipo local.

* **El punto (`.`):** Indica que el contenido se clonará directamente en el **directorio o carpeta actual** (la cual debe estar vacía).

* **Sin el punto:** Git creará automáticamente una nueva carpeta con el nombre del repositorio, lo que puede generar estructuras de carpetas innecesarias o anidadas.

### Configuración Global del Usuario

Antes de comenzar a realizar commits, es necesario configurar tu identidad en Git:

```
# Configurar el nombre de usuario
git config --global user.name "Tu Nombre"

# Configurar el correo electrónico asociado
git config --global user.email "tu_email@ejemplo.com"

```

**Explicación:**

* `--global`: Aplica esta configuración a todos los repositorios de tu sistema.

* `user.name` y `user.email`: Definen los metadatos de autoría que se adjuntarán a cada *commit* que realices.

### Verificar la Configuración

```
git config --global --list

```

**Explicación:**
Muestra en pantalla la lista de todos los parámetros globales configurados actualmente (nombre, correo, editor por defecto, etc.).

## 2. Flujo Básico de Trabajo: Guardar y Subir Cambios

Para actualizar tu repositorio remoto (GitHub, GitLab, etc.) con los cambios realizados localmente, debes seguir tres pasos en secuencia desde la terminal:

### Paso 1: Preparar los cambios (`git add`)

```
# Preparar un archivo específico
git add nombre_del_archivo

# O preparar todos los archivos modificados
git add .

```

**Explicación:**
Agrega los archivos modificados o nuevos al área de preparación (*Staging Area*). Esto le indica a Git qué archivos formarán parte del próximo paquete de cambios.

### Paso 2: Confirmar los cambios (`git commit`)

```
git commit -m "Mensaje descriptivo sobre los cambios realizados"

```

**Explicación:**
Crea un punto de control o "fotografía" de los archivos agrupados en el paso anterior. El parámetro `-m` permite añadir un mensaje breve explicativo sobre lo que se trabajó o modificó.

### Paso 3: Subir los cambios al repositorio remoto (`git push`)

```
git push origin <nombre_de_rama>

```

*(Ejemplo común: `git push origin main` o `git push origin master`)*

**Explicación:**
Envía los commits guardados en tu máquina local hacia el servidor o repositorio remoto para sincronizar el proyecto.

## 3. Apuntes de Programación Orientada a Objetos (POO)

### Concepto: `self` *(21/09)*

* **Definición:** `self` representa la **instancia única del objeto mismo**.

* **Explicación:** Dentro de una clase, `self` se utiliza para hacer referencia a los atributos y métodos pertenecientes a la instancia específica que está ejecutando el código, permitiendo diferenciar las variables globales o locales de los datos propios del objeto.



### `@property` (Getter / Capta datos) y `@<atributo>.setter` (Setter / Asigna datos)
En lenguajes como Python, se utilicen estos decoradores para implementar el encapsulamiento y controlar la forma en que se leen y modifican los atributos de una clase.

* **Definición `@property`:** Permite definir un método para que sea accedido **como si fuera un atributo público** (sin parentesis `()`).

* **Explicación:** Funciona como un "Getter" (obtenedor). Protege el atributo directo (frecuentemente privado o protegido, como `_precio`) al retornar su valor o una versión modificada de él.

* **Definición `@<atributo>.setter`:** Permite definir un método que asigna un nuevo valor al atributo manejado por `@property`.

* **Explicación:** Funciona como un "Setter" (establecedor). Permite añadir **validaciones y controles de seguridad** antes de modificar el valor de un atributo.