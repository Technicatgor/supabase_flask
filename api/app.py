import os
from flask import Flask, request, redirect
from dotenv import load_dotenv
from postgrest.exceptions import APIError
from supabase import create_client, Client
from middleware import token_required

load_dotenv()

app = Flask(__name__)

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


@app.route("/login", methods=["GET"])
def login():
    return {"message": "Login Here"}


@app.route("/supabase/login", methods=["POST"])
def supabase_login():
    email = request.form.get("email")
    password = request.form.get("password")
    user = supabase.auth.sign_in_with_password({"email": email, "password": password})
    response = redirect("/user_profile")
    response.set_cookie("auth", user.session.access_token)
    supabase.auth.sign_out()
    return response


@app.route("/supabase/logout", methods=["POST"])
def supabase_logout():
    response = redirect("/login")
    response.set_cookie("auth", expires=0)
    supabase.auth.sign_out()
    return response


@app.route("/user_profile", methods=["GET"])
@token_required
def user_profile(supabase_user):
    print(supabase_user)
    return {"message": "Logged in successfully."}, 200


@app.route("/devices", methods=["GET"])
@token_required
def get_devices(supabase_user):
    try:
        if supabase_user:
            response = supabase.table("device").select("*").execute()
            return response.data
    except APIError:
        return {"message": "Please login."}, 401


@app.route("/devices/<id>", methods=["GET"])
@token_required
def get_one_device(supabase_user, id):
    try:
        if supabase_user:
            response = supabase.table("device").select("*").eq("id", id).execute()
            if len(response.data) == 0:
                return {"message": "Record is not found."}
            return response.data

    except APIError:
        return {"message": "Please login."}, 401


@app.route("/devices", methods=["POST"])
@token_required
def create_device(supabase_user):
    try:
        data = request.json
        if supabase_user:
            response = supabase.table("device").insert(data).execute()
            return response.data
    except APIError:
        return {"message": "Please login."}, 401


@app.route("/devices/<id>", methods=["PUT"])
@token_required
def update_device(supabase_user, id):
    try:
        data = request.json
        if supabase_user:
            check_id = supabase.table("device").select("*").eq("id", id).execute()
            if len(check_id.data) == 0:
                return {"message": "Record is not found."}
            response = supabase.table("device").update(data).eq("id", id).execute()
            return response.data
    except APIError:
        return {"message": "Please login."}, 401


@app.route("/devices/<id>", methods=["DELETE"])
@token_required
def delete_device(supabase_user, id):
    try:
        if supabase_user:
            check_id = supabase.table("device").select("*").eq("id", id).execute()
            if len(check_id.data) == 0:
                return {"message": "Record is not found."}
            response = supabase.table("device").delete().eq("id", id).execute()
            return response.data
    except APIError:
        return {"message": "Please login."}, 401


@app.route("/users", methods=["GET"])
@token_required
def get_users(supabase_user):
    try:
        if supabase_user:
            response = supabase.table("user").select("*").execute()
            return response.data
    except APIError:
        return {"message": "Please login."}, 401


@app.route("/users/<id>", methods=["GET"])
@token_required
def get_one_user(supabase_user, id):
    try:
        if supabase_user:
            response = supabase.table("user").select("*").eq("id", id).execute()
            if len(response.data) == 0:
                return {"message": "Record is not found."}
            return response.data
    except APIError:
        return {"message": "Please login."}, 401


@app.route("/users", methods=["POST"])
@token_required
def create_user(supabase_user):
    try:
        data = request.json
        if supabase_user:
            response = supabase.table("user").insert(data).execute()
            return response.data
    except APIError:
        return {"message": "Please login."}, 401


@app.route("/users/<id>", methods=["PUT"])
@token_required
def update_user(supabase_user, id):
    try:
        data = request.json
        if supabase_user:
            check_id = supabase.table("user").select("*").eq("id", id).execute()
            if len(check_id.data) == 0:
                return {"message": "Record is not found."}
            response = supabase.table("user").update(data).eq("id", id).execute()
            return response.data
    except APIError:
        return {"message": "Please login."}, 401


@app.route("/users/<id>", methods=["DELETE"])
@token_required
def delete_user(supabase_user, id):
    try:
        if supabase_user:
            check_id = supabase.table("user").select("*").eq("id", id).execute()
            if len(check_id.data) == 0:
                return {"message": "Record is not found."}
            response = supabase.table("user").delete().eq("id", id).execute()
            return response.data
    except APIError:
        return {"message": "Please login."}, 401


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
