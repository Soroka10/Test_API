# Real-Time Query Assistant

## Опис проєкту
**Real-Time Query Assistant** — це веб-застосунок, що дозволяє користувачам завантажувати фотографії або зробити знімок з камери та задавати запитання про зображення. Відповідь генерується за допомогою **API Gemini**.

## Використані технології
- **Backend:** Python 3, Flask, Flask-SocketIO
- **AI API:** Google Gemini API
- **Frontend:** JavaScript, HTML, CSS

---

## Встановлення

### 1. Клонування репозиторію
```bash
git clone https://github.com/Soroka10/Test_API.git
cd real-time-query-assistant
```

### 2. Встановлення залежностей
Переконайтеся, що у вас встановлений **Python 3.10+**. Створіть та активуйте **віртуальне середовище**:
```bash
python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate    # Для Windows
```
Потім встановіть необхідні залежності:
```bash
pip install -r requirements.txt
```

### 3. Налаштування API
Створіть **файл `.env`** у кореневій директорії проєкту та додайте у нього API-ключ **Google Gemini API**:
```bash
GOOGLE_GEMINI_API_KEY=your_api_key_here
```

---

## Запуск проєкту

### Запуск сервера
```bash
flask run
```
Сервер запуститься на `http://127.0.0.1:5000/`.

Для автоматичного перезавантаження сервера під час змін у коді використовуйте режим розробки:
```bash
export FLASK_ENV=development  # Для macOS/Linux
set FLASK_ENV=development     # Для Windows
flask run
```

---

## Використання
1. Відкрийте браузер і перейдіть за адресою `http://127.0.0.1:5000/`.
2. Завантажте зображення або зробіть знімок з камери.
3. Введіть питання щодо зображення.
4. Натисніть "Ask", і отримайте відповідь!

---

## Додаткові команди

### Деактивація віртуального середовища
```bash
deactivate
```

### Оновлення залежностей
```bash
pip freeze > requirements.txt
```

### Видалення віртуального середовища
```bash
rm -rf venv  # Для macOS/Linux
rmdir /s /q venv  # Для Windows
```

---

## Контактна інформація
Якщо у вас є питання або пропозиції щодо покращення проєкту, звертайтесь за email: **your-email@example.com**.
