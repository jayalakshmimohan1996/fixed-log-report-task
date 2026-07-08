import json
from pathlib import Path


REPORT = Path("/app/report.json")


def load_report():
    return json.loads(REPORT.read_text())


def test_report_exists():
    """Criterion 1: /app/report.json exists and contains valid JSON."""
    assert REPORT.exists(), "no report.json found"
    load_report()


def test_report_schema():
    """Criterion 2: the JSON object has exactly the required keys."""
    data = load_report()
    assert set(data) == {
        "total_requests",
        "unique_ips",
        "requests_by_ip",
        "requests_by_path",
        "top_path",
    }


def test_total_requests():
    """Criterion 3: total_requests is the number of non-empty log entries."""
    data = load_report()
    assert data["total_requests"] == 6


def test_unique_ips():
    """Criterion 4: unique_ips is the number of distinct client IP addresses."""
    data = load_report()
    assert data["unique_ips"] == 3


def test_requests_by_ip():
    """Criterion 5: requests_by_ip maps each client IP to its request count."""
    data = load_report()
    assert data["requests_by_ip"] == {
        "10.0.0.5": 2,
        "192.168.0.1": 2,
        "192.168.0.2": 2,
    }


def test_requests_by_path():
    """Criterion 6: requests_by_path maps each requested path to its count."""
    data = load_report()
    assert data["requests_by_path"] == {
        "/about.html": 2,
        "/api/login": 1,
        "/index.html": 3,
    }


def test_top_path():
    """Criterion 7: top_path is the most frequent path, tie-broken lexicographically."""
    data = load_report()
    assert data["top_path"] == "/index.html"
