from pathlib import Path

# Створює базовий шлях для проєкту. Використовується для побудови шляхів до файлів всередині проєкту.
BASE_DIR = Path(__file__).resolve().parent.parent

# Налаштування для швидкого запуску на етапі розробки. Небезпечно для використання у продакшн-середовищі.

# УВАГА: Тримайте секретний ключ у таємниці, якщо запускаєте проєкт у продакшні.
SECRET_KEY = 'django-insecure-o-upvyy7(zq9_)a6g^w=96rnd(jbhn-u(eq0+2pow2t@3w=(q0'

# УВАГА: Не використовуйте DEBUG=True у продакшні, оскільки це може відкрити вразливості для атак.
DEBUG = True

# Дозволені хости – список IP-адрес або доменів, з яких дозволяється доступ до сайту.
ALLOWED_HOSTS = []

# Налаштування додатків, які використовуються у проєкті.
INSTALLED_APPS = [
    'django.contrib.admin',      # Панель адміністратора Django.
    'django.contrib.auth',       # Система аутентифікації користувачів.
    'django.contrib.contenttypes', # Налаштування типів контенту.
    'django.contrib.sessions',    # Система сесій для користувачів.
    'django.contrib.messages',    # Система повідомлень.
    'django.contrib.staticfiles', # Обробка статичних файлів (CSS, JavaScript, зображення).
]

# Налаштування посередників, що обробляють запити і відповіді в додатку.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',         # Захист і налаштування безпеки.
    'django.contrib.sessions.middleware.SessionMiddleware',   # Обробка сесій.
    'django.middleware.common.CommonMiddleware',              # Загальні налаштування.
    'django.middleware.csrf.CsrfViewMiddleware',             # Захист від CSRF атак.
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Аутентифікація користувачів.
    'django.contrib.messages.middleware.MessageMiddleware',   # Система повідомлень.
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Захист від Clickjacking атак.
]

# Основний файл конфігурації URL-адрес для проєкту.
ROOT_URLCONF = 'mysite.urls'

# Налаштування шаблонів, які використовуються у проєкті.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # Бекенд для рендерингу шаблонів.
        'DIRS': [],                    # Список додаткових директорій для пошуку шаблонів.
        'APP_DIRS': True,              # Автоматичний пошук шаблонів в додатках.
        'OPTIONS': {
            'context_processors': [    # Контекстні процесори, що додають змінні у шаблони.
                'django.template.context_processors.debug',           # Додає змінні для налагодження.
                'django.template.context_processors.request',         # Додає об'єкт запиту.
                'django.contrib.auth.context_processors.auth',        # Додає дані користувача.
                'django.contrib.messages.context_processors.messages', # Додає систему повідомлень.
            ],
        },
    },
]

# Конфігурація WSGI для розгортання проєкту.
WSGI_APPLICATION = 'mysite.wsgi.application'

# Налаштування бази даних. У цьому випадку використовується SQLite3.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',       # Тип бази даних (SQLite3).
        'NAME': BASE_DIR / 'db.sqlite3',              # Розташування файлу бази даних.
    }
}

# Валідатори паролів, які забезпечують мінімальні вимоги до паролів користувачів.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # Мінімальна довжина паролю.
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # Запобігає використанню поширених паролів.
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # Забороняє лише числові паролі.
    },
]

# Налаштування для інтернаціоналізації та часової зони.
LANGUAGE_CODE = 'en-us'       # Код мови для інтерфейсу (англійська).
TIME_ZONE = 'UTC'             # Часовий пояс (UTC).
USE_I18N = True               # Використання інтернаціоналізації.
USE_TZ = True                 # Використання часових зон.

# Налаштування для роботи зі статичними файлами.
STATIC_URL = 'static/'        # URL для доступу до статичних файлів.

# Тип первинного ключа за замовчуванням для моделей Django.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
