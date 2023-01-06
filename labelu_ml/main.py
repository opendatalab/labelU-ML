import os
import sys
import shutil
import uvicorn
import importlib
from loguru import logger
from typer import Typer, Argument
from typing import List, Optional


cli = Typer()

@cli.command(name="init", help="Initailize an ML app from a example")
def init(
    app: str = Argument(...),
    path: Optional[str] = None,
):
    logger.debug(f"init current path is: {os.getcwd()}")
    output_dir = os.path.join(app)
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    shutil.copytree(path, output_dir)

@cli.command(name="start", help="Start ML app server")
def start(
    app: str,
    host: Optional[str] = "localhost",
    port: Optional[int] = 9000,
    with_args: Optional[List[str]] = None,
):
    logger.debug(f"current path is: {os.getcwd()}")
    sys.path.append(os.getcwd())

    app_name = app.strip(".").strip("/")
    module = importlib.import_module(f"{app_name}._wsgi")
    parsed_kwargs = dict([args.split("=") for args in with_args])
    module.init_kwargs(**parsed_kwargs)
    uvicorn.run(app=module.app, host=host, port=port, log_level="debug")


if __name__ == "__main__":
    cli()
