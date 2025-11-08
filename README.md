# 🐍 Proyecto POO en Python

Este proyecto forma parte del curso de **Programación Orientada a Objetos (POO)** en Python de Platzi.  
Para la gestión de dependencias y entornos virtuales se utiliza **[uv](https://github.com/astral-sh/uv)**, una herramienta moderna, ultrarrápida y compatible con VS Code.

---

## 🚀 ¿Qué es `uv`?

`uv` es una herramienta escrita en **Rust** que combina las funciones de `pip`, `venv`, y `pip-tools`, permitiendo:

- Crear entornos virtuales.
- Instalar y actualizar dependencias.
- Ejecutar scripts dentro del entorno.
- Integrarse automáticamente con editores como **VS Code**.

Es ideal para proyectos que buscan **velocidad, simplicidad y compatibilidad total con PyPI**.

---

## 🧠 ¿Por qué usar `uv`?

| Ventaja | Descripción |
|----------|--------------|
| ⚡ **Rápido** | Es significativamente más veloz que `pip` o `venv` tradicionales. |
| 🧩 **Compatible** | Usa los mismos repositorios y formatos que `pip` y `requirements.txt`. |
| 🧠 **Simple** | Un solo comando para crear el entorno, instalar dependencias y ejecutar código. |
| 💻 **Integración VS Code** | Detecta automáticamente el entorno `.venv` en VS Code. |
| 🔄 **Ligero** | No instala dependencias innecesarias, todo se ejecuta directamente. |

---

## 🧰 Instalación

### 1️⃣ Requisitos previos
- Tener **Python 3.8+** instalado.
- Tener **pip** disponible.

### 2️⃣ Instalar `uv`
Ejecuta en tu terminal:

```bash
pip install uv

---

## ⚙️ Uso básico — Paso a paso

## 🏗️ 1. Crear un entorno virtual
```bash
uv venv
```

Esto crea una carpeta llamada `.venv` dentro del proyecto.

---

## 🔑 2. Activar el entorno virtual

### En Linux / macOS:
```bash
source .venv/bin/activate
```

### En Windows (PowerShell):
```bash
.venv\Scripts\activate
```

Cuando el entorno esté activo, verás el nombre del entorno antes del prompt del terminal.

---

## 📦 3. Instalar dependencias
```bash
uv pip install fastapi
```

Puedes instalar cualquier paquete disponible en **PyPI** reemplazando `fastapi` por el paquete deseado.

---

## 📋 4. Guardar dependencias en un archivo
```bash
uv pip freeze > requirements.txt
```

Esto crea o actualiza `requirements.txt` con las dependencias instaladas en el entorno.

---

## 🧩 5. Instalar dependencias desde un archivo
```bash
uv pip install -r requirements.txt
```

---

## ▶️ 6. Ejecutar un script dentro del entorno
```bash
uv run main.py
```

También puedes ejecutar módulos o comandos:
```bash
uv run python clientes.py
uv run pytest
```

---

## 🔍 Comparación rápida

| Acción | Comando tradicional | Con `uv` |
|--------|----------------------|-----------|
| Crear entorno | `python -m venv .venv` | `uv venv` |
| Activar entorno | `source .venv/bin/activate` | *(igual — se usa el mismo entorno)* |
| Instalar paquete | `pip install paquete` | `uv pip install paquete` |
| Instalar desde archivo | `pip install -r requirements.txt` | `uv pip install -r requirements.txt` |
| Guardar dependencias | `pip freeze > requirements.txt` | `uv pip freeze > requirements.txt` |
| Ejecutar script | `python script.py` | `uv run script.py` |