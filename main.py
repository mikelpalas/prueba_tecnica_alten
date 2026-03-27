import os
import requests
import pandas as pd
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

print("DEBUG 1")

class APIClient:

    def __init__(self, url):
        self.url = url

    def fetch_data(self, limit=100):
        response = requests.get(self.url)

        if response.status_code != 200:
            raise Exception("Error")

        data = response.json()

        return data[:limit]


class BigQueryUploader:

    def __init__(self, project_id, dataset_id, table_id):
        self.client = bigquery.Client(project=project_id)
        self.dataset_id = dataset_id
        self.table_id = table_id

    def upload_data(self, data):

        df = pd.DataFrame(data)
        table_ref = f"{self.client.project}.{self.dataset_id}.{self.table_id}"
        job = self.client.load_table_from_dataframe(df, table_ref)

        job.result()

        print(f"Datos cargados en {table_ref}")


def main():

    api_url = "https://jsonplaceholder.typicode.com/posts"

    project_id = "prueba-tecnica-alten"
    dataset_id = "SANDBOX_prueba_tecnica"
    table_id = "upload_prueba_tecnica"

    api_client = APIClient(api_url)

    print("Descargando datos de la API")
    data = api_client.fetch_data()

    uploader = BigQueryUploader(project_id, dataset_id, table_id)

    print("Subiendo datos a BigQuery")
    uploader.upload_data(data)


if __name__ == "__main__":
    main()