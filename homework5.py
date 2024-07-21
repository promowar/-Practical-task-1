immutable_var = (1, 'Russia', 0.44, False)
print (immutable_var)
#immutable_var [1] = 'Poland'
print (immutable_var)
#При выполнении кода, консоль выдаст ошибку о том, что объект кортежа не поддерживает
#присвоение элементов, другими словами объекты кортежа являются не изменяемыми
mutable_list = [2, 'Germany', 0.55, True]
mutable_list [0] = 20
mutable_list [1] = 'Egypt'
mutable_list [2] = 1.88
mutable_list [3] = False
print (mutable_list)
