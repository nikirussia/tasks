import pyowm

owm = pyowm.OWM('6bed291744d74f51ca0b57e6024304c0', language="ru")

place = input("Какой город интересует?: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print("В городе " + place + " сейчас " + w.get_detailed_status())
print("Температура сейчас в районе " + str(temp))

if temp < 5:
    print("Не выходи из дома, не совершай ошибок")
elif temp < 10:
    print("Прежде чем выйти - оденься")
else:
    print("Иди смело")
