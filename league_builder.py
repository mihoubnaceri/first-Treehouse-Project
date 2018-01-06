import csv
def main():
    experienced = []

    inexperienced = []
    sharks =[] # each team will get 6 players with three experienced players
    dragons = []# each team will get 6 players with three experienced players
    raptors = []# each team will get 6 players with three experienced players
    teams = [sharks,dragons,raptors]
    total_players =[]
    with open("soccer_players.csv",newline="") as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            if row["Soccer Experience"] == "YES":
                experienced.append(row) # adding experienced players as objects to the experienced list
            else:
                inexperienced.append(row) # adding inexperienced players as objects to the inexperienced list
    # the exxperienced list has 9 players and also the inesperienced has 9
    # we need to disturbute the 3 from each list to each team
    sharks.extend(experienced[:3])
    dragons.extend(experienced[3:6])
    raptors.extend(experienced[6:])
    sharks.extend(inexperienced[:3])
    dragons.extend(inexperienced[3:6])
    raptors.extend(inexperienced[6:])
    for player in sharks:
        player.update({"time":"6 am on  7 january 2018" ,"teamname":"Sharks"})
    for player in dragons:
        player.update({"time":"2 pm on  9 january 2018" ,"teamname":"Dragons"})
    for player in raptors:
        player.update({"time":"9 pm on  4 january 2018" ,"teamname":"Raptors"})

    for team in teams:
        total_players.extend(team)


    with open("teams.txt","a") as file:
        file.write("Sharks" + "\n" +"==========" + "\n")
        for player in sharks:
            file.write("{}, {}, {}".format(player["Name"],player["Soccer Experience"],player["Guardian Name(s)"]) +"\n")
        file.write("\n\n")
        file.write("Dragons" + "\n"+"==========" + "\n")
        for player in dragons:
            file.write("{}, {},{}".format(player["Name"],player["Soccer Experience"],player["Guardian Name(s)"]) +"\n")
        file.write("\n\n")
        file.write("Raptors" +"\n"+"==========" + "\n")
        for player in raptors:
            file.write("{}, {}, {}" .format(player["Name"],player["Soccer Experience"],player["Guardian Name(s)"]) +"\n")

    for player in total_players:
        with open("{}.txt".format(adding_hyphen(player["Name"])),"a" ) as player_file: # called the function that calls hypen to add to name
            player_file.write("Dear {}, \n".format(player["Guardian Name(s)"]))
            player_file.write("Hello {}, {} Welcome to the {} team big welcome your training starts at {} \n".format(player["Name"],player["Guardian Name(s)"],player["teamname"],player["time"]))

def adding_hyphen(my_list):
    my_list=list(my_list)
    index = my_list.index(" ")
    my_list.insert(index,"_")
    my_list.remove(" ")

    return "".join(my_list)

if __name__ == "__main__":
    main()
