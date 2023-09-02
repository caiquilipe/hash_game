from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import settings


class HashGameFastApi(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_config()

    def _set_config(self):
        self.title = settings.PROJECT_NAME
        self.description = settings.PROJECT_DESCRIPTION
        self.version = settings.PROJECT_VERSION
        self.docs_url = settings.DOCS_URL
        self.openapi_url = settings.OPENAPI_URL
        self.add_middleware(
            CORSMiddleware,
            allow_origins=settings.ALLOWED_HOSTS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        # self.include_router(api_router, prefix=settings.API_PREFIX)


app = HashGameFastApi()
