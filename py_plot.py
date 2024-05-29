import matplotlib.pyplot as plt
ref_id = {}
def get_key_many(x, value):
    q = []
    for k, v in x.items():
        if v == value:
            q.append(k)
    return q
def plot(tags):
    with open('ref_id.txt') as file:
        for line in file:
            key, *value = line.split()
            ref_id[key] = value[0]
    x_list = list(range(len(tags)))
    print(x_list)
    y1_list = [len(get_key_many(ref_id, 'mamochka_ryadom')), 0, 0, 0]
    y = []
    for i in range(len(x_list)):
        y_list = [0] * len(x_list)
        y_list[i] = len(get_key_many(ref_id, tags[i]))
        y.append(y_list)
    for i in range(len(x_list)):
        plt.bar(x_list, y[i], label=tags[i])
    plt.legend()
    plt.savefig('marketing.png')
    plt.clf()
    plt.close()