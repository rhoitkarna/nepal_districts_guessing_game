import turtle
import pandas

screen = turtle.Screen()
screen.title("Nepal District Guess")
screen.setup(width=900, height=600)
image = "image.gif"
score = 0
writing_turtle = turtle.Turtle()
writing_turtle.hideturtle()
writing_turtle.penup()

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("district - Sheet1.csv")
districts = data["district"].to_list()

while score != 75:
    user_guess = screen.textinput(title=f"{score}/75 Guesses Correct", prompt="Make a guess").title()
    if user_guess == "Exit":
        break
    if user_guess in districts:
        score = score + 1
        x_cor = int(data[data.district == user_guess].x)
        y_cor = int(data[data.district == user_guess].y)
        writing_turtle.goto(x_cor, y_cor - 5)
        writing_turtle.write(f"{user_guess}", align="center", font=("Arial", 6, "bold"))
        districts.remove(user_guess)

districts_not_guessed = pandas.DataFrame(districts)
districts_not_guessed.to_csv("learn_these.csv")

screen.mainloop()
