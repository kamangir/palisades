import osmnx as ox
import geopandas as gpd
import rasterio
from rasterio.features import geometry_mask
from shapely.geometry import shape
import numpy as np
from typing import Tuple, List


# Step 1: Download OSM Building Footprints
def get_building_footprints(
    bbox: Tuple[float, float, float, float]
) -> gpd.GeoDataFrame:
    # bbox: (min_lat, min_lon, max_lat, max_lon)
    buildings = ox.features_from_bbox(
        north=bbox[2],
        south=bbox[0],
        east=bbox[3],
        west=bbox[1],
        tags={"building": True},
    )
    return buildings[buildings.geometry.notnull()].reset_index()


# Step 2: Load Fire Damage Assessment Layer
def load_fire_damage_layer(
    geoimage_path: str,
) -> Tuple[
    np.ndarray, rasterio.Affine, rasterio.crs.CRS, Tuple[float, float, float, float]
]:
    with rasterio.open(geoimage_path) as src:
        damage_layer = src.read(1)  # Assuming single-band raster with values 0-1
        affine = src.transform
        crs = src.crs
        bounds = src.bounds
        bbox = (
            bounds.bottom,
            bounds.left,
            bounds.top,
            bounds.right,
        )  # Convert to (min_lat, min_lon, max_lat, max_lon)
        return damage_layer, affine, crs, bbox


# Step 3: Overlay Building Footprints and Assess Damage
def assess_damage(
    buildings: gpd.GeoDataFrame, damage_layer: np.ndarray, affine: rasterio.Affine
) -> gpd.GeoDataFrame:
    results = []

    for _, row in buildings.iterrows():
        geom = row.geometry
        mask = geometry_mask(
            [geom], transform=affine, invert=True, out_shape=damage_layer.shape
        )

        # Calculate damage within the footprint
        affected_area = np.sum(damage_layer[mask])
        total_area = np.sum(mask)

        damage_percentage = (affected_area / total_area) * 100 if total_area > 0 else 0
        results.append({"id": row["osmid"], "damage_percentage": damage_percentage})

    return gpd.GeoDataFrame(results)


# Step 4: Save Results as GeoJSON
def save_damage_gdf(damage_gdf: gpd.GeoDataFrame, crs: str, output_path: str) -> None:
    damage_gdf.set_crs(crs, inplace=True)
    damage_gdf.to_file(output_path, driver="GeoJSON")


# Step 5: Visualize Results
def visualize_results(
    buildings: gpd.GeoDataFrame, damage_gdf: gpd.GeoDataFrame
) -> None:
    merged = buildings.merge(damage_gdf, left_on="osmid", right_on="id")
    merged.plot(column="damage_percentage", cmap="Reds", legend=True)
