import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}

phone_facturer = ["ACER",
"ALCATEL",
"ALLVIEW",
"AMAZON",
"AMOI",
"APPLE",
"ARCHOS",
"ASUS",
"AT&T",
"BENEFO,N",
"BENQ",
"BENQ-SIEMENS",
"BIRD",
"BLACKBERRY",
"BLACKVIEW",
"BLU",
"BOSCH",
"BQ",
"CASIO",
"CAT",
"CELKON",
"CHEA",
"COOLPAD",
"DELL",
"EMPORIA",
"ENERGIZER",
"ERICSSON",
"ETEN",
"FAIRPHONE",
"FUJITSU SIEMENS",
"GARMIN-ASUS",
"GIGABYTE",
"GIONEE",
"GOOGLE",
"HAIER",
"HONOR",
"HP",
"HTC",
"I-MATE",
"I-MOBILE",
"ICEMOBILE",
"INFINIX",
"INNOSTREAM",
"INQ",
"INTEX",
"JOLLA",
"KARBONN",
"KYOCERA",
"LAVA",
"LEECO",
"LG",
"MAXON",
"MAXWEST",
"MEIZU",
"MICROMAX",
"MICROSOFT",
"MITAC",
"MITSUBISHI",
"MODU",
"MOTOROLA",
"MWG",
"NEC",
"NEONODE",
"NIU",
"NOKIA",
"NVIDIA",
"O2",
"ONEPLUS",
"OPPO",
"ORANGE",
"PALM",
"PANASONIC",
"PANTECH",
"PARLA",
"PHILIPS",
"PLUM",
"POSH",
"PRESTIGIO",
"QMOBILE",
"QTEK",
"RAZER",
"REALME",
"SAGEM",
"SAMSUNG",
"SENDO",
"SEWON",
"SHARP",
"SIEMENS",
"SONIM",
"SONY",
"SONY ERICSSON",
"SPICE",
"T-MOBILE",
"TCL",
"TECNO",
"TEL.ME",
"TELIT",
"THURAYA",
"TOSHIBA",
"ULEFONE",
"UNNECTO",
"VERTU",
"VERYKOOL",
"VIVO",
"VK MOBILE",
"VODAFONE",
"WIKO",
"WND",
"XCUTE",
"XIAOMI",
"XOLO",
"YEZZ",
"YOTA",
"YU",
"ZTE",
"LG",
"Fossil",
"Polar",
"Garmin",
"Fitbit",
"ASUSTeK ",
"Acer",
"Alienware",
"Logitech",
"SteelSeries",
"Zowie",
"Roccat",
"Audio-Technica",
"Beyerdynamic",
"Sennheiser",
"Behringer",
"Neumann",
"Skullcandy"
]

def search_string_top(desc):
    for i in range(0,len(phone_facturer)):
        phone_facturer[i] = phone_facturer[i].title()
    search_string = desc

    page = requests.get("https://www.google.com/search?q=" + search_string, headers=headers)
    soup = BeautifulSoup(page.content)
    import re

    # links = soup.findAll("a")
    # for link in links:
    #     print(link)
    final = []
    output_link = []
    increment = 0
    phone_rev = {}
    for link in soup.find_all("a", href=re.compile("(htt.*://.*)")):
        link = re.split(":(?=http)", link["href"].replace("/url?q=", ""))
        # if "pd" in link[0]:
        link[0] = link[0][link[0].find("http"):]
        if "google" not in link[0]:
            page = requests.get(link[0], headers=headers)
            soup = BeautifulSoup(page.content)
            for paragraph in soup.find_all("p"):
                for y in phone_facturer:
                    if y in paragraph.text:
                        if len(paragraph.text) >50:
                            if y in phone_rev.keys():
                                phone_rev[y].append(paragraph.text)
                                output_link.append(link[0])
                            else:
                                phone_rev[y] = [paragraph.text]
                                output_link.append(link[0])

            increment +=1
        if increment ==15:
            break
    return (phone_rev,output_link)