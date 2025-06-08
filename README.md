# VRChat Group AutoPost

このスクリプトは、**VRChat Group** に自動で投稿を行うツールです。  
ブラウザ操作なしで、定型的な告知やメッセージを簡単に投稿できます🚀

---

## 🛠 構成ファイル
- `config.json` … 投稿内容の設定ファイル
- `session.json` … VRChatの認証セッション情報（`save_session.py`で作成）
- `autopost.py` … メインスクリプト（投稿処理）

---

## 📌 使い方

1. **VRChat公式サイトでログイン → `save_session.py` を実行して `session.json` を作成**
2. **`config.json` を編集して投稿内容を設定**
3. **`autopost.py` を実行 → VRChat Groupに投稿されます！**

---

## 📝 `config.json` の設定項目

| **キー** | **内容** | **備考** |
|---------|---------|---------|
| `"group_id"` | 対象GroupのID | 例: `"grp_xxxxxxxxxx"` |
| `"title"` | 投稿タイトル | 空欄の場合、実行時に入力を求められます |
| `"text"` | 投稿本文 | 空欄の場合、実行時に入力を求められます |
| `"sendNotification"` | 通知を送信するか | `"true"` または `"false"` |
| `"visibility"` | 投稿の公開範囲 | `"public"` または `"group"` |

---

## ❌ 注意事項

- **先に `save_session.py` を実行して、`session.json` を作成してください。**  
  これがない場合、`autopost.py` はエラーになります。
- **Groupのロール指定投稿 (`roleIds`) には現在未対応です。**

---

## 🧑‍💻 更新履歴

- 2025/6/8 初版作成

---

ご要望・不明点・改善点などありましたら気軽にご連絡ください！  
Issue や Pull Request も歓迎します 🙌