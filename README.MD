# ETL Project: Weather Data

Este repositório contém um projeto de ETL (Extract, Transform, Load) para coleta, transformação e carregamento de dados meteorológicos. O objetivo é processar dados climáticos de diferentes fontes e armazená-los para análise.

## Estrutura do Projeto

- **`/data`**: Contém os arquivos de entrada e saída de dados.
- **`/scripts`**: Scripts Python para as etapas de ETL.
- **`/docs`**: Documentação adicional do projeto.

## Funcionalidades

1. **Extração**: Coleta de dados meteorológicos de APIs ou arquivos CSV.
2. **Transformação**: Limpeza e formatação dos dados.
3. **Carregamento**: Armazenamento dos dados processados em um banco de dados ou arquivo.

## Requisitos

- Python 3.8+
- Bibliotecas: `pandas`, `requests`, `sqlalchemy`, `dotenv`, `pyarrow`


## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/etl_project_weather.git
    ```
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3. Crie o arquivo para o dotenv
    ```
    Crie um arquivo .env
    Exemplo:
    api_key="22222222222222222222222222222222"
    base_url="https://api.openweathermap.org/data/2.5/weather?"

    ```    
4. Execute o pipeline ETL:
    ```bash
    python scripts/etl_pipeline.py
    ```

