def float_converter(list):
    float_list=[]
    for item in list:
        try:
            float_item=float(item)
            float_list.append(float_item)
            print(f"{float_item} sumado correctamente")
        except ValueError:
            print(f"Elemento invalido: {item}")
    return float_list


def float_adder(list):
    float_sum=sum(list)
    print(f'Total de la suma: {float_sum}')


def main(list):
    try:
        my_floats=float_converter(list)
        float_adder(my_floats)
    except Exception:
        exit()


my_list=["Carlos","Pizza","19","18.65","20.5"]


main(my_list)