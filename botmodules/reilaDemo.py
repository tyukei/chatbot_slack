from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('AI の定義|ＡＩの定義')
def reila_1(message):
    # Slackに応答を返す
    message.reply('さあ。あなたたち人間が作った、人間のようなロボット・・・いや、ReiLaはソフトウェアですから、ソフト、でしょうか。')


@respond_to('AI の強弱って|ＡＩの強弱って')
def reila_2(message):
    # Slackに応答を返す
    message.reply('ふふ。私は強いらしいですよ。')


@respond_to('(汎用型|特化型)')
def reila_3(message, group):
    if group == '特化型':
        message.reply('ReiLaは、会話専門の特化型AIですね')
    else:
        message.reply('どらえもんは汎用型AIですね')

@respond_to('AI をつくれると|ＡＩをつくれると')
def reila_4(message):
    message.reply('さあ。さっぱり。とっても難しそうですね。')

@respond_to('強化学習')
def reila_5(message):
    message.reply('')


# 分岐文もできる
@respond_to('^(hungry|tired)？$')
def question_4(message, group):
    if group == 'hungry':
        message.react('ok_hand')
    else:
        message.react('bangbang')
        message.react('thinking_face')
        message.react('woman-gesturing-no')


'''
^xxx　= start to xxx
ex) ^ab    >>   abc  ok
xxx$  = end to xxx
ex)ab$     >> 123ab   ok

reference
【Python】Slackbotにリアクションをさせる
https://miyabikno-jobs.com/slackbot-react/ 
'''
