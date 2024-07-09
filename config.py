import gspread
from aiogram.types import FSInputFile
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
import os
from aiogram import Bot, Dispatcher


url = "https://yandex.ru/maps/21641/lobnja/house/ulitsa_lenina_1/Z04Ycg9jT0AFQFtsfXxwcHVmYw==/?ll=37.483651%2C56.011958&z=17.2"
image = FSInputFile("img1.jpg")

# Загрузка переменных окружения из .env файла
load_dotenv()

# Получение значений из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
GOOGLE_SHEET_CREDENTIALS_PATH = os.getenv("GOOGLE_SHEET_CREDENTIALS_PATH")
YOOMONEY_CLIENT_ID = os.getenv("YOOMONEY_CLIENT_ID")
YOOMONEY_ACCESS_TOKEN = os.getenv("YOOMONEY_ACCESS_TOKEN")

# Настройки для доступа к Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEET_CREDENTIALS_PATH, scope)
client = gspread.authorize(creds)
sheet = client.open("гугл_табличка").sheet1

# Создаем экземпляр бота с использованием токена и создаем диспетчер для обработки сообщений
bot = Bot(BOT_TOKEN)
dp = Dispatcher()
