def area(figure, data):
    if figure == "krok":
        print(data[0])
        res = 3.14*(data[0]**2)
    if figure == "kavadrat":
        a,b = data 
        res = a*b 
    if figure == "trokolnik":
        res = (a*b)/2
    return "plochad{}={}".format(figure, res)
figure = input("fegora")
data = [float(i)for i in input("dane cherez probel").split()]
print(area(figure, data))