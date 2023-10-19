# histogram-matching

This repository contains few example of histogram matching which is implemented in Python.

There are 3 main files:

1) [histogram-matching.py](https://github.com/VRSYS-NPR4VR/histogram-matching/blob/main/histogram_matching.py) - By providing the path of source image and reference image to match_histogram() function, you will be able to perform histogram matching on global level of image and save it as the result. Histogram chart will also displays at the end of function.

2) [histogram_matching_v2.py](https://github.com/VRSYS-NPR4VR/histogram-matching/blob/main/histogram_matching_v2.py) - This is another histogram matching implementation, similar to above file. However, there is masking mechanism added here which can be focus only specific part of image. Masked image need to be provided to the function.

3) [masking.ipynb](https://github.com/VRSYS-NPR4VR/histogram-matching/blob/main/masking.ipynb) - This is an example script that we extract specific part from orginal image and produce the masking image as the result. There is an example code how to executed masking function in the file itself.

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [Jupyter Notebook](https://jupyter.org/install)
- [Scikit-Image](https://scikit-image.org/docs/stable/install.html)
- [OpenCV](https://opencv.org/releases/)
