# PySpark Transformations

The process of this directory is as follows:

1. The raw JSON data is loaded into a PySpark dataframe.
2. The data is transformed and cleaned using PySpark functions.
3. The resulting PySpark dataframe is written to `coins_data_gold` GCS bucket. Using the `transformations.py` script at dataproc
4. This `coins.csv` is a sample output of the transformation
