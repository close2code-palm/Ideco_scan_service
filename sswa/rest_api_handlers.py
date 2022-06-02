"""Web application, REST endpoint of scanner
module also contains supportive function
"""

import ipaddress as ipaddress
import syslog

import aiohttp.web
from aiohttp import web
from aiohttp.web_routedef import Request

from sswa.scanner import run_scan


def validate_data(ip, s_p, e_p):
    """Exfiltrates user data"""
    try:
        ipaddress.ip_address(ip)
        s_p = int(s_p)
        e_p = int(e_p)
        if s_p > e_p or s_p < 1 or e_p < 1 or 65535 < e_p:
            raise ValueError
    except ValueError:
        syslog.syslog(syslog.LOG_ERR, 'Provided values are not valid')
    else:
        return ip, s_p, e_p


async def process_scan(request: Request):
    """Handling request and serves response with results"""
    syslog.syslog(f'Scan request received from {request.remote}')
    ip_for_scan = request.match_info['ip']
    begin_port = request.match_info['begin_port']
    end_port = request.match_info['end_port']
    if valid := validate_data(ip_for_scan, begin_port, end_port):
        syslog.syslog('Starting scan with given parameters')
        ip_for_scan, begin_port, end_port = valid
        scan_run = await run_scan(ip=ip_for_scan, start_port=begin_port, end_port=end_port)
        scan_result = [{'port': f'{p}', 'state': f'{s}'} for s, p in scan_run]
        return web.json_response(scan_result)
    syslog.syslog(syslog.LOG_ERR, f'Request from {request.remote} is not processable')
    raise aiohttp.web.HTTPBadRequest


app = web.Application()
scan_route = r'/scan/{ip}/{begin_port:\d+}/{end_port:\d+}'
app.add_routes([web.get(scan_route,
                        process_scan)])

runable_app = app
