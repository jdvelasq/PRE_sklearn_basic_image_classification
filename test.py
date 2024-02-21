"""GitHub Classroom autograding script."""

import os

#
# Retorna error si la carpeta output/ no existe
if not os.path.exists("forecasts.csv"):
    raise Exception("File 'forecasts.csv' not found")
