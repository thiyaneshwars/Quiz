questions = ["Which is the largest planet in our solar system?",
             "Who wrote the Indian national anthem Jana Gana Mana?",
             "What is the capital of Canada?",
             "Who discovered gravity?"]
options = [["a) Sydney", "b) Jupiter", "c) Canberra", "d) Perth"],
           ["a) Alexander Graham Bell", "b) Rabindranath Tagore", "c) Nikola Tesla", "d) Albert Einstein"],
           ["a) Alexander Graham Bell", "b) Thomas Edison", "c) Ottawa", "d) Albert Einstein"],
           ["a) Venus", "b) Mars", "c) Sir Isaac Newton", "d) Saturn"]]

ans = ["b", "b", "c", "c"]
answer = []
score = 0
question = 0

for i in questions:
    print(i)
    for y in options[question]:
        print(y)
    
    answers = input("Enter the answer: ")
    answer.append(answers)
    if answers == ans[question]:
        score += 1
        print("Correct")
    else:
        print("Wrong")
    question += 1
   

for g, ans in enumerate(answer):
    print(f"Your guess for Q{g+1} is {ans}")


print(f"Your total score is {score}")
