# Emojizones
**Emojizones** helps you convert one datetime in one time zone to another, using the emojiis you are used to from your iPhone. Never have time zone conversion been this easy!

## Installation

```bash
pip install emojizones
```

## Getting started

```python
from emojizones import convert
from datetime import datetime

# Here we have a naive datetime without a time zone
from_time = datetime(2020, 3, 7, 0, 0, 0)

# Now we use the emojizones.convert-method
to_time = convert(
    from_time,
    "🗻",  # Mount Fuji, Japan --> Asia/Tokyo
    "🗽"   # Statue of Libery, New York --> America/New_York
)
print(to_time)
# 2020-03-06 10:00:00
```

Note how time has shifted 14 hours back, corresponding to the difference between Japan (UTC+9) and New York (UTC-5).

Couldn't be simpler!

## Technical notes

1. **Country flags** make this project quite usable, all countries are represented!

    ```python
    convert(
        "2020-03-07 00:00:00",
        "🇸🇪",  # Sweden --> Europe/Stockholm
        "🇫🇮"   # Finland --> Europe/Helsinki
    )
    # 2020-03-07 01:00:00
    ```

2. Some contries have multiple time zones, but no emoji to represent them. Luckily, you can use emoji aritmetics to append a UTC offset to your time zone!

    ```python
    convert(
        "2020-03-07 00:00:00",
        "🗽",  # Sweden --> Europe/Stockholm
        "🗽➕4️⃣"   # Finland --> Europe/Helsinki
    )
    # 2020-03-07 04:00:00
    ```

    You can even do emoji aritmetic with complex statments... Here's somthing that evaluates to Europe/Paris + 5 hours.

    ```python
    convert(
        "2020-03-07 00:00:00", 
        "🥖", 
        "🥖➕4️⃣✖3️⃣➗2️⃣➖1️⃣"
    )
    # 2020-03-07 05:00:00
    ```

3. This means you can use this as a calculator if you want! Let's say you want to calculate `4 * 3`.

    ```python
    from_time = datetime(2000, 1, 1, 0, 0, 0)
    time_difference = convert(from_time, "👨‍🎤", "👨‍🎤➕4️⃣✖3️⃣").replace(tzinfo=None) - from_time
    hours = time_difference.total_seconds() / (60 * 60)
    hours
    # 12
    ```

4. To lookup what timezone a specific emoji corresponds to, use the `emoji_lookup` method.

    ```python
    from emojizones import emoji_lookup

    emoji_lookup("🥖")  # --> "Europe/Paris"
    emoji_lookup("🥖➕2️⃣", from_dt="2020-03-07 00:00:00")  # --> "Europe/Istanbul"
    ```

<!-- Don't add stuff after the below heading, it will be overwritten by docs_from_lookup -->
## Supported emojis

### People

| Emoji | Timezone | Comment |
|---|---|---|
| 💂 | Europe/London | British guard |
| 💂‍♂️ | Europe/London | British guard |
| 💂‍♀️ | Europe/London | British guard |
| 👨‍🎤 | Europe/London | David Bowie, born in London |
| 👩‍🎤 | Europe/London | David Bowie, born in London |
| 🧛 | Europe/Bucharest | Dracula, Transylvania, Romania |
| 🧛‍♂️ | Europe/Bucharest | Dracula, Transylvania, Romania |
| 🧛‍♀️ | Europe/Bucharest | Dracula, Transylvania, Romania |
| 👘 | Asia/Tokyo | A traditional Japanese robe that can be worn by women or men |
| 👑 | Europe/London | The Queen, Longond, Great Britain |

### Nature

