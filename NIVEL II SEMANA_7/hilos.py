import threading
import time

def countdown(name, start):
    while start > 0:
        print(f"{name} cuenta regresiva: {start}")
        start -= 1
        time.sleep(1)
    print(f"{name} ¡despegue!")

# Crear dos hilos con diferentes contadores
thread1 = threading.Thread(target=countdown, args=("Hilo 1", 5))
thread2 = threading.Thread(target=countdown, args=("Hilo 2", 8))

# Iniciar los hilos
thread1.start()
thread2.start()

# Esperar a que los hilos terminen
thread1.join()
thread2.join()

print("Tareas concurrentes completadas.")
