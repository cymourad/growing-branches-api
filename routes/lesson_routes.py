import json
import os

from dotenv import load_dotenv
from flask import Flask, Blueprint, request
from utils.load_response import load_response

from db.utils.growing_branches_db import GBTable

app = Flask(__name__)

# create the blueprint that will house all the routes
# the URL prefix means that every URL in this file will have /lessons first
lesson_routes = Blueprint("lesson_routes", __name__, url_prefix="/lessons")


@lesson_routes.route("", methods=["GET"])
def get_lesson():
    # get the query params
    # TODO handle errors
    try:
        grade = request.args.get("grade")
        era = request.args.get("era")
        week = request.args.get("week")
        return load_response(
            data={
                "grade": grade,
                "era": era,
                "week": week
            },
            status_code=200
        )
    except Exception as e:
        print(e)

    return load_response(
        data={
            "error": "Not data found"
        },
        status_code=404
    )

# TODO dummy salalchemy route to be removed before pushing


@lesson_routes.route("/test", methods=["GET"])
def create_dummy_table():
    try:
        dummy_table = GBTable()
        dummy_table.create_test_table()
        return load_response(
            data={
                "success": "table got created"
            },
            status_code=200
        )
    except Exception as e:
        print(e)

    return load_response(
        data={
            "error": "Not data found"
        },
        status_code=404
    )
