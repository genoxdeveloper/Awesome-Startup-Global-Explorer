<div align="center">

# Awesome Startup Global Explorer

**Discover startup funding, grants, accelerators & cloud perks across 188+ countries and 100+ industries.**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)

[**English**](README.md) | [**한국어**](README.ko.md) | [**中文**](README.zh_Hans.md) | [**Español**](README.es.md) | [**العربية**](README.ar.md)

*Built for startups, by a startup in Seoul, South Korea*  
*An open-source project by**[Genox](https://genoxholdings.com)**&**[Buygit.com](https://buygit.com)***

</div>

---

Bienvenido a**Awesome Startup Global Explorer**, su puerta de entrada definitiva para navegar por el ecosistema global de startups. Ya sea que sea un fundador en etapa inicial que busca financiación inicial o una empresa de tecnología en expansión que busca subvenciones gubernamentales y capitalistas de riesgo de primer nivel, esta plataforma centraliza**más de 35 000 oportunidades de financiación en más de 188 países**.

![Panel de demostración](demo_en.png)

## 🏢 Acerca de Genox

**Genox**es una empresa tecnológica innovadora con sede en Seúl, Corea del Sur. Diseñamos soluciones y plataformas basadas en datos que potencian a las empresas emergentes globales. Creemos en democratizar el acceso a las oportunidades, romper fronteras y acelerar la innovación.

Pasamos innumerables horas recorriendo portales gubernamentales, bases de datos de capital de riesgo y sitios de aceleradores en docenas de países. Primero creamos esta herramienta internamente y ahora la estamos abriendo porque**todos los fundadores merecen acceso a oportunidades globales**, no solo las de Silicon Valley.

## 🚀 ¿Qué te permite hacer este sitio?

Encontrar el programa de financiación o apoyo adecuado puede resultar abrumador, especialmente cuando se mira más allá de las fronteras. Esta aplicación resuelve eso haciendo el trabajo pesado por usted:

### 1. Descubra la financiación global al instante
Explore una base de datos masiva y continuamente actualizada de:
-**Subvenciones gubernamentales**(por ejemplo, SBIR en EE. UU., Innovate UK, K-Startup en Corea, Horizon Europe)
-**VC y aceleradores**(Y Combinator, Techstars, 500 Global y miles de micro-VC regionales)
- Programas de**Innovación Abierta Corporativa (OI)**
-**Créditos y ventajas de la nube**(AWS Activate, Google para empresas emergentes)
- Iniciativas de**reubicación y crecimiento**(visas de inicio, residencias en centros tecnológicos)

### 2. Soporte nativo en varios idiomas (rompiendo fronteras)
Reconocemos que el próximo gran unicornio podría venir de cualquier parte. Para garantizar que ningún fundador se quede atrás debido a las barreras del idioma, nuestra plataforma cuenta con un**Sistema de soporte nativo multilingüe**increíblemente poderoso.

Con un solo clic en nuestra barra de navegación superior, puede traducir sin problemas toda la plataforma y todas las**35,000+ descripciones de programas profundamente anidadas**a:
-**Inglés**|**한국어 (coreano)**|**中文 (chino)**|**Español (Español)**|**العربية (árabe)**

Nuestro proceso de traducción utiliza representación asincrónica inteligente para preservar esquemas de datos exactos mientras localiza perfectamente la interfaz de usuario y los criterios. Esto significa que un fundador en Bogotá, Riad o Seúl puede navegar por las redes globales de capital de riesgo en su lengua materna con tanta facilidad como un fundador en San Francisco.

![Ver demostración en coreano](demo_ko.png)

### 3. Clasificación inteligente de "puntuación de relevancia"
No todos los programas son iguales. Nuestro algoritmo personalizado `fit_score` evalúa las oportunidades y automáticamente coloca los programas más activos y de nivel más alto en la cima, para que no pierda tiempo desplazándose por enlaces inactivos.

### 4. Potente filtrado y búsqueda
¿Necesita una subvención FinTech en LatAm? ¿O un acelerador de IA en Asia? Utilice la interfaz de usuario intuitiva para filtrar por país/región, categoría, industria y fechas límite.

### 5. Portales de "Aplicación" directa
Cuando encuentre la combinación perfecta, haga clic en "Aplicar" para ir *directamente* al portal oficial de solicitudes.

---

## 💻 Pila técnica y arquitectura

-**Servicio de fondo:**Python (Flask, SQLAlchemy)
-**Base de datos:**SQLite (actualizaciones masivas de transacciones únicas hiperescalables)
-**Frontend:**HTML5, CSS3 (CSS básico personalizado, interfaz de usuario Glassmorphism), JavaScript básico
-**Traducción:**Flask-Babel y `deep-translator` (API del Traductor de Google) para traducción asíncrona en tiempo real
-**Motor de datos:**Rastreador Python asíncrono (`aiohttp`, `asyncio`) que utiliza generación de procedimientos para inyección masiva de datos a hiperescala.

## 🛠️ Cómo ejecutar localmente

1.**Clonar el repositorio:**
   ```golpecito
   clon de git https://github.com/genoxdeveloper/Awesome-Startup-Global-Explorer.git
   cd Awesome-Startup-Global-Explorer
   ```

2.**Instalar dependencias:**
   ```golpecito
   instalación de pip -r requisitos.txt
   ```

3.**Inicializar y ejecutar:**
   ```golpecito
   aplicación python.py
   ```
   *La aplicación inicializará automáticamente la base de datos, comenzará la generación de datos en segundo plano (generando más de 35 000 registros) y alojará el servidor local en `http://localhost:5000`.*

## 📊 Vista de base de datos
Para los usuarios que prefieren datos sin procesar, ofrecemos un modo de**Base de datos**tabular con integración ultrarrápida de DataTables, que admite exportaciones CSV directas para su CRM o herramientas de seguimiento.

![Vista de base de datos](demo_db.png)

---

## 💖 Apoye este proyecto y socios

Si este proyecto ha sido útil para usted o su startup, ¡considere apoyarnos! Su apoyo nos ayuda a mantener y mejorar esta herramienta para la comunidad global de startups.

<div align="center">

| Platform | Link |
|----------|------|
| ⭐**Star this repo**| It's free and helps others discover this tool! |
| 🤝**Buygit.com**| Check out our partner [Buygit.com](https://buygit.com) |
| 💼**GitHub Sponsors**| [Sponsor Genox-developer](https://github.com/sponsors/genoxdeveloper) |
| ☕**Ko-fi**         | [ko-fi.com/genoxholdings](https://ko-fi.com/genoxholdings) |
| 🪙**USDT (TRC20)**  | `TUmUVHfxsFLZQToE5j4oGaPCMRKBLRjEcv` |

</div>

>**Cómprenos un café**: ¡cada taza nos ayuda a rastrear una fuente de datos más!  
>**Cómpranos una pizza**y ¡a continuación agregaremos los programas de inicio de tu país!

Su apoyo, ya sea una estrella, una participación en las redes sociales o una pequeña donación, contribuye en gran medida a mantener este proyecto vivo y gratuito para todos.

---

## 🤝 Contribuyendo
¡Agradecemos las contribuciones de fundadores y desarrolladores de todo el mundo! Si conoce una subvención, VC o aceleradora en su país que no figura en la lista, abra una incidencia o envíe una solicitud de extracción.

## 📬 Contacto

Para preguntas, consultas comerciales o propuestas de asociación:
-**Correo electrónico**: [desarrollador@genox.one](correo a:desarrollador@genox.one)  
-**Sitio web**: [genoxholdings.com](https://genoxholdings.com)
-**Socio**: [buygit.com](https://buygit.com)

---

<div align="center">

**Construido con ❤️ por [Genox](https://genoxholdings.com) y [Buygit.com](https://buygit.com) · Seúl, Corea del Sur**

*Ayudando a las startups a encontrar oportunidades en todo el mundo, un punto de datos a la vez.*

</div>