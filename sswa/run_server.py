from aiohttp import web

try:
    from rest_api_handlers import runable_app
except ModuleNotFoundError:
    from sswa.rest_api_handlers import runable_app


# syslog.syslog('Web application is starting')
def main():
    web.run_app(runable_app, host='localhost', port=9091)
