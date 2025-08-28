# Taller 2.2
# Concurrencia
# Especialización en Analítica y Ciencia de Datos
# Universidad de Antioquia


### 📁 Archivos del Proyecto
- `asyncio_urls.py` - Implementación usando programación asíncrona con asyncio
- `threading_urls.py` - Implementación usando threading con ThreadPoolExecutor
- `multiprocessing_urls.py` - Implementación usando multiprocesamiento

## 🎯 Objetivo

Comparar el rendimiento y comportamiento de tres paradigmas de concurrencia en Python:

1. **Asyncio**: Programación asíncrona con corrutinas
2. **Threading**: Hilos de ejecución paralelos
3. **Multiprocessing**: Procesos separados


### Ejecución

Ejecuta cada script individualmente para ver los resultados:

```bash
# Asyncio
python asyncio_urls.py

# Threading
python threading_urls.py

# Multiprocessing
python multiprocessing_urls.py
```

## 📊 Dataset

Todos los scripts utilizan el mismo conjunto de 8 URLs que incluyen:
- 5 imágenes de Unsplash (800px de ancho)
- 3 archivos PDF de prueba

El dataset se multiplica por 80 para un total de 640 descargas por ejecución.
