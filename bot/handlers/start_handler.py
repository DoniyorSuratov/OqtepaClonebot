from aiogram import types
from bot.buttons.inline import menu_button, close, branch_button1,branch_button2, setting_button
from bot.buttons.reply import language, back_button, ask_deliver, location_button, ask_loc_true, settings_phone_btn,closest_branch
from bot.buttons.language import uzb_lang, eng_lang, lang
from bot.dispatcher import dp
from aiogram.dispatcher import FSMContext
from DB.config import Pg
import json
import requests

# @dp.message_handler(lambda msg: msg.text in [lang.get(uzb_lang).get("back"), lang.get(eng_lang).get("back")], state="main")
@dp.message_handler(commands="start")
async def start_handlers(msg: types.Message, state: FSMContext):
    obj = Pg()
    result = obj.check_user(msg.from_user.id)
    if not result:
        obj.add(msg.from_user.id, msg.from_user.first_name, msg.from_user.username)
    await state.set_state("lang")
    await msg.answer(" Tilni tanlang⬇️ || Choose language⬇️  ", reply_markup=language())




@dp.message_handler(lambda msg : msg.text in [lang.get(uzb_lang).get("back"), lang.get(eng_lang).get("back")] , state = "back")
@dp.message_handler(lambda msg : msg.text in [lang.get(uzb_lang).get("back"), lang.get(eng_lang).get("back")] , state = "saved_contact")
@dp.message_handler(lambda msg : msg.text in [lang.get(uzb_lang).get("back"), lang.get(eng_lang).get("back")] , state = "manzil")
@dp.message_handler(lambda msg : msg.text in [lang.get(uzb_lang).get("back"), lang.get(eng_lang).get("back")] , state = "location")
@dp.message_handler(lambda msg : msg.text in [lang.get(uzb_lang).get("back"), lang.get(eng_lang).get("back")] , state = "buttons")
@dp.message_handler(lambda msg : msg.text in [lang.get(uzb_lang).get("back"), lang.get(eng_lang).get("back")] , state = "locc")
@dp.message_handler(lambda msg: msg.text in [uzb_lang, eng_lang], state="lang")
async def menu_handler(msg:types.Message, state: FSMContext):
    if msg.text == uzb_lang or msg.text == eng_lang:
        async with state.proxy() as dt: dt["lang"] = msg.text
        data = lang.get(msg.text)

    else:
        async with state.proxy() as dt:
            pass

        data = lang.get(dt.get("lang"))
    link = f"""{data.get("welcome_text").format(msg.from_user.first_name)}\n\n[Oqtepa Lavash menu](https://telegra.ph/Taomnoma-09-02)"""
    await state.set_state("main")
    await msg.answer(data.get("ask"), reply_markup=back_button(data))
    await msg.answer(link,parse_mode="Markdown", reply_markup=menu_button(data))


#menyudagi buttonlaga kirish

@dp.callback_query_handler(lambda call: call.data  in list(lang.get(uzb_lang).keys()) + list(lang.get(eng_lang).keys()), state="main")
async def about_handler(callback: types.CallbackQuery, state: FSMContext):

    async with state.proxy() as data:
        user_lang = data.get("lang")
    data = lang.get(user_lang)
    if callback.data == "order":
        text = data.get("buyurtma turi")
        await callback.message.answer(text, reply_markup=ask_deliver(data))
        await state.set_state("back")
        await state.set_state("locc")
        # await state.set_state("locc2")
        await callback.message.delete()


    elif callback.data == "about_us_info":
        text = data.get("about_us_info")
        await callback.message.answer(text, reply_markup=back_button(data))
        await callback.message.delete()
        await state.set_state("back")


    elif callback.data == "my_last_order":
        text = data.get("my_last_order")
        await callback.message.answer(text,reply_markup=close(data))
        await state.set_state("back")
        await state.set_state("close")
        await callback.message.delete()


    elif callback.data == "branch_names":

        link = f"""{data.get("about_branches")}[Oqtepa Lavash menu](https://telegra.ph/Taomnoma-09-02)"""
        await callback.message.answer(link, parse_mode="Markdown", reply_markup=branch_button1(data))
        await callback.message.delete()
        await state.set_state("back")
        await state.set_state("manzil")
        # await state.set_state("keyingisi")


    elif callback.data == "rewiev":
        await callback.message.answer("Fikrlaringizni yozing")
        await state.set_state("fikr")
        await callback.message.delete()



    elif callback.data == "settings":
        obj = Pg()
        phone_number = obj.show_num(callback.from_user.id)
        lat=obj.user_latitude(callback.from_user.id)
        long = obj.user_longtitude(callback.from_user.id)
        url = "https://geocode-maps.yandex.ru/1.x/"
        params = {
            "apikey": "f3d55107-23fa-41bf-88c4-51b44aaf6781",
            "geocode": f"{long[0]},{lat[0]}",
            "lang": "en_US",
            "format": "json"
        }

        response = requests.get(url, params=params)
        data_p = response.json()
        city = data_p['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
            'GeocoderMetaData']['Address']['Components'][1]['name']
        await callback.message.answer(data.get("info").format(user_lang, f"+{phone_number[0]}",city), reply_markup=setting_button(data))
        await callback.message.delete()
        await state.set_state("back")
        await state.set_state("buttons")




