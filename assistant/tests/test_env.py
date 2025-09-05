import os

def test_slack_env_loaded():
    """Check that SLACK_WEBHOOK_URL is set (dummy value in CI)."""
    url = os.getenv("SLACK_WEBHOOK_URL", "")
    assert url != "", "SLACK_WEBHOOK_URL is not set!"
