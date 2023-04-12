print("Введите шестизначный номер билета")
array_string = input()

str = list(array_string)
count_array = len(str)
print(str)

s_first = 0
s_last = 0
for i in range(count_array):
    str[i] = int(str[i])
    if i <= 2:
        s_first = s_first + str[i]
    if i >= 3:
        s_last = s_last + str[i]

print(s_first)
print(s_last)

if s_first == s_last:
    print("Ваш билет счастливый")
else:
    print("Билет несчастливый")