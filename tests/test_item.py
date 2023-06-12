"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

item1 = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_name():
    assert item1.name == "Смартфон"


def test_instantiate_from_csv():
    Item.instantiate_from_csv("./src/items.csv")
    assert len(Item.all) == 6


def test_string_to_number():
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.66") == 6