| Emoji | Timezone | Comment |
|---|---|---|
| 🐲 | Asia/Shanghai | Chinese dragon |
| 🐉 | Asia/Shanghai | Chinese dragon |
| 🌍 | Africa/Kinshasa | Map centered on Africa, which has DNC as the centre |
| 🌎 | America/Guayaquil | Map centered on South America with Ecuador in the middle |
| 🌏 | Asia/Jakarta | Map centered on Jakarta, Indonesia |
| 🌧️ | Africa/Conakry | Conakry, Guinea is the place with the most rain worldwide |
| 🎋 | Asia/Tokyo | A Tanabata tree, a type of wish tree from the Japanese festival |
| 🎍 | Asia/Tokyo | A Japanese kadomatsu, traditionally placed outside homes in Japan around the New Year |

### Food Drink

| Emoji | Timezone | Comment |
|---|---|---|
| 🍊 | Africa/Casablanca | Orange-colored citrus fruit, originally from Tangier, Morocco |
| 🥐 | Europe/Paris | Croissant, France |
| 🥖 | Europe/Paris | Baguette, France |
| 🥨 | Europe/Berlin | Pretzel, Germany |
| 🥯 | Europe/Warsaw | A bagel is a bread product originating in the Jewish communities of Poland |
| 🍟 | Europe/Paris | FRENCH fries |
| 🌮 | America/Mexico_City | A Mexican or Tex-Mex taco on a hard or soft corn tortilla |
| 🌯 | America/Mexico_City | A Mexican or Tex-Mex burrito, featuring a wrapped flour tortilla |
| 🥙 | Asia/Baghdad | Kebab, In 10th-century Baghdadi cookbook Kitab al-Tabikh, there are descriptions of kabāb |
| 🍱 | Asia/Tokyo | Japanese Bento box |
| 🍘 | Asia/Tokyo | A Japanese senbei, or rice cracker, wrapped with a sheet of nori |
| 🍙 | Asia/Tokyo | A Japanese onigiri, a cone-shaped ball of white rice, a snack wrapped with a sheet of nori |
| 🍝 | Europe/Rome | A plate of Italian spaghetti with tomato sauce, as a bolognese |
| 🍢 | Asia/Tokyo | A skewer of three bites of Japanese oden, a winter dish made with fishcakes |
| 🍣 | Asia/Tokyo | Japanese sushi, generally depicted as two pieces of raw pinkish-orange fish |
| 🍥 | Asia/Tokyo | A slice of Japanese narutomaki, a ridged fishcake of processed whitefish with an pink swirl |
| 🥮 | Asia/Shanghai | Golden-brown pastry of a Chinese mooncake, traditional delicacy of the Mid-Autumn Festival |
| 🍡 | Asia/Tokyo | A Japanese sweet dumpling made from rice flour and served on a skewer. |
| 🥠 | Asia/Shanghai | Chinese fortune cookie |
| 🍵 | Asia/Tokyo | A cup of green tea, as the minty-colored Japanese matcha |
| 🍶 | Asia/Tokyo | Japanese sake, an alcoholic beverage made from rice |
| 🍾 | Europe/Paris | Campagne, France |
| 🥃 | Europe/London | Scotch, Great Britain |

### Activites

| Emoji | Timezone | Comment |
|---|---|---|
| 🏈 | America/New_York | American football, originating from Princeton University, New York |
| 🏉 | Europe/London | Rugby, is a contact team sport that originated in England |
| 🏏 | Europe/London | Cricket's rules are held in a code called the Laws of Cricket in London |

### Places

| Emoji | Timezone | Comment |
|---|---|---|
| 🗾 | Asia/Tokyo | Map of Japan |
| 🗻 | Asia/Tokyo | Mount Fuji |
| 🏣 | Asia/Tokyo | Japanese Hospital |
| 🏯 | Asia/Tokyo | Japanese Castle |
| 🗼 | Asia/Tokyo | Tokyo Tower |
| 🗽 | America/New_York | Statue of Liberty |
| 🏛️ | Europe/Athens | Classical building |
| 🕋 | Asia/Riyadh | Kaaba, A cube-shaped building located at the centre of the Mosque in Mecca |
| 🌉 | America/Los_Angeles | Golden Gate Bridge, San Fransisco |
| 🛸 | America/Los_Angeles | Area 51, US Air fource facility, Nevada |
| 💴 | Asia/Tokyo | Yen bank note, Japan |
| 💵 | America/New_York | Dollar bank note, Fort Knox, is a fortified vault building in Kentucky |
| 💶 | Europe/Berlin | Euro bank note, European Central bank, Berlin, Germany |
| 💷 | Europe/London | Pound bank note, Great Britain |
| 🗿 | Pacific/Easter | Moai, monolithic human figures carved by the Rapa Nui people on Easter Island |
| 🎑 | Asia/Tokyo | Moon Viewing Ceremony, Japan |

