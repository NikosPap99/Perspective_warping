# Perspective_warping
 A script and a jupyter notebook presentation on image perspective wrapping, using perspective transform.

## Description

 Sometimes, an object may look different in an image from how it appears in real life. This mismatch is due to perspective distortion. Images of the same object captured from different camera distances and angles of view exhibit different perspective distortion.

 With perspective wrapping, you can adjust the perspective of a certain area of the image in order too see it from your perspective. In this presentation, an image of a newspaper laying on a sofa is used in order to exhibit the effects of the transform (granma.jpg).

 ## How to use

 The warp.py script can be run through the command "python warp.py input_image_name output_image_name", where input_image_name and output_image_name need to be replaced by the names of the input image and the output image respectively. In this case, you can use granma.jpg as input.

 Once the script shows you the window with the loaded image, you need to click 4 times, one for each edge of the area you wish to wrap. Try this process on the edges of the newspaper. Then the program will save the wrapped image for you.

 You can see an exaple of that in the .ipynb presentation.