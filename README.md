# TinyMLaaS - Backend

Bienvenido al repositorio del backend de **TinyMLaaS**. A continuación se detallan las instrucciones paso a paso para configurar el entorno de desarrollo local e instalar las dependencias necesarias en sistemas Windows.

---

## 🛠️ Configuración del Entorno de Desarrollo (Windows)

Abre tu terminal (`Símbolo del sistema` o `PowerShell`) y sigue los pasos a continuación:

### 1. Ubicación en el repositorio
Navega hasta la carpeta raíz del proyecto:
```bash
cd ruta\hacia\tu\carpeta\tinymlaas
```

### 2. Creación del entorno virtual
Crea un entorno virtual aislado para gestionar las dependencias de Python del proyecto:
```bash
python -m venv venv
```
> **Nota:** La creación del entorno puede tardar unos segundos.

### 3. Activación del entorno virtual
Es indispensable activar el entorno virtual antes de instalar paquetes o ejecutar el código:
```bash
venv\Scripts\activate
```
> **Nota de activación:** Confirmarás que el entorno está activo al visualizar la etiqueta `(venv)` al inicio de tu línea de comandos. 
> 
> *Si utilizas PowerShell y recibes un mensaje de error indicando que la ejecución de scripts está deshabilitada, ejecuta el siguiente comando y confirma la acción:*
> ```powershell
> Set-ExecutionPolicy Unrestricted -Scope CurrentUser
> ```

### 4. Instalación de dependencias
Con el entorno virtual activado, procede a instalar FastAPI junto con su servidor web (Uvicorn):
```bash
pip install "fastapi[standard]"
```

Para instalar todas las dependencias ya registradas por el equipo, puedes ejecutar:
```bash
pip install -r requirements.txt
```

### 5. Registro de dependencias (`requirements.txt`)
Para registrar y congelar la versión exacta de las dependencias instaladas y permitir que el resto del equipo replique el entorno sin discrepancias, ejecuta:
```bash
pip freeze > requirements.txt
```

---

Una vez finalizada la configuración inicial, la infraestructura base estará lista para continuar con la implementación de servicios, endpoints de la API y la conexión con PostgreSQL.
