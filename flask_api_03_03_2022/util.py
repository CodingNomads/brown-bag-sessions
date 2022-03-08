import pandas as pd
import pathlib as pl
from flask_sqlalchemy import SQLAlchemy

def parse_exoplanets(csv_path: pl.Path) -> pd.DataFrame:
    """Reads data CSV and converts to pandas Dataframe"""
    df_planets = pd.read_csv(csv_path)[["pl_name","hostname","sy_snum","sy_pnum","discoverymethod","disc_year","disc_refname","disc_facility","pl_orbper","pl_rade","st_rad","sy_dist" ]]
    df_planets = df_planets.reset_index().rename(
        columns={
            "index":                   "id",
            "pl_name":                 "planet_name",
            "hostname":                "host_name",
            "sy_snum":                 "num_stars",
            "sy_pnum":                 "num_planets",
            "discoverymethod":         "method",
            "disc_year":               "year_discovered",
            "disc_refname":            "reference",
            "disc_facility":           "facility",
            "pl_orbper":               "orbital_period_d",
            "pl_rade":                 "earth_radius",
            "st_rad":                  "stellar_radius_sr",
            "sy_dist":                 "stellar_distance_pc",
        }
    )
    return df_planets

def insert_exoplanets(df_planets: pd.DataFrame, db: SQLAlchemy):
    df_planets.to_sql('exoplanets', db.engine, chunksize=512, if_exists="replace")
