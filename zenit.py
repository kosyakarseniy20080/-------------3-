import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime

# Данные с историческими датами
events = [
    {
        "task": "Основание Санкт-Петербурга",
        "year": 1703,
        "month": 5,
        "day": 27
    },
    {
        "task": "Начало Великой Отечественной войны",
        "year": 1941,
        "month": 6,
        "day": 22
    },
    {
        "task": "Новый 2025 год",
        "year": 2025,
        "month": 1,
        "day": 1
    },
    {
        "task": "День Защитника Отечества",
        "year": 2027,
        "month": 2,
        "day": 23
    },
    {
        "task": "День Победы",
        "year": 2027,
        "month": 5,
        "day": 9
    }
]

def show_selected_date():
    """Отображает выбранную дату из календаря."""
    selected_date = cal.get_date()
    result_label.config(text=f"Выбранная дата: {selected_date}")

def display_events():
    """Отображает список исторических событий."""
    events_text.delete(1.0, tk.END)  # Очищаем текстовое поле
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
    year=2024,
    month=5,
    day=23,
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

