import numpy as np
from numpy.linalg import svd,matrix_rank

def array2eigan(a,size):
    flag = True
    compressed_channels = []
    for i in range(3):
        target_img = a[:,:,i]
        U,s,V = svd(target_img,full_matrices=False)
        if flag:
            print(f"the shape of U:{U.shape}")
            print(f"the shape of V:{V.shape}")
            flag = False

        # 特定の主成分だけを保持
        U_comp = U[:, :size]
        s_comp = np.diag(s[:size])
        V_comp = V[:size, :]

        # 近似された行列を取得
        compressed_channel = U_comp @ s_comp @ V_comp
        compressed_channels.append(compressed_channel)
    return compressed_channels,compressed_channel