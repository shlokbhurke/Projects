import random
def main():
  score = []
  name = str(input("Please enter your name:"))
  while name == "":
    print("Name cannot be blank")
    name = str(input("Please enter your name:"))
  print("Welcome", name, ".")
  print("Let's play golf, CP1401 style!")
  par = int_valid("Choose a par for this course (between 3-5 inclusive):")
  while par > 5 or par < 3:
    par = int_valid("I’m sorry, you must choose a number between 3-5 inclusive. Please enter again:")
  dist_hole = int_valid("How many meters to the hole (between 195 – 250 inclusive):")
  while dist_hole < 195 or dist_hole > 250:
    dist_hole = int_valid("I’m sorry, you must choose a distance between 195-250 inclusive. Please enter distance again:")
  
  print("(I)ntructions")
  print("(P)lay golf")
  print("(Q)uit")
  option = str(input("Please enter your preferred option:")).upper()
  option_check(option)
  totalshot = 0
  hole = 0
  while option == "I":
    print("This is a simple golf game in which each hole is 230m game away with par 5. You are able to choose from 3 clubs, the Driver, Iron or Putter. The Driver will hit around 100m, the Iron around 30m and the Putter around 10m. The putter is best used very close to the hole.")
    print("For each shot, you may use a driver, iron or a putter – each shot will vary in distance. \n The average distance each club can hit is:")
    print("{:^20s}".format("Driver = 100m"))
    print("{:^20s}".format("Iron = 30m"))
    print("{:^20s}".format("Putter = 10m"))
    print("(I)ntructions")
    print("(P)lay golf")
    print("(Q)uit")
    option = str(input("Please enter the preferred option:"))
  option_check(option)
  while option == "P":
    shot = 0
    print("This hole is a", dist_hole, "m par", par)
    print("You are", dist_hole, "m from the hole after", shot, "shot/s.")
    while dist_hole != 0:
      print("Club selection: press D for driver, I for Iron, P for Putter.")
      club_select = str(input("Choose club:")).upper()
      if club_select == "D":
        driver_averagedist = random.randint(80, 120)
        distance_travelled = dist_hole - driver_averagedist
        dist_hole = distance_travelled
        shot += 1
        if dist_hole < 0:
          dist_hole = -dist_hole
        print("Your shot went", driver_averagedist, "m. You are", dist_hole, "m from the hole after", shot, "shots.")
      elif club_select == "I":
        iron_averagedist = random.randint(24, 36)
        distance_travelled = dist_hole - iron_averagedist
        dist_hole = distance_travelled
        shot += 1
        if dist_hole < 0:
          dist_hole = -dist_hole
        print("Your shot went", iron_averagedist, "m. You are", dist_hole, "m from the hole after", shot, "shots.")
      elif club_select == "P":
        if dist_hole < 10:
          putter_min = round(dist_hole * 0.8)
          putter_max = round(dist_hole * 1.2)
          putter_averagedist = random.randint(putter_min,putter_max)
          dist_hole = dist_hole - putter_averagedist
          shot +=1
      else:
        print("Invalid Club Selection = air swing :(")
        shot += 1
        dist_hole = dist_hole
        print("Your shot went 0 m. You are", dist_hole, "m from the hole after", shot, "shots.")
    print("Clunk... After", shot, "shots, the ball is in the hole!")
    if shot > par:
      print("Disappointing. You are", shot - par, "over par.")
    elif shot == par:
      print("And's that's par.")
    elif shot < par:
      print("Congratulations, you are under", par - shot, "par for this hole.")
    totalshot += shot
    hole += 1
    par_total = par * hole
    score.append(shot)
    calculate(par_total,totalshot,hole)
    print("(I)ntructions")
    print("(P)lay golf")
    print("(Q)uit")
    option = str(input("Please enter your preffered option:")).upper()
  option_check(option)
  if option == "Q":
    print("Thanks for playing,", name, ",Goodbye.")
    print_scores(score, par)
    exit()

def print_scores(score, par):
    for i in range(len(score)):
        if score[i] < par:
            print("Round", i + 1, ":", score[i], "shots. Under", par - score[i], "par/s.")
        elif score[i] > par:
            print("Round", i + 1, ":", score[i], "shots. Over", score[i] - par, "par/s.")
        elif score[i] == par:
            print("Round", i + 1, ":", score[i], "shots. On par.")

def int_valid(prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Please enter a valid integer")
        else:
            return number

def calculate(par_total, totalshot, hole):
    if par_total > totalshot:
        print("Your overall score is", totalshot, "and You are under", par_total - totalshot, "par after", hole,
              "hole/s.")
    elif totalshot > par_total:
        print("Your overall score is", totalshot, "and You are over", totalshot - par_total, "par after", hole,
              "hole/s.")
    elif par_total == totalshot:
        print("Your overall score is", totalshot, "and You are on par after", hole, "hole/s.")

def option_check(option):
    begin = ["I", "P", "Q"]
    while option not in begin:
        print("Invalid menu choice.")
        print("Let's play golf, CP1401 Style!")
        print("Golf!")
        print("(I)ntructions")
        print("(P)lay golf")
        print("(Q)uit")
        option = str(input("Please enter your preffered option:")).upper()

main()
