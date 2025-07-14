# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


import os
import zipfile
import pandas as pd

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```
    """

    os.makedirs("files/output", exist_ok=True)
    
    # Check if input directory exists, if not extract the zip file
    if not os.path.exists("files/input"):
        with zipfile.ZipFile("files/input.zip", "r") as zip_ref:
            zip_ref.extractall("files")
    
    # Process each dataset (train and test)
    for dataset_type in ["train", "test"]:
        data = []
        
        # Process each sentiment directory
        for sentiment in ["positive", "negative", "neutral"]:
            sentiment_dir = os.path.join("files/input", dataset_type, sentiment)
            
            # Process each file in the sentiment directory
            for filename in os.listdir(sentiment_dir):
                if filename.endswith(".txt"):
                    file_path = os.path.join(sentiment_dir, filename)
                    
                    # Read the phrase from the file
                    with open(file_path, "r", encoding="utf-8") as file:
                        phrase = file.read().strip()
                    
                    # Add to data list
                    data.append({
                        "phrase": phrase,
                        "target": sentiment
                    })
        
        # Create DataFrame and save to CSV
        df = pd.DataFrame(data)
        output_file = os.path.join("files/output", f"{dataset_type}_dataset.csv")
        df.to_csv(output_file, index=False)

    return