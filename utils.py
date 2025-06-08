import sys
import os

# ========================
# ログ出力関数
# ========================
def log_success(message):
    print(f"✅ {message}")

def log_failure(message="続行するには Enter を押してください。"):
    print(f"⚠ {message}")

# ========================
# config読み込み関数
# ========================
def get_config_path(filename="config.json"):
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, filename)

# ========================
# session.json 読み込み関数
# ========================
def get_session_path(filename="session.json"):
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, filename)