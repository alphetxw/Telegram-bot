import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# НАСТРОЙКА: ЗАМЕНИТЕ ЭТИ ДАННЫЕ!
TOKEN = "8158148515:AAGwN1EOWFaVMgoWU-iZU858J_cJKDzG9O4"  # Замените на реальный токен
ADMIN_ID = 5349039932  # Замените на ваш Telegram ID

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    """Обработчик команды /start"""
    if message.from_user.id != ADMIN_ID:
        await message.answer("⛔ Доступ запрещен")
        return
    
    await message.answer(
        "🤖 <b>Telegram Bot</b>\n\n"
        "Команды:\n"
        "/start - это сообщение\n"
        "/attack IP:PORT - запуск атаки\n"
        "/status - статус бота\n\n"
        "⚡ Работает на GitHub"
    )

@dp.message(Command("attack"))
async def attack_cmd(message: types.Message):
    """Обработчик команды /attack"""
    if message.from_user.id != ADMIN_ID:
        return
    
    try:
        args = message.text.split()
        if len(args) < 2:
            await message.answer("❌ Формат: /attack IP:PORT")
            return
        
        target = args[1]
        await message.answer(f"🎯 Цель: {target}")
        
        # Имитация атаки (на GitHub реальный UDP не работает)
        import time
        for i in range(3):
            await message.answer(f"⚡ Шаг {i+1}/3...")
            time.sleep(1)
        
        await message.answer(f"✅ Атака завершена: {target}")
        
    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}")

@dp.message(Command("status"))
async def status_cmd(message: types.Message):
    """Обработчик команды /status"""
    if message.from_user.id != ADMIN_ID:
        return
    
    await message.answer("✅ Бот активен\n📍 Хостинг: GitHub")

async def main():
    """Основная функция"""
    logging.basicConfig(level=logging.INFO)
    print("Бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
