import json

from aiohttp import web

from scanner import run_scan

routes = web.RouteTableDef()


@routes.get('/scan/{ip}/{begin_port}/{end_port}')
async def process_scan(request):
    ip_for_scan = request.match_info['ip']
    begin_port = int(request.match_info['begin_port'])
    end_port = int(request.match_info['end_port'])
    scan_run = await run_scan(ip=ip_for_scan, start_port=begin_port, end_port=end_port)
    scan_result = [{'port': f'{p}', 'state': f'{s}'} for s, p in scan_run]
    return web.json_response(scan_result)


app = web.Application()
app.add_routes(routes)
web.run_app(app, host='localhost', port=9091)
