# failed-2Dto3D-cad-backend
The goal is to make a 3D model from 2D projections. It currently works only for a square.
Vertices and edges are reconstructed, not faces and solids.
This project is stopped.
Frontend is failed-2Dto3D-cad-frontend, go there for screenshots.

# Why stop?
The hypothesis is that a 3D model can be recreated from a projection from each 3 sides. I still think it is possible but the endeavour is too great. 
Too many issues were raised, mostly because it's too hard to code the "I guess it is like that behind" part.

Vertices and edges can easily hide each other in 2D projection (e.g. a square). We suppose here that the 2D projections are transparent to avoid having faces hiding vertices and edges. 

Intentionally hidden vertices and edges are not managed (think of a 3D U shape).
Faces and multiple shapes are not managed.

# Why make repository public?
To be used as a source of inspiration : front is fine and data structure is ok.
To be used as a source of information : it's damn hard to make it work

# Conclusion
A machine learning approach seems more pertinent as it will naturally embed the 'I guess' part. 
