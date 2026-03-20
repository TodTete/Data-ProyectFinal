from pyspark.sql.functions import year, month, hour, col, avg, count

# 1. Preparar el DataFrame con columnas de tiempo
# (Asegúrate de que el nombre de la columna sea exacto, a veces es 'tpep_pickup_datetime')
df_final = df.withColumn("year", year(col("tpep_pickup_datetime"))) \
             .withColumn("hour", hour(col("tpep_pickup_datetime")))

# 2. KPI 1: Viajes por año (Lo que verás en una gráfica de barras)
viajes_anio = df_final.groupBy("year").count().orderBy("year")
viajes_anio.show()

# 3. KPI 2: Tarifa promedio por año (Para ver la inflación del taxi)
tarifa_anio = df_final.groupBy("year").agg(avg("fare_amount").alias("avg_fare")).orderBy("year")
tarifa_anio.show()

