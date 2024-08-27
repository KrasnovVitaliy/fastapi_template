"""Fastapi template service.

The version of the OpenAPI document: 1.0.0
Generated by: https://openapi-generator.tech
"""

import logging

import sentry_sdk
from fastapi import FastAPI
from settings import Settings
from store.factory import StoreFactory

from app.controllers.sample_controller import router as SampleApiRouter
from app.services.sample_service import SampleService

logging.basicConfig(
    level=logging.getLevelNamesMapping()[Settings().LOGGING_LEVEL],
    format=Settings().LOGGING_FORMAT,
)

logger = logging.getLogger(__name__)


sentry_sdk.init(
    dsn=Settings().SENTRY_DSN,
    traces_sample_rate=1.0,
)

app = FastAPI(
    title="Fastapi service",
    description="Fastapi template service",
    version="0.0.0",
)

store_factory = StoreFactory(sample_store_type="inmemory")

app.state.auth_service = SampleService(
    sample_store=store_factory.sample_store(),
)

app.include_router(SampleApiRouter)
