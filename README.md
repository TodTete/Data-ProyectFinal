
# 🚕 NYC Taxi Data Pipeline (AWS + Hadoop + Spark)

## 📌 Descripción

Este proyecto implementa un pipeline de datos completo basado en tecnologías de Big Data y servicios en la nube. Se procesan los datos del dataset **NYC Taxi Trip Records (2020–2025)** para generar análisis relevantes sobre viajes, tarifas y comportamiento temporal.

El flujo incluye ingestión, limpieza, almacenamiento distribuido, procesamiento y visualización.

---

## 🏗️ Arquitectura

```
S3 (raw data)
    ↓
AWS Lambda (limpieza automática)
    ↓
S3 (clean data)
    ↓
Hadoop HDFS (almacenamiento distribuido)
    ↓
Apache Spark (procesamiento)
    ↓
S3 (resultados)
    ↓
Streamlit (dashboard)
```

---

## ⚙️ Tecnologías utilizadas

* AWS S3
* AWS Lambda
* EC2
* Hadoop HDFS
* Apache Spark (PySpark)
* Python (Pandas, boto3)
* Streamlit

---

## 📂 Dataset

Fuente oficial:

NYC Taxi Trip Records
[https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

Periodo utilizado:

* Enero 2020 → Diciembre 2025

Formato:

* Archivos `.parquet`

---

## 🔄 Flujo del proyecto

### 1. Carga de datos

Los datos se almacenan en S3 con la siguiente estructura:

```
raw/
 ├── 2020/
 ├── 2021/
 ├── ...
 └── 2025/
```

---

### 2. Limpieza y transformación (AWS Lambda)

La función Lambda se activa automáticamente al subir archivos y realiza:

* Eliminación de valores nulos
* Eliminación de duplicados
* Filtrado de datos inválidos

Salida:

```
s3://bucket/clean_data/
```

---

### 3. Almacenamiento distribuido (Hadoop HDFS)

Los datos limpios se copian a HDFS:

```
/data/nyc_taxi/clean/
```

Esto permite trabajar en un entorno distribuido.

---

### 4. Procesamiento y análisis (Apache Spark)

Se realizan análisis como:

* Número de viajes por año
* Promedio de tarifas
* Ingresos totales
* Horas pico
* Distancia promedio

Ejemplo:

```python
df.groupBy("year").count().show()
```

---

### 5. Resultados

Los resultados se almacenan en S3:

```
s3://bucket/results/
```

Formato:

* Parquet (optimizado)
* CSV (para visualización)

---

### 6. Dashboard (Streamlit)

Se construye un dashboard interactivo que muestra:

* Total de viajes
* Viajes por año
* Tarifas promedio
* Distribución por hora

---

## 📊 Justificación de tecnologías

### AWS S3

Almacenamiento escalable y económico para grandes volúmenes de datos.

### AWS Lambda

Permite automatizar la limpieza de datos bajo un enfoque event-driven.

### Hadoop HDFS

Proporciona almacenamiento distribuido, simulando entornos reales de Big Data.

### Apache Spark

Motor de procesamiento distribuido eficiente para análisis a gran escala.

### Streamlit

Herramienta ligera para crear dashboards interactivos rápidamente.

---

## 🚀 Cómo ejecutar

### 1. Subir datos a S3

```bash
aws s3 cp ./raw s3://bucket/raw/ --recursive
```

### 2. Ejecutar pipeline

* Lambda se ejecuta automáticamente
* Copiar datos a HDFS:

```bash
hdfs dfs -put clean_data/* /data/nyc_taxi/clean/
```

### 3. Ejecutar Spark

```bash
pyspark
```

### 4. Ejecutar dashboard

```bash
streamlit run app.py
```

---

## 📈 Resultados esperados

* Identificación de tendencias por año
* Análisis de demanda por hora
* Estimación de ingresos
* Insights sobre comportamiento de viajes

---

## 📌 Autor
Ricardo Vallejo Sanchez
Proyecto desarrollado como solución de análisis de datos con arquitectura Big Data en la nube.



Solo indíquelo.
