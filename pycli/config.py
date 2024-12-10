import os
import json
import click
from pathlib import Path


def get_config_file() -> Path:
    """Get the path to the config file"""
    config_dir = Path.home() / ".firecrawl"
    config_dir.mkdir(exist_ok=True)
    return config_dir / "config.json"


def load_config() -> dict:
    """Load configuration from file"""
    config_file = get_config_file()
    if config_file.exists():
        with open(config_file) as f:
            return json.load(f)
    return {}


def save_config(config: dict):
    """Save configuration to file"""
    config_file = get_config_file()
    with open(config_file, "w") as f:
        json.dump(config, f, indent=2)
    # Secure the config file
    config_file.chmod(0o600)


def get_api_key():
    """Get API key from config, environment variable, or prompt user"""
    # Try environment first
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if api_key:
        return api_key

    # Try config file
    config = load_config()
    api_key = config.get("api_key")
    if api_key:
        return api_key

    # Prompt user
    api_key = click.prompt(
        "Please enter your FireCrawl API key (get one at https://firecrawl.dev)",
        type=str,
        hide_input=True,
    )

    # Save to config if user wants to
    if click.confirm(
        "Would you like to save the API key for future use?", default=True
    ):
        config["api_key"] = api_key
        save_config(config)
        click.echo("API key saved to ~/.firecrawl/config.json")
    else:
        # If not saving to config, at least save for current session
        os.environ["FIRECRAWL_API_KEY"] = api_key
        click.echo("API key saved for this session")

    return api_key
