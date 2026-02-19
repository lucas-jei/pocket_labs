import sys

from calc import Calc
from calc import Make_Array


a = Calc(5, 2)
b = Calc(9, 1)

print(f"a value=>{a.set_number_1}")
print(f"b value=>{b.set_number_1}")


name_1 = "aplle_페이스_1"
name_2 = name_1.replace("페이스", "face")

print(f"old={name_1} new={name_2}")

print_num = 1


for k in range(1, 11):

    print(f"img_{print_num:02}")
    var_1 = f"test_{k:03}"
    print(f"var_1={var_1}")
    print_num+=1







sys.exit()

print(f"a.number_1=>{a.set_number_1}, a.number_2=>{a.set_number_2}")
print(f"b.number_1=>{b.set_number_1}, b.number_2=>{b.set_number_2}")

a.set_number_1 = 9

add_result_1 = a.add_number()
add_result_2 = b.add_number()

print(f"add_result_1={add_result_1}")
print(f"add_result_1={add_result_2}")

c = Make_Array()
c.push_array(9, 10, 20, 21)
print(f"push_array={c.result_array}")
c.pull_array(9, 20)
print(f"pull_array={c.result_array}")

print(f"c.make_new=>{c.make_new()}")




