workers_base = {}
print("СТВОРЮЄМО БІБЛІОТЕКУ З ВІДОМОСТЯМИ ПРО ПРАЦІВНИКІВ")
while True:
    def name_type():
        a = input("Будь-ласка, введіть дані: ")
        if all(x.isalpha() for x in a.split()):
            return a
        else:
            print("Вводити треба тільки літери!")
            return name_type()

    def number_type():
        a = input("Будь-ласка, введіть дані: ")
        if all(x.isdigit() for x in a.split()):
            return int(a)
        else:
            print("Вводити треба тільки числа!")
            return number_type()

    print("Введіть знизу ім'я працівника (EXIT замість імені для виходу):")
    name = name_type()
    if name == "EXIT":
        print("Створення бази даних завершено")
        break
    print("Введіть знизу позицію працівника: ")
    pos = name_type()
    print("Введіть знизу досвід роботи в роках: ")
    exp = number_type()
    portfolio = input("Введіть знизу портфоліо працівника: ")
    print("Введіть знизу коефіціент ефективності працівника: ")
    effic_k = number_type()
    tech_stack = input("Введіть стек технологій працівника: ")
    print("Введіть знизу зарплату в нац. валюті: ")
    salary = number_type()

    workers_base[name] = {
        "Позиція": pos,
        "Досвід": exp,
        "Портфоліо": portfolio,
        "Коефіціент ефективності": effic_k,
        "Стек технологій": tech_stack,
        "Зарплата": salary
    }

print(workers_base)

print("""1 - видалити працівника   2 - редагувати інформацію по працівнику"
         3 - сортування за прізвищем     4 - сортування за ефективністю працівника""")

def type():
    a = input("Введіть бажану дію: ")
    match a:
        case "1" | "2" | "3" | "4":
            return a
        case _:
            print("Вводити можна тільки 1, 2, 3 або 4. Спробуйте ще!")
            return type()

choice = type()

match choice:
    case "1":
        worker_to_del = input("Введіть працівника, якого хочете видалити: ")
        if worker_to_del not in workers_base.keys():
            print("Такого працівника в бібліотеці не існує")
        else:
            del workers_base[worker_to_del]
            print(f"Інформація про {worker_to_del} була успішно видалена")
            print(workers_base)
    case "2":
        worker_for_change = input("Введіть працівника, інформацію про якого треба змінити: ")
        if worker_for_change not in workers_base.keys():
            print("Такого працівника не знайдено")
        else:
            field = input("Введіть ключове поле, в якому треба внести зміни:")
            if field not in workers_base[worker_for_change]:
                print("Такого поля не існуює")
            else:
                workers_base[worker_for_change][field] = input("Введіть змінену інформацію: ")
                print(workers_base)
    case "3":
        print("Бібліотека, відсортована за прізвіщами: ", sorted(workers_base.items()))
    case _:
        new_list = []

        for i in workers_base.keys():
            new_list.append(workers_base[i]["Коефіціент ефективності"])

        new_list.sort(reverse=True)


        def value_sort(n, new_dict = {}):
            if n == int(len(new_list)):
                print("Відсортована бібліотека по коефіціенту ефективності працівника:", new_dict)
                return False
            else:
                for key, value in workers_base.items():
                    if value["Коефіціент ефективності"] == new_list[n]:
                        new_dict[key] = value
                        return value_sort(n + 1)

        n = 0
        value_sort(n)
