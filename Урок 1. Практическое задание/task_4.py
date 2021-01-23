"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

# сложность алгоритма O(n) - линейная.

def f_chk_user(username_chk_tmp, userpassw_chk_tmp):
    for userdict_tmp in users_bd:
        pass_chck = None
        username_tmp = userdict_tmp.get("username")
        userpassw_tmp = userdict_tmp.get("userpassw")
        useractiv_tmp = userdict_tmp.get("useractive")
        #       print(f"{username_tmp}|{userpassw_tmp}|{useractiv_tmp}")
        if username_chk_tmp == username_tmp and userpassw_chk_tmp == userpassw_tmp and useractiv_tmp == True:
            pass_chck = "active_ok"  # все проверки успешны
            break
        elif username_chk_tmp == username_tmp and userpassw_chk_tmp == userpassw_tmp and useractiv_tmp == False:
            pass_chck = "active_false"  # логин / пароль верны, учетка неактивна
            break
        elif username_chk_tmp == username_tmp and userpassw_chk_tmp != userpassw_tmp:
            pass_chck = "passw_false"  # логин / пароль неверны, учетка неактивна
            break
        else:
            pass_chck = "new_user"
    return pass_chck

def f_activateuser(username_act, userpassw_act):
    active_chk=int(input("Для активации введите ответ на вопрос. Сколько будет 2^3 ?"))
    if active_chk==8:
        i=0 # индекс по списку
        for userdict_tmp in users_bd:
            username_tmp = userdict_tmp.get("username")
            userpassw_tmp = userdict_tmp.get("userpassw")
            useractiv_tmp = userdict_tmp.get("useractive")
            if username_tmp==username_act and userpassw_tmp==userpassw_act:
                users_bd[i]={"username": username_tmp, "userpassw": userpassw_tmp, "useractive": True}
                active_chk='active_ok'
                break
            else:
                i+=1
    else:
        active_chk = 'active_nok'
    return active_chk

def f_newuser(username_tmp, userpassw_tmp):
    users_bd.append({"username": username_tmp, "userpassw": userpassw_tmp, "useractive": True})
    print("Активация нового пользователя успешная.")
    return


# словарь с данными по пользователяи
users_bd = [
    {"username": "user1", "userpassw": "pas1", "useractive": True},
    {"username": "user2", "userpassw": "pas2", "useractive": False},
    {"username": "user3", "userpassw": "pas3", "useractive": True},
    {"username": "admin", "userpassw": "pas5", "useractive": True}
]
print("Для доступа к ресурсу необходимо иметь активированную учетную запись. Введите имя пользователя и пароль "
      "в запросах ниже.")

v_user = None
v_passw = None
while v_user is None:
    v_user = str(input("имя пользователя >>>")).lower()
    v_passw = str(input("пароль >>>"))
    if v_user == '' or len(v_user) < 5 or len(v_user) > 8:
        print("Имя пользователя не может быть пустым и должно иметь длину от 5 до 8 символов")
        v_user = None
    else:
        userchk = f_chk_user(v_user, v_passw)
#        print(userchk)
        if userchk == "active_ok": # логин/пароль совпадают, учетка активная
            print("Доступ разрешен")
            break
        elif userchk == "active_false": # логин/пароль совпадают, учетка неактивная
            print("Учетная запись не активирована. Необходимо подтвердить активацию...")
            v_acive_chk=f_activateuser(v_user, v_passw)
            if v_acive_chk=="active_ok":
                print("Учетная запись активирована.")
                break
            else:
                print("Учетная запись не активирована.")
                break
        elif userchk == "passw_false":  # логин верный, пароль неверный
            print("Пароль неверный. Доступ запрещен")
            break
        elif userchk == "new_user":
            newuser = input("Учетная запись не найдена. Создать новую [y/n] ?").lower()
            if newuser=="y":
                f_newuser(v_user, v_passw)

print("проверка что в БД")
for userdict_tmp in users_bd:
    print("логин: ", userdict_tmp)