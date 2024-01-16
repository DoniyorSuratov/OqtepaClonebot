from aiogram import types
from bot.buttons.reply import language, back_button, ask_deliver, location_button, ask_loc_true, user_num
from bot.buttons.language import uzb_lang, eng_lang, lang
from bot.dispatcher import dp
from aiogram.dispatcher import FSMContext
from DB.config import Pg
import requests


# locatsiyani sorash

@dp.message_handler(lambda msg: "Eltib berish" in msg.text, state="locc")
async def location_handler(msg: types.Message, state: FSMContext):
    print(msg.text)
    async with state.proxy() as data:
        user_lang = data.get("lang")
    data = lang.get(user_lang)
    text = data.get("ask_location")
    await state.set_state("location")
    await msg.answer(text, reply_markup=location_button(data), parse_mode="Markdown")


# locatsiyani databasega saqlidi

@dp.message_handler(content_types=types.ContentTypes.LOCATION, state="adresga")
@dp.message_handler(content_types=types.ContentTypes.LOCATION, state="back")
@dp.message_handler(content_types=types.ContentTypes.LOCATION, state="location")
async def cach_location(message: types.Message, state: FSMContext):
    obj = Pg()
    long = message.location.longitude
    lat = message.location.latitude
    obj.insert_longtitude(user_id=message.from_user.id, latitude=lat, longtitude=long)

    # locatsiyaga sozlar bilan aniqlik kiritadi

    lati = obj.user_latitude(message.from_user.id)
    longi = obj.user_longtitude(message.from_user.id)
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": "f3d55107-23fa-41bf-88c4-51b44aaf6781",
        "geocode": f"{longi[0]},{lati[0]}",
        "lang": "ru_RU",
        "format": "json"
    }
    response = requests.get(url, params=params)
    data_p = response.json()
    city = data_p['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
        'GeocoderMetaData']['Address']['formatted']
    async with state.proxy() as data:
        user_lang = data.get("lang")
    data = lang.get(user_lang)
    text = data.get("ask_loc_true").format(city)
    await message.answer(text, reply_markup=ask_loc_true(data), parse_mode="Markdown")
    await state.set_state("so'rov")


# locatsiya soragandan keyingi yo'q knopkasi

@dp.message_handler(state="so'rov")
async def answer_yes_handler(msg: types.Message, state: FSMContext):
    if msg.text == "❎ Yo'q":
        async with state.proxy() as data:
            user_lang = data.get("lang")
        data = lang.get(user_lang)
        text = data.get("ask_location")
        await msg.answer(text, reply_markup=location_button(data), parse_mode="Markdown")
        await state.set_state("adresga")
        await state.set_state("back")

        print(msg.text)
    if msg.text == "✅ HA":
        async with state.proxy() as data:
            user_lang = data.get("lang")
        data = lang.get(user_lang)
        text = data.get("aniq_manzil")
        await msg.answer(text, parse_mode="Markdown")
        await state.set_state("wait_for_message")


@dp.message_handler(state="wait_for_message")
async def wait_for_message(msg: types.Message, state: FSMContext):
    obj = Pg()
    user_message = "Dostavka => " + msg.text  # Save the user's message
    id = msg.from_user.id
    obj.user_info_add(id, user_message)

    async with state.proxy() as data:
        user_lang = data.get("lang")
    data = lang.get(user_lang)
    text = data.get("Ask_contact")
    await msg.answer(text, reply_markup=user_num(data))
    await state.set_state("back")
    await state.set_state("contact1")
