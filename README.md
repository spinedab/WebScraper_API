# WebScraper_API

> **Estado: script de ejemplo / ejercicio (2024).** A pesar del nombre, este repositorio **no** expone una API: es un script básico que consume una página web y una API JSON de ejemplo, y guarda el resultado en SQLite y CSV. Sirve como punto de partida para aprender o adaptar, no como herramienta terminada.

## Contenido del repositorio

| Archivo | Descripción |
|---|---|
| `web_scraper.py` | Script (~2 KB) con funciones para descargar una página, consultar una API, combinar ambos resultados y guardarlos. |
| `LICENSE` | Licencia Apache 2.0. |
| `.gitignore` | Plantilla estándar de Python. |

No hay `requirements.txt`, pruebas, servidor HTTP ni argumentos de línea de comandos.

## Qué hace el script

1. `scrape_website(url)`: descarga la página con `requests` y extrae el texto de todos los `<h2>` con BeautifulSoup.
2. `get_api_data(api_url)`: hace un GET y devuelve el JSON.
3. `process_data()`: junta ambos resultados con una marca de tiempo.
4. `store_in_database()`: crea (si no existe) la tabla `scraped_data` en `scraped_data.db` (SQLite) e inserta una fila.
5. `export_to_csv()`: escribe esa misma fila en `scraped_data.csv`.

Las URL están fijas dentro de `main()`: `https://example.com` y `https://api.example.com/data`.

## Cómo probarlo

```bash
git clone https://github.com/spinedab/WebScraper_API.git
cd WebScraper_API
python3 -m venv .venv && source .venv/bin/activate
pip install requests beautifulsoup4
```

Edita `web_url` y `api_url` en `main()` y ejecuta:

```bash
python web_scraper.py
```

**Importante:** con los valores por defecto el script falla, porque `api.example.com` no resuelve (comprobado el 2026-10-22). Debes poner una API real o comentar esa llamada.

## Limitaciones conocidas

- Sin `timeout`, reintentos ni manejo de errores HTTP.
- Las listas y el JSON se guardan como texto (`str(...)`) en una sola fila, no como datos estructurados.
- Cada ejecución sobrescribe el CSV.
- No revisa `robots.txt` ni limita la frecuencia de peticiones.

## Ideas para extenderlo

- Recibir las URL y los selectores por argumentos (`argparse`) o archivo de configuración.
- Añadir `timeout`, reintentos con espera y registro de errores.
- Guardar una fila por elemento extraído, con columnas definidas.
- Añadir `requirements.txt` con versiones fijadas y pruebas con HTML de ejemplo guardado localmente.
- Si de verdad se necesita una API, exponer los datos con un servicio pequeño (por ejemplo FastAPI).

## Uso responsable

Extrae solo datos públicos que tengas derecho a usar, respetando los términos de servicio de cada sitio y su `robots.txt`. No uses este código para evadir protecciones ni para recolectar datos personales.

## Licencia

Apache License 2.0. Ver [`LICENSE`](LICENSE).

---

Autor: Santiago Pineda (DreamLabs Tech) · [LinkedIn](https://www.linkedin.com/in/santiago-pineda-149566424/) · dnework.col@gmail.com
