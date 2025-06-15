# VRChat Group AutoPost

このスクリプトは、VRChatのグループで自動postを行うツールです。複数投稿にも対応しています。
ブラウザ操作なしで、定型的な告知やメッセージを簡単に投稿できます🚀

---

## 🛠 構成ファイル
- `config.json` … 投稿内容の設定ファイル
- `session.json` … VRChatの認証セッション情報（`save_session.exe`で作成）
- `save_session.exe` … 事前処理（VRChatにログインしてセッション情報を取得）
- `autopost.exe` … メイン処理（投稿処理）

---

## 📌 使い方
1. **`vrc-group-autopost-v*.*.zip` をダウンロードし、解凍。→最新版(https://github.com/hamikuma/vrc-group-autopost/releases/latest)**
2. **`save_session.exe` を実行してVRChatにログインし、`session.json` を作成**
3. **`config.json` を編集して投稿内容を設定**
4. **`autopost.py` を実行 → VRChat Groupに投稿されます！**

---

## 📝 `config.json` の設定項目

`config.json` を編集して、Groupにpostする内容を設定してください。
`config.json` に既に記載している内容を参考に書き換えてください。以下詳細説明です。

※groupIdは、VRChat公式(https://vrchat.com/)の各GroupページのURLに含まれているので、その値を入力してください。

| **キー** | **内容** | **備考** |
|---------|---------|---------|
| `"username"` | ログインユーザーネーム | 空白なら実行時に入力可能です |
| `"password"` | ログインパスワード | 空白なら実行時に入力可能です |
| `"group_id"` | 対象GroupのID | 例: `"grp_xxxxxxxx-yyyy-zzzz-aaaa-bbbbbbbbbbbb"` |
| `"title"` | 投稿タイトル | 空欄の場合、実行時に入力を求められます |
| `"text"` | 投稿本文 | 空欄の場合、実行時に入力を求められます |
| `"sendNotification"` | 通知を送信するか | `"true"` または `"false"` |
| `"visibility"` | 投稿の公開範囲 | `"public"` または `"group"` |
| `"role_names"` | ロールの制限(group時にさらに特定ロールに絞りたい場合) | `"Group Owner"` 、 `"Member"` などをカンマ区切りで入力|

---

## ❌ 注意事項

- 公式でガイドされていないapiを使用しているため、予期しない仕様変更等によって動作しなくなる可能性があります。

---

## 🧑‍💻 更新履歴

- 2025/6/9 group roleの指定、複数投稿に対応
- 2025/6/8 初版作成

---

ご要望・不明点・改善点などありましたら気軽にご連絡ください！  
Issue や Pull Request も歓迎します 🙌