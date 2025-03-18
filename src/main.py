import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from pipeline.pipeline import ETLPipeline

if __name__ == "__main__":
    cities = ["São Paulo", "Rio de Janeiro", "Lisboa"]

    print("Iniciando o pipeline ETL...")
    
    pipeline = ETLPipeline(cities)
    result = pipeline.run()
    

    print("Pipeline concluído!")
    # print(f"Resultado: {result}")

