from typing import Dict, Union

import psutil
from rich.console import RenderableType
from rich.text import Text

from .constants import GREEN, YELLOW, ORANGE, RED
from .sysinfo import SysInfo


class Temperature(SysInfo):
    CPU_SENSORS = {
        "coretemp": ["Package", "Core"],
        "k10temp": ["Tctl", "Tdie"]
    }

    def _get_infos(self) -> Dict[RenderableType, RenderableType]:
        infos = {"🌡️  Temperature": ""}
        temp_info = psutil.sensors_temperatures()

        for sensor, labels in self.CPU_SENSORS.items():
            if sensor in temp_info:
                for shwtemp in temp_info[sensor]:
                    if any(label in shwtemp.label for label in labels):
                        key = "🌡️  Temperature" if shwtemp.label in labels[:1] else f"    - {shwtemp.label}"
                        infos[key] = self.__get_format_temp(shwtemp)
                return infos

        infos["🌡️  Temperature"] = "Unable to get CPU temperature"
        return infos

    @staticmethod
    def __get_format_temp(shwtemp) -> Union[str, Text]:
        high = shwtemp.high
        current = shwtemp.current
        if not current:
            return "No data"
        if not high:
            return f"{current}°C"
        if current < high - 40:
            return Text(f"{current}°C", style=GREEN)
        if current < high - 20:
            return Text(f"{current}°C", style=YELLOW)
        if current < high:
            return Text(f"{current}°C", style=ORANGE)
        else:
            return Text(f"{current}°C", style=RED)
