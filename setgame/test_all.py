
import random
from models import cards, cards_css, shuffle, validate_move


def setup():
    random.seed(42)


def test_correct_number_of_cards():
    assert len(list(cards())) == 81


def test_validate_moves_different():
    assert validate_move('green-squiggle-striped-one', 'red-diamond-solid-one', 'blue-diamond-solid-one') == False


def test_cards_css():
    assert cards_css() == '''.red-circle-solid span { background-position: -0px -0px; }
.red-circle-transparent span { background-position: -33px -0px; }
.red-circle-striped span { background-position: -66px -0px; }
.blue-circle-solid span { background-position: -99px -0px; }
.blue-circle-transparent span { background-position: -132px -0px; }
.blue-circle-striped span { background-position: -165px -0px; }
.green-circle-solid span { background-position: -198px -0px; }
.green-circle-transparent span { background-position: -231px -0px; }
.green-circle-striped span { background-position: -264px -0px; }
.red-diamond-solid span { background-position: -0px -55px; }
.red-diamond-transparent span { background-position: -33px -55px; }
.red-diamond-striped span { background-position: -66px -55px; }
.blue-diamond-solid span { background-position: -99px -55px; }
.blue-diamond-transparent span { background-position: -132px -55px; }
.blue-diamond-striped span { background-position: -165px -55px; }
.green-diamond-solid span { background-position: -198px -55px; }
.green-diamond-transparent span { background-position: -231px -55px; }
.green-diamond-striped span { background-position: -264px -55px; }
.red-squiggle-solid span { background-position: -0px -110px; }
.red-squiggle-transparent span { background-position: -33px -110px; }
.red-squiggle-striped span { background-position: -66px -110px; }
.blue-squiggle-solid span { background-position: -99px -110px; }
.blue-squiggle-transparent span { background-position: -132px -110px; }
.blue-squiggle-striped span { background-position: -165px -110px; }
.green-squiggle-solid span { background-position: -198px -110px; }
.green-squiggle-transparent span { background-position: -231px -110px; }
.green-squiggle-striped span { background-position: -264px -110px; }'''


def test_shuffle():
    shuffled_deck = shuffle()

    assert set(list(cards())) == set(shuffled_deck)
    assert shuffled_deck == [
        'green-circle-solid-three', 'green-circle-striped-two', 'blue-circle-transparent-one',
        'green-diamond-striped-three', 'green-circle-striped-three', 'blue-squiggle-striped-two',
        'blue-diamond-striped-three', 'red-circle-striped-one', 'green-circle-striped-one',
        'blue-circle-striped-one', 'blue-squiggle-solid-three', 'red-diamond-striped-one',
        'red-squiggle-striped-two', 'green-diamond-striped-two', 'red-circle-striped-three',
        'blue-circle-striped-three', 'blue-diamond-solid-two', 'red-squiggle-transparent-two',
        'green-squiggle-solid-three', 'red-squiggle-striped-one', 'blue-circle-solid-three',
        'red-squiggle-striped-three', 'blue-squiggle-solid-one', 'green-diamond-solid-three',
        'blue-diamond-solid-one', 'blue-diamond-solid-three', 'red-squiggle-solid-two',
        'red-squiggle-solid-one', 'red-diamond-transparent-three', 'red-circle-transparent-one',
        'red-diamond-solid-three', 'blue-diamond-transparent-three', 'blue-squiggle-striped-three',
        'green-circle-transparent-three', 'blue-squiggle-transparent-two', 'blue-squiggle-solid-two',
        'green-diamond-striped-one', 'red-circle-transparent-three', 'red-squiggle-transparent-one',
        'green-diamond-transparent-three', 'blue-circle-striped-two', 'blue-circle-transparent-three',
        'blue-circle-transparent-two', 'green-diamond-transparent-one', 'red-squiggle-transparent-three',
        'red-circle-transparent-two', 'green-squiggle-striped-one', 'blue-circle-solid-one',
        'red-circle-solid-three', 'red-diamond-transparent-two', 'green-diamond-transparent-two',
        'green-circle-solid-two', 'blue-circle-solid-two', 'blue-diamond-transparent-one',
        'green-circle-solid-one', 'red-diamond-solid-two', 'green-squiggle-striped-three',
        'red-diamond-solid-one', 'green-circle-transparent-two', 'blue-diamond-striped-one',
        'blue-squiggle-striped-one', 'blue-diamond-transparent-two', 'red-circle-striped-two',
        'blue-diamond-striped-two', 'blue-squiggle-transparent-one', 'red-diamond-striped-three',
        'red-circle-solid-two', 'green-diamond-solid-two', 'green-squiggle-striped-two',
        'green-squiggle-transparent-one', 'red-diamond-striped-two', 'green-squiggle-transparent-two',
        'green-diamond-solid-one', 'green-squiggle-solid-two', 'red-circle-solid-one',
        'red-squiggle-solid-three', 'red-diamond-transparent-one', 'green-squiggle-transparent-three',
        'green-circle-transparent-one', 'blue-squiggle-transparent-three', 'green-squiggle-solid-one'
    ]
