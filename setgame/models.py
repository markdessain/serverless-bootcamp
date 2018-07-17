import boto3
import random
import string
import json

dynamodb = boto3.resource('dynamodb') # endpoint_url='http://localstack:4569'


def cards():
    for shape in ['circle', 'diamond', 'squiggle']:
        for colour in ['red', 'blue', 'green']:
            for shade in ['solid', 'transparent', 'striped']:
                for number in ['one', 'two', 'three']:
                    yield '%s-%s-%s-%s' % (colour, shape, shade, number)


def temp_css_cards():
    for shape in ['circle', 'diamond', 'squiggle']:
        for colour in ['red', 'blue', 'green']:
            for shade in ['solid', 'transparent', 'striped']:
                yield '%s-%s-%s' % (colour, shape, shade)


def cards_css():
    return '\n'.join([
        '.%s span { background-position: -%spx -%spx; }' % (card, i%9 * 33, i//9 * 55)
        for i, card in enumerate(temp_css_cards())
    ])


def shuffle():
    cs = list(cards())
    for _ in range(5):
        random.shuffle(cs)
    return cs


def game_id():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))


def create_game():
    cards = shuffle()
    games = dynamodb.Table('games')

    item = {
        'game_id': game_id(),
        'deck': cards[12:],
        'drawn': cards[:12],
        'player_1': [],
        # 'player_2': [],
    }

    games.put_item(Item=item)

    return item['game_id']


def select_set(game_id, card_1, card_2, card_3):
    if validate_cards(game_id, card_1, card_2, card_3) and  validate_move(card_1, card_2, card_3):
        drawn = get_drawn(game_id)
        deck = get_deck(game_id)

        if len(drawn) == 12:
            new_card_1 = deck.pop()
            new_card_2 = deck.pop()
            new_card_3 = deck.pop()

            drawn[drawn.index(card_1)] = new_card_1
            drawn[drawn.index(card_2)] = new_card_2
            drawn[drawn.index(card_3)] = new_card_3
        else:
            del drawn[drawn.index(card_1)]
            del drawn[drawn.index(card_2)]
            del drawn[drawn.index(card_3)]

        games = dynamodb.Table('games')
        response = games.update_item(
            Key={'game_id': game_id},
            UpdateExpression="set drawn = :d, deck = :f",
            ExpressionAttributeValues={
                ':d': drawn,
                ':f': deck,
            },
            ReturnValues="UPDATED_NEW"
        )

        return True
    else:
        return False


def validate_cards(game_id, card_1, card_2, card_3):
    drawn = get_drawn(game_id)

    print(drawn, card_1, card_2, card_3)
    return (
        card_1 in drawn and
        card_2 in drawn and
        card_3 in drawn
    )


def validate_move(card_1, card_2, card_3):
    card_1 = card_1.split('-')
    card_2 = card_2.split('-')
    card_3 = card_3.split('-')

    if len(set([card_1[0]] + [card_2[0]] + [card_3[0]])) == 2:
        return False

    if len(set([card_1[1]] + [card_2[1]] + [card_3[1]])) == 2:
        return False

    if len(set([card_1[2]] + [card_2[2]] + [card_3[2]])) == 2:
        return False

    if len(set([card_1[3]] + [card_2[3]] + [card_3[3]])) == 2:
        return False
    # Check that the cards are a valid combination
    return True


def deal_more_cards(game_id):
    drawn = get_drawn(game_id)
    deck = get_deck(game_id)

    new_card_1 = deck.pop()
    new_card_2 = deck.pop()
    new_card_3 = deck.pop()

    drawn.append(new_card_1)
    drawn.append(new_card_2)
    drawn.append(new_card_3)

    games = dynamodb.Table('games')
    response = games.update_item(
        Key={'game_id': game_id},
        UpdateExpression="set drawn = :d, deck = :f",
        ExpressionAttributeValues={
            ':d': drawn,
            ':f': deck,
        },
        ReturnValues="UPDATED_NEW"
    )


def get_drawn(game_id):
    games = dynamodb.Table('games')
    game = games.get_item(
        TableName='games',
        Key={'game_id': game_id}
    )
    if 'Item' in game:
        return game['Item'].get('drawn', [])
    else:
        return []


def get_deck(game_id):
    games = dynamodb.Table('games')
    game = games.get_item(
        TableName='games',
        Key={'game_id': game_id}
    )
    if 'Item' in game:
        return game['Item'].get('deck', [])
    else:
        return []
