Preprocess API
======================
Process images, apply filters, rotate, zoom, etc.

System requirements
-------------------
- Python >= 3.6

Installation
------------

```bash
$ sudo mkdir /var/log/fksolutions  # creates fksolutions logging folder
$ sudo chown $USER:$USER /var/log/fksolutions  # give fksolutions logging folder group permissions
$ pip install -e .
```

Usage
-----
```bash
$ preprocess  # run API
```
Read REST API documentation through ``/docs`` endpoint for API usage.