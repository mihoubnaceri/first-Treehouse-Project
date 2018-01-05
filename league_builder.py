import csv


def main():
    experienced = []
    inexperienced = []
    sharks =[] # each team will get 6 players with three experienced players
    dragons = []# each team will get 6 players with three experienced players
    raptors = []# each team will get 6 players with three experienced players
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
    for i in range(18):

        with open("{}.txt".format("chafik"),"a") as file_save:
            file_save.write("kiwee")

if __name__ == "__main__":
    main()
