# Portafolio Personal — Kevin Moreno

Documentación del proyecto de portafolio personal desarrollado con **Reflex** (framework web en Python).

---

## Tabla de contenido

1. [¿Qué es este proyecto?](#1-qué-es-este-proyecto)
2. [Tecnologías que usé](#2-tecnologías-que-usé)
3. [Estructura del proyecto](#3-estructura-del-proyecto)
4. [Cómo funciona la app](#4-cómo-funciona-la-app)
5. [Secciones del portafolio](#5-secciones-del-portafolio)
6. [Instalación y ejecución](#6-instalación-y-ejecución)
7. [Qué me falta mejorar](#7-qué-me-falta-mejorar)

---

## 1. ¿Qué es este proyecto?

Es mi portafolio personal: una Single Page Application construida con [Reflex](https://reflex.dev), un framework que me permite desarrollar aplicaciones web completas usando solo Python. No tiene backend propio ni base de datos — es 100% frontend.

La navegación entre secciones se hace con anclas HTML, sin recargar la página. El diseño es vertical con un navbar fijo arriba.

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
portofolio/
├── requirements.txt
├── rxconfig.py                  # Configuración de Reflex y plugins
├── assets/                      # Imágenes, iconos y mi CV en PDF
└── portofolio/
    ├── portofolio.py            # Punto de entrada — arma la página
    ├── elements/                # Un archivo por sección
    │   ├── navbar.py
    │   ├── profile.py
    │   ├── tecnologies.py
    │   ├── experience.py
    │   ├── studies.py
    │   ├── proyects.py
    │   ├── contact.py
    │   └── footer.py
    └── styles/                  # Estilos separados por componente
```

---

## 4. Cómo funciona la app

El único estado reactivo que implementé es este:

```python
class PortfolioState(rx.State):
    show_email: bool = False
```

Controla el botón **"Show Mail"** en mi sección de perfil:

1. Carga con el correo oculto (`show_email = False`)
2. Al hacer clic, `show_email` pasa a `True`
3. Reflex re-renderiza y muestra mi dirección + un botón `mailto:`

Esto evita que mi correo quede expuesto directamente en el HTML al cargar la página.

---

## 5. Secciones del portafolio

| Sección | Estado | Contenido |
|---|---|---|
| **Navbar** | ✅ Listo | Links internos a cada sección |
| **Profile** | ✅ Listo | Foto, nombre, descripción, links a GitHub/LinkedIn y descarga de CV |
| **Technologies** | ✅ Listo | Mis tecnologías principales y secundarias con iconos |
| **Experience** | ✅ Listo | Experiencia laboral con cargo, empresa, fechas y responsabilidades |
| **Studies** | ✅ Listo | Formación académica |
| **Projects** | ⚠️ En desarrollo | Placeholder — aún sin proyectos reales cargados |
| **More** | ⚠️ En desarrollo | Reservada para certificaciones, idiomas u otros datos |
| **Contact** | ✅ Listo | Repite los medios de contacto al final de la página |
| **Footer** | ⚠️ Mínimo | Por completar |

---

## 6. Instalación y ejecución

> Comandos para **Windows PowerShell**, desde la raíz del proyecto.

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

> Si PowerShell bloquea la activación, ejecuta primero:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

> En **macOS/Linux** activa el entorno con: `source .venv/bin/activate`

---

## 7. Qué me falta mejorar

| Prioridad | Tarea |
|---|---|
| 🔴 Alta | Completar la sección de proyectos con mis repos reales |
| 🔴 Alta | Definir el contenido de la sección "More" |
| 🟡 Media | Unificar `experience_styles.py` y `style_experience.py` (están duplicados) |
| 🟡 Media | Revisar posible importación incorrecta en `studies_styles.py` |
| 🟡 Media | Agregar contenido al footer |
| 🟢 Baja | Corregir nombres: `tecnologies` → `technologies`, `proyects` → `projects` |
| 🟢 Baja | Mejorar responsive para móvil |
| 🟢 Baja | Agregar metaetiquetas SEO y Open Graph |
