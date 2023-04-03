import time

start_time = None
elapsed_time = 0
running = False

while True:
    user_input = input("Press 's' to start/stop or 'e' to end the stopwatch.")
    if user_input == 's':
        if not running:
            start_time = time.time()
            running = True
        else:
            elapsed_time += time.time() - start_time
            running = False
    elif user_input == 'e':
        if running:
            elapsed_time += time.time() - start_time
        break

    if running:
        current_time = time.time() - start_time + elapsed_time
        hours, remainder = divmod(current_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"Elapsed time: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}", end='\r')
    else:
        print(f"Elapsed time: {int(elapsed_time // 3600):02d}:{int((elapsed_time // 60) % 60):02d}:{int(elapsed_time % 60):02d}", end='\r')

print(f"\nTotal elapsed time: {int(elapsed_time // 3600):02d}:{int((elapsed_time // 60) % 60):02d}:{int(elapsed_time % 60):02d}")


        