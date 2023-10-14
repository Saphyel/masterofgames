from pathlib import Path

from litestar import Litestar
from litestar.config.compression import CompressionConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.logging.config import LoggingConfig
from litestar.middleware.logging import LoggingMiddlewareConfig
from litestar.static_files import StaticFilesConfig
from litestar.template import TemplateConfig

from masterofgames.controllers import view_router

logging_middleware_config = LoggingMiddlewareConfig()

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
)
