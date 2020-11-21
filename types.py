# v = int(input('Введите число от 1 до 10: '))
# summ = 10 + v
# print(summ)

# print(float('1'))  # ???
# print(int(float('2.5')))  # ???
# print(bool(1))  # ???
# print(bool(''))  
# print(bool(0)) 

# counts = [3, 5, 7, 9, 10.5]
# print(counts)
# counts.append('Python')
# print(len(counts))
# print(counts)
# print(counts[0])
# print(counts[-1])
# print(counts[1:5])
# counts.remove('Python')
# print(counts)

# weather = {"city": "Москва", "temperature": "20"}
# print(weather["city"])
# weather["temperature"] = int(weather["temperature"]) - 5
# print(weather)
# print(weather.get("country"))
# print(weather.get("country", "Россия"))
# print(weather)
# weather["date"] = "21.11.2020"
# print(weather)
# print(len(weather))

def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    return f"{one}{delimiter}{two}"
print(get_summ("Learn", "Python").upper())