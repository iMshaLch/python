import keyboard
import time
a = '\
# # #   # # # #   #       #   # # # #   #  #       # # # #   # # #   # # # #   \n\
#   #   #     #   # #   # #   #     #   #     #    #     #   #   #   #     #   \n\
# # #   #     #   #   #   #   #     #   #     #    #     #   # # #   #     #   \n\
#       #     #   #       #   #     #   #     #    #     #   # #     #     #   \n\
#       # # # #   #       #   # # # #   #  #       # # # #   #   #   # # # #   '
print(a)
def countdown(t):
    while t:
        print("\033[H\033[J", end="")
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        # if keyboard.read_key() == None:
        #     continue
        # else:
        #     print("\033[H\033[J", end="")
        #     break
        
    print('Fire in the hole!!')

print("Standart pomidor 25 minut [1]\nKatta pomidor 60 minut [2]")
s =int(keyboard.read_key())
t = s * 25 * 60 if s == 1 else s/2 * 60 * 60

countdown(int(t))
print("\033[H\033[J", end="")