### Objects

| Emoji | Timezone | Comment |
|---|---|---|
| 🏺 | Europe/Athens | Amphora, as used by ancient Greeks and Romans to hold water and wine. |
| 🗺️ | Africa/Accra | Map centered on Accra, Ghana |
| 🎎 | Asia/Tokyo | Ornamental Japanese Emperor and Empress dolls |
| 🎏 | Asia/Tokyo | Japanese koinobori, decorative, carp-shaped windsocks |
| 🎐 | Asia/Tokyo | A Japanese wind chime |
| 🧧 | Asia/Shanghai | A red envelope, as gifted with money on Chinese New Year |
| 🧿 | Europe/Istanbul | Nazar Amulet, commonly used to represent Turkey and Turkish culture |
| 💸 | America/New_York | Money with Wings, Fort Knox, is a fortified vault building in Kentucky |

### Symbols

| Emoji | Timezone | Comment |
|---|---|---|
| 💮 | Asia/Tokyo | White Flower with japanese characters roughly translating to very well done |
| ♨️ | Asia/Tokyo | Hot springs, common symbol used to represent an onsen on maps in Japan |
| 🀄 | Asia/Tokyo | Mahjong Red Dragon, the red dragon tile in the game of Japanese Mahjong |
| 🎴 | Asia/Tokyo | Flower Playing Cards, a type of cards known as hanafuda cards in Japan |
| ☢️ | Europe/Kiev | Chernobyl Nuclear Power Plant, near the city of Pripyat in the north of the Ukrainian |
| ✡️ | Asia/Jerusalem | Star of David is a generally recognized symbol of modern Jewish identity and Judaism |
| 🈁 | Asia/Tokyo | Japanese “Here” Button |
| 🈂 | Asia/Tokyo | Japanese “Service Charge” Button |
| 🈷 | Asia/Tokyo | Japanese “Monthly Amount” Button |
| 🈶 | Asia/Tokyo | Japanese “Not Free of Charge” Button |
| 🈯 | Asia/Tokyo | Japanese “Reserved” Button |
| 🉐 | Asia/Tokyo | Japanese “Bargain” Button |
| 🈹 | Asia/Tokyo | Japanese “Discount” Button |
| 🈚 | Asia/Tokyo | Japanese “Free of Charge” Button |
| 🈲 | Asia/Tokyo | Japanese “Prohibited” Button |
| 🉑 | Asia/Tokyo | Japanese “Acceptable” Button |
| 🈸 | Asia/Tokyo | Japanese “Application” Button |
| 🈴 | Asia/Tokyo | Japanese “Passing Grade” Button |
| 🈳 | Asia/Tokyo | Japanese “Vacancy” Button |
| ㊗ | Asia/Tokyo | Japanese “Congratulations” Button |
| ㊙ | Asia/Tokyo | Japanese “Secret” Button |
| 🈺 | Asia/Tokyo | Japanese “Open for Business” Button |
| 🈵 | Asia/Tokyo | Japanese “No Vacancy” Button |

### Flags

