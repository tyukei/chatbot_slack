import json
from slackbot.bot import respond_to
import urllib.request
import datetime

# def get_weather(city_number):
# https://openweathermap.org/api weather api
API_KEY = "7434d1ef3a0d583f4c8ed35905d5edbc"

try:
    url = "http://api.openweathermap.org/data/2.5/onecall?lat=35.0211&lon=135.7538&units=metric&appid=7434d1ef3a0d583f4c8ed35905d5edbc"
    res = urllib.request.urlopen(url)

    # json_loads() でPythonオブジェクトに変換
    data = json.loads(res.read().decode('utf-8'))


except urllib.error.HTTPError as e:
    print('HTTPError: ', e)
except json.JSONDecodeError as e:
    print('JSONDecodeError: ', e)


# テストコード
def main():
    if __name__ == "__main__":
        main()


@respond_to('今の天気')
def whether_1(message):
    message.reply('京都の今の天気は%sです' % (data["current"]["weather"][0]['main']))


@respond_to('(今日|明日|明後日|三日後|３日後|3日後|四日後|４日後|4日後|五日後|５日後|5日後|六日後|６日後|6日後)の天気')
def whether_2(message, group):
    dic_weather = {
        '01d': 'sunny',
        '01n': 'sunny',
        '02d': 'barely_sunny',
        '02n': 'barely_sunny',
        '03d': 'cloud',
        '03n': 'cloud',
        '04d': 'cloud',
        '04n': 'cloud',
        '09d': 'rain_cloud',
        '10d': 'umbrella',
        '11d': 'cloud with lightning and rain',
        '13d': 'snow_cloud',
        '50d': 'cyclone',
    }

    dic_date = {
        '今日': 0,
        '明日': 1,
        '明後日': 2,
        '三日後': 3,
        '３日後': 3,
        '3日後': 3,
        '四日後': 4,
        '４日後': 4,
        '4日後': 4,
        '五日後': 5,
        '５日後': 5,
        '5日後': 5,
        '六日後': 6,
        '６日後': 6,
        '6日後': 6,
    }
    w = data['daily']
    t = w[dic_date[group]]
    icon = t['weather'][0]['icon']
    telop = t['weather'][0]['main']
    date = t['dt']
    max_temp = t['temp']['max']
    min_temp = t['temp']['min']

    dt = datetime.datetime.fromtimestamp(date)
    # 辞書にない天気が来たら絵文字に空文字を設定する
    if icon in dic_weather:
        emoji = ':' + dic_weather[icon] + ':'
    else:
        emoji = ""

    message.reply('%sの京都の天気は%sです%s' % (dt, telop, emoji))
    message.reply('最高気温は%s℃で最低気温は%s℃です' % (max_temp, min_temp))


'''
reference
天気予報
https://miyabikno-jobs.com/slackbot-weather/
livedoor いまはもう使えない

https://parco1021.hatenablog.com/entry/2019/10/12/223525
data　使えない

unix utc を変換
import datetime
dt = datetime.datetime.fromtimestamp(ここにutcかく)

https://note.nkmk.me/python-unix-time-datetime/

'''
