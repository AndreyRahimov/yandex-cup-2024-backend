def solve_viking_problem(n, h, lengths, stacks):
    # Площадка для контейнеров (4 места)
    port_space = [[] for _ in range(4)]

    # Список для действий
    actions = []

    # Функция для загрузки обоза
    def load_cart(cart):
        if cart:
            actions.append(f"3")  # Отправить текущий обоз
        else:
            return  # Если обоз пуст, ничего не отправляем

    # Проходим по всем драккарам и их стекам
    for i in range(n):
        for j in range(lengths[i]):
            stack = stacks[i][j]
            container_count = stack[0]
            containers = stack[1:]

            # Перемещаем контейнеры из стека на площадку или в обоз
            for container in containers:
                # Берем контейнер из стека на драккаре
                actions.append(f"1 {i + 1} {j + 1} 0")  # Перемещение в обоз
                cart = [container]  # Создаем текущий обоз
                while cart:
                    # Если можем отправить текущий обоз
                    if len(cart) > h:
                        cart = cart[:h]  # Отправляем только h контейнеров

                    load_cart(cart)
                    cart = []  # Очищаем обоз для следующей загрузки

            # Теперь перемещаем контейнеры на площадку
            for k in range(4):
                while len(port_space[k]) < 4 and len(containers) > 0:
                    port_space[k].append(containers.pop(0))
                    actions.append(f"1 {i + 1} {j + 1} {k + 1}")

            # Перемещаем контейнеры из площадки в обоз
            for k in range(4):
                while len(port_space[k]) > 0 and len(cart) < h:
                    container = port_space[k].pop(0)
                    actions.append(f"2 {k + 1}")
                    cart.append(container)

            load_cart(cart)

    # В конце выводим, что все обозы отправлены
    actions.append("0")

    # Печатаем все действия
    for action in actions:
        print(action)


# Чтение ввода
n, h = map(int, input().split())
lengths = list(map(int, input().split()))

stacks = []
for i in range(n):
    stacks.append([])
    for j in range(lengths[i]):
        data = list(map(int, input().split()))
        stacks[i].append(data)

# Получаем и выводим действия
solve_viking_problem(n, h, lengths, stacks)
