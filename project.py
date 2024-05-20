import requests
import json
import sys
import csv
import random
import re
from tabulate import tabulate
import os

# The Startup Machine
industries = ["marketing", "gaming", "finance", "law"]
niche_mark = ["newsletters", "brand"]
niche_gam = ["esports", "console", "youtubers"]
niche_fin = ["e-commerce", "crypto"]
niche_law = ["law-tech", "immigration"]


class Startup:

    def feature(self):
        keys = []

        with open("keywords_others.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            features = reader.fieldnames

            for row in reader:
                keys.append(
                    {
                        "feature1": row["USP"],
                        "feature2": row["Time"],
                        "feature3": row["Budget"],
                        "feature4": row["Monetization"],
                    }
                )

            feature1_usp = [key["feature1"] for key in keys]
            feature2_time = [key["feature2"] for key in keys]
            feature3_bud = [key["feature3"] for key in keys]
            feature4_mon = [key["feature4"] for key in keys]

            return feature1_usp, feature2_time, feature3_bud, feature4_mon

    def get_niche(self, industry):
        match industry:
            case "marketing":
                niche = random.choice(niche_mark)
            case "gaming":
                niche = random.choice(niche_gam)
            case "finance":
                niche = random.choice(niche_fin)
            case "law":
                niche = random.choice(niche_law)

        return niche

    def get_feature(self, feature):
        return random.choice(feature)

    def sep(self):
        print("")
        for i in range(20):
            print("#", end="")
        print("")

    def starts(self):
        self.sep()
        print("Hi, this is The Startup Machine!")
        print(f"List of available industries: {industries}", end="")
        self.sep()

        while True:
            print("Please, use the format '[industry]'")
            info = input("Please, introduce [industry]: ")
            if matches := re.search(r"^\[(.+)\]$", info):
                if matches.group(1).lower() in industries:
                    industry = matches.group(1)
                    niche = self.get_niche(industry)
                    return industry, niche
                else:
                    print("Industry not in the list")
                    print("")
            else:
                print("Wrong format")

    def combine(
        self,
        industry,
        niche,
        usp,
        time,
        bud,
        mon,
    ):
        print("\nThis is your Startup: \n")
        text = str(f"A business in the INDUSTRY of {industry}\n")
        text0 = str(f"with a NICHE in {niche}\n")
        text1 = str("\nThe restirctions are as follows:\n")
        text2 = str(f"USP: {usp}\n")
        text3 = str(f"Time: {time}\n")
        text4 = str(f"Budget:{bud}\n")
        text5 = str(f"Monetization: {mon}\n")
        return text + text0 + text1 + text2 + text3 + text4 + text5


def get_startups_list():
    try:
        startups = []
        table = []
        print('REMEMBER: it must end in ".csv"')
        x = input("What file would like to open? ")
        with open(x) as csvfile:
            reader = csv.DictReader(csvfile)
            headers = reader.fieldnames
            for row in reader:
                startups.append(
                    {"name": row["name"], "description": row["description"]}
                )

        for startup in startups:
            row = list(startup.values())
            table.append(row)
            # print(f'{startup["name"]}: {startup["description"]}\n')
        return str(tabulate(table, headers, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


def add_startups_list(name, desc, x):
    flag = 0

    n = desc.split()
    if len(n) > 5:
        return str("Too long of a description")

    if not x.endswith(".csv"):
        sys.exit("Not a .csv file")

    if not os.path.exists(x):
        flag = 1

    with open(x, "a") as csvfile:
        fieldnames = ["name", "description"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if flag == 1:
            writer.writeheader()
        writer.writerow({"name": name, "description": desc})


def this_that_generator(n):
    i = 0
    l = []
    while (i < n):
        url = "https://itsthisforthat.com/api.php?json"
        response = requests.get(url)
        o = response.json()
        i += 1
        l.append(o)

    for ii in l:
        print(ii['this'] + " " + ii['that'])

    return len(l)

def hacker_news(n):
    url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    response = requests.get(url)
    stories = json.loads((json.dumps(response.json(), indent=2)))
    top = stories[:n]
    all_urls = []

    for story in top:
        url_story = (
            f"https://hacker-news.firebaseio.com/v0/item/{story}.json?print=pretty"
        )
        response_story = requests.get(url_story)
        o = json.loads((json.dumps(response_story.json(), indent=2)))
        if "url" in o:
            o_urls = str(o["url"])
            o_title = str(o["title"])
            all_urls.append(f"Title: {o_title}\nURL: {o_urls}\n")

    with open("news.txt", "w") as file:
        for url in all_urls:
            file.write(url + "\n")

    return len(top)

def main():

    print("Hello. Welcome to the Startup Machine\n")
    print("Please, select action:")

    x = input(
        """1. Random Start-up Idea Generator
2. Get access to the latest Hacker News
3. This That Generator
4. (Create)/(Add to) a Start-up Ideas Journal
5. Print the Start-up Ideas Journal\n"""
    )

    if x == "1":
        test = Startup()
        industry, niche = test.starts()
        usp, time, budget, monetization = test.feature()
        usp_1 = test.get_feature(usp)
        time_1 = test.get_feature(time)
        budget_1 = test.get_feature(budget)
        monetization_1 = test.get_feature(monetization)
        print(test.combine(industry, niche, usp_1, time_1, budget_1, monetization_1))

    elif x == "2":
        n = input("Please, input the number of articles (20 recommended): ")
        hacker_news(int(n))
        print("Please, check your newly created 'news.txt' file")

    elif x == "3":
        n = input("Please, input the number of generations (5 recommended): ")
        this_that_generator(int(n))


    elif x == "4":
        name = input("What startup have you found? ")
        description = input("Describe the company in 5 words: ")
        print('REMEMBER: it must end in ".csv"')
        x = input("What is the file name you want to add to/create? ")

        add_startups_list(name, description, x)

    elif x == "5":
        print(get_startups_list())


if __name__ == "__main__":
    main()
