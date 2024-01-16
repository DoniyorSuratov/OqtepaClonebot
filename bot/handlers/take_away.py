from aiogram import types
from bot.buttons.reply import language, back_button, ask_deliver, location_button, ask_loc_true, user_num, name_btn
from bot.buttons.language import uzb_lang, eng_lang, lang
from bot.dispatcher import dp
from aiogram.dispatcher import FSMContext
from DB.config import Pg
import requests


@dp.message_handler(lambda msg: msg.text == "🚶 Borib olish", state="locc")
async def location_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user_lang = data.get("lang")
    data = lang.get(user_lang)
    print(msg.text)
    text=data.get("borib olish")
    await state.set_state("location1")
    await msg.answer(text, reply_markup=location_button(data), parse_mode="Markdown")


@dp.message_handler(content_types=types.ContentTypes.LOCATION , state = "location1")
async def cach_location(message: types.Message, state:FSMContext):
    obj = Pg()
    long = message.location.longitude
    lat = message.location.latitude
    obj.insert_longtitude(user_id=message.from_user.id, latitude=lat, longtitude=long )

#locatsiyaga sozlar bilan aniqlik kiritadi

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
    data= lang.get(user_lang)
    text = data.get("ask_loc_true").format(city)
    await message.answer(text, reply_markup=ask_loc_true(data), parse_mode="Markdown")
    await state.set_state("ask_name")
    PLACES_API_KEY = "AIzaSyA6ZE783Act7puvme3pVM0mBTuNDrjjIc8"
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lati},{longi}&radius=2000&type=restaurant&key={PLACES_API_KEY}"
    response = requests.get(url)
    data = response.json()
    restaurants = data.get("results", [])
    if not restaurants:
        await message.answer("sizga 2 km radiusda restoranlar topilmadi")
        return

    response_message = "2 km radiusingizdagi restoranlar:\n"
    for restaurant in restaurants:
        name = restaurant.get("name", "Unknown")
        address = restaurant.get("vicinity", "Adresi topilmadi")
        response_message += f"\n{name}\nAdres: {address}\n"

    await message.answer(response_message)









@dp.message_handler(state="ask_name")
async def answer_yes_handler (msg: types.Message, state:FSMContext):
    if msg.text == "❎ Yo'q":
        async with state.proxy() as data:
            user_lang = data.get("lang")
        data = lang.get(user_lang)
        text=data.get("ask_location")
        await msg.answer(text, reply_markup=location_button(data), parse_mode="Markdown")
        await state.set_state("adresga")
        await state.set_state("back")

        print(msg.text)
    if msg.text == "✅ HA":
        async with state.proxy() as data:
            user_lang = data.get("lang")
        data = lang.get(user_lang)
        data['username'] = msg.from_user.username
        print(data)
        text = data.get("name")
        await msg.answer(text, reply_markup=name_btn(data), parse_mode="Markdown")
        await state.set_state("wait_for_message2")


@dp.message_handler(state="wait_for_message2")
async def wait_for_message(msg: types.Message, state: FSMContext):
    obj = Pg()
    user_message = "Take away => " + msg.text  # Save the user's message
    id=msg.from_user.id
    obj.user_info_add(id, user_message)

    async with state.proxy() as data:
        user_lang = data.get("lang")
    data = lang.get(user_lang)
    text = data.get("Ask_contact")
    await msg.answer(text, reply_markup=user_num(data))
    await state.set_state("back")
    await state.set_state("contact1")


