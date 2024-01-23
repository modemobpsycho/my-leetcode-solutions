from datetime import datetime
from typing import Any, Callable


def metrika_wrapper(callback: Callable[..., None]) -> Callable[..., dict[str, Any]]:
    statDays: list = []
    users: list = []

    def wrapper(user: dict[str, Any]) -> list[dict[str, Any]]:
        if user and user["login"] and user["password"] and user["date"]:
            currStatDay: list[int] = [
                i
                for i, x in enumerate(statDays)
                if x["date"] == user["date"].strftime("%Y-%m-%d")
            ]
            isUser: list[int] = [
                i
                for i, x in enumerate(users)
                if x["date"] == user["date"].strftime("%Y-%m-%d")
                and x["login"] == user["login"]
                and x["password"] == user["password"]
            ]
            if currStatDay:
                if not isUser:
                    users.append(user)
                    statDays[currStatDay[0]]["users"] += 1
                    callback()
            else:
                statDays.append(
                    dict({"date": user["date"].strftime("%Y-%m-%d"), "users": 1})
                )
                if not isUser:
                    users.append(user)
                callback()
        return statDays

    return wrapper


def my_function(*args) -> None:
    print("called")


wrapped_func = metrika_wrapper(my_function)

print(wrapped_func({"login": "a", "password": "a", "date": datetime(2023, 6, 26)}))
print(wrapped_func({"login": "b", "password": "a", "date": datetime(2023, 6, 26)}))
print(wrapped_func({"login": "c", "password": "c", "date": datetime(2023, 6, 26)}))
