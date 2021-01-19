from flask import Blueprint

oauth = Blueprint("oauth", url_prefix="/oauth", import_name="oauth")