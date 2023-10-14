from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from pathlib import Path

import httpx
from litestar import Litestar
from litestar.config.compression import CompressionConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.logging.config import LoggingConfig
from litestar.middleware.logging import LoggingMiddlewareConfig
from litestar.static_files import StaticFilesConfig
from litestar.template import TemplateConfig

from masterofgames.config import config
from masterofgames.controllers import view_router

logging_middleware_config = LoggingMiddlewareConfig()


def raise_on_4xx_5xx(response):
    response.raise_for_status()


@asynccontextmanager
async def http_client(app: Litestar) -> AsyncGenerator[None, None]:
    client = getattr(app.state, "client", None)
    if client is None:
        app.state.client = httpx.AsyncClient(base_url=config.steam_url, event_hooks={"response": [raise_on_4xx_5xx]})
        app.state.api_key = config.steam_api_key

    try:
        yield
    finally:
        if client:
            await client.close()


app = Litestar(
    route_handlers=[view_router],
    openapi_config=None,
    logging_config=LoggingConfig(),
    compression_config=CompressionConfig(backend="gzip", gzip_compress_level=6),
    middleware=[logging_middleware_config.middleware],
    template_config=TemplateConfig(
        directory=Path("templates"),
        engine=JinjaTemplateEngine,
    ),
    static_files_config=[StaticFilesConfig(path="/static", directories=[Path("static")], name="static")],
    lifespan=[http_client],
)
