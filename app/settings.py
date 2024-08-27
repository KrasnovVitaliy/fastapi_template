from __future__ import annotations  # noqa: D100, INP001

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)


class Settings(BaseSettings):
    """Application settings class."""

    LOGGING_LEVEL: str
    LOGGING_LEVEL: str
    LOGGING_FORMAT: str
    WEB_HOST: str
    WEB_PORT: int
    SENTRY_DSN: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,  # noqa: ARG003
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        """Define the sources and their order for loading the settings values.

        Args:
        ----
            settings_cls: The Settings class.
            init_settings: The `InitSettingsSource` instance.
            env_settings: The `EnvSettingsSource` instance.
            dotenv_settings: The `DotEnvSettingsSource` instance.
            file_secret_settings: The `Secreye settings` instance.

        Returns:
        -------
            A tuple containing the sources and their order for loading the settings values.

        """
        return (
            init_settings,
            env_settings,  # environment is final authority
            dotenv_settings,
            YamlConfigSettingsSource(settings_cls, yaml_file="./config.yml"),
        )
