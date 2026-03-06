from aw_core.config import load_config_toml

default_config = """
[server]
hostname = "127.0.0.1"
port = "5600"

[server-remote]
# 可选：远程宿主机，用于双写（本机 + 宿主机）；宿主机不可达时仅写本机，由 aw-sync 后续合并
enabled = false
hostname = ""
port = "5600"

[client]
commit_interval = 10

[server-testing]
hostname = "127.0.0.1"
port = "5666"

[server-remote-testing]
enabled = false
hostname = ""
port = "5666"

[client-testing]
commit_interval = 5
""".strip()


def load_config():
    return load_config_toml("aw-client", default_config)
