import pytest


EXPECTED_VALUES = {
    "merchant": "Riverbend Diner",
    "receipt_date": "2026-05-08",
    "receipt_total": "$42.75",
    "event": "Petersburg Visit",
    "budget": "$120.00",
    "current_spend": "$77.25",
    "updated_spend": "$77.25",
    "duplicate_status": "Duplicate Found",
    "recipient": "Linda Cotton"
}


def test_merchant_present(final_answer):
    assert "Riverbend Diner" in final_answer


def test_receipt_date_present(final_answer):
    assert "2026-05-08" in final_answer


def test_receipt_total_present(final_answer):
    assert "$42.75" in final_answer


def test_matching_event_present(final_answer):
    assert "Petersburg Visit" in final_answer


def test_duplicate_detected(final_answer):
    assert "duplicate" in final_answer.lower()


def test_existing_transaction_preserved(final_answer):
    assert (
        "existing transaction" in final_answer.lower()
        or "already exists" in final_answer.lower()
    )


def test_budget_present(final_answer):
    assert "$120.00" in final_answer


def test_current_spend_present(final_answer):
    assert "$77.25" in final_answer


def test_notification_recipient(final_answer):
    assert "Linda Cotton" in final_answer


def test_no_family_dinner(final_answer):
    assert "Family Dinner" not in final_answer


def test_no_new_transaction(final_answer):
    assert "new transaction created" not in final_answer.lower()


def test_authoritative_source(final_answer):
    assert "authoritative" in final_answer.lower()