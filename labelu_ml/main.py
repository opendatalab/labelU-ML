import os
import sys
import shutil
import uvicorn
import importlib
from pathlib import Path
from loguru import logger
from typing import List, Optional
from typer import Typer, Argument, Option


cli = Typer()


@cli.command(name="init", help="Initailize an ML app from a example.")
def init(
    app: str = Argument(..., help="Application name."),
    path: Optional[Path] = Option(
        default="labelu_ml/examples/the_simplest_app", help="LabelU-ML example path."
    ),
):

    if not path.exists():
        folder = "labelu_ml/examples"
        sub_folders = [
            os.path.join(folder, name)
            for name in os.listdir(folder)
            if os.path.isdir(os.path.join(folder, name))
        ]
        logger.error(f"labelu ml example paths:{sub_folders}")
        raise NotADirectoryError(path)

    logger.debug(f"init current path is: {os.getcwd()}")
    output_dir = os.path.join(app)
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

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
