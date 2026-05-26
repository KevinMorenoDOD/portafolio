# Portafolio Personal — Kevin Moreno

Documentación del proyecto de portafolio personal desarrollado con **Reflex** (framework web en Python).

---

## Tabla de contenido

1. [¿Qué es este proyecto?](#1-qué-es-este-proyecto)
2. [Tecnologías que usé](#2-tecnologías-que-usé)
3. [Estructura del proyecto](#3-estructura-del-proyecto)
4. [Cómo funciona la app](#4-cómo-funciona-la-app)
5. [Secciones del portafolio](#5-secciones-del-portafolio)
6. [Contenido actual de componentes](#6-contenido-actual-de-componentes)
7. [Instalación y ejecución](#7-instalación-y-ejecución)
8. [Qué me falta mejorar](#8-qué-me-falta-mejorar)

---

## 1. ¿Qué es este proyecto?

Es mi portafolio personal: una Single Page Application construida con [Reflex](https://reflex.dev), un framework que me permite desarrollar aplicaciones web completas usando solo Python. No tiene backend propio ni base de datos — es 100% frontend.

La navegación entre secciones se hace con anclas HTML, sin recargar la página. El diseño es vertical con un navbar fijo arriba. Todos los textos de la app están en español.

---

## 2. Tecnologías que usé

| Tecnología | Para qué la usé |
|---|---|
| **Python 3.x** | Lenguaje principal |
| **Reflex** | Framework frontend (compila Python → React) |
| **TailwindCSS v4** | Estilos utilitarios |
| **SitemapPlugin** | Generación automática de sitemap para SEO |

> No escribí JavaScript directamente. Reflex se encarga de compilar todo a React.

---

## 3. Estructura del proyecto

```
portofolio/                          # raíz del repositorio
├── requirements.txt
├── rxconfig.py                      # Configuración de Reflex y plugins
├── assets/                          # Imágenes, iconos y mi CV en PDF
└── portofolio/                      # Código de la app
    ├── __init__.py
    ├── portofolio.py               # Punto de entrada — arma la página
    ├── elements/                   # Componentes / secciones
    │   ├── navbar.py
    │   ├── profile.py
    │   ├── tecnologies.py
    │   ├── experience.py
    │   ├── studies.py
    │   ├── proyects.py
    │   ├── contact.py
    │   └── footer.py
    └── styles/                     # Estilos separados por componente
        ├── contact_styles.py
        ├── experience_styles.py
        ├── footer_styles.py
        ├── general_styles.py
        ├── index_styles.py
        ├── tecnologies_styles.py
        ├── studies_styles.py
        ├── proyects_style.py
        ├── profile_styles.py
        └── navbar_styles.py
```

---

## 4. Cómo funciona la app

La aplicación usa estados reactivos en varias secciones. Ejemplo en `profile`:

```python
class PortfolioState(rx.State):
    show_email: bool = False
```

Este estado controla el botón **"Show Mail"** en `profile`: al hacer clic se revela el correo (evitando exponerlo en el HTML estático) y se ofrece la opción para abrir el cliente. 

La sección `contact` ahora incorpora reactividad para manejar su comportamiento (por ejemplo, mostrar/ocultar formularios, mensajes de confirmación o interacciones dinámicas). Ya no depende exclusivamente de un enlace `mailto:`.

---

## 5. Secciones del portafolio

| Sección | Estado | Contenido |
|---|---|---|
| **Navbar** | ✅ Listo | Links internos a cada sección |
| **Profile** | ✅ Listo | Foto, nombre, descripción, links a GitHub/LinkedIn y descarga de CV |
| **Technologies** | ✅ Listo | Tecnologías principales y secundarias con iconos |
| **Experience** | ✅ Listo | Experiencia laboral con cargo, empresa, fechas y responsabilidades |
| **Studies** | ✅ Listo | Formación académica |
| **Projects** | ⚠️ En desarrollo | Placeholders — aún sin proyectos reales cargados |
| **Contact** | ✅ Listo | Medios de contacto; ahora con reactividad (formulario/estado) |
| **Footer** | ✅ Listo | Completado — información y enlaces finales presentes |

---

## 6. Contenido actual de componentes

Listado de archivos actuales (directorio `portofolio`):

- Componentes (`portofolio/elements`):
  - navbar.py
  - profile.py
  - tecnologies.py
  - experience.py
  - studies.py
  - proyects.py
  - contact.py
  - footer.py

- Estilos (`portofolio/styles`):
  - contact_styles.py
  - experience_styles.py
  - footer_styles.py
  - general_styles.py
  - index_styles.py
  - tecnologies_styles.py
  - studies_styles.py
  - proyects_style.py
  - profile_styles.py
  - navbar_styles.py

Notas rápidas:
- Los textos de la app están en español.
- Los imports de estilos en `studies` ya fueron corregidos.

---

## 7. Instalación y ejecución

Comandos para **Windows PowerShell**, desde la raíz del proyecto:

```powershell
# 1. Crear el entorno virtual
python -m venv .venv

# 2. Activarlo
.\.venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Correr la app
reflex run
```

La app queda disponible en `http://localhost:3000`.

Si PowerShell bloquea la activación, ejecuta:
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

En macOS/Linux activa el entorno con: `source .venv/bin/activate`

---

## 8. Qué me falta mejorar

| Prioridad | Tarea |
|---|---|
| 🔴 Alta | Completar la sección de proyectos con repos reales y ejemplos |
| 🟢 Baja | Evaluar renombrar archivos: `tecnologies` → `technologies`, `proyects` → `projects` (requiere actualizar imports) |
| 🟢 Baja | Agregar metaetiquetas SEO y Open Graph |

