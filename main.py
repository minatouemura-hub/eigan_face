import numpy as np
from numpy.linalg import svd , matrix_rank
from PIL import Image
import matplotlib.pyplot as plt
from util import array2eigan
from config import get_config


def main(config):
    num_components = config.components
    path = config.path
    img = Image.open(path)
    face_matrix = np.asarray(img)
    compressed,blue_channel = array2eigan(face_matrix,num_components)
    compressed = np.stack(compressed,axis=2)

    print(compressed.shape)

    compressed_image = np.clip(compressed, 0, 255).astype(np.uint8)
    blue_channel = np.clip(blue_channel,0,255).astype(np.uint8)
    compressed_image = Image.fromarray(compressed_image)
    blue_channel = Image.fromarray(blue_channel)


    # オリジナル画像と圧縮された画像の表示
    
    plt.subplot(1, 3, 1), plt.imshow(img), plt.title('Original Image')
    plt.xticks([]), plt.yticks([])  # 横軸と縦軸のメモリを非表示にする
    plt.subplot(1, 3, 2), plt.imshow(compressed_image), plt.title(f'Compressed Image (n={num_components})')
    plt.xticks([]), plt.yticks([])  # 横軸と縦軸のメモリを非表示にする
    plt.subplot(1, 3, 3), plt.imshow(blue_channel), plt.title("Blue_channel")
    plt.xticks([]), plt.yticks([])  
    plt.tight_layout()
    
    plt.show()
    
if __name__=="__main__":
    config,unparsed = get_config()
    main(config)