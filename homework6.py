my_dict = { 'Ivan' : 1997, 'Konstantin' : 2000, 'Anubis' : 1111}
print (my_dict)
print (my_dict ['Ivan'])
print (my_dict.get('Dmitry', 'Информация о пользователе отсутствует'))
my_dict.update({'Anastasya' : 2003,
                'Thomas' : 2007})
remote = my_dict.pop('Anubis')
print (remote)
print (my_dict)
##############################################
my_set = {2000, 2121, 2222 , 'Half', 'All',2000,2121,'All', True,True,False}
print(my_set)
my_set.update({3000,'very'})
my_set.remove(True)
print(my_set)