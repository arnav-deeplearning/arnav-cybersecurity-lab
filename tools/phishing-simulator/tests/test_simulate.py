import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from recipients import SYNTHETIC_RECIPIENTS  # noqa: E402
from simulate import run_campaign  # noqa: E402
from templates import TEMPLATES  # noqa: E402


def test_run_campaign_covers_every_recipient():
    result = run_campaign("password-expiring", seed=1)
    assert len(result.results) == len(SYNTHETIC_RECIPIENTS)


def test_same_seed_is_deterministic():
    a = run_campaign("prize-notification", seed=42)
    b = run_campaign("prize-notification", seed=42)
    assert [r.clicked for r in a.results] == [r.clicked for r in b.results]


def test_different_seeds_can_differ():
    outcomes = set()
    for seed in range(20):
        result = run_campaign("ceo-gift-card", seed=seed)
        outcomes.add(tuple(r.clicked for r in result.results))
    assert len(outcomes) > 1


def test_unknown_template_raises():
    with pytest.raises(ValueError):
        run_campaign("not-a-real-template")


def test_click_rate_bounds():
    result = run_campaign("password-expiring", seed=7)
    assert 0.0 <= result.click_rate <= 1.0


def test_more_convincing_template_has_higher_average_click_rate():
    # ceo-gift-card (difficulty 0.7) should, on average across many
    # simulated runs, produce a higher click rate than
    # prize-notification (difficulty 0.15).
    def average_click_rate(template_id, trials=200):
        total = 0.0
        for seed in range(trials):
            total += run_campaign(template_id, seed=seed).click_rate
        return total / trials

    convincing_rate = average_click_rate("ceo-gift-card")
    obvious_rate = average_click_rate("prize-notification")
    assert convincing_rate > obvious_rate


def test_every_template_has_red_flags_documented():
    for template in TEMPLATES:
        assert len(template.red_flags) >= 3, f"{template.id} should document its tells"


def test_to_dict_never_includes_real_email_sending_fields():
    result = run_campaign("password-expiring", seed=1)
    payload = result.to_dict()
    serialized = str(payload).lower()
    assert "smtp" not in serialized
    assert "@" not in serialized  # no real addresses in the report
