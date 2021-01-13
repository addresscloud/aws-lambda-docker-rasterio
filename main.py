import json
import rasterio
from rasterio import features

def handler(event, context):
    """Accepts Lambda event and context object, returns raster values."""
    try:
        # Open raster
        src = rasterio.open(event["raster"])

        with rasterio.Env(CPL_CURL_VERBOSE=False, CPL_VSIL_CURL_ALLOWED_EXTENSIONS='.tif', \
        GDAL_DISABLE_READDIR_ON_OPEN='YES'):
            
            # Convert geometry to pixel coordinates
            window = features.geometry_window(src, event["geom"])
            
            # Read pixels in window
            pixels = src.read(window=window)

            # Return as JSON list
            return json.dumps(pixels.tolist())

    except Exception as err:
        return str(err)

