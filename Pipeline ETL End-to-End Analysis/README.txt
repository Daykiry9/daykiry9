# Pipeline ETL End-to-End: Análisis de Capitalización de Bancos Globales

Este repositorio contiene un script Python (`banks_project.py`) que implementa un proceso ETL completo para extraer, transformar y cargar datos sobre la capitalización de mercado de los bancos más grandes del mundo, incluyendo conversiones de divisas y almacenamiento en base de datos.

## Propósito para Reclutadores

Este proyecto es una demostración integral de mis capacidades en **Ingeniería de Datos y Procesamiento ETL**, abarcando desde la **extracción de datos no estructurados de la web** hasta su **almacenamiento y consulta en una base de datos relacional**. Muestra mi habilidad para construir un **pipeline de datos robusto y automatizado**, manejar conversiones de datos complejas (como tasas de cambio), y trabajar con datos relevantes para el sector financiero o empresarial. Es un caso de estudio práctico de cómo transformo datos crudos en información valiosa para el análisis.

**Habilidades Demostradas:**
* **Ingeniería de Datos (End-to-End):** Diseño e implementación de un flujo de datos completo, desde la fuente hasta el destino.
* **Web Scraping Avanzado:** Extracción de datos tabulares de sitios web utilizando `BeautifulSoup` y `requests`.
* **Manipulación y Transformación de Datos:** Uso experto de `pandas` para limpieza, reestructuración, uniones (merge) y cálculos (ej. conversiones de moneda).
* **Gestión de Bases de Datos:** Conectividad, carga y consulta de datos en bases de datos relacionales (SQLite en este caso).
* **Manejo de Archivos:** Lectura y escritura de datos en formatos CSV.
* **Manejo de Errores y Logging:** Implementación de un sistema de registro para monitorear el progreso y depurar el pipeline.
* **Trabajo con Datos Financieros:** Aplicación de ETL a un dominio de negocio específico como la capitalización de mercado y las tasas de cambio.
* **Automatización de Procesos:** Creación de un script autónomo para la actualización de datos.

## Descripción

El archivo `banks_project.py` automatiza el siguiente flujo de trabajo ETL:
1.  **Extracción (Extract):** Obtiene la lista de los bancos más grandes del mundo y su capitalización de mercado de una fuente web (ej. Wikipedia) mediante web scraping. Adicionalmente, extrae las tasas de cambio de un archivo CSV externo.
2.  **Transformación (Transform):**
    * Limpia y estandariza los datos extraídos.
    * Realiza una conversión de la capitalización de mercado a diferentes monedas (ej. GBP, EUR, CHF) utilizando las tasas de cambio obtenidas.
    * Calcula y agrega nuevas columnas derivadas.
3.  **Carga (Load):**
    * Guarda los datos transformados en un archivo CSV local.
    * Almacena los datos transformados en una tabla dentro de una base de datos SQLite.
4.  **Consulta (Query):** (Opcional, pero incluido en tu código) Ejecuta varias consultas SQL sobre la base de datos para verificar la integridad de los datos y obtener insights básicos (ej. capitalización promedio, bancos principales).

## Requisitos

Para ejecutar este script, necesitarás tener instalado Python (preferiblemente Python 3.x) y las siguientes bibliotecas. Puedes instalarlas usando pip:

```bash
pip install requests beautifulsoup4 pandas numpy sqlite3 # SQLite3 viene con Python, no necesita pip