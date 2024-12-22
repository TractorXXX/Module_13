import asyncio

async def start_strongman(name, power):

# Цикл поднятия 5 шаров Атласа каждым участником
    for i in range(1, 6):
        print(f'Силач {name} начал соревнования.')
        await asyncio.sleep(1 / power) # Задержка обратно пропорциональна его силе power
        print(f'Силач {name} поднял шар №{i}')

    print(f'Силач {name} закончил соревнования.')

async def start_tournament():

# Создаем 3 задачи для 3-х участников соревнования

    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))

# Ставим каждую задачу в ожидание

    await task_1
    await task_2
    await task_3


asyncio.run(start_tournament())
