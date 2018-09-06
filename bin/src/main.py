from socketIO_client import SocketIO
#import logging
#logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
#logging.basicConfig()

user_id = 'happybirthdaytome1'
username = "[Bot] Aeden_bot"
custom_game_id = 'aedensgame'


def on_connect():
    print 'Connected to server'

    #Set the username for the bot.
    #This should only ever be done once. See the API reference for more details.
    socketIO.emit('set_username', user_id, username)

    # Join a custom game and force start immediately.
    # Custom games are a great way to test your bot while you develop it because you can play against your bot!
    socketIO.emit('join_private', custom_game_id, user_id)
    print 'Joined custom game at http://bot.generals.io/games/' + custom_game_id
    socketIO.emit('set_force_start', custom_game_id, "true")
    socketIO.emit('join_team', 5, "happybirthdaytome1")

def on_disconnect():
    print 'Disconnected from server.'

def on_aaa_response(*args):
    print('on_aaa_response', args)

socketIO = SocketIO('http://botws.generals.io')
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.wait(seconds = 10)
