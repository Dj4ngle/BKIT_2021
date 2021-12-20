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

milk_price={
    "Молоко 3,2%" : 65,
    "Йогурт" : 25,
    "Сметана 20%" : 70
}
meat_fish_price={
    "Курина грудка" : 250,
    "Форель копчёная" : 570,
    "Говяжий фарш" : 450
}
bread_price={
    "Батон белого" : 35,
    "Пол чёрного" : 20,
    "Пирожёк с повидлом" : 35
}

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



def summary(first_table,first_table_price,second_table,second_table_price,third_table,third_table_price,first_answer,second_answer,third_answer):
    a = first_table_price[first_table[first_answer]]
    b = second_table_price[second_table[second_answer]]
    c = third_table_price[third_table[third_answer]]
    return "Итоговая сумма = " + str(a+b+c)+ "\n"


@dp.message_handler(state="*", commands=['start'])
async def starting_process(message: types.Message):
    await bot.send_message(message.from_user.id,"Приветствуем вас в нашем интернет магазине.\nЗдесь вы можете заказать продукты из следующих категорий:\n \
    1)Молочные продукты\n \
    2)Мясо и рыба\n \
    3)Хлебобулочные изделия\nЧтобы начать формировать заказ напиши /order")
    await Test.Q0.set()

@dp.message_handler(state=Test.Q0, commands=['order'])
async def starting_process(message: types.Message,state: FSMContext):
    await bot.send_message(message.from_user.id, "Выберите молочный продукт\n1)Молоко 3,2% - 65\n2)Йогурт - 25\n3)Сметана 20% - 70")
    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def first_choosing(message: types.Message,state: FSMContext):
    answer = int(message.text)
    if (answer != 1 and answer !=2 and answer !=3):
        return await bot.send_message(message.from_user.id,"К сожалению, такого товара нет в наличии, попробуйте выбрать другой")
    await state.update_data(q1 = answer)
    await bot.send_message(message.from_user.id,"Мясо или рыба\n1)Курина грудка - 250\n2)Форель копчёная - 570\n3)Говяжий фарш - 450")
    await Test.Q2.set()

@dp.message_handler(state=Test.Q2)
async def second_choosing(message: types.Message,state: FSMContext):
    answer = int(message.text)
    if (answer != 1 and answer !=2 and answer !=3):
        return await bot.send_message(message.from_user.id,"К сожалению, такого товара нет в наличии, попробуйте выбрать другой")
    await state.update_data(q2 = answer)
    await bot.send_message(message.from_user.id, "Выберите хлебобулочное изделие\n1)Батон белого - 35\n2)Пол чёрного - 20\n3)Пирожёк с повидлом - 35")
    await Test.Q3.set()



@dp.message_handler(state=Test.Q3)
async def third_choosing(message: types.Message,state: FSMContext):
    answer = int(message.text)
    if (answer != 1 and answer !=2 and answer !=3):
        return await bot.send_message(message.from_user.id,"К сожалению, такого товара нет в наличии, попробуйте выбрать другой")
    await state.update_data(q3 = answer)
    data = await state.get_data()
    sumcheck=summary(milk,milk_price,meat_fish,meat_fish_price,bread,bread_price,data.get("q1"),data.get("q2"),data.get("q3"))
    await bot.send_message(message.from_user.id,"Ваш заказ:\nМолочный продукт:\n{}\nМясо или рыба:\n{}\nХлебобулочное изделие:\n{}".format(milk[data.get("q1")],meat_fish[data.get("q2")],bread[data.get("q3")]))
    await bot.send_message(message.from_user.id, sumcheck)
    await Test.Q0.set()


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)