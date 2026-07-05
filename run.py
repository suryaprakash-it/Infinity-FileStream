import subprocess
import threading


def start_bot():
    subprocess.run(["python", "bot.py"])


def start_web():
    subprocess.run(["uvicorn", "web:app", "--host", "0.0.0.0", "--port", "8080"])


bot_thread = threading.Thread(target=start_bot)
web_thread = threading.Thread(target=start_web)

bot_thread.start()
web_thread.start()

bot_thread.join()
web_thread.join()