
#Exercise4.12 Simulation: The Tortoise and the Hare

import random

def move_tortoise(pos):
    i = random.randint(1, 10)
    if 1 <= i <= 5: pos += 3     # Fast plod
    elif 6 <= i <= 7: pos -= 6   # Slip
    else: pos += 1               # Slow plod
    return max(1, pos)           # Don't go below 1

def move_hare(pos):
    i = random.randint(1, 10)
    if 1 <= i <= 2: pass         # Sleep
    elif 3 <= i <= 4: pos += 9   # Big hop
    elif i == 5: pos -= 12       # Big slip
    elif 6 <= i <= 8: pos += 1   # Small hop
    else: pos -= 2               # Small slip
    return max(1, pos)

t_pos, h_pos = 1, 1
print("BANG !!!!!\nAND THEY'RE OFF !!!!!")

while t_pos < 70 and h_pos < 70:
    t_pos = move_tortoise(t_pos)
    h_pos = move_hare(h_pos)
    
    line = [" "] * 71
    if t_pos == h_pos:
        line[t_pos] = "OUCH!!!"
    else:
        line[t_pos] = "T"
        line[h_pos] = "H"
    print("".join(line))

if t_pos >= 70 and h_pos >= 70: print("It's a tie.")
elif t_pos >= 70: print("TORTOISE WINS!!! YAY!!!")
else: print("Hare wins. Yuch.")
