import json

from models import create_game, get_drawn, select_set, cards_css, deal_more_cards


def index(event, context):
    return {
        'statusCode': 200,
        'body': '''
            <style>
                #table {
                    width: 443px;
                    margin: 0 auto;
                }

                #table a {
                    float: left;
                }

                .card {
                    width: 99px;
                    height: 55px;
                    margin: 20px;
                    border: 2px solid white;
                }

                .card span {
                    background-image: url('http://markdessain-setgame.s3-website-eu-west-1.amazonaws.com/images/cards.png');
                    width: 33px;
                    height: 55px;
                    float: left;
                }

                .selected {
                    border: 2px solid red;
                }

                %s

            </style>
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
            <script>

                var endpoint = 'http://localhost:3000'; // https://udy11c2m7j.execute-api.eu-west-1.amazonaws.com/dev';
                var game_id = '';
                var selected_cards = [];

                function join_game(game_id){
                    console.log('Joined Game: ' + game_id);
                    $.get(endpoint + '/join_game?game_id=' + game_id, function( data ) {
                        $('#table').empty();

                        $.each(data['drawn'], function(index, value) {
                            var arr = value.split('-');
                            var c = arr[0] + '-' + arr[1] + '-' + arr[2];
                            var n = ''
                            if(arr[3] == 'one') {
                                n = '<span></span>'
                            } else if(arr[3] == 'two') {
                                n = '<span></span><span></span>'
                            } else if(arr[3] == 'three') {
                                n = '<span></span><span></span><span></span>'
                            }
                            $("#table").append("<a href='#' name='" + value + "' class='card " + c + "'>" + n + "</a>");
                        });

                        $('.card').click(function() {
                            $(this).toggleClass('selected');
                            var name = $(this).attr('name');

                            var index = selected_cards.indexOf(name);
                            if (index >= 0) {
                                selected_cards.splice(index, 1);
                            } else {
                                selected_cards.push(name)
                            }
                            console.log(selected_cards);

                            if(selected_cards.length == 3) {
                                console.log('selected');
                                console.log(endpoint + '/select_cards?game_id=' + game_id + '&card_1=' + selected_cards[0] + '&card_2=' + selected_cards[1] + '&card_3=' + selected_cards[2]);
                                $.get(endpoint + '/select_cards?game_id=' + game_id + '&card_1=' + selected_cards[0] + '&card_2=' + selected_cards[1] + '&card_3=' + selected_cards[2], function( data ) {
                                    selected_cards = [];
                                    join_game(game_id);
                                });
                            }
                        });
                    });
                }

                function start_game(){
                    console.log('Started Game');
                    $.get(endpoint + '/start_game', function( data ) {
                        $('#game_id').val(data['game_id']);
                        game_id = data['game_id'];
                        join_game(data['game_id'])
                    });
                }

                $(document).ready(function() {

                    $('#start_game').click(function() {
                        start_game();
                    });

                    $('#join_game').click(function() {
                        join_game($('#game_id').val());
                    });

                    $('#add_extra_cards').click(function() {
                        console.log('a');
                        $.get(endpoint + '/add_extra?game_id=' + game_id, function( data ) {
                            console.log('b');
                            join_game(game_id);
                        });
                    });

              });
            </script>

            <h1>Set Game</h1>

            <div id='controls'>
                <input type='text' id='game_id' /> <a href='#' id='join_game'>Join Game</a> or
                <a href='#' id='start_game'>Start Game</a> <br /><br />
                <a href='#' id='add_extra_cards'>Add Extras Cards</a>
            </div>

            <div id='table'>
            </div>
        ''' % cards_css(),
        'headers': {
            'Content-Type': 'text/html'
        },
    }


def start_game(event, context):
    game_id = create_game()

    return {
        'statusCode': 200,
        'body': json.dumps({
            'game_id': game_id
        })
    }


def join_game(event, context):
    query = event.get('queryStringParameters', {})

    game_id = query.get('game_id')
    drawn = get_drawn(game_id)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'game_id': game_id,
            'drawn': drawn
        })
    }


def select_cards(event, context):
    game_id = event['queryStringParameters'].get('game_id')
    card_1 = event['queryStringParameters'].get('card_1')
    card_2 = event['queryStringParameters'].get('card_2')
    card_3 = event['queryStringParameters'].get('card_3')

    valid = select_set(game_id, card_1, card_2, card_3)
    drawn = get_drawn(game_id)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'game_id': game_id,
            'drawn': drawn,
            'valid': valid
        })
    }


def add_extra(event, context):
    game_id = event['queryStringParameters'].get('game_id')

    deal_more_cards(game_id)
    drawn = get_drawn(game_id)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'game_id': game_id,
            'drawn': drawn
        })
    }
