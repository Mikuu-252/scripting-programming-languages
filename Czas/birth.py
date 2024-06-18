import time, datetime

day = int(input("Podaj dzien urodzenia: "))
month = int(input("Podaj miesiąc urodzenia: "))
year = int(input("Podaj rok urodzenia: "))

nowDate = datetime.datetime.now()
birthDate = datetime.datetime(year, month, day, 0,0,0,0)

birthTime = (nowDate - birthDate)

print(f'Urodziłeś się {round(birthTime.days/365.25)} lat, {round(birthTime.days/12)} misięcy, {birthTime.days} dni temu.')