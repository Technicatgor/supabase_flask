from functools import wraps
from flask import request
from dotenv import load_dotenv
from supabase import create_client, Client
import os

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        jwt = request.cookies.get("auth") or ""
        if not jwt:
            return {"message": "Please Login."}, 401
        try:
            supabase_user = supabase.auth.get_user(jwt)

        except Exception as e:
            return {"message": (f"Exception: {e}")}

        return f(supabase_user.user, *args, **kwargs)

    return decorated_function
