from flask import Blueprint

to_do_bp=Blueprint('to_do',__name__)

@to_do_bp.route('/')
def home():
    return "maybe one day she will be back?"