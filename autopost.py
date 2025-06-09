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
posts = config.get("posts", [])

if not posts:
    log_failure("投稿設定 (posts) が見つかりません！")
    sys.exit(1)

for idx, post_config in enumerate(posts, start=1):
    print(f"\n=== {idx} 件目の投稿開始 ===")

    # --- パラメータ取得 ---
    title = post_config.get("title", "")
    if not title:
        title = input("タイトルを入力してください: ")

    text = post_config.get("text", "")
    if not text:
        text = input("本文を入力してください: ")

    sendNotification = post_config.get("sendNotification", False)

    visibility = post_config.get("visibility", "")
    if not visibility:
        visibility = input("ポストが見える範囲(public/group): ")

    role_names_str = post_config.get("role_names", "")
    role_names = [name.strip() for name in role_names_str.split(",") if name.strip()]

    role_ids = []

    # --- Group の場合は roleIds 処理 ---
    if visibility == "group":
        # GET /groups/{groupId}?includeRoles=true
        group_info_url = f"https://vrchat.com/api/1/groups/{group_id}?includeRoles=true&purpose=other"
        group_response = session.get(group_info_url)

        if group_response.status_code != 200:
            log_failure(f"Group 情報取得失敗！（Status: {group_response.status_code}）")
            sys.exit(1)

        group_json = group_response.json()
        roles = group_json.get("roles", [])

        if role_names:
            log_success(f"指定された roleNames → roleIds を取得します: {role_names}")
            for role in roles:
                if role["name"] in role_names:
                    role_ids.append(role["id"])

            if not role_ids:
                log_failure("指定された roleNames に該当する roleIds が見つかりませんでした！")
                sys.exit(1)
            else:
                log_success(f"roleNames → roleIds 変換成功！: {role_ids}")

    # --- POSTデータ構築 ---
    post_data = {
        "text": text,
        "title": title,
        "imageId": None,
        "sendNotification": sendNotification,
        "roleIds": role_ids,
        "visibility": visibility
    }

    print("送信する POST データ:", json.dumps(post_data, indent=2, ensure_ascii=False))

    # --- API呼び出し ---
    response = session.post(
        f"https://vrchat.com/api/1/groups/{group_id}/posts",
        json=post_data
    )

    # --- 結果表示 ---
    print("Status:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except Exception:
        print("Response Text:", response.text)

    if response.status_code in (401, 403):
        log_failure("セッションが無効または期限切れです。")
        print("対処法：save_session.py を再実行して新しいセッションを保存してください。")
    elif response.status_code == 200:
        log_success(f"{idx} 件目の投稿成功！")
    else:
        log_failure(f"{idx} 件目の投稿失敗！（Status: {response.status_code}）")

print("\n✅ すべての投稿が完了しました！")
input("終了します。ウィンドウを閉じてください。")
sys.exit()