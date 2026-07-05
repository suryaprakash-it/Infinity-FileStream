from .start import register as register_start
from .upload import register as register_upload
from .admin import register as register_admin

def register_handlers(app):
    register_start(app)
    register_upload(app)
    register_admin(app)