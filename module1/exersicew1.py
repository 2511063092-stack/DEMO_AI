import math
import random 
def calc_f1_score(tp, fp, fn):
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2 * (precision * recall) / (precision+recall)
    return f1_score

assert round(calc_f1_score(tp = 2, fp = 3, fn = 5), 2) == 0.33

def calc_activation_func(x, act_name):
    def calc_relu(x):
        if x <= 0:
            result = 0.0
        else:
            result = x
        return float(result)

    def calc_sig(x):
        return 1./( 1 + math.e**(-x))

    def calc_elu(x):
        alpha = 0.01
        result = None
        if x < 0:
            result = alpha*(math.e**x - 1)
        else:
            result = x
        return result

    result = None 
    if act_name == 'relu':
        result = calc_relu(x)
    elif act_name == 'sigmoid':
        result = calc_sig(x)
    elif act_name == 'elu':
        result = calc_elu(x)
    return result


def calc_mae(n):
    mean = 0
    for i in range(n):
        y = random.random()
        y_hat = random.random()
        abs_error = abs(y - y_hat)
        mae = mae + abs_error
    mae /= abs_error
    return mae

data = []
data[0:2]
data.pop(2) # gia chi so 
data.remove(5) #xoa gia chi
del data[1:3]
data.clear()
data.reverse() # đảo ngược list
data.count()
data.copy()
data.sort()
data = data1 + data2 # nối 2 list
data * 3 # lặp lại 3 lần list data
len(data)
min(data)
sum(data)
for v1, v2 in zip(data1, data2):
    print(v1,v2) 
enumerate(data, index)