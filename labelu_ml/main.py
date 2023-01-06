import os
import sys
import shutil
import uvicorn
import importlib
from loguru import logger
from typer import Typer, Argument, Option
from typing import List, Optional


cli = Typer()

@cli.command(name="init", help="Initailize an ML app from a example.")
def init(
    app: str = Argument(..., help="Application name."),
    path: Optional[str] = Option(default="labelu_ml/examples/the_simplest_app", help="LabelU-ML example path."),
):
    logger.debug(f"init current path is: {os.getcwd()}")
    output_dir = os.path.join(app)
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    shutil.copytree(path, output_dir)

@cli.command(name="start", help="Start ML app server.")
def start(
    app: str = Argument(..., help="Application name."),
    host: Optional[str] = Option(default="localhost", help="Bind socket to this host."),
    port: Optional[int] = Option(default=9000, help="Bind socket to this port."),
    with_args: Optional[List[str]] = Option(default=None, help="Application args."),
):
    logger.debug(f"application current path is: {os.getcwd()}")
    sys.path.append(os.getcwd())

    app_name = app.strip(".").strip("/")
    module = importlib.import_module(f"{app_name}._wsgi")
    parsed_kwargs = dict([args.split("=") for args in with_args])
    module.init_kwargs(**parsed_kwargs)
    uvicorn.run(app=module.app, host=host, port=port, log_level="debug")


if __name__ == "__main__":
    cli()
