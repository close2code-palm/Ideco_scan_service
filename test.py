from aiohttp import web
from aiohttp.abc import Application
from aiohttp.test_utils import AioHTTPTestCase

from sswa.rest_api_handlers import process_scan, scan_route


class ScannerPointTestCase(AioHTTPTestCase):

    async def get_application(self) -> Application:
        app = web.Application()
        app.add_routes([web.get(
            scan_route, process_scan)])
        return app

    async def test_scan_res(self):
        test_server_port = self.server.port
        async with self.client.request(
                'GET', f'/scan/127.0.0.1/{test_server_port}/'
                       f'{test_server_port}') as resp:
            self.assertEqual(resp.status, 200)
            answer = await resp.json()
        self.assertIn({'port': f'{test_server_port}', 'state': 'open'}, answer, )

    async def test_scan_fail(self):
        async with self.client.request('GET', '/scan/127.0.0.1/65555/65666') as response:
            self.assertEqual(response.status, 400)
            response = await response.text()
            self.assertIn('Bad', response)
