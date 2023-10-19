import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure, data, color
from utils import plot_images, save_image

def plot_histograms(source, ref, result):
    fig2, axes = plt.subplots(nrows=4, ncols=3, figsize=(8, 8))

    for i, img in enumerate((source, ref, result)):
        for c, c_color in enumerate(('red', 'green', 'blue')):
            # plot histogram
            img_hist, bins = exposure.histogram(img[..., c], source_range='dtype')
            axes[c+1, i].plot(bins, img_hist) # y axis / img_hist.max()
            img_cdf, bins = exposure.cumulative_distribution(img[..., c])
            #plot cdf
            axes[c+1, i].plot(bins, img_cdf * img_hist.max())
            #color label
            axes[c+1, 0].set_ylabel(c_color)

    axes[0, 0].set_title('SOURCE')
    axes[0, 0].imshow(source)
    axes[0, 0].set_axis_off()
    axes[0, 1].set_title('REFERENCE')
    axes[0, 1].imshow(ref)
    axes[0, 1].set_axis_off()
    axes[0, 2].set_title('RESULT')
    axes[0, 2].imshow(result)
    axes[0, 2].set_axis_off()
    fig2.tight_layout()
    fig2.show()

def match_histogram(filename, sourcepath, refpath, plotgraph=False, saveresult=True):
    source = cv2.cvtColor(cv2.imread(sourcepath), cv2.COLOR_BGR2RGB)
    ref = cv2.cvtColor(cv2.imread(refpath), cv2.COLOR_BGR2RGB)
    
    result = exposure.match_histograms(source, ref, channel_axis=-1)

    if (plotgraph):
        plot_images(source, ref, result)
        plot_histograms(source, ref, result)

    if (saveresult):
        save_image(result, filename)

