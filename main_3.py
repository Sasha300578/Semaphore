import threading
import time


semaphore = None
semaphore_kol = 0
padding = 0
flag_i = False


def worker(num):
    global padding, semaphore_kol, flag_i

    if num == 'I' :
        while flag_i == False:
            time.sleep(1.5)
            print(f"Поток {num} начался и ожидает семафор.")
            time.sleep(8.5)

            semaphore.acquire()
            padding += 100
            print(f"Поток {num} захватывает семафор.")
            time.sleep(1 + padding / 1000)

            print(f"Поток {num} в семафоре.")
            print(f"Переменная семафора равна: {semaphore_kol}. Поток {num} выходит из семафора.")
            semaphore_kol += 1
    else:
        print(f"Поток {num} начался и ожидает семафор.")
        semaphore.acquire()
        padding += 200

        print(f"Поток {num} захватывает семафор.")
        time.sleep(1.5 + padding / 1000)

        print(f"Поток {num} в семафоре.")
        print(f"Переменная семафора равна: {semaphore_kol}. Поток {num} выходит из семафора.")
        semaphore_kol += 1



# Начало
a = threading.Thread(target=worker, args=("A",))
semaphore = threading.Semaphore(1)
a.start()
time.sleep(0.5)
semaphore.release()
time.sleep(3)
a.join()
print()

semaphore_kol = 0
# Точка 1
b = threading.Thread(target=worker, args=("B",))
c = threading.Thread(target=worker, args=("C",))
i = threading.Thread(target=worker, args=("I",))
j = threading.Thread(target=worker, args=("J",))
semaphore = threading.Semaphore(3)
b.start()
time.sleep(0.1)
c.start()
i.start()
time.sleep(0.5)
j.start()

time.sleep(0.5)
# Приостанавливаем поток i
flag_i = True

semaphore.release(3)
time.sleep(3)

b.join()
c.join()
j.join()
print()

semaphore_kol = 0

# Точка 2
d = threading.Thread(target=worker, args=("D",))
e = threading.Thread(target=worker, args=("E",))
f = threading.Thread(target=worker, args=("F",))
semaphore = threading.Semaphore(3)
f.start()
d.start()
time.sleep(0.1)
e.start()

time.sleep(0.5)
time.sleep(2)

semaphore.release(3)

e.join()
d.join()
f.join()
print()

semaphore_kol = 0

# Точка 3
g = threading.Thread(target=worker, args=("G",))
h = threading.Thread(target=worker, args=("H",))
semaphore = threading.Semaphore(3)
g.start()
h.start()
time.sleep(0.5)
time.sleep(2)

# возобновляем поток i
flag_i = False

semaphore.release(3)
time.sleep(3)
# Приостанавливаем поток i
flag_i = True

i.join()
h.join()
g.join()
print()

semaphore_kol = 0

# Точка 4
k = threading.Thread(args=("K",))
print("Поток 'K' начался.")
k.start()
k.join()
print("\nЗавершено")

