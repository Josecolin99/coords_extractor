# 📍 Extractor de Coordenadas para enlaces acortados de Google Maps (`maps.app.goo.gl`)

Este proyecto permite extraer automáticamente la **latitud y longitud** desde enlaces acortados de Google Maps, específicamente los que usan este formato:

```
https://maps.app.goo.gl/XXXXXXXXXXXX
```

Ejemplo real:

```
https://maps.app.goo.gl/4ha5CvTcSpXmSCLMA
```

Estos enlaces no contienen coordenadas directamente; redirigen a una página interna de Maps.  
Este script **abre el enlace, analiza el HTML real y extrae las coordenadas ocultas** desde la URL del `staticmap`.

---

## 🚀 ¿Cómo funciona?

### 1. Descargar el HTML del enlace acortado  
La función:

```python
def get_html_google_maps(url)
```

Obtiene el HTML final al que redirige Google Maps.

---

### 2. Buscar la URL “Static Map”
En el HTML hay una URL como:

```
https://maps.google.com/maps/api/staticmap?center=LAT,LNG
```

La función:

```python
def extract_staticmap_url(html)
```

La localiza usando expresiones regulares.

---

### 3. Extraer las coordenadas
La función:

```python
def coords_from_staticmap_text(text)
```

Extrae la latitud y longitud del parámetro `center`.

---

### 4. Función final
```python
def get_coords(url)
```

Retorna una tupla:

```
(latitud, longitud)
```

---

## 📦 Dependencias

- `requests`
- `re`
- `urllib.parse`

Instalación:

```bash
pip install requests
```

---

## 📌 Ejemplo de uso

```python
lat, lng = get_coords("https://maps.app.goo.gl/4ha5CvTcSpXmSCLMA")
print(lat, lng)
```

---

## ✔️ Ventajas

- Funciona con cualquier enlace acortado de Google Maps.
- No necesita API Key.
- 100% automático.
