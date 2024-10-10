import time
import keyboard

def cronometro():
    print("Cronômetro iniciado. Pressione 'p' para pausar/resumir e Enter para parar.")
    start_time = time.time()
    elapsed_time = 0
    pausado = False

    while True:
        if not pausado:
            elapsed_time = time.time() - start_time
            print("\r" + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), end="")
            time.sleep(1)

        # Verifica se a tecla 'p' foi pressionada
        if keyboard.is_pressed('p'):
            pausado = not pausado
            if pausado:
                print(f"\nCronômetro pausado. Pressione 'p' para retomar.")
            else:
                # Atualiza o tempo de início ao retomar
                start_time = time.time() - elapsed_time
                print("\r" + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), end="")
            time.sleep(0.1)  # Reduzido para 0.1 segundos para melhorar a detecção

        # Verifica se a tecla 'enter' foi pressionada
        if keyboard.is_pressed('enter'):
            print("\nCronômetro finalizado.")
            break

cronometro()
