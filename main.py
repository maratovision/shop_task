# username1 = "testusername123"
# password1 = "testpassword123"
#
# username = input("Введите имя: ")
# password = input("Введите пароль: ")
#
# def auth(username, password):
#     if username == username1 and password == password1 and not username.isalnum():
#         print('welcome')
#     else:
#         print("Неверное имя или пароль")
#
#
# auth(username, password)

catalogue = {'hot-dot':50,'hamburger':120,'shaurma':150,'naggets':130,'piza':930,
             'boso-lagman':250,'plov':190,'giro-lagman':240,'mantes':160,'rolls':600,
             'garnir':100,'grechka':70,'pelmeni':130,'french meat':400,'fish':500,
             't-bone':870,'Beijing duck':5000,'shashlyk assorti':50000
             }

def counter(money, price):
    if money < price:
        return "no money"
    else:
        result = money - price
        return  result

def choise(num_of_food):
    list1 = []
    for i in range(num_of_food):
        new_elem = input()
        if new_elem in catalogue:
            list1.append(new_elem)
    return list1

def order():
    money = 1000
    list1 = choise(3)
    for food in list1:
        price = catalogue[food]
        if money >= price:
            money = counter(money, price)
    print(money)
order()