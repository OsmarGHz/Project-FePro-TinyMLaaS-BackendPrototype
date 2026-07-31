# TinyMLaaS - Backend

Backend de la plataforma **TinyMLaaS** para AgroInteligencia, desarrollado con FastAPI.

---

## 📁 Estructura del Proyecto

```
tinymlaas/
├── main.py            # Servidor principal y configuración de CORS
├── routers/           # Endpoints modulares
│   ├── alerts.py      # Endpoints de alertas
│   └── devices.py     # Endpoints de dispositivos IoT
├── schemas/           # Schemas de Pydantic (próximamente)
└── models/            # Modelos de datos / BD (próximamente)
```

---

## 🛠️ Configuración e Instalación

### 1. Entorno virtual

Crea y activa el entorno virtual:

```bash
python -m venv venv
```

- **Windows (CMD / PowerShell):**
  ```powershell
  venv\Scripts\activate
  ```
  *(Si PowerShell bloquea la ejecución de scripts, ejecuta: `Set-ExecutionPolicy Unrestricted -Scope CurrentUser`)*

### 2. Instalación de dependencias

Con el entorno activo `(venv)`, instala los paquetes del proyecto:

```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución del Servidor

Para levantar el servidor de desarrollo con recarga automática:

```bash
fastapi dev main.py
```

El servidor estará corriendo en: `http://127.0.0.1:8000`

---

## 🧪 Prueba de Endpoints

Endpoints simulados disponibles:

- **Healthcheck:** `GET http://127.0.0.1:8000/`
- **Alertas:** `GET http://127.0.0.1:8000/api/alerts`
- **Dispositivos IoT:** `GET http://127.0.0.1:8000/api/devices`

### 📖 Documentación Interactiva (Swagger UI)

Accede a la documentación automática de FastAPI en el navegador:

👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

Desde ahí puedes probar los endpoints usando el botón **"Try it out"** y luego **"Execute"**.
