from collections import Counter


def load_convoy(h, drakkars: dict[int, list[list[int]]], platforms: dict):
    convoy = []
    closest_destinations = Counter()
    closest_destinations += Counter(destination for destination in platforms.values() if destination)

    for stacks in drakkars.values():
        closest_destinations += Counter(destinations[0] for destinations in stacks if len(destinations) >= 1)

    i = 1
    longest_stack = 0

    for drakkar in drakkars:
        for stack in drakkars[drakkar]:
            if len(stack) > longest_stack:
                longest_stack = len(stack)

    while closest_destinations.most_common(1)[0][1] < h and i <= longest_stack:
        for stacks in drakkars.values():
            closest_destinations += Counter(destinations[i] for destinations in stacks if len(destinations) >= i + 1)
            i += 1

    destination = closest_destinations.most_common(1)[0][0]

    while len(convoy) < h:
        if destination in platforms.values():
            for platform, platform_destination in platforms.items():
                if platform_destination == destination:
                    convoy.append(platform)
                    platforms[platform] = None
                    print(2, platform)

                    if len(convoy) == h:
                        break

        else:
            break

    i = 0
    while (len(convoy) < h) and (Counter(platforms.keys())[None] + i <= 4):
        for drakkar, stacks in drakkars.items():
            if any(stack for stack in drakkars[drakkar]):
                for stack_index, stack in enumerate(stacks):
                    if (len(stack) >= i + 1) and stack[i] == destination:
                        if i > 0:
                            for _ in range(i):
                                for platform in platforms:
                                    if not platforms[platform]:
                                        platforms[platform] = stack.pop(0)
                                        print(1, drakkar + 1, stack_index + 1, platform)
                                        break

                        while stack and stack[0] == destination and len(convoy) < h:
                            container = stack.pop(0)
                            convoy.append(container)
                            print(1, drakkar + 1, stack_index + 1, 0)

                        if len(convoy) == h:
                            break

                if len(convoy) == h:
                    break

        for drakkar in tuple(drakkars.keys()):
            if not any(stack for stack in drakkars[drakkar]):
                del drakkars[drakkar]

        i += 1


n, h = (int(num) for num in input().split())
ls = [int(num) for num in input().split()]
drakkars = {}

for i in range(n):
    stacks = []
    for l in ls:
        for _ in range(int(l)):
            stacks.append([int(num) for num in input().split()[1:]])

    if stacks:
        drakkars[i] = stacks

platforms = {1: None, 2: None, 3: None, 4: None}

while drakkars:
    load_convoy(h, drakkars, platforms)
    print(3)

print(0)
