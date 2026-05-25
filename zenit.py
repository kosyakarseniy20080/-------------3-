import tkinter as tk

# Ваш список событий встроен прямо в код, чтобы избежать ошибок с файлами
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

# Создаем окно
root = tk.Tk()
root.title("Список исторических событий и праздников")
root.geometry("500x300")

# Создаем простое текстовое поле для вывода
events_text = tk.Text(root, font=("Arial", 11), padx=10, pady=10)
events_text.pack(fill=tk.BOTH, expand=True)

# Перебираем данные и сразу выводим на экран
for event in events:
    day = event['day']
    month = event['month']
    year = event['year']
    task = event['task']
    
    # Форматируем дату в красивый вид ДД.ММ.ГГГГ
    date_str = f"{day:02d}.{month:02d}.{year}"
    events_text.insert(tk.END, f"{date_str} — {task}\n")

# Запуск программы
root.mainloop()
