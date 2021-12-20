from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup,State
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.storage import FSMContext
from aiogram.utils import executor
from config import TOKEN
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton,Message

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


class Test(StatesGroup):
    Q0 = State()
    Q1 = State()
    Q2 = State()
    Q3 = State()

milk={
    1 : "Молоко 3,2%",
    2 : "Йогурт",
    3 : "Сметана 20%"
}
meat_fish={
    1 : "Курина грудка",
    2 : "Форель копчёная",
    3 : "Говяжий фарш"
}
bread={
    1 : "Батон белого",
    2 : "Пол чёрного",
    3 : "Пирожёк с повидлом"
}
   
@dp.message_handler(state="*", commands=['start'])
async def starting_process(message: types.Message):
    await bot.send_message(message.from_user.id,"Приветствуем вас в нашем интернет магазине.\nЗдесь вы мошете заказать продукты из следующих категорий:\n \
    1)Молочные продукты\n \
    2)Мясо и рыба\n \
    3)Хлебобулочные изделия\nЧтобы начать формировать заказ напиши /order")
    await Test.Q0.set()

@dp.message_handler(state=Test.Q0, commands=['order'])
async def starting_process(message: types.Message,state: FSMContext):
    await bot.send_message(message.from_user.id, "Выберите молочный продукт\n1)Молоко 3,2%\n2)Йогурт\n3)Сметана 20%")
    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def first_choosing(message: types.Message,state: FSMContext):
    
    answer = int(message.text)
    if (answer != 1 and answer !=2 and answer !=3):
        return await bot.send_message(message.from_user.id,"К сожалению, такого товара нет в наличии, попробуйте выбрать другой")
    await state.update_data(q1 = answer)
    await bot.send_message(message.from_user.id,"Мясо или рыба\n1)Курина грудка\n2)Форель копчёная\n3)Говяжий фарш")
    await Test.Q2.set()

@dp.message_handler(state=Test.Q2)
async def second_choosing(message: types.Message,state: FSMContext):
    answer = int(message.text)
    if (answer != 1 and answer !=2 and answer !=3):
        return await bot.send_message(message.from_user.id,"К сожалению, такого товара нет в наличии, попробуйте выбрать другой")
    await state.update_data(q2 = answer)
    await bot.send_message(message.from_user.id, "Выберите хлебобулочное изделие\n1)Батон белого\n2)Пол чёрного\n3)Пирожёк с повидлом")
    await Test.Q3.set()



@dp.message_handler(state=Test.Q3)
async def second_choosing(message: types.Message,state: FSMContext):
    answer = int(message.text)
    if (answer != 1 and answer !=2 and answer !=3):
        return await bot.send_message(message.from_user.id,"К сожалению, такого товара нет в наличии, попробуйте выбрать другой")
    await state.update_data(q3 = answer)
    data = await state.get_data()

    
    
    await bot.send_message(message.from_user.id,"Ваш заказ:\nМолочный продукт:\n{}\nМясо или рыба:\n{}\nХлебобулочное изделие:\n{}".format(milk[data.get("q1")],meat_fish[data.get("q2")],bread[data.get("q3")]))
    await Test.Q0.set()


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)