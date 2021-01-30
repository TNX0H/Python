if __name__ == '__main__':
    import json
    cont = 0
    total_rev = 0
    average_rev = 0
    dict_firm = dict()
    dict_average = dict()
    my_list = []
    with open('text_2.txt', 'r+', encoding= ' utf - 8') as f_obj:
        for line in f_obj:
            firm_name = line.split(' ')[0]
            revenue = int(line.split(' ')[2]) - int(line.split(' ')[3])
            if revenue > 0:
                total_rev += revenue
                cont += 1
            average_rev = total_rev / cont
            dict_firm.update({firm_name:revenue})
        dict_average.update({'average_rev':average_rev})
    my_list.append(dict_firm)
    my_list.append(dict_average)
    print(my_list)
    my_json = json.dumps(my_list)
    with open('my.json', 'w') as j_obj:
        json.dump(my_list, j_obj)
