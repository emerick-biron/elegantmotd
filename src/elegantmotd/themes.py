import distro

NF_OS_ICONS = {
    "AlmaLinux": "  ",
    "Alpine": "  ",
    "Amazon": " ",
    "Android": " ",
    "Arch": "󰣇 ",
    "Artix": " ",
    "CentOS": " ",
    "Debian": " ",
    "DragonFly": "  ",
    "EndeavourOS": "  ",
    "Fedora": "  ",
    "FreeBSD": "  ",
    "Garuda": "󰛓 ",
    "Gentoo": "  ",
    "Illumos": " ",
    "Kali": "  ",
    "Linux": " ",
    "Macos": "  ",
    "Manjaro": "  ",
    "Mint": "  ",
    "NixOS": " ",
    "Nobara": "󰣯 ",
    "OpenBSD": "  ",
    "openSUSE": "  ",
    "OracleLinux": " ",
    "Pop": "  ",
    "Raspbian": " ",
    "Redhat": "  ",
    "RedHatEnterprise": "  ",
    "RockyLinux": " ",
    "Solus": "  ",
    "SUSE": "  ",
    "Ubuntu": "  ",
    "Unknown": " ",
    "Void": "  ",
    "Windows": "  ",
}

ICONS = {
    "none": {
        "net_iface": " - ",
        "temp_sensor": " - ",
        "os": " ",
    },
    "emoji": {
        "cpu": "🚀 ",
        "memory": "🧠 ",
        "swap": "🔄 ",
        "temperature": "🌡️  ",
        "temp_sensor": "    - ",
        "load": "⚡ ",
        "disk": "💾 ",
        "processes": "🏗️  ",
        "users": "👤 ",
        "network": "🌐 ",
        "net_iface": "    - ",
        "os": "💻 ",
        "title": "📊 ",
        "date": "📅 ",
        "time": "🕒 ",
    },
    "nerdfont": {
        "cpu": "  ",
        "memory": "  ",
        "swap": "󰴋  ",
        "temperature": "  ",
        "temp_sensor": "    - ",
        "load": "󰓅  ",
        "disk": "  ",
        "processes": "  ",
        "users": "  ",
        "network": "󰖩  ",
        "net_iface": "    - ",
        "os": NF_OS_ICONS.get(distro.id().capitalize(), "  "),
        "title": "  ",
        "date": "  ",
        "time": "  ",
    }
}


def get_icon(theme: str, icon: str) -> str:
    return ICONS.get(theme, {}).get(icon, "")
