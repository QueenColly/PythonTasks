
#Excercises 4.14, 4.15, 4.16, 4.17 CAI System

import random

def get_numbers(difficulty):
    limit = 9 if difficulty == 1 else 99
    return random.randint(1, limit), random.randint(1, limit)

def get_question(n1, n2, p_type):
    if p_type == 5: p_type = random.randint(1, 4)
    
    if p_type == 1: return f"How much is {n1} plus {n2}?", n1 + n2
    if p_type == 2: return f"How much is {n1} minus {n2}?", n1 - n2
    if p_type == 3: return f"How much is {n1} times {n2}?", n1 * n2
    if p_type == 4: 
        if n2 == 0: n2 = 1
        return f"How much is {n1} divided by {n2} (integer)?", n1 // n2

def main_cai():
    diff = int(input("Difficulty (1 or 2): "))
    prob = int(input("Type (1:Add, 2:Sub, 3:Mul, 4:Div, 5:Mix): "))
    
    while True:
        num1, num2 = get_numbers(diff)
        prompt, answer = get_question(num1, num2, prob)
        
        while True:
            user_ans = int(input(f"{prompt} "))
            if user_ans == answer:
                print(random.choice(['Very good!', 'Nice work!', 'Keep up the good work!']))
                break
            else:
                print(random.choice(['No. Please try again.', 'Wrong. Try once more.', 'No. Keep trying.']))

