import awswrangler as wr
import os
def lambda_handler(event, context):
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        input_path = f"s3://{bucket}/{key}"
        output_path = f"s3://{bucket}/{key.replace('raw/', 'clean_data/')}"
        
        # Leemos sin parámetros extra para evitar TypeErrors
        df = wr.s3.read_parquet(path=input_path)
        
        # Limpieza mínima
        df_clean = df.dropna(subset=["tpep_pickup_datetime", "fare_amount"])
        
        # Guardamos
        wr.s3.to_parquet(df=df_clean, path=output_path, index=False)
        
        return {
            "statusCode": 200,
            "body": f"EXITO: Procesado {key} y guardado en clean_data"
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "error_final": str(e)
        }
