from aiogram import types
from bot.buttons.inline import menu_button, close, branch_button1,branch_button2, setting_button
from bot.buttons.reply import language, back_button, ask_deliver, location_button, ask_loc_true, settings_phone_btn
from bot.buttons.language import uzb_lang, eng_lang, lang
from bot.dispatcher import dp
from aiogram.dispatcher import FSMContext
from DB.config import Pg
from bot.buttons.reply import settings_phone_btn

@dp.callback_query_handler(lambda call: call.data  in list(lang.get(uzb_lang).keys()) + list(lang.get(eng_lang).keys()), state="buttons")
@dp.callback_query_handler(lambda call: call.data  in list(lang.get(uzb_lang).keys()) + list(lang.get(eng_lang).keys()), state="back")
async def phone_handler(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        user_lang = data.get("lang")
    data = lang.get(user_lang)
    if call.data == "phone_number":
        text=data.get("phone_ask")
        await call.message.answer(text, reply_markup = settings_phone_btn(data), parse_mode="Markdown")
        await state.set_state("next")
    await state.set_state("back")
@dp.message_handler(content_types=types.ContentTypes.CONTACT, state="next")
async def cach_contact_handler(msg: types.Message, state:FSMContext):
    obj = Pg()
    phone_num = msg.contact.phone_number
    user_id = msg.from_user.id
    obj.add_contact(user_id, phone_num)
    await state.set_state("back")