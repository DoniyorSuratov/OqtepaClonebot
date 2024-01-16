from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

from bot.buttons.language import uzb_lang, eng_lang


def language():
    design = [
        [uzb_lang, eng_lang]

    ]
    markup = ReplyKeyboardMarkup(design, resize_keyboard=True, one_time_keyboard=True)
    return markup


def back_button(data):
    design = [
        [KeyboardButton(data.get("back"))],
    ]
    markup = ReplyKeyboardMarkup(design, resize_keyboard=True, one_time_keyboard=True)
    return markup

def ask_deliver(data):
    design = [
        [KeyboardButton(data.get("🚴‍♂️ Eltib berish")), KeyboardButton(data.get("🚶 Borib olish"))],
        [KeyboardButton(data.get("back"))]
    ]
    markup = ReplyKeyboardMarkup(design, resize_keyboard=True, one_time_keyboard=True)
    return markup

def location_button(data):
    design = [
        [KeyboardButton(data.get("location"), request_location= True)],
        [KeyboardButton(data.get("back"))]
    ]
    markup = ReplyKeyboardMarkup(design, resize_keyboard=True, one_time_keyboard=True)
    return markup

def ask_loc_true(data):
    design = [
        [KeyboardButton(data.get("yes")), KeyboardButton(data.get("no"))]
    ]
    markup = ReplyKeyboardMarkup(design, resize_keyboard=True, one_time_keyboard=True)
    return markup

def user_num(data):
    design = [
        [KeyboardButton(data.get("send_contact"), request_contact=True)],
        [KeyboardButton(data.get("back"))]
    ]
    markup = ReplyKeyboardMarkup(design, one_time_keyboard=True, resize_keyboard=True)
    return markup

def settings_phone_btn(data):
    design = [
        [KeyboardButton(data.get("phone_change"),request_contact=True)],
        [KeyboardButton(data.get("back"))],

    ]
    markup = ReplyKeyboardMarkup(design, one_time_keyboard=True, resize_keyboard=True)
    return markup

def closest_branch(data):
    design = [
        [KeyboardButton(data.get("location"), request_location=True)],
        [KeyboardButton(data.get("back"))]
    ]
    markup = ReplyKeyboardMarkup(design, one_time_keyboard=True, resize_keyboard=True)
    return markup

def name_btn(data):
    design = [
        [KeyboardButton(data.get("username"))],
        [KeyboardButton(data.get("back"))]
    ]
    markup = ReplyKeyboardMarkup(design, one_time_keyboard=True, resize_keyboard=True)
    return markup
