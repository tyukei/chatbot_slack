# ライブラリのインポート
import os
# 環境変数に定義しておく
API_TOKEN = os.environ['BOT_API_TOKEN']


# 知らない言葉を聞いた時のデフォルトの応答
DEFAULT_REPLY = "その言葉の意味は知りません"

# 外部ファイルを読み込む。botmodule.pyを読み込んでおく
PLUGINS = [
    'slackbot.plugins',
    'botmodules.conversation',
    'botmodules.weather',
    'botmodules.tuen',
    'botmodules.reilaDemo',
]
