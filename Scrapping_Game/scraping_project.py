import random
from bs4 import BeautifulSoup
import requests
from time import sleep
def game():
    baseURL = "http://quotes.toscrape.com/"
    url = "/page/1/"
    quotation = []
    while url:
        request_url = f"{baseURL}{url}"
        print(f"Scraping {url}")
        content = requests.get(request_url)
        txt_content = content.text
        soup = BeautifulSoup(txt_content,"html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            quotation.append({"text":quote.find(class_="text").get_text(),
                              "author":quote.find(class_="author").get_text(),
                              "bio_link":quote.find("a")["href"]})
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        sleep(1)
    # print(quotation)

    replay = True
    while replay:
        quote = random.choice(quotation)
        answer = input(f"Guess the author of the following quote, you have 4 chance - \n{quote['text']}\n")
        if answer == quote["author"]:
            print("Vola!!!")
            replay_game = input("Want to play again? y / n - ")
            if replay_game.upper() != "Y":
                print("Good Bye!!!")
                replay = False
        else:
            answer = input(f"Wrong Guess!!! You have 3 chances left.\nHint - Author's name starts with \"{quote['author'][0]}\" -\n")
            if answer == quote["author"]:
                print("Vola!!!")
                replay_game = input("Want to play again? y / n - ")
                if replay_game.upper() != "Y":
                    print("Good Bye!!!")
                    replay = False
            else:
                last_name = quote['author'].split()
                answer = input(f"Wrong Guess!!! You have 2 chances left.\nHint - Author's last name starts with \"{last_name[-1][0]}\" -\n")
                if answer == quote["author"]:
                    print("Vola!!!")
                    replay_game = input("Want to play again? y / n - ")
                    if replay_game.upper() != "Y":
                        print("Good Bye!!!")
                        replay = False
                else:
                    req_url = f"{baseURL}{quote['bio_link']}"
                    response = requests.get(req_url)
                    soup_next = BeautifulSoup(response.text,"html.parser")
                    bDate = soup_next.find(class_="author-born-date").get_text()
                    bPlace = soup_next.find(class_="author-born-location").get_text()
                    hintMsg = f"Author was born {bPlace}, and date of birth {bDate}"
                    answer = input(f"Wrong Guess!!! You have 1 chance left.\nHint - {hintMsg} -\n")
                    if answer == quote["author"]:
                        print("Vola!!!")
                        replay_game = input("Want to play again? y / n - ")
                        if replay_game.upper() != "Y":
                            print("Good Bye!!!")
                            replay = False
                    else:
                        print(f"Bad Luck!!! Author is {quote['author']}")
                        replay_game = input("Want to play again? y / n - ")
                        if replay_game.upper() != "Y":
                            print("Good Bye!!!")
                            replay = False