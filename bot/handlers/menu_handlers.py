from aiogram import types
from bot.buttons.inline import menu_show_btn, qarsildoq_joja, salatlar_btn, souslar_btn, ichimliklar_btn, lavashlar_btn, \
    setlar_btn, pitsalar_btn, hot_doglar_btn, haggi_btn, sneklar_btn, klab_sendvich_btn, burger_doner_btn
from bot.buttons.reply import language, back_button, ask_deliver, location_button, ask_loc_true, user_num
from bot.buttons.language import uzb_lang, eng_lang, lang
from bot.dispatcher import dp
from aiogram.dispatcher import FSMContext
from DB.config import Pg
import requests
import logging


@dp.message_handler(content_types=types.ContentTypes.CONTACT,state="contact1")
async def main_menu_handler(msg: types.Message, state:FSMContext):
    obj = Pg()
    phone_num = msg.contact.phone_number
    user_id = msg.from_user.id
    obj.add_contact(user_id, phone_num)
    async with state.proxy() as data:
        user_lang = data.get("lang")
    data = lang.get(user_lang)
    await msg.answer(data.get("ask"), reply_markup=back_button(data))
    link = "[Kategoriyalardan birini tanlang](https://telegra.ph/Taomnoma-09-02)"
    await msg.answer(link,"Markdown",reply_markup = menu_show_btn(data))
    await state.set_state("categories")


@dp.callback_query_handler(lambda call: call.data in list(lang.get(uzb_lang).keys()) + list(lang.get(eng_lang).keys()), state = "categories")
@dp.callback_query_handler(lambda call: call.data in list(lang.get(uzb_lang).keys()) + list(lang.get(eng_lang).keys()), state = "bita_qayt")
async def categories_handler(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        user_lang = data.get("lang")
    data = lang.get(user_lang)
    if call.data == "qarsildoq jo'jalar":
        text = data.get("Qarsildoq Jo'jalar")
        photo = "https://telegra.ph/file/53f86f8d272b1d4eba56c.png"
        await call.message.answer(data.get("ask"), reply_markup=back_button(data))
        await call.message.answer_photo(photo, text, reply_markup=qarsildoq_joja(data), parse_mode="Markdown")
        await call.message.delete()
        await state.set_state("joja")
        print(call.data)


    if call.data == "salatlar":
        text = data.get("Salatlar")
        photo = "https://telegra.ph/file/21972604e5a1f5c90554d.png"
        await call.message.answer(data.get("ask"), reply_markup=back_button(data))
        await call.message.answer_photo(photo, text, reply_markup=salatlar_btn(data),parse_mode="Markdown")
        await call.message.delete()

    if call.data == "ichimliklar":
        text = data.get("Ichimliklar")
        photo = "https://telegra.ph/file/6fb08c615e16d455131c2.png"
        await call.message.answer(data.get("ask"), reply_markup=back_button(data))
        await call.message.answer_photo(photo, text, reply_markup=ichimliklar_btn(data),parse_mode="Markdown")
        await call.message.delete()

    if call.data == "souslar":
        text = data.get("Souslar")
        photo = "https://telegra.ph/file/8eaf47b6275a1a52e6723.png"
        await call.message.answer(data.get("ask"), reply_markup=back_button(data))
        await call.message.answer_photo(photo, text, reply_markup=souslar_btn(data),parse_mode="Markdown")
        await call.message.delete()

    if call.data == "lavashlar":
        text = data.get("Lavashlar")
        photo = "https://telegra.ph/file/1cf30cfb75c61863cadf0.png"
        await call.message.answer(data.get("ask"), reply_markup=back_button(data))
        await call.message.answer_photo(photo, text, reply_markup=lavashlar_btn(data),parse_mode="Markdown")
        await call.message.delete()

    if call.data == "setlar":
        text = data.get("Setlar")
        photo = "https://telegra.ph/file/d885fc857f54883a1b5a3.png"
        await call.message.answer(data.get("ask"), reply_markup=back_button(data))
        await call.message.answer_photo(photo, text, reply_markup=setlar_btn(data), parse_mode="Markdown")
        await call.message.delete()

    if call.data == "pitsalar":
        text = data.get("Pitsalar")
        photo = "https://telegra.ph/file/175da03043f5a079f76aa.png"
        await call.message.answer(data.get("ask"), reply_markup=back_button(data))
        await call.message.answer_photo(photo, text, reply_markup=pitsalar_btn(data), parse_mode="Markdown")
        await call.message.delete()

    if call.data == "burger va donerlar":
        text = data.get("Burger va donerlar")
        photo = "https://telegra.ph/file/75de3ab17545b2588a9d8.png"
        await call.message.answer(data.get("ask"), reply_markup=back_button(data))
        await call.message.answer_photo(photo, text, reply_markup=burger_doner_btn(data), parse_mode="Markdown")
        await call.message.delete()

    if call.data == "hot doglar":
        text = data.get("Hot doglar")
        photo = "https://telegra.ph/file/0aa023a31cf09bdaba3fa.png"
        await call.message.answer(data.get("ask"), reply_markup=back_button(data))
        await call.message.answer_photo(photo, text, reply_markup=hot_doglar_btn(data), parse_mode="Markdown")
        await call.message.delete()

    if call.data == "haggi":
        text = f"""{data.get("Narxi")}: *31 000 so'm* \n{data.get("Haggi_tasnifi")}\n{data.get("Haggi")}"""
        photo = "https://telegra.ph/file/61cfab663c629ab697d5f.png"
        await call.message.answer(data.get("ask"), reply_markup=back_button(data))
        await call.message.answer_photo(photo, text, reply_markup=haggi_btn(data), parse_mode="Markdown")
        await call.message.delete()

    if call.data == "klab sendvich":
        text = f"""{data.get("Narxi")}: *30 000 so'm* \n{data.get("Klab_tasnifi")}\n{data.get("Klab sendvich")}"""
        photo = "https://telegra.ph/file/e53489d89c023609b9041.png"
        await call.message.answer(data.get("ask"), reply_markup=back_button(data))
        await call.message.answer_photo(photo, text, reply_markup=klab_sendvich_btn(data), parse_mode="Markdown")
        await call.message.delete()

    if call.data == "sneklar":
        text = data.get("Sneklar")
        photo = "https://telegra.ph/file/0d64eadf3a9f64664953e.png"
        await call.message.answer(data.get("ask"), reply_markup=back_button(data))
        await call.message.answer_photo(photo, text, reply_markup=sneklar_btn(data), parse_mode="Markdown")
        await call.message.delete()
    await state.set_state("back")




@dp.callback_query_handler(lambda call: "back_main" in call.data,state = "joja")
async def bitta_ortga_handler(call: types.CallbackQuery, state: FSMContext):

    async with state.proxy() as data:
        user_lang = data.get("lang")
    data = lang.get(user_lang)
    print(data)
    if call.data == "back_main":
        await call.message.answer("salom")
        await state.set_state("bita_qayt")