n, h = map(int, input().split())
stacks_amount = [int(num) for num in input().split()]

drakkars: list[list[list[int]]] = []

for i in range(n):
    drakkar_stacks: list[list[int]] = []

    for j in range(stacks_amount[i]):
        stack = [int(num) for num in input().split()]
        stack = stack[stack[0]:0:-1]
        drakkar_stacks.append(stack)

    drakkars.append(drakkar_stacks)

containers_on_cart = drakkar_ind = 0
village = 1
platforms = []

while drakkar_ind > -1:
    drakkar_ind = stack_ind = -1

    while village in platforms:
        print(2, platform_ind + 1)
        platform_ind = platforms.index(village)
        del platforms[platform_ind]
        containers_on_cart += 1

        if containers_on_cart == h:
            print(3)
            containers_on_cart = 0

    for i in range(n):
        for j in range(len(drakkars[i])):
            stack = drakkars[i][j]

            if stack and village in stack:
                drakkar_ind, stack_ind = i, j
                container_ind = drakkars[drakkar_ind][stack_ind].index(village)

                if len(platforms) + len(stack) - container_ind + 1 <= 4:
                    while drakkars[drakkar_ind][stack_ind][container_ind] != village:
                        print(1, drakkar_ind + 1, stack_ind + 1, len(platforms))
                        platforms.append(drakkars[drakkar_ind][stack_ind].pop())

                    print(1, drakkar_ind + 1, stack_ind + 1, 0)
                    containers_on_cart += 1
                    del drakkars[drakkar_ind][stack_ind][container_ind]

                    if containers_on_cart == h:
                        print(3)
                        containers_on_cart = 0

    if any(stack for drakkar in drakkars for stack in drakkar) and not any(
            village in stack for drakkar in drakkars for stack in drakkar):

        if containers_on_cart:
            print(3)
            containers_on_cart = 0

        village += 1
        drakkar_ind = 0

if containers_on_cart:
    print(3)

print(0)
