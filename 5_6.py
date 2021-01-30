if __name__ == '__main__':
    import re
    my_dict = []
    result = 0
    my_list = []
    with open('text_2.txt','r+', encoding ='utf - 8') as f_obj:
        for line in f_obj:
            result = 0
            my_list = re.findall(r'\d+',line)
            for el in my_list:
                result = result + int(el)
            my_dict.append({line.split(':')[0]: result})
        print(my_dict)