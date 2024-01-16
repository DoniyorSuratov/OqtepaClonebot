from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


def menu_button(data):
    design = [
        [InlineKeyboardButton(data.get("order"), callback_data="order")],
        [InlineKeyboardButton(data.get("about_us"),callback_data="about_us_info"),InlineKeyboardButton(data.get("my_orders"), callback_data="my_last_order")],
        [InlineKeyboardButton(data.get("branches"), callback_data="branch_names")],
        [InlineKeyboardButton(data.get("rewiev"), callback_data="rewiev"),InlineKeyboardButton(data.get("settings"), callback_data="settings")],
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm

def close(data):
    design = [
        [InlineKeyboardButton(data.get("goback"), callback_data="x_back")],
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm


def branch_button1(data):
    design = [
        [InlineKeyboardButton(data.get("closest_branch"), callback_data="eng_yaqin_filial")],
          [InlineKeyboardButton(data.get("next_button"), callback_data="next1")],
        [InlineKeyboardButton(data.get("Algoritm"), callback_data="🏠 Algoritm"),
         InlineKeyboardButton(data.get("Andijon-1"), callback_data="🏠 Andijon-1")],
        [InlineKeyboardButton(data.get("Bektemir"), callback_data="🏠 Bektemir"),
         InlineKeyboardButton(data.get("Beruniy"), callback_data="🏠 Beruniy")],
        [InlineKeyboardButton(data.get("Bodomzor"), callback_data="🏠 Bodomzor"),
         InlineKeyboardButton(data.get("Chigatoy"), callback_data="🏠 Chigatoy")],
        [InlineKeyboardButton(data.get("Chilonzor 19"), callback_data="🏠 Chilonzor 19"),
         InlineKeyboardButton(data.get("Chilonzor metro"), callback_data="🏠 Chilonzor metro")],
        [InlineKeyboardButton(data.get("Chinoz"), callback_data="🏠 Chinoz"),
         InlineKeyboardButton(data.get("Chirchiq"), callback_data="🏠 Chirchiq")]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm

def branch_button2(data):
    design = [
        [InlineKeyboardButton(data.get("main_menu1"), callback_data="asosiy_menu"),
         InlineKeyboardButton(data.get("closest_branch1"), callback_data="eng_yaqin_filial")],
        [InlineKeyboardButton(data.get("back_button1"), callback_data="back_button1"),InlineKeyboardButton(data.get("next_button1"), callback_data="cb_next_button1")],
        [InlineKeyboardButton(data.get("Hadra"), callback_data="Hadra"),
         InlineKeyboardButton(data.get("Chopon ota"), callback_data="Chopon ota")],
        [InlineKeyboardButton(data.get("Compas"), callback_data="Compas"),
         InlineKeyboardButton(data.get("Depomall"), callback_data="Depomall")],
        [InlineKeyboardButton(data.get("Drujba"), callback_data="Drujba"),
         InlineKeyboardButton(data.get("Farg'ona-1"), callback_data="Farg'ona-1")],
        [InlineKeyboardButton(data.get("Farg'ona-2"), callback_data="Farg'ona-2"),
         InlineKeyboardButton(data.get("Farxadskiy"), callback_data="Farxadskiy")],
        [InlineKeyboardButton(data.get("Goldenlife"), callback_data="Goldenlife"),
         InlineKeyboardButton(data.get("Gulzor"), callback_data="Gulzor")]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm

def setting_button(data):
    design = [
        [InlineKeyboardButton(data.get("phone"), callback_data="phone_number"),
         InlineKeyboardButton(data.get("city"), callback_data="city")],
        [InlineKeyboardButton(data.get("main_menu"), callback_data="main_menu")]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm

def menu_show_btn(data):
    design = [
        [InlineKeyboardButton(data.get("Qarsildoq Jo'jalar"), callback_data="qarsildoq jo'jalar"),
         InlineKeyboardButton(data.get("Salatlar"), callback_data="salatlar")],
        [InlineKeyboardButton(data.get("Ichimliklar"), callback_data="ichimliklar"),
        InlineKeyboardButton(data.get("Souslar"), callback_data="souslar")],
        [InlineKeyboardButton(data.get("Lavashlar"), callback_data="lavashlar"),
         InlineKeyboardButton(data.get("Setlar"), callback_data="setlar")],
        [InlineKeyboardButton(data.get("Pistalar"), callback_data="pistalar"),
         InlineKeyboardButton(data.get("Burger va donerlar"), callback_data="burger va donerlar")],
        [InlineKeyboardButton(data.get("Hot doglar"), callback_data="hot doglar"),
         InlineKeyboardButton(data.get("Haggi"), callback_data="haggi")],
        [InlineKeyboardButton(data.get("Klab sendvich"), callback_data="klab sendvich"),
         InlineKeyboardButton(data.get("Sneklar"), callback_data="sneklar")],
        [InlineKeyboardButton(data.get("Asosiy menu"), callback_data="asosiy menu")],

    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm


def qarsildoq_joja(data):
    design = [
        [InlineKeyboardButton(data.get("Jo'ja box"), callback_data = "jo'ja box"),
         InlineKeyboardButton(data.get("Stips 5 dona"), callback_data="stips 5 dona")],
        [InlineKeyboardButton(data.get("Stips 3 dona"), callback_data="stips 3 dona"),
            InlineKeyboardButton(data.get("Bayts"), callback_data="bayts")],
        [InlineKeyboardButton(data.get("back_button1"), callback_data="back_main")]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm


def salatlar_btn(data):
    design = [
        [InlineKeyboardButton(data.get("Mujskoy kapriz"), callback_data = "mujskoy kapriz"),
         InlineKeyboardButton(data.get("Sezar"), callback_data="sezar")],
        [InlineKeyboardButton(data.get("back_button1"), callback_data="back")]

    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm

def ichimliklar_btn(data):
    design = [
        [InlineKeyboardButton(data.get("Qaynoq ichimliklar"), callback_data = "qaynoq ichimliklar"),
         InlineKeyboardButton(data.get("Yahna ichimliklar"), callback_data="yahna ichimliklar")],
        [InlineKeyboardButton(data.get("back_button1"), callback_data="back")]

    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm


def souslar_btn(data):
    design = [
        [InlineKeyboardButton(data.get("Ketchup"), callback_data = "ketchup"),
         InlineKeyboardButton(data.get("Chili sous"), callback_data="chili sous")],
        [InlineKeyboardButton(data.get("Pishloqli sous"), callback_data="pishloqli sous"),
         InlineKeyboardButton(data.get("Oq sous"), callback_data="oq sous")],
        [InlineKeyboardButton(data.get("back_button1"), callback_data="back")]

    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm

def lavashlar_btn(data):
    design = [
        [InlineKeyboardButton(data.get("Orginal lavash"), callback_data="orginal lavash"),
         InlineKeyboardButton(data.get("Orginal kichik lavash"), callback_data="orginal kichik lavash")],
        [InlineKeyboardButton(data.get("Pishloqli lavash"), callback_data="pishloqli lavash"),
         InlineKeyboardButton(data.get("Pishloqli kichik lavash"), callback_data="pishloqli kichik lavash")],
        [InlineKeyboardButton(data.get("Tandir lavash"), callback_data="tandir lavash"),
         InlineKeyboardButton(data.get("Pishloqli tandir lavash"), callback_data="pishloqli tandir lavash")],
        [InlineKeyboardButton(data.get("back_button1"), callback_data="back")]

    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm


def setlar_btn(data):
    design = [
        [InlineKeyboardButton(data.get("Oqtepa Seti"), callback_data = "oqtepa Seti"),
         InlineKeyboardButton(data.get("Juftlik Seti"), callback_data="juftlik Seti")],
        [InlineKeyboardButton(data.get("Baraka Seti"), callback_data="baraka Seti")],
        [InlineKeyboardButton(data.get("back_button1"), callback_data="back")]

    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm


def pitsalar_btn(data):
    design = [
        [InlineKeyboardButton(data.get("Assorti pitsa"), callback_data = "assorti pitsa"),
         InlineKeyboardButton(data.get("Pepperoni pitsa"), callback_data="pepperoni pitsa")],
        [InlineKeyboardButton(data.get("Go'shtli pitsa"), callback_data="go'shtli pitsa"),
         InlineKeyboardButton(data.get("Qazi pitsa"), callback_data="qazi pitsa")],
        [InlineKeyboardButton(data.get("Tovuqli pitsa"), callback_data="tovuqli pitsa")],
        [InlineKeyboardButton(data.get("back_button1"), callback_data="back")]

    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm


def burger_doner_btn(data):
    design = [
        [InlineKeyboardButton(data.get("Gamburger"), callback_data="gamburger"),
         InlineKeyboardButton(data.get("Chizburger"), callback_data="chizburger")],
        [InlineKeyboardButton(data.get("Big burger"), callback_data="big burger"),
         InlineKeyboardButton(data.get("Big Chizburger"), callback_data="big chizburger")],
        [InlineKeyboardButton(data.get("Big doner"), callback_data="big doner"),
         InlineKeyboardButton(data.get("Shaurma"), callback_data="Shaurma")],
        [InlineKeyboardButton(data.get("back_button1"), callback_data="back")]

    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm


def hot_doglar_btn(data):
    design = [
        [InlineKeyboardButton(data.get("Hot-dog"), callback_data = "hot-dog"),
         InlineKeyboardButton(data.get("Pishloqli Hot-dog"), callback_data="pishloqli Hot-dog")],
        [InlineKeyboardButton(data.get("Shohona Hot-dog"), callback_data="shohona Hot-dog")],
        [InlineKeyboardButton(data.get("back_button1"), callback_data="back")]

    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm


def haggi_btn(data):
    design = [
        [InlineKeyboardButton(data.get("Minus"), callback_data = "minus"),
         InlineKeyboardButton(data.get("Son"), callback_data="son"),
         InlineKeyboardButton(data.get("Plus"), callback_data="plus")],
        [InlineKeyboardButton(data.get("Savatga qo'shish"), callback_data="savatga qo'shish")],
        [InlineKeyboardButton(data.get("back_button1"), callback_data="back")]

    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm

def klab_sendvich_btn(data):
    design = [
        [InlineKeyboardButton(data.get("Minus"), callback_data = "minus"),
         InlineKeyboardButton(data.get("Son"), callback_data="son"),
         InlineKeyboardButton(data.get("Plus"), callback_data="plus")],
        [InlineKeyboardButton(data.get("Savatga qo'shish"), callback_data="savatga qo'shish")],
        [InlineKeyboardButton(data.get("back_button1"), callback_data="back")]

    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm

def sneklar_btn(data):
    design = [
        [InlineKeyboardButton(data.get("Kartoshka fri"), callback_data="kartoshka fri"),
         InlineKeyboardButton(data.get("Kartoshka fri katta"), callback_data="kartoshka fri katta")],
        [InlineKeyboardButton(data.get("Kartoshka fri kichkina"), callback_data="kartoshka fri kichkina"),
         InlineKeyboardButton(data.get("Jaydari kartoshka"), callback_data="jaydari kartoshka")],
        [InlineKeyboardButton(data.get("Non"), callback_data="non"),
         InlineKeyboardButton(data.get("Xalapenyo"), callback_data="xalapenyo")],
        [InlineKeyboardButton(data.get("back_button1"), callback_data="back_to_one")]

    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm