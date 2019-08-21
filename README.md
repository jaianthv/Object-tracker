# Object-tracker
Tracks a user defined object and plots how much it moved from the initial position 

X-ray photoemission electron microscopy is a technique where one can acquire spatially resolved absorption process. Most of the XPEEM microscopes are used in a synchrotron facility and it requires adequate amount of training to handle the microcope, which make it difficult for users to independently handle the microscope. Aligning the position or the tilt of the sample inside the microscope is an important step to acquire a good quality image, which users find it hard to perform by themselves. One of the hardship involved in correcting the sample tilt is the inability to navigate the movement of the marker while toggling the objective lens. This code can be one solution to navigate the marker as well as track its movement from the initial position. The objective during a tilt correction is to minimize the amplitude of the movement such that object is not moving in the X-Y plane but towards the Z-plane. 

Following video is a description on how this code works. In Image_detection.Py one can define the marker (imaged by a camera) that needs to be traced before toggling the lens. After defining the region with a square box, the box follows the movement of the marker and reads the coordinate. Then, Plot.py code extracts the coordinate and calculates the center of the box, which will be plotted in the graph simultaneously as the marker moves. If the marker is in the same position the X-Y axis appear red with text "X-OK" and "Y-OK".

This code needs to be customized according to the beamline, the ultimate objective is to use this code to automize the tilt correction process with the need of users/experts.

<IMG SRC="test_gif.gif" height="500" width="900"><br>
