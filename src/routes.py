from flask import Blueprint
from controllers import post_bill_items, get_bill_items, update_bill_items, delete_bill_items

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register bill_items routes with api blueprint
api.register_blueprint(post_bill_items)
api.register_blueprint(get_bill_items)
api.register_blueprint(update_bill_items)
api.register_blueprint(delete_bill_items)