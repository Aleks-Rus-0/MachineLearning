import numpy as np


def prod_non_zero_diag_vec(x):
    x_non_zero = np.diag(x)
    x_non_zero = x_non_zero[x_non_zero != 0]
    return x_non_zero.prod()


def are_multisets_equal_vec(x, y):
    x = np.sort(x)
    y = np.sort(y)
    return np.array_equal(x, y)


def max_after_zero_vec(x):
    mask = x == 0
    return np.max(x[1:][mask[:-1]])


def convert_image_np(img, coefs):
    arr = np.array([0.299, 0.587, 0.114])

    return np.dot(img, arr)


def run_length_encoding_np(x):
    x = np.array(x)
    mask_ = np.array(np.array(x - np.append(np.array(x[1:]), 0)) != 0)
    mask_[-1] = True

    ind = np.insert(np.where(mask_ == True), 0, -1)
    cnt = np.array(np.array(ind[1:]) - ind[:-1])

    return (x[mask_], cnt)

def pairwise_distance_np(x, y):
    x = np.array(x)
    y = np.array(y)
    res = x[:, np.newaxis, :] - y[np.newaxis, :, :]
    return np.sqrt(np.sum(res ** 2, axis=2))

