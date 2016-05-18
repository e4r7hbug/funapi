"""API application."""
import connexion

APP = connexion.App(__name__)
APP.add_api('swagger.yml')
