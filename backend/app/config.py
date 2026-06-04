from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

print("HOST =", DB_HOST)
print("PORT =", DB_PORT)
print("DB =", DB_NAME)
print("USER =", DB_USER)
print("PASSWORD =", DB_PASSWORD)