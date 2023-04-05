from seasons import get_mins, validate
import pytest
from datetime import datetime, timedelta, date

one_year_ago = (datetime.now() - timedelta(days=365)).date()


def test_date_invalid_format():
    with pytest.raises(SystemExit):
        validate("1.1.2022")

def test_date_valid():
    assert(validate("2022-04-03")) == datetime.strptime("2022-04-03", r"%Y-%m-%d").date()


