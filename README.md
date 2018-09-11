# eeswebgl
EES accident reconstruction method based on web.py and webGL

# Introduction

This project is a demonstration of a simple integration of web.py and webGL. The app calculates the pre-impact phase (velocities, impact angles etc.) for a collision of two vehicles based on data given in the input form according to the EES (Energy Equivalent Speed) Reconstruction Method. It also animates the post-impact phase according to impact and rest positions, rotation and heading angles of the vehicles. The animation is by no means a real physical representation of the post-impact motion of the vehicles and is not a part of the original EES method.

Predefined input data and the pictures of the input parameters are from:

H.-H. Schreier and W. D. Nelson: "Applicability of the EES-Accident Reconstruction Method with MacCAR", SAE Transactions, Vol. 96, Section 1 (1987), pp. 152-174,

while the algorithms of the EES method can be found in:

F. Zeidler et al.: "Accident Research and Accident Reconstruction by the EES-Accident Reconstruction Method," SAE Technical Paper 850256, 1985.

# Prerequisites

web.py is needed. You can install it, e.g., via pip:

  pip install web.py

# Installation

The app can be run as a script in Python, e.g.:

  python EESWebGL.py

which starts the web.py server on port 8080.

To access the input page of the app open your browser and go to [http://localhost:8080/](http://localhost:8080/).

In qpython (on android systems) you can launch the app via the 'launch.py' script. You have to set the paths both in the launch script and in 'EESWebGL.py' for running the app.

# Using the app

You can do a calculation with the predefined input data (or you can use data according to your own cases) by clicking on the "Calculate" button. The results of the calculation are shown on a new page on the right side of the screen, while on the left you can run an animation of the post-impact phase. The buttons of the animation are pretty self-explanatory.

# Possible issues

The animation code is tested only with head-on collisions. For other types some addition to the code is probably needed.

# License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
