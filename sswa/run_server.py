"""Used as entry point"""

from aiohttp import web

from sswa.rest_api_handlers import runable_app

syslog.syslog('Web application is starting')
web.run_app(runable_app, port=9091)
