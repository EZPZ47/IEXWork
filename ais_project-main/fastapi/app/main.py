from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, Table, Column, select, func
from geoalchemy2 import Geography

app = FastAPI()

engine = create_engine(
    "postgresql+psycopg2://aisuser:aispass@localhost:5432/mydatabase"
)

metadata = MetaData()
ais = Table(
    "ais_raw",
    metadata,
    Column("geom", Geography(geometry_type="POINT", srid=4326)),
    autoload_with=engine,
    keep_existing=True,
)

@app.get("/mmsi/{mmsi_value}")
async def fetch_by_mmsi(mmsi_value: int):
    # push the geom conversion into the SQL so you get a string
    stmt = select(
        *(c for c in ais.c if c.name != "geom"),               # all non-geom columns
        func.ST_AsGeoJSON(ais.c.geom).label("geom_geojson"),  # JSON-friendly geometry
    ).where(ais.c.mmsi == mmsi_value)

    with engine.connect() as conn:
        rows = conn.execute(stmt).mappings().all()
        return rows
