import json
import os
import platform
from pathlib import Path
from typing import List, Dict, Any


class ConfigManager:
    def __init__(self) -> None:
        self.config_dir = self._get_config_dir()
        self.config_dir.mkdir(parents=True, exist_ok=True)

    def _get_config_dir(self) -> Path:
        system = platform.system()

        if system == "Windows":
            # Use %APPDATA% directory on Windows
            config_dir = Path(os.environ.get("APPDATA", "")) / "automudae"
        elif system == "Darwin":  # macOS
            # Use Application Support directory on macOS
            config_dir = Path.home() / "Library" / "Application Support" / "automudae"
        else:  # Linux and other Unix-like systems
            # Use XDG config directory standard
            config_dir = Path.home() / ".config" / "automudae"

        return config_dir

    def _get_file_path(self, config_type: str) -> Path:
        return self.config_dir / f"{config_type}.json"

    def _load_json(self, config_type: str) -> Dict[str, Any]:
        file_path = self._get_file_path(config_type)

        if not file_path.exists():
            return {}

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data if isinstance(data, dict) else {}
        except (json.JSONDecodeError, IOError):
            # Return empty dict on any file operation errors
            return {}

    def _save_json(self, config_type: str, data: Dict[str, Any]) -> None:
        file_path = self._get_file_path(config_type)

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except IOError:
            raise Exception(f"Failed to save {config_type} configuration")

    # Public API - Credentials Management
    def get_credentials(self) -> Dict[str, Any]:
        return self._load_json("credentials")

    def set_credential(self, key: str, value: Any) -> None:
        credentials = self.get_credentials()
        credentials[key] = value
        self._save_json("credentials", credentials)

    def get_credential(self, key: str, default: Any = None) -> Any:
        credentials = self.get_credentials()
        return credentials.get(key, default)

    # Private helper methods for preferences
    def _load_preferences(self, preference_type: str) -> List[str]:
        file_path = self._get_file_path(preference_type)

        if not file_path.exists():
            return []

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, IOError):
            return []

    def _save_preferences(self, preference_type: str, items: List[str]) -> None:
        file_path = self._get_file_path(preference_type)

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(items, f, indent=2, ensure_ascii=False)
        except IOError:
            raise Exception(f"Failed to save {preference_type} preferences")

    # Public API - Character Preferences
    def get_characters(self) -> List[str]:
        return self._load_preferences("characters")

    def add_character(self, character: str) -> bool:
        characters = self.get_characters()
        if character not in characters:
            characters.append(character)
            self._save_preferences("characters", characters)
            return True
        return False

    def remove_character(self, character: str) -> bool:
        characters = self.get_characters()
        if character in characters:
            characters.remove(character)
            self._save_preferences("characters", characters)
            return True
        return False

    def clear_characters(self) -> None:
        self._save_preferences("characters", [])

    # Public API - Series Preferences
    def get_series(self) -> List[str]:
        return self._load_preferences("series")

    def add_series(self, series: str) -> bool:
        series_list = self.get_series()
        if series not in series_list:
            series_list.append(series)
            self._save_preferences("series", series_list)
            return True
        return False

    def remove_series(self, series: str) -> bool:
        series_list = self.get_series()
        if series in series_list:
            series_list.remove(series)
            self._save_preferences("series", series_list)
            return True
        return False

    def clear_series(self) -> None:
        self._save_preferences("series", [])

    # Public API - Kakera Preferences
    def get_kakeras(self) -> List[str]:
        kakeras = self._load_preferences("kakeras")
        # Return defaults if no kakeras configured
        if not kakeras:
            return ["kakeraP", "kakeraY", "kakeraO", "kakeraR", "kakeraW", "kakeraL"]
        return kakeras

    def add_kakera(self, kakera: str) -> bool:
        kakeras = self.get_kakeras()
        if kakera not in kakeras:
            kakeras.append(kakera)
            self._save_preferences("kakeras", kakeras)
            return True
        return False

    def remove_kakera(self, kakera: str) -> bool:
        kakeras = self.get_kakeras()
        if kakera in kakeras:
            kakeras.remove(kakera)
            self._save_preferences("kakeras", kakeras)
            return True
        return False

    def clear_kakeras(self) -> None:
        self._save_preferences("kakeras", [])

    def reset_kakeras(self) -> None:
        """Reset kakeras to default values"""
        self._save_preferences(
            "kakeras",
            ["kakeraP", "kakeraY", "kakeraO", "kakeraR", "kakeraW", "kakeraL"],
        )

    def reset_credentials(self) -> None:
        """Reset all credentials (clear them)"""
        self._save_json("credentials", {})

    def reset_characters(self) -> None:
        """Reset characters (clear them)"""
        self._save_preferences("characters", [])

    def reset_series(self) -> None:
        """Reset series (clear them)"""
        self._save_preferences("series", [])


# Global configuration manager instance
config_manager = ConfigManager()

# Legacy compatibility - expose configuration values as module-level variables
token = config_manager.get_credential("token", "")
channel_id = config_manager.get_credential("channel_id", "")
server_id = config_manager.get_credential("server_id", "")
roll_command = config_manager.get_credential("roll_command", "wa")
poke_roll = config_manager.get_credential("poke_roll", True)
repeat_minute = config_manager.get_credential("repeat_minute", "25")

# User preferences
desired_characters = config_manager.get_characters()
desired_series = config_manager.get_series()
desired_kakeras = config_manager.get_kakeras()
