import logging
from typing import List
import azure.functions as func


def main(events: List[func.EventHubEvent]):
    for event in events:
        event.get_body()