import pandas
import os.path
from datetime import datetime

timestamp = datetime.timestamp(datetime.now())
dt_object = datetime.fromtimestamp(timestamp).strftime('%d_%m_%y_%H_%M_%S')
filename = "files/file_output_"+dt_object+".xlsx"
file_out = pandas.DataFrame({"id": [],"amount": []})
file_out.to_excel(filename)
arr_pos = []
arr_neg = []
while True:
    usr_input = input("1 - Ввести файл, который нужно сложить\n2 - Ввести файл, который нужно отнять\n3 - Поехали! ")
    if usr_input == "1":
        pos_input = input("Название файла: ")
        if os.path.isfile('files/'+pos_input):
            arr_pos.append(pos_input)
        else:
            print("Неправильное название файла")
    elif usr_input == "2":
        neg_input = input("Название файлов: ")
        if os.path.isfile('files/'+neg_input):
            arr_neg.append(neg_input)
        else:
            print("Неправильное название файла")
    elif usr_input == "3":
        break
    else:
        print("По-нормальному введи!")
print(arr_pos)
print(arr_neg)

for pmt in arr_pos:
    file1 = pandas.read_excel("files/"+pmt, sheet_name=0)
    file_out = pandas.merge(file_out, file1, on=('id'), how ='outer')
    file_out["amount"] = file_out[["amount_x", "amount_y"]].sum(axis = 1, skipna = True)
    file_out = file_out.drop(["amount_x", "amount_y"], axis = 1)
for pmt in arr_neg:
    file1 = pandas.read_excel("files/"+pmt, sheet_name=0)
    file_out = pandas.merge(file_out, file1, on=('id'), how ='outer')
    file_out["amount_y"] *= -1
    file_out["amount"] = file_out[["amount_x", "amount_y"]].sum(axis = 1, skipna = True)
    file_out = file_out.drop(["amount_x", "amount_y"], axis = 1)
file_out.to_excel(filename)
print(file_out)
