import cv2
import numpy as np
from skimage import exposure
from utils import save_image
from utils import plot_images
from histogram_matching import plot_histograms

def match_histogram_with_masking(filename, sourcepath):
    source = cv2.cvtColor(cv2.imread(f'{sourcepath}{filename}'), cv2.COLOR_BGR2RGB) 
    mask_source = cv2.imread(f'masked_images/{filename}', cv2.IMREAD_GRAYSCALE) 
    ref = cv2.cvtColor(cv2.imread('sample_images/ref3.png'), cv2.COLOR_BGR2RGB)
    mask_ref = cv2.imread('masked_images/ref3-bw.png', cv2.IMREAD_GRAYSCALE) 

    # Mask source image
    coord_source = np.where(mask_source == 255) # store x,y locations with value 255 (white) to the tuple
    pixels_source_3d = np.array([source[coord_source]]) # Pick intensity values in these locations from source image

    # Mask ref image
    coord_ref = np.where(mask_ref == 255)
    pixels_ref_3d = np.array([ref[coord_ref]])

    # Histogram matching
    matching_pixels = exposure.match_histograms(pixels_source_3d, pixels_ref_3d, channel_axis = -1)

    # Store these enhanced values in those locations:
    result = source.copy()
    for i, C in enumerate(zip(coord_source[0], coord_source[1])): # zip() is pairing item in each list
        result[C[0], C[1]] = matching_pixels[0][i] 

    save_image(result, filename)
    #plot_images(source, ref, result)
    #plot_histograms(pixels_source_3d, pixels_ref_3d, matching_pixels)
    #input()
    #cv2.waitKey()

# Below code is an example how to execute this function for multiple images
#file_number = 1673 # starting file
#while (file_number <= 1673):
#    filename = f'000{file_number}_texture.png'
#    match_histogram_with_masking(filename, '../../../Unity Project/Avatar_Player/Assets/Resources/Avatar_Sequence/')
#    file_number += 1
