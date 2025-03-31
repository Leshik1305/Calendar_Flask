from typing import List
from datetime import date
import model
import db


TITLE_LIMIT = 30
TEXT_LIMIT = 200


class LogicException(Exception):
    pass


class CalendarLogic:
    def __init__(self):
        self._calendar_db = db.CalendarDB()

    @staticmethod
    def _validate_calendar(calendar: model.Calendar, existing_dates: set):
        if calendar is None:
            raise LogicException("Calendar is None")
        if calendar.title is None or len(calendar.title) > TITLE_LIMIT:
            raise LogicException(f"Title length > MAX: {TITLE_LIMIT}")
        if calendar.text is None or len(calendar.text) > TEXT_LIMIT:
            raise LogicException(f"Text length > MAX: {TEXT_LIMIT}")


        # Проверка уникальности даты
        if calendar.DATE in existing_dates:
            raise LogicException(f"Another event already exists on the date: {calendar.DATE}")
        else:
            existing_dates.add(calendar.DATE)

    def create(self, calendar: model.Calendar) -> str:
        self._validate_calendar(calendar, self._get_existing_dates())# доб set
        try:
            return self._calendar_db.create(calendar)
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[model.Calendar]:
        try:
            return self._calendar_db.list()
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> model.Calendar:
        try:
            return self._calendar_db.read(_id)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _id: str, calendar: model.Calendar):
        self._validate_calendar(calendar, self._get_existing_dates()) # доб set
        try:
            return self._calendar_db.update(_id, calendar)
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._calendar_db.delete(_id)
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")

    def _get_existing_dates(self):
        existing_dates = set()
        for event in self._calendar_db.list():
            existing_dates.add(event.DATE)
        return existing_dates
