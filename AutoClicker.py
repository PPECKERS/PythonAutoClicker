import tkinter as tk
import pyautogui
import threading
import keyboard

is_auto_clicking = False  # Otomatik tıklama durumunu takip etmek için bir bayrak

def toggle_auto_click():
    global is_auto_clicking

    if is_auto_clicking:
        stop_auto_click()
    else:
        start_auto_click()

def start_auto_click():
    global is_auto_clicking
    is_auto_clicking = True
    auto_click()

def stop_auto_click():
    global is_auto_clicking
    is_auto_clicking = False

def auto_click():
    while is_auto_clicking:
        pyautogui.click()

def listen_keyboard_event():
    keyboard.add_hotkey("q", stop_program)

def stop_program():
    global root
    root.destroy()

def main():
    global root
    root = tk.Tk()
    root.title("Auto Clicker")
    root.attributes("-toolwindow", 1)
    root.attributes("-topmost", True)
    root.geometry("200x100")

    button = tk.Button(root, text="Tıklama İşlemini Başlat/Durdur", command=toggle_auto_click)
    button.pack(padx=20, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_thread = threading.Thread(target=main)
    main_thread.start()

    keyboard_thread = threading.Thread(target=listen_keyboard_event)
    keyboard_thread.start()
