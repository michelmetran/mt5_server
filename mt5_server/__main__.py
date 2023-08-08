"""
Summary

07.08.2023
"""


import argparse
import shutil
from pathlib import Path
from subprocess import Popen

from rpyc.utils.classic import DEFAULT_SERVER_PORT, DEFAULT_SERVER_SSL_PORT

from mt5_server import server


def main():
    """
    Summary

    """
    parser = argparse.ArgumentParser(description='Create Server.')
    parser.add_argument(
        'python',
        type=str,
        help='Python that will run the server (have to be a Windows version!)',
    )
    parser.add_argument(
        '--host',
        type=str,
        default='localhost',
        help='The host to connect to. The default is localhost',
    )
    parser.add_argument(
        '-p',
        '--port',
        type=int,
        default=DEFAULT_SERVER_PORT,
        help=f'The TCP listener port (default = {DEFAULT_SERVER_PORT!r}, default for SSL = {DEFAULT_SERVER_SSL_PORT!r})',
    )
    parser.add_argument(
        '-s',
        '--server',
        type=str,
        default='tmp/mt5linux',
        help='Path where the server will be build and run (default = /tmp/mt5linux)',
    )
    # parser.add_argument(
    #     '-w',
    #     '--wine',
    #     type=str,
    #     default='wine',
    #     help='Command line to call wine program (default = wine)',
    # )
    args = parser.parse_args()

    # Parameters
    # wine_cmd = args.wine
    win_python_path = args.python
    server_dir = args.server
    port = args.port
    host = args.host
    server_code = 'server.py'

    # Create Dir (in Windows) for server MT5
    # Popen(['mkdir', '-p', str(server_dir)], shell=True).wait()
    module_path = Path(__file__).parent
    project_path = module_path.parent
    server_path = project_path / server_dir
    server_path.mkdir(exist_ok=True, parents=True)
    print(server_path)

    # Copy Server
    shutil.copy2(src=server.__file__, dst=server_path / server_code)

    # Execute
    Popen(
        [
            # wine_cmd,
            str(win_python_path),
            str(server_path / server_code),
            '--host',
            host,
            '-p',
            str(port),
        ],
        shell=True,
    ).wait()


if __name__ == '__main__':
    main()
