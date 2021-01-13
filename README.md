# aws-lambda-docker-rasterio

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

AWS Lambda Container Image with Python Rasterio for querying Cloud Optimised GeoTiffs.

This repository contains an example AWS Lambda Docker image which uses Rasterio to query pixel values from a Cloud Optimised GeoTIFF (COG) stored in an S3 bucket. You can test the function locally using the Lambda Runtime Interface Emulator.

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [API](#api)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background

Previously Addresscloud built stripped-down Python packages to include Rasterio in AWS Lambda functions, using a script developed by Mapbox (see: https://github.com/mapbox/aws-lambda-python-packages). At re:Invent 2020 AWS launched support for custom container images to be executed as Lambda functions (see: https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/), making the use of Rasterio inside AWs Lambda's much easier and more accessible.


## Install

```sh
# Build the Docker image locally
docker build -t rasterio .
```

## Usage

The handler function reads the pixel values from a COG within a specificed polygon.

The Docker container includes the Lambda Runtime Interface Emulator so you can test the functions by running the images with Docker locally:

```sh
docker run -p 9000:8080 -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY rasterio:latest
```

Then in a separate terminal you can make calls to the service, specifying the raster file and area to query:

```sh
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations"\
    -d '{
            "raster": "s3://copernicus-dem-30m/Copernicus_DSM_COG_10_N55_00_W006_00_DEM/Copernicus_DSM_COG_10_N55_00_W006_00_DEM.tif",
            "geom": [
                {
                "type": "Polygon",
                "coordinates": [[[-5.2857375145,55.7018595345],[-5.2792572975,55.7018595345],[-5.2792572975,55.7052207941],[-5.2857375145,55.7052207941],[-5.2857375145,55.7018595345]]]
                }
            ]
        }'
```

This example queries elevation values from the [Copernicus DEM](Copernicus DEM is a Digital Surface Model).

## Maintainers

[@tomasholderness](https://github.com/tomasholderness)

## Contributing

PRs accepted.

Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © 2021 Addresscloud Limited
