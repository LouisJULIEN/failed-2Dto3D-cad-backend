# small-2Dto3D-cad-backend
This backend makes 3D model from 2D projections.
2D projections are expected to be made up only of edges and points i.e. without any faces.  
Frontend is [small-2Dto3D-cad-frontend](https://github.com/LouisJULIEN/small-2Dto3D-cad-frontend), go there for screenshots.
# How to run it
### Run backend
Install dependencies
```
pip install -r requirements.txt
```
Run in local with hot reload and no CORS
```bash
APP_ENV=local python web.py
```
Run prod like
```bash
gunicorn --workers 4 --bind 127.0.0.1:8000 web:app
```
You can also build and run the docker (rquires docker installed)
```bash
docker build -t small_2Dto3D_cad_backend . && docker run -p 8000:8000 small_2Dto3D_cad_backend
```

### Run tests
All tests should be green
```bash
pytest
```

# What's next?
- Remove shapely which is a 2D only library which is not very helpful (and is misleading)
- Tests dandling points and edges
- Improve frontend UX (and UI thanks to external contributors)
- Maybe reconstruct faces directly from reconstructed edges (we can't have faces in projections)

# Contributing
Any PR is welcome, feel free to open one! It will be my pleasure to read it, comment it and merge it.

# Credits
Inspired by [Long Hoang's paper](https://api.intechopen.com/chapter/pdf-download/72385/4187482)
