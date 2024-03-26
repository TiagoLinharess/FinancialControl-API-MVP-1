from flask import Blueprint
from controllers.bill_item_controller import post_bill_items
from controllers.bill_item_controller_get import get_bill_items

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register bill_items with api blueprint
api.register_blueprint(post_bill_items)
api.register_blueprint(get_bill_items)