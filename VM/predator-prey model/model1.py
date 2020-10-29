import numpy as np
import matplotlib.pyplot as plt

# Гиперпараметры
count_predator = 50
count_victim = 100
successful_hunts = 0.0007
mortality_predator = 0.05
reproduction_victim = 0.07

def count_population_on_next_iter():
    # func return (victim, predator)
    return ((count_victim + reproduction_victim * count_victim - successful_hunts * count_predator * count_victim),
            (count_predator - mortality_predator * count_predator + successful_hunts * count_predator * count_victim))


list_count_predators = []
list_count_victims = []
while True:
    count_victim, count_predator = count_population_on_next_iter()
    list_count_predators.append(count_predator)
    list_count_victims.append(count_victim)
    if count_victim <= 0:
        list_count_victims[-1] = 0
        break
    elif count_predator <= 0:
        list_count_predators[-1] = 0
        break
    elif len(list_count_predators) == 500:
        break

print('list_count_predators')
print(list_count_predators, '\n')
print('list_count_victims')
print(list_count_victims)

x = range(0, len(list_count_predators))
plt.plot(x, list_count_predators, '-', label='Хищники')
plt.plot(x, list_count_victims, '-', label='Жертвы')
plt.title('Популяция')
plt.ylabel('Кол-во особей')
plt.xlabel('Итерация')
plt.legend()
plt.show()