| Emoji | Timezone | Comment |
|---|---|---|
| 🎌 | Asia/Tokyo | Two Japanese Flags |
| 🇦🇩 | Europe/Andorra | AD |
| 🇦🇪 | Asia/Dubai | AE |
| 🇦🇫 | Asia/Kabul | AF |
| 🇦🇬 | America/Antigua | AG |
| 🇦🇮 | America/Anguilla | AI |
| 🇦🇱 | Europe/Tirane | AL |
| 🇦🇲 | Asia/Yerevan | AM |
| 🇦🇴 | Africa/Luanda | AO |
| 🇦🇶 | Antarctica/Vostok | AQ |
| 🇦🇷 | America/Argentina/Ushuaia | AR |
| 🇦🇸 | Pacific/Pago_Pago | AS |
| 🇦🇹 | Europe/Vienna | AT |
| 🇦🇺 | Australia/Sydney | AU |
| 🇦🇼 | America/Aruba | AW |
| 🇦🇽 | Europe/Mariehamn | AX |
| 🇦🇿 | Asia/Baku | AZ |
| 🇧🇦 | Europe/Sarajevo | BA |
| 🇧🇧 | America/Barbados | BB |
| 🇧🇩 | Asia/Dhaka | BD |
| 🇧🇪 | Europe/Brussels | BE |
| 🇧🇫 | Africa/Ouagadougou | BF |
| 🇧🇬 | Europe/Sofia | BG |
| 🇧🇭 | Asia/Bahrain | BH |
| 🇧🇮 | Africa/Bujumbura | BI |
| 🇧🇯 | Africa/Porto-Novo | BJ |
| 🇧🇱 | America/St_Barthelemy | BL |
| 🇧🇲 | Atlantic/Bermuda | BM |
| 🇧🇳 | Asia/Brunei | BN |
| 🇧🇴 | America/La_Paz | BO |
| 🇧🇶 | America/Kralendijk | BQ |
| 🇧🇷 | America/Sao_Paulo | BR |
| 🇧🇸 | America/Nassau | BS |
| 🇧🇹 | Asia/Thimphu | BT |
| 🇧🇼 | Africa/Gaborone | BW |
| 🇧🇾 | Europe/Minsk | BY |
| 🇧🇿 | America/Belize | BZ |
| 🇨🇦 | America/Yellowknife | CA |
| 🇨🇨 | Indian/Cocos | CC |
| 🇨🇩 | Africa/Lubumbashi | CD |
| 🇨🇫 | Africa/Bangui | CF |
| 🇨🇬 | Africa/Brazzaville | CG |
| 🇨🇭 | Europe/Zurich | CH |
| 🇨🇮 | Africa/Abidjan | CI |
| 🇨🇰 | Pacific/Rarotonga | CK |
| 🇨🇱 | Pacific/Easter | CL |
| 🇨🇲 | Africa/Douala | CM |
| 🇨🇳 | Asia/Urumqi | CN |
| 🇨🇴 | America/Bogota | CO |
| 🇨🇷 | America/Costa_Rica | CR |
| 🇨🇺 | America/Havana | CU |
| 🇨🇻 | Atlantic/Cape_Verde | CV |
| 🇨🇼 | America/Curacao | CW |
| 🇨🇽 | Indian/Christmas | CX |
| 🇨🇾 | Asia/Nicosia | CY |
| 🇨🇿 | Europe/Prague | CZ |
| 🇩🇪 | Europe/Busingen | DE |
| 🇩🇯 | Africa/Djibouti | DJ |
| 🇩🇰 | Europe/Copenhagen | DK |
| 🇩🇲 | America/Dominica | DM |
| 🇩🇴 | America/Santo_Domingo | DO |
| 🇩🇿 | Africa/Algiers | DZ |
| 🇪🇨 | Pacific/Galapagos | EC |
| 🇪🇪 | Europe/Tallinn | EE |
| 🇪🇬 | Africa/Cairo | EG |
| 🇪🇭 | Africa/El_Aaiun | EH |
| 🇪🇷 | Africa/Asmara | ER |
| 🇪🇸 | Europe/Madrid | ES |
| 🇪🇹 | Africa/Addis_Ababa | ET |
| 🇫🇮 | Europe/Helsinki | FI |
| 🇫🇯 | Pacific/Fiji | FJ |
| 🇫🇰 | Atlantic/Stanley | FK |
| 🇫🇲 | Pacific/Pohnpei | FM |
| 🇫🇴 | Atlantic/Faroe | FO |
| 🇫🇷 | Europe/Paris | FR |
| 🇬🇦 | Africa/Libreville | GA |
| 🇬🇧 | Europe/London | GB |
| 🇬🇩 | America/Grenada | GD |
| 🇬🇪 | Asia/Tbilisi | GE |
| 🇬🇫 | America/Cayenne | GF |
| 🇬🇬 | Europe/Guernsey | GG |
| 🇬🇭 | Africa/Accra | GH |
| 🇬🇮 | Europe/Gibraltar | GI |
| 🇬🇱 | America/Thule | GL |
| 🇬🇲 | Africa/Banjul | GM |
| 🇬🇳 | Africa/Conakry | GN |
| 🇬🇵 | America/Guadeloupe | GP |
| 🇬🇶 | Africa/Malabo | GQ |
| 🇬🇷 | Europe/Athens | GR |
| 🇬🇸 | Atlantic/South_Georgia | GS |
| 🇬🇹 | America/Guatemala | GT |
| 🇬🇺 | Pacific/Guam | GU |
| 🇬🇼 | Africa/Bissau | GW |
| 🇬🇾 | America/Guyana | GY |
| 🇭🇰 | Asia/Hong_Kong | HK |
| 🇭🇳 | America/Tegucigalpa | HN |
| 🇭🇷 | Europe/Zagreb | HR |
| 🇭🇹 | America/Port-au-Prince | HT |
| 🇭🇺 | Europe/Budapest | HU |
| 🇮🇩 | Asia/Pontianak | ID |
| 🇮🇪 | Europe/Dublin | IE |
| 🇮🇱 | Asia/Jerusalem | IL |
| 🇮🇲 | Europe/Isle_of_Man | IM |
| 🇮🇳 | Asia/Kolkata | IN |
| 🇮🇴 | Indian/Chagos | IO |
| 🇮🇶 | Asia/Baghdad | IQ |
| 🇮🇷 | Asia/Tehran | IR |
| 🇮🇸 | Atlantic/Reykjavik | IS |
| 🇮🇹 | Europe/Rome | IT |
| 🇯🇪 | Europe/Jersey | JE |
| 🇯🇲 | America/Jamaica | JM |
| 🇯🇴 | Asia/Amman | JO |
| 🇯🇵 | Asia/Tokyo | JP |
| 🇰🇪 | Africa/Nairobi | KE |
| 🇰🇬 | Asia/Bishkek | KG |
| 🇰🇭 | Asia/Phnom_Penh | KH |
| 🇰🇮 | Pacific/Tarawa | KI |
| 🇰🇲 | Indian/Comoro | KM |
| 🇰🇳 | America/St_Kitts | KN |
| 🇰🇵 | Asia/Pyongyang | KP |
| 🇰🇷 | Asia/Seoul | KR |
| 🇰🇼 | Asia/Kuwait | KW |
| 🇰🇾 | America/Cayman | KY |
| 🇰🇿 | Asia/Qyzylorda | KZ |
| 🇱🇦 | Asia/Vientiane | LA |
| 🇱🇧 | Asia/Beirut | LB |
| 🇱🇨 | America/St_Lucia | LC |
| 🇱🇮 | Europe/Vaduz | LI |
| 🇱🇰 | Asia/Colombo | LK |
| 🇱🇷 | Africa/Monrovia | LR |
| 🇱🇸 | Africa/Maseru | LS |
| 🇱🇹 | Europe/Vilnius | LT |
| 🇱🇺 | Europe/Luxembourg | LU |
| 🇱🇻 | Europe/Riga | LV |
| 🇱🇾 | Africa/Tripoli | LY |
| 🇲🇦 | Africa/Casablanca | MA |
| 🇲🇨 | Europe/Monaco | MC |
| 🇲🇩 | Europe/Chisinau | MD |
| 🇲🇪 | Europe/Podgorica | ME |
| 🇲🇫 | America/Marigot | MF |
| 🇲🇬 | Indian/Antananarivo | MG |
| 🇲🇭 | Pacific/Majuro | MH |
| 🇲🇰 | Europe/Skopje | MK |
| 🇲🇱 | Africa/Bamako | ML |
| 🇲🇲 | Asia/Yangon | MM |
| 🇲🇳 | Asia/Ulaanbaatar | MN |
| 🇲🇴 | Asia/Macau | MO |
| 🇲🇵 | Pacific/Saipan | MP |
| 🇲🇶 | America/Martinique | MQ |
| 🇲🇷 | Africa/Nouakchott | MR |
| 🇲🇸 | America/Montserrat | MS |
| 🇲🇹 | Europe/Malta | MT |
| 🇲🇺 | Indian/Mauritius | MU |
| 🇲🇻 | Indian/Maldives | MV |
| 🇲🇼 | Africa/Blantyre | MW |
| 🇲🇽 | America/Tijuana | MX |
| 🇲🇾 | Asia/Kuching | MY |
| 🇲🇿 | Africa/Maputo | MZ |
| 🇳🇦 | Africa/Windhoek | NA |
| 🇳🇨 | Pacific/Noumea | NC |
| 🇳🇪 | Africa/Niamey | NE |
| 🇳🇫 | Pacific/Norfolk | NF |
| 🇳🇬 | Africa/Lagos | NG |
| 🇳🇮 | America/Managua | NI |
| 🇳🇱 | Europe/Amsterdam | NL |
| 🇳🇴 | Europe/Oslo | NO |
| 🇳🇵 | Asia/Kathmandu | NP |
| 🇳🇷 | Pacific/Nauru | NR |
| 🇳🇺 | Pacific/Niue | NU |
| 🇳🇿 | Pacific/Chatham | NZ |
| 🇴🇲 | Asia/Muscat | OM |
| 🇵🇦 | America/Panama | PA |
| 🇵🇪 | America/Lima | PE |
| 🇵🇫 | Pacific/Tahiti | PF |
| 🇵🇬 | Pacific/Port_Moresby | PG |
| 🇵🇭 | Asia/Manila | PH |
| 🇵🇰 | Asia/Karachi | PK |
| 🇵🇱 | Europe/Warsaw | PL |
| 🇵🇲 | America/Miquelon | PM |
| 🇵🇳 | Pacific/Pitcairn | PN |
| 🇵🇷 | America/Puerto_Rico | PR |
| 🇵🇸 | Asia/Hebron | PS |
| 🇵🇹 | Europe/Lisbon | PT |
| 🇵🇼 | Pacific/Palau | PW |
| 🇵🇾 | America/Asuncion | PY |
| 🇶🇦 | Asia/Qatar | QA |
| 🇷🇪 | Indian/Reunion | RE |
| 🇷🇴 | Europe/Bucharest | RO |
| 🇷🇸 | Europe/Belgrade | RS |
| 🇷🇺 | Europe/Volgograd | RU |
| 🇷🇼 | Africa/Kigali | RW |
| 🇸🇦 | Asia/Riyadh | SA |
| 🇸🇧 | Pacific/Guadalcanal | SB |
| 🇸🇨 | Indian/Mahe | SC |
| 🇸🇩 | Africa/Khartoum | SD |
| 🇸🇪 | Europe/Stockholm | SE |
| 🇸🇬 | Asia/Singapore | SG |
| 🇸🇭 | Atlantic/St_Helena | SH |
| 🇸🇮 | Europe/Ljubljana | SI |
| 🇸🇯 | Arctic/Longyearbyen | SJ |
| 🇸🇰 | Europe/Bratislava | SK |
| 🇸🇱 | Africa/Freetown | SL |
| 🇸🇲 | Europe/San_Marino | SM |
| 🇸🇳 | Africa/Dakar | SN |
| 🇸🇴 | Africa/Mogadishu | SO |
| 🇸🇷 | America/Paramaribo | SR |
| 🇸🇸 | Africa/Juba | SS |
| 🇸🇹 | Africa/Sao_Tome | ST |
| 🇸🇻 | America/El_Salvador | SV |
| 🇸🇽 | America/Lower_Princes | SX |
| 🇸🇾 | Asia/Damascus | SY |
| 🇸🇿 | Africa/Mbabane | SZ |
| 🇹🇨 | America/Grand_Turk | TC |
| 🇹🇩 | Africa/Ndjamena | TD |
| 🇹🇫 | Indian/Kerguelen | TF |
| 🇹🇬 | Africa/Lome | TG |
| 🇹🇭 | Asia/Bangkok | TH |
| 🇹🇯 | Asia/Dushanbe | TJ |
| 🇹🇰 | Pacific/Fakaofo | TK |
| 🇹🇱 | Asia/Dili | TL |
| 🇹🇲 | Asia/Ashgabat | TM |
| 🇹🇳 | Africa/Tunis | TN |
| 🇹🇴 | Pacific/Tongatapu | TO |
| 🇹🇷 | Europe/Istanbul | TR |
| 🇹🇹 | America/Port_of_Spain | TT |
| 🇹🇻 | Pacific/Funafuti | TV |
| 🇹🇼 | Asia/Taipei | TW |
| 🇹🇿 | Africa/Dar_es_Salaam | TZ |
| 🇺🇦 | Europe/Zaporozhye | UA |
| 🇺🇬 | Africa/Kampala | UG |
| 🇺🇲 | Pacific/Wake | UM |
| 🇺🇸 | Pacific/Honolulu | US |
| 🇺🇾 | America/Montevideo | UY |
| 🇺🇿 | Asia/Tashkent | UZ |
| 🇻🇦 | Europe/Vatican | VA |
| 🇻🇨 | America/St_Vincent | VC |
| 🇻🇪 | America/Caracas | VE |
| 🇻🇬 | America/Tortola | VG |
| 🇻🇮 | America/St_Thomas | VI |
| 🇻🇳 | Asia/Ho_Chi_Minh | VN |
| 🇻🇺 | Pacific/Efate | VU |
| 🇼🇫 | Pacific/Wallis | WF |
| 🇼🇸 | Pacific/Apia | WS |
| 🇾🇪 | Asia/Aden | YE |
| 🇾🇹 | Indian/Mayotte | YT |
| 🇿🇦 | Africa/Johannesburg | ZA |
| 🇿🇲 | Africa/Lusaka | ZM |
| 🇿🇼 | Africa/Harare | ZW |

