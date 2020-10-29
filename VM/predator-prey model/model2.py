import numpy as np
import matplotlib.pyplot as plt

# Гиперпараметры
alpha = 0.001
count_predator = 10
count_victim = 100
successful_hunts = 0.0007
mortality_predator = 0.5
#reproduction_victim = 0.7

def count_population_on_next_iter():
    # func return (victim, predator)
    return ((count_victim + reproduction_victim * count_victim - successful_hunts * count_predator * count_victim), \
            (count_predator - mortality_predator * count_predator + successful_hunts * count_predator * count_victim))

def food_relation(count_pop):
    return np.exp(-alpha*count_pop)

list_count_predators = []
list_count_victims = []
list_food_relation = []
while True:
    reproduction_victim = food_relation(count_victim)
    count_victim, count_predator = count_population_on_next_iter()
    list_count_predators.append(count_predator)
    list_count_victims.append(count_victim)
    list_food_relation.append(reproduction_victim)
    if count_victim <= 0:
        list_count_victims[-1] = 0
        break
    elif count_predator <= 0:
        list_count_predators[-1] = 0
        break
    elif len(list_count_predators) == 150:
        break
print('list_count_predators')
print(list_count_predators, '\n')
print('list_count_victims')
print(list_count_victims, ' \n')
print('list_food_relation')
print(list_food_relation, '\n')

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
x = range(0, len(list_count_predators))
plt.plot(x, list_count_predators, '-', label='Хищники')
plt.plot(x, list_count_victims, '-', label='Жертвы')
plt.title('Популяция')
plt.ylabel('Кол-во особей')
plt.xlabel('Итерация')
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(x, list_food_relation, '-')
plt.title('Скорось размножения жертв')
plt.ylabel('Скорость')
plt.xlabel('Итерация')
plt.legend()
plt.show()

