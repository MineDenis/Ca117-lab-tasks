def build_dictionary(file):
    dic = {}
    with open(file) as fd:
        for lines in fd:
            tokens = lines.strip().split()
            dic[tokens[0]] = tokens[1]
    return dic
def extract_range(d, low, high):
    new_dic = {}
    for k, v in d.items():
        if int(v) >= low and high >= int(v):
            new_dic[k] = v
    return new_dic
