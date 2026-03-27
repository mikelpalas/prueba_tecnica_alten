import os
import requests

def test():
    print("prueba1")
    try:
        r = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=10)
        print(f" Recibidos {len(r.json())} registros.")
    except Exception as e:
        print(f"Error1")

    print("prueba2")
    cred_path = "credentials.json"
    if os.path.exists(cred_path):
        print(f"Archivo {cred_path} encontrado.")
    else:
        print(f"ERROR2")

if __name__ == "__main__":
    test()