#filiallarni qolganlarini korish
@dp.callback_query_handler(lambda call: call.data == "next1", state="manzil")
async def pagination_handler(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        user_lang = data.get("lang")
    data = lang.get(user_lang)

    photo = f"""{data.get("about_branches_page_two")}[Oqtepa Lavash menu](https://telegra.ph/Taomnoma-09-02)"""
    await call.message.answer(photo, parse_mode="Markdown", reply_markup=branch_button2(data))
    await call.message.delete()
    # await state.set_state("back")


@dp.callback_query_handler(lambda call: call.data == "eng_yaqin_filial", state="manzil")
async def pagination_handler(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        user_lang = data.get("lang")
    data = lang.get(user_lang)
    text = data.get("closest_branch_loc")
    await call.message.answer(text, reply_markup=closest_branch(data))
    await state.set_state("near_loc")


@dp.message_handler(content_types=types.ContentTypes.LOCATION , state = "near_loc")
async def cach_location(message: types.Message, state:FSMContext):
    long = message.location.longitude
    lat = message.location.latitude
    obj = Pg()
    k=obj.closest_branch_location(lat,long)
    print(k)
    await state.set_state("back")







#comment gruppaga yozish
@dp.message_handler(state = 'fikr')
async def otziv_handler(message: types.Message, state : FSMContext):
    async with state.proxy() as data:
        user_lang = data.get("lang")
    data = lang.get(user_lang)
    text = message.text
    await state.set_state("back")
    if not text == "⬅️ Ortga":
        await message.forward(-1001836071723,text)
    await message.answer("Izoh uchun raxmat",reply_markup=back_button(data))
    await message.delete()


#main menu

@dp.callback_query_handler(lambda call: call.data in list(lang.get(uzb_lang).keys()) + list(lang.get(eng_lang).keys()), state="close")
async def close_handler(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        user_lang = data.get("lang")
    data = lang.get(user_lang)
    logo = f"""{data.get("welcome_text").format(call.message.from_user.first_name)}[Oqtepa Lavash menu](https://telegra.ph/Taomnoma-09-02)"""
    await state.set_state("main")
    await call.message.answer(data.get("ask"), reply_markup=back_button(data))
    await call.message.answer(logo,parse_mode="Markdown" ,reply_markup=menu_button(data))


#databasedagi filiallarni lokatsiyasini jonatadi

@dp.callback_query_handler(lambda call: call.data in list(lang.get(uzb_lang).keys()) + list(lang.get(eng_lang).keys()), state="manzil")
async def address_handler(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        user_lang = data.get("lang")
    data = lang.get(user_lang)
    obj = Pg()
    result = obj.branch_name(call.data)
    if result is not None and call.data == result[0]:
        await call.message.delete()
        latitude = obj.latitude(call.data)[0]
        longitude = obj.longtitude(call.data)[0]
        text1 = obj.branch_name(call.data)[0]
        text = data.get("about_branches")
        # photo = "[Oqtepa Lavash menu](https://telegra.ph/Taomnoma-09-02)" lokatsiyani linkini shunaqa saqlasa boladi databasega
        await state.set_state("manzil")
        await call.bot.send_venue(call.from_user.id, latitude, longitude,text1, address=text,  reply_markup=branch_button1(data))



