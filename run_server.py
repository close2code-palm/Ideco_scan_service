from aiohttp import web

from rest_api_handlers import runable_app

syslog.syslog('Web application is starting')
web.run_app(runable_app, host='localhost', port=9091)
