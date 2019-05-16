import asyncio
import time
from pyatv import helpers

@asyncio.coroutine
def print_what_is_playing(atv):
    playing = yield from atv.metadata.playing()
    print('Currently playing:')
    print(playing)

@asyncio.coroutine
def go_home(atv):
    yield from atv.remote_control.top_menu() #GO TO HOME MENU
    ###CMD 1 Complete

@asyncio.coroutine
def open_hbo(atv):
    x = 0
    while x < 7:
        yield from atv.remote_control.left() #GO TO LEFT
        x+=1
    x = 0
    while x < 8:
        yield from atv.remote_control.up() #GO TO TOP CORNER
        x+=1
    x = 0
    while x < 1:
        yield from atv.remote_control.down() #GO TO HBO ROW
        x+=1
    x = 0
    while x < 2:
        yield from atv.remote_control.right() #GO TO HBO
        x+=1
    x = 0
    yield from atv.remote_control.select() #OPEN HBO
    ###CMD 2 complete

@asyncio.coroutine
def select_search(atv):
    x = 0
    while x < 10:
        yield from atv.remote_control.up() #GO TO TOP of screen
        x+=1
    x = 0
    while x < 4:
        yield from atv.remote_control.right() #GO TO RIGHT CORNER
        x+=1
    x = 0
    while x < 1:
        yield from atv.remote_control.left() #GO TO SEARCH
        x+=1
    x = 0
    yield from atv.remote_control.select() #SELECT SEARCH
    ##CMD 3 complete

@asyncio.coroutine
def find_letter_v(atv):
    x = 0
    while x < 23:
        yield from atv.remote_control.right() #GO TO V
        x+=1
    yield from atv.remote_control.select() #SELECT V
    ##CMD 4 complete
    

@asyncio.coroutine
def find_letter_i(atv):
    x = 0
    while x < 13:
        yield from atv.remote_control.left() #GO TO I FROM V
        x+=1
    x = 0
    yield from atv.remote_control.select() #SELECT I
    ##CMD 5 complete
    
@asyncio.coroutine
def select_vice(atv):
    x = 0
    while x < 2:
        yield from atv.remote_control.down() #GO TO VICE
        x+=1
    x = 0
    yield from atv.remote_control.select() #SELECT VICE
    ##CMD 6 complete
    
@asyncio.coroutine
def select_latest_episode(atv):
    x = 0
    while x < 1:
        yield from atv.remote_control.down() #GO TO LATEST EPISODE
        x+=1
    x = 0
    yield from atv.remote_control.select() #SELECT LATEST EPISODE

@asyncio.coroutine
def play_latest_episode(atv):
    yield from atv.remote_control.select() #PLAY LATEST EPISODE

@asyncio.coroutine
def full_run(atv):
    a = yield from atv.remote_control.top_menu() #GO TO HOME MENU
    ###CMD 1 Complete
    if a:
        time.sleep(1)
    x = 0
    while x < 7:
        yield from atv.remote_control.left() #GO TO LEFT
        x+=1
    x = 0
    while x < 8:
        yield from atv.remote_control.up() #GO TO TOP CORNER
        x+=1
    x = 0
    while x < 1:
        yield from atv.remote_control.down() #GO TO HBO ROW
        x+=1
    x = 0
    while x < 2:
        yield from atv.remote_control.right() #GO TO HBO
        x+=1
    x = 0
    a = yield from atv.remote_control.select() #OPEN HBO
    ###CMD 2 complete
    if a:
        time.sleep(1)
    # x = 0
    # while x < 10:
    #     yield from atv.remote_control.up() #GO TO TOP of screen
    #     x+=1
    # x = 0
    # while x < 4:
    #     yield from atv.remote_control.right() #GO TO RIGHT CORNER
    #     x+=1
    # x = 0
    # while x < 1:
    #     yield from atv.remote_control.left() #GO TO SEARCH
    #     x+=1
    # x = 0
    # yield from atv.remote_control.select() #SELECT SEARCH
    # ##CMD 3 complete
    # x = 0
    # while x < 23:
    #     yield from atv.remote_control.right() #GO TO V
    #     x+=1
    # yield from atv.remote_control.select() #SELECT V
    # ##CMD 4 complete
    # time.sleep(1)
    # x = 0
    # while x < 13:
    #     yield from atv.remote_control.left() #GO TO I FROM V
    #     x+=1
    # x = 0
    # yield from atv.remote_control.select() #SELECT I
    # ##CMD 5 complete
    # time.sleep(1)
    # x = 0
    # while x < 2:
    #     yield from atv.remote_control.down() #GO TO VICE
    #     x+=1
    # x = 0
    # yield from atv.remote_control.select() #SELECT VICE
    # ##CMD 6 complete
    # time.sleep(1)
    # x = 0
    # while x < 1:
    #     yield from atv.remote_control.down() #GO TO LATEST EPISODE
    #     x+=1
    # x = 0
    # yield from atv.remote_control.select() #SELECT LATEST EPISODE
    # ##CMD 7 complete
    # time.sleep(1)
    # yield from atv.remote_control.select() #PLAY LATEST EPISODE


helpers.auto_connect(go_home)
helpers.auto_connect(open_hbo)
helpers.auto_connect(select_search)
helpers.auto_connect(find_letter_v)
helpers.auto_connect(find_letter_i)
helpers.auto_connect(select_vice)
helpers.auto_connect(select_latest_episode)
helpers.auto_connect(play_latest_episode)

# helpers.auto_connect(full_run)

# yield from atv.remote_control.top