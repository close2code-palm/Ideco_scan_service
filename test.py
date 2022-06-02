from aiohttp.abc import Application
from aiohttp.test_utils import AioHTTPTestCase

from rest_api_handlers import runable_app


class ScannerPointTestCase(AioHTTPTestCase):

    async def get_application(self) -> Application:
        return runable_app

    async def test_scan_res(self):
        async with self.client.request('GET', '/scan/127.0.0.1/5430/5435') as resp:  # dummy host
            self.assertEqual(resp.status, 200)
            answer = await resp.json()
        self.assertIn({'port': '5433', 'state': 'open'}, answer, )

    async def test_scan_fail(self):
        async with self.client.request('GET', '/scan/127.0.0.1/555555/-2') as response:
            self.assertEqual(response.status, 400)
