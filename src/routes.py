from flask import Blueprint
from controllers.bill_item_controller import bill_items

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register bill_items with api blueprint
api.register_blueprint(bill_items)