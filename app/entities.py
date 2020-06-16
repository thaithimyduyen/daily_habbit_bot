#!/usr/bin/env python3
import enum
import uuid
import datetime

MessageId = str
ChatId = str


class LevelHabit(enum.Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class Mark(enum.Enum):
    DONE = "✅ "
    NOT_DONE = "⬜ "
    DELETE = "🗑 "
    TODO = "📝 "


class KindOfTask(enum.Enum):
    HABIT = "habit"
    TODO = "todo"


class Task:
    def __init__(
        self, name
    ):
        self.kind = KindOfTask.HABIT
        self.name = name
        self.id = str(uuid.uuid1())
        self.__done_time = datetime.datetime.fromtimestamp(0)

    @property
    def is_done(self):
        today = datetime.datetime.utcnow().date()
        return self.__done_time.date() == today

    @is_done.setter
    def is_done(self, is_done: bool) -> bool:
        if is_done:
            self.__done_time = datetime.datetime.utcnow()
        else:
            self.__done_time = datetime.datetime.fromtimestamp(0)

    @property
    def done_date(self) -> datetime.date:
        return self.__done_time.date()

    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)
