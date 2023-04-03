import tkinter as tk

class StopWatch(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.pack()

        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self._running = False
        self._after_id = None

    def create_widgets(self):
        self.display = tk.Label(self, text="00:00:00", font=("Helvetica", 48))
        self.display.pack(padx=20, pady=20)

        self.start_button = tk.Button(self, text="Start", command=self.start_stopwatch)
        self.start_button.pack(side="left", padx=10)
        
        self.stop_button = tk.Button(self, text="Stop", command=self.stop_stopwatch, state="disabled")
        self.stop_button.pack(side="left", padx=10)
        
        self.reset_button = tk.Button(self, text="Reset", command=self.reset_stopwatch)
        self.reset_button.pack(side="left", padx=10)
        
    def start_stopwatch(self):
        self._running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.update()
    
    def stop_stopwatch(self):
        self._running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        if self._after_id:
            self.after_cancel(self._after_id)
            self._after_id = None
    
    def reset_stopwatch(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.display.config(text="00:00:00")
    
    def update(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
        time_str = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        self.display.config(text=time_str)
        if self._running:
            self._after_id = self.after(1000, self.update)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Tyron's Stopwatch")
    sw = StopWatch(root)
    sw.mainloop()
        
    























# import time

# # def start_stopwatch():
# #     start_time = time.time()
# #     elapsed_time = 0
# #     while True:
# #         print(f"\r{elapsed_time // 3600:02.0f}hrs {elapsed_time // 60:02.0f}mins {elapsed_time % 60:02.0f}secs", end="")
# #         command = input()
#         if command == "s":
#             start_time = time.time() - elapsed_time
#         elif command == "t":
#             elapsed_time = time.time() - start_time
#         elif command == "e":
#             break
#         print("Stopwatch has stopped.")


# start_stopwatch()













# start_time = None
# elapsed_time = 0
# running = False

# while True:
#     user_input = input("Press 's' to start/stop or 'e' to end the stopwatch.")
#     if user_input == 's':
#         if not running:
#             start_time = time.time()
#             running = True
#             # if running:
#             #     current_time = time.time() - start_time + elapsed_time
#             #     hours, remainder = divmod(current_time, 3600)
#             #     minutes, seconds = divmod(remainder, 60)
#             #     print(f"Elapsed time: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}", end='\r')
#             # else:
#             #     print(f"Elapsed time: {int(elapsed_time // 3600):02d}:{int((elapsed_time // 60) % 60):02d}:{int(elapsed_time % 60):02d}", end='\r')

                
#         else:
#             elapsed_time += time.time() - start_time
#             running = False
#     elif user_input == 'e':
#         if running:
#             elapsed_time += time.time() - start_time
#         break

# print(f"\nTotal elapsed time: {int(elapsed_time // 3600):02d}:{int((elapsed_time // 60) % 60):02d}:{int(elapsed_time % 60):02d}")


        