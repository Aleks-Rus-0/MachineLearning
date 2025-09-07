import math

def prod_non_zero_diag(x):
    ans = 1
    for i in range(len(x)):
        if x[i][i] != 0:
            ans *= x[i][i]
    return ans


def are_multisets_equal(x, y):
    if len(x) != len(y):
        return False

    x_ = list(x)
    y_ = list(y)

    x_.sort()
    y_.sort()

    for i in range(len(x)):
        if x_[i] != y_[i]:
            return False
    return True


def max_after_zero(x):
    ans = -1
    for i in range(1, len(x)):
        if x[i - 1] == 0:
            ans = max(ans, x[i])
    return ans


def convert_image(img, coefs):
    ans = [[0] * len(img[0]) for i in range(len(img))]
    for i in range(len(img)):
        for j in range(len(img[0])):
            ans[i][j] += img[i][j][0] * coefs[0] + img[i][j][1] * coefs[1] + img[i][j][2] * coefs[2]
    return ans


def run_length_encoding(x):
    ans = []
    ind = []
    cnt = 0
    for i in range(0, len(x) - 1):
        if x[i] != x[i + 1]:
            ans.append(x[i])
            ind.append(cnt)
            cnt = 1
        else:
            cnt += 1
    ans.append(x[-1])
    ind.append(cnt)

    return (ans, ind)


def pairwise_distance(x, y):
    ans = [[0] * len(y) for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(y)):
            for l in range(len(x[0])):
                ans[i][j] += (x[i][l] - y[j][l]) ** 2
            ans[i][j] = math.sqrt(ans[i][j])
    return ans

