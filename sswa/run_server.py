"""Used as entry point"""

from aiohttp import web
import syslog

from rest_api_handlers import runable_app

PORT = 9091

def main():
    """Starts the app, via entry_point script"""
    syslog.syslog(f'Web application is starting on port {PORT}')
    web.run_app(runable_app, port=PORT)
    