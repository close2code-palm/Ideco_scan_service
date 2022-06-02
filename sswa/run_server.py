"""Used as entry point"""

from aiohttp import web
import syslog

from sswa.rest_api_handlers import runable_app

PORT = 9091

syslog.syslog(f'Web application is starting on port {PORT}')
web.run_app(runable_app, port=PORT)
