import cv2
import matplotlib.pyplot as plt

def plot_images(source, ref, result):
    fig1, axes = plt.subplots(nrows=1, ncols=3, figsize=(8, 3), sharex=True, sharey=True)
    axes[0].set_title('SOURCE')
    axes[0].imshow(source)
    axes[0].set_axis_off()
    axes[1].set_title('REFERENCE')
    axes[1].imshow(ref)
    axes[1].set_axis_off()
    axes[2].set_title('RESULT')
    axes[2].imshow(result)
    axes[2].set_axis_off()
    fig1.tight_layout()
    fig1.show()

def save_image(result, filename):
    is_success = cv2.imwrite(f'output_images/{filename}', cv2.cvtColor(result, cv2.COLOR_RGB2BGR))
    if is_success == True:
        print(f'{filename}, saved successfully')
    else:
        print(f'{filename}, error in saving file')