from socketIO_client import SocketIO
import logging
#logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
#logging.basicConfig()

#bot variables
user_id = 'this_is_my_ID'
username = "[Bot] BOT1324"
custom_game_id = 'aedensgame'

#game variables
playerIndex = 0
generals = []
cities = []
map = []
game_over = False

def on_connect():
    print 'Connected to server'
    #Set the username for the bot.
    #This should only ever be done once. See the API reference for more details.
    """socketIO.emit('set_username', user_id, username)"""

    # Join a custom game and force start immediately.
    # Custom games are a great way to test your bot while you develop it because you can play against your bot!
    socketIO.emit('join_private', custom_game_id, user_id)
    print 'Joined custom game at http://bot.generals.io/games/' + custom_game_id
    socketIO.emit('set_force_start', custom_game_id, "true")

def on_disconnect():
    print 'Disconnected from server.'

def on_queue_update(data):
    #if we recieve a queue update, make sure we still have force start activated
    if data["isForcing"] == False:
        socketIO.emit("set_force_start", custom_game_id, "true")

def on_chat_message(*data):
    #print out any chat message we get
    if not game_over:
        print "Chat Message:  " + data[1][u'text']

def on_game_start(*data):
    #notify user of game start
    playerIndex = data[0][u'playerIndex']
    print "Game has started. Player index: " + str(playerIndex)
    print 'Game replay will be available at http://bot.generals.io/replays/' + str(data[0][u'replay_id'])

def on_game_update(*data):
    print "game update"

def leave_game():
    global game_over
    game_over = True
    socketIO.emit('leave_game')

def on_game_won(*data):
  print "Won Game."
  on_disconnect()
  leave_game()

def on_game_lost(*data):
  print "Lost Game. Killed by " + str(data[0][u'killer'])
  on_disconnect()
  leave_game()

socketIO = SocketIO('http://botws.generals.io')

socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('queue_update', on_queue_update)
socketIO.on('chat_message', on_chat_message)
socketIO.on('game_start', on_game_start)
socketIO.on('game_update', on_game_update)
socketIO.on('game_lost', on_game_lost)
socketIO.on('game_won', on_game_won)

while not game_over:
    socketIO.wait(seconds = 1)
socketIO.wait(seconds = 1)
