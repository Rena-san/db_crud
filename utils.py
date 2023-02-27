from random import randint


class Utils:

    @staticmethod
    def some_random_id(num):
        id_list = ''
        for i in range(num):
            if i % 10 == i // 10 and i != 0:
                id_list = id_list + str(i) + "," + " "
        return id_list[:-2]

    @staticmethod
    def get_list_id(list_of_dict):
        list_id = []
        str_id = ''
        for i in list_of_dict:
            list_id.append(i['id'])
        for i in list_id:
            str_id = str_id + str(i) + "," + " "
        return str_id

    @staticmethod
    def random_id(num):
        random_index = randint(0, num - 1)
        return str(random_index)

    @staticmethod
    def from_list_to_str(lis):
        s = ''
        for i in lis:
            s = s + str(i) + ", "
        return s[:-2]
