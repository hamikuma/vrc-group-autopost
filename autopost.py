# autopost.py

import requests
import json
import sys
from utils import log_success, log_failure, get_config_path, get_session_path

# --- 設定ファイル読み込み ---
config_path = get_config_path()

try:
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
except FileNotFoundError:
    log_failure(f"設定ファイルが見つかりません: {config_path}")
    exit(1)

# --- セッション情報読み込み ---
session_path = get_session_path()

try:
    with open(session_path, "r", encoding="utf-8") as f:
        session_data = json.load(f)
except FileNotFoundError:
    log_failure("session.json が見つかりません！ まず save_session.py を実行してください。")
    exit(1)

# --- セッション作成 ---
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
})
session.cookies.set("auth", session_data["auth"], domain="vrchat.com")

# --- パラメータ設定 ---
group_id = config["group_id"]

# --- POSTデータ（履歴型Post用） ---
title = config["title"]
if not title:
    title = input("タイトルを入力してください: ")
    
text = config["text"]
if not text:
    text = input("本文を入力してください: ")

sendNotification = config["sendNotification"]
if not sendNotification:
    sendNotification = input("通知しますか？(true/false)")

visibility = config["visibility"]
if not visibility:
    visibility = input("ポストが見える範囲(public/group)")

post_data = {
    "text": text,
    "title": title,
    "imageId": None,
    "sendNotification": sendNotification, # true or false
    "roleIds": [], #grolidが定まらないので非対応
    "visibility": visibility #public or group
}

# --- API呼び出し ---
response = session.post(
    f"https://vrchat.com/api/1/groups/{group_id}/posts",
    json=post_data
)

# --- 結果表示 ---
print("Status:", response.status_code)
print("Response JSON:", response.json())

if response.status_code in (401, 403):
    log_failure("セッションが無効または期限切れです。")
    print("対処法：save_session.py を再実行して新しいセッションを保存してください。")
elif response.status_code == 200:
    log_success("通常Post 投稿完了！")
else:
    log_failure(f"投稿失敗！（Status: {response.status_code}）")

input("終了します。ウィンドウを閉じてください。")
sys.exit()