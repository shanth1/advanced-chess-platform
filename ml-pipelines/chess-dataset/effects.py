from PIL import Image
import numpy as np

def add_noise(image):
    noise = np.random.normal(0, 10, (image.size[1], image.size[0], 3)).astype('uint8')
    noisy_image = Image.fromarray(np.clip(np.array(image) + noise, 0, 255).astype('uint8'))
    return noisy_image
