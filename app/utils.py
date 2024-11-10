from database import SessionLocal
from fastapi import Request


# global functions that jinja templates can access
# send flash messages to the alert area during redirect
def flash(request: Request, message: str, category: str = "primary") -> None:
    if "_messages" not in request.session:
        request.session["_messages"] = []
    request.session["_messages"].append({"message": message, "category": category})


def get_flashed_messages(request: Request) -> list[str]:
    return request.session.pop("_messages") if "_messages" in request.session else []


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
