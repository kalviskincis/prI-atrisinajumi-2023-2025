from maizites import aprekins, varda_formatesana
import pytest

def test_aprekins():
    assert aprekins(0.90, 3) == 2.70
    assert aprekins(1, 1) == 1
    assert aprekins(1.5, 2) == 3

def test_varda_formatesana():
    assert varda_formatesana("kalvis") == "KALVIS"
    assert varda_formatesana("Kalvis") == "KALVIS"
    assert varda_formatesana("KALVIS") == "KALVIS"

test_aprekins()
test_varda_formatesana()