### Hard Flags

| Emoji | Timezone | Comment |
|---|---|---|
| 🇦🇨 | Atlantic/St_Helena | AC, Ascension Island |
| 🇧🇻 | Europe/Oslo | BV, Bouvet Island |
| 🇨🇵 | Europe/Paris | CP, Clipperton Island |
| 🇩🇬 | Indian/Chagos | DG, Diego Garcia |
| 🇪🇦 | Africa/Ceuta | EA, Ceuta & Melilla |
| 🇪🇺 | Europe/Brussels | EU, European Union headquarters |
| 🇭🇲 | Indian/Kerguelen | HM, Heard & McDonald Islands |
| 🇮🇨 | Atlantic/Canary | IC, Canary Islands |
| 🇹🇦 | Atlantic/St_Helena | TA, Tristan Da Cunha |
| 🇺🇳 | America/New_York | UN, United Nations headquarters |
| 🇽🇰 | Europe/Belgrade | XK, Kosovo |
| 🏴󠁧󠁢󠁥󠁮󠁧󠁿 | Europe/London | England |
| 🏴󠁧󠁢󠁳󠁣󠁴󠁿 | Europe/London | Scotland |
| 🏴󠁧󠁢󠁷󠁬󠁳󠁿 | Europe/London | Wales |
| 🏴󠁵󠁳󠁴󠁸󠁿 | America/Chicago | Texas flag |

