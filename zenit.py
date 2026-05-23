import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import json
from datetime import datetime

def load_events():
    """Загружает события из JSON‑файла."""
    try:
        with open('events.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def show_selected_date():
    """Отображает выбранную дату из календаря."""
    selected_date = cal.get_date()
    result_label.config(text=f"Выбранная дата: {selected_date}")

def display_events():
    """Отображает список исторических событий из JSON‑файла."""
    events_text.delete(1.0, tk.END)  # Очищаем текстовое поле

    events = load_events()
    if not events:
        events_text.insert(tk.END, "Ошибка: файл events.json не найден или пуст.\n")
        return

    events_text.insert(tk.END, "Список исторических событий:\n\n")
    for event in events:
        date_str = f"{event['day']:02d}.{event['month']:02d}.{event['year']}"
        events_text.insert(tk.END, f"{date_str} — {event['task']}\n")

# Создание главного окна
root = tk.Tk()
root.title("Календарь с историческими датами")
root.geometry("600x500")

# Создание календаря
cal = Calendar(
    root,
    selectmode='day',
    year=datetime.now().year,
    month=datetime.now().month,
    day=datetime.now().day,
    date_pattern='dd.mm.yyyy'
)
cal.pack(pady=10)

# Кнопка для получения выбранной даты
get_date_btn = ttk.Button(root, text="Получить выбранную дату", command=show_selected_date)
get_date_btn.pack(pady=5)

# Метка для отображения выбранной даты
result_label = ttk.Label(root, text="Выбранная дата: ")
result_label.pack(pady=5)

# Кнопка для отображения списка событий
show_events_btn = ttk.Button(root, text="Показать исторические даты", command=display_events)
show_events_btn.pack(pady=5)

# Текстовое поле для отображения списка событий
events_text = tk.Text(root, height=12, width=60)
events_text.pack(pady=10)

# Автоматический показ списка событий при запуске
display_events()

# Запуск главного цикла
root.mainloop()
