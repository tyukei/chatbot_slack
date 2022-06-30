from slackbot.bot import respond_to
from slackbot.bot import listen_to


# 「respond_to」はメンションする(@でターゲットを指定すること)と応答する
@respond_to('こんにちは')
def greeting_1(message):
    # Slackに応答を返す
    message.reply('こんにちは!')


# 「listen_to」はメンションがなくても応答する
@listen_to('コニチハ')
def greeting_2(message):
    message.reply('コニチハ')


# Slackbotにメッセージで応答させる場合は、「reply」
@respond_to('^ご機嫌いかが？$')
def question_1(message):
    message.reply('元気です！')


# 絵文字のとき「reply」を「react」に置き換える
@respond_to('^元気？$')
def question_2(message):
    message.react('smile')


# 複数の絵文字もおっけー
@respond_to('How are you?')
def question_3(message):
    message.react('bangbang')
    message.react('thinking_face')
    message.react('woman-gesturing-no')


# 分岐文もできる
@respond_to('^(おなかへった|つかれた)？$')
def question_4(message, group):
    if group == 'つかれた':
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
