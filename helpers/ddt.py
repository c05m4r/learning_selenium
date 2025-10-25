import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Sequence


@dataclass(frozen=True)
class TestDataItem:
    testid: str
    descripcion: str
    json_data: Dict[str, Any]


class DDTHelper:
    def __init__(self, file_path: Path | str) -> None:
        self.file_path = Path(file_path)
        self._data = self._load()

    def _load(self) -> List[TestDataItem]:
        if not self.file_path.exists():
            raise FileNotFoundError(f"Data file not found: {self.file_path}")

        raw_content = self.file_path.read_text(encoding="utf-8")
        try:
            payload = json.loads(raw_content)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON format in {self.file_path}") from exc

        if not isinstance(payload, list):
            raise ValueError("Data must be a list of objects")

        items: List[TestDataItem] = []
        for entry in payload:
            if not isinstance(entry, dict):
                raise ValueError("Each entry must be a JSON object")

            if "testid" not in entry or "json_data" not in entry:
                raise ValueError("Entries must define 'testid' and 'json_data'")

            descripcion = entry.get("descripcion", "")
            if descripcion is None:
                descripcion = ""

            json_data = entry["json_data"]
            if not isinstance(json_data, dict):
                raise ValueError("'json_data' must be an object")

            items.append(
                TestDataItem(
                    testid=str(entry["testid"]),
                    descripcion=str(descripcion),
                    json_data=json_data,
                )
            )

        return items

    @property
    def data(self) -> Sequence[TestDataItem]:
        return tuple(self._data)

    def get_by_testid(self, testid: str) -> List[TestDataItem]:
        return [item for item in self._data if item.testid == testid]

    def get_json_data_by_testid(self, testid: str) -> List[Dict[str, Any]]:
        return [item.json_data for item in self.get_by_testid(testid)]

    def get_by_description(self, descripcion: str) -> List[TestDataItem]:
        return [item for item in self._data if item.descripcion == descripcion]

    def get_json_data_by_description(self, descripcion: str) -> List[Dict[str, Any]]:
        return [item.json_data for item in self.get_by_description(descripcion)]
