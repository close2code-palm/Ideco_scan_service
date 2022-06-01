import asyncio
import ipaddress
from typing import List, Tuple


async def scan_port(ip: ipaddress, port: int) -> Tuple[str, int]:
    """Handling one connection per call"""
    connection = asyncio.open_connection(ip, port)
    try:
        await asyncio.wait_for(
            connection, timeout=4)
        return 'open', port
    except (asyncio.TimeoutError, OSError, ConnectionRefusedError) as err:
        return 'closed', port


async def run_scan(ip: ipaddress, start_port: int, end_port: int) -> List[Tuple[str, int]]:
    """Makes full scan y giveng clean paraeters"""
    tasks = [asyncio.create_task(scan_port(ip, p)) for p in range(start_port, end_port + 1)]
    responses = await asyncio.gather(*tasks)
    return responses
