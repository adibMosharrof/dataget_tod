from dataclasses import dataclass


@dataclass
class TodCsvData:
    dialog_id: int
    turn_id: int
    domains: str
    domains_original: str
    context: str
    schema: str
    target: str
    is_api_call: bool
