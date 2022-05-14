from web import validator_reconstruct


def a_tester_reconstruct_three_D(payload_to_check: dict, expected_validation_status: bool,
                                 expected_errors: list = None):
    payload_ok = validator_reconstruct.validate(payload_to_check)
    assert payload_ok == expected_validation_status, validator_reconstruct.errors

    if expected_errors is not None:
        assert validator_reconstruct.errors == expected_errors


def test_validation_reconstruct_three_D_empty():
    payload = {
        "xy": {"type": "polygon", "vertices": {}, "edges": {}},
        "xz": {"type": "polygon", "vertices": {}, "edges": {}},
        "yz": {"type": "polygon", "vertices": {}, "edges": {}}
    }
    a_tester_reconstruct_three_D(payload, True)
