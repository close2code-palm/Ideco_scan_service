# from syslog import syslog

import ipaddress as ipaddress

import aiohttp.web
from aiohttp import web

from scanner import run_scan

routes = web.RouteTableDef()


def validate_data(ip, s_p, e_p):
    """Exfiltrates user data"""
    try:
        ipaddress.ip_address(ip)
        s_p = int(s_p)
        e_p = int(e_p)
        if s_p > e_p or s_p < 1 or e_p < 1:
            raise ValueError
    except ValueError:
        pass
        # syslog(syslog.LOG_ERR, 'Provided values are not valid')
    else:
        return ip, s_p, e_p


@routes.get('/scan/{ip}/{begin_port:\d+}/{end_port:\d+}')
async def process_scan(request):
    """Handling request and serves response with results"""
    # syslog('Scan request received')
    ip_for_scan = request.match_info['ip']
    begin_port = request.match_info['begin_port']
    end_port = request.match_info['end_port']
    if valid := validate_data(ip_for_scan, begin_port, end_port):
        # syslog('Starting scan with given parameters')
        ip_for_scan, begin_port, end_port = valid
        scan_run = await run_scan(ip=ip_for_scan, start_port=begin_port, end_port=end_port)
        scan_result = [{'port': f'{p}', 'state': f'{s}'} for s, p in scan_run]
        return web.json_response(scan_result)
    raise aiohttp.web.HTTPBadRequest


app = web.Application()
app.add_routes(routes)
web.run_app(app, host='localhost', port=9091)
# syslog('Web application started')