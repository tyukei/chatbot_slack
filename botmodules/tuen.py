import json
from slackbot.bot import respond_to
import urllib.request
import pygame.mixer
import time
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


def sound(f, i, n):
    pygame.mixer.init()  # 初期化します
    pygame.mixer.music.load(f)  # 音声ファイルを読み込みます
    pygame.mixer.music.play(i)  # 再生します
    time.sleep(n)  # 再生時間を指定します
    pygame.mixer.music.stop()  # 終了します


@respond_to('今にあった曲')
def whether(message):
    c = data["current"]
    w = c["weather"][0]['main']
    message.reply('京都の今の天気は%sです。なのでこの曲を選びました' % w)

    if w == "Clear":
        sound("./botmodules/music/y2mate.com - 大空と大地の中で  松山千春フル.mp3", 1, 100)
    elif w == "Rain":
        sound("./botmodules/music/y2mate.com - Rain.mp3", 1, 100)
    elif w == "Clouds":
        sound("./botmodules/music/y2mate.com - 猿岩石 白い雲のように1996.mp3", 1, 100)
    else:
        sound("./botmodules/music/y2mate.com - SEKAI NO OWARIRPG.mp3", 1, 100)


@respond_to('悲しい')
def sad(message):
    message.reply("Don't worry be happy")
    sound("./botmodules/music/y2mate.com - 尾崎紀世彦さんまた逢う日まで.mp3", 1, 100)


@respond_to('夜')
def night(message):
    dt_now = datetime.datetime.now()
    message.reply("今は%s:%s" % (dt_now.hour, dt_now.minute))
    if dt_now.hour >= 18:
        message.reply("%s時も過ぎたので、もう夜っすね" % dt_now.hour)
    elif 0 <= dt_now.hour < 4:
        message.reply("時も過ぎたので、もう夜っすね")
    elif 16 <= dt_now.hour < 18:
        message.reply("ん～まだ早いような")
    else:
        message.reply("アメリカ基準でしょうか？")


@respond_to('音楽聞きたい')
def night(message):
    dt_now = datetime.datetime.now()
    message.reply("今は%s:%s" % (dt_now.hour, dt_now.minute))
    if dt_now.hour >= 18:
        message.reply("%s時も過ぎたので、もう夜っすね" % dt_now.hour)
        message.reply("こんな曲でもどうですか？")
        sound("./botmodules/music/y2mate.com - SEKAI NO OWARI  Dragon Night.mp3", 1, 100)
    elif 0 <= dt_now.hour < 4:
        message.reply("時も過ぎたので、もう夜っすね")
        message.reply("こんな曲でもどうですか？")
        sound("./botmodules/music/y2mate.com - SEKAI NO OWARI  Dragon Night.mop3", 1, 100)
    elif 16 <= dt_now.hour < 18:
        message.reply("夕方だー。この曲どうですか")
        sound("./botmodules/music/西城秀樹  ヤングマン.mp3", 1, 100)
    else:
        message.reply("まだまだ今日という日はありますよ！この曲聞いてもうひと踏ん張り！！")
        sound("./botmodules/music/西城秀樹  ヤングマン.mp3", 1, 100)


""""""""""
reference
https://aoshimasan.com/play-sound/

sound の第一引数はbot.pyからみた相対パス
　　　　　第二引数は再生回数
　　　　　第三引数は再生時間

大空と大地の中で
猿岩石 白い雲のように
SEKAI NO OWARI 「Rain」
SEKAI NO OWARI 「Dragon Night」
SEKAI NO OWARI「RPG」
YMCA

https://taira-komori.jpn.org/anime01.html
"""""""""""
