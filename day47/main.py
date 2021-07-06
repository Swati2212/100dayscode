from bs4 import BeautifulSoup
from requests_html import HTMLSession

WEB_PAGE = "https://www.empireonline.com/movies/features/best-movies-2/"
WEB_FILE = "100_best_movies.html"


# Using requests_html to render JavaScript
def get_web_page():
    # create an HTML Session object
    session = HTMLSession()
    # Use the object above to connect to needed webpage
    response = session.get(WEB_PAGE)
    # Run JavaScript code on webpage
    response.html.render()

    # Save web page to file
    with open(WEB_FILE, mode="w", encoding="utf-8") as fp:
        fp.write(response.html.html)


def read_web_file():
    try:
        open(WEB_FILE)
    except FileNotFoundError:
        get_web_page()
    else:
        pass
    finally:
        # Read the web page from file
        with open(WEB_FILE, mode="r", encoding="utf-8") as fp:
            content = fp.read()
        return BeautifulSoup(content, "html.parser")


def get_all_titles(soup):
    # Get all article details
    all_titles = soup.findAll(name="h3", class_="title")
    title_texts = []
    title_index = []
    index = 100
    for title in all_titles:
        text = title.getText().lstrip("0123456789) :")
        title_index.append(index)
        title_texts.append(text)
        index -= 1
    return title_index, title_texts


def sort_results(lists):
    # The list used as the sort index must be the first item in zip()
    sorted_lists = [(x, y) for (x, y) in sorted(zip(lists[0], lists[1]))]

    # print(sorted_lists)
    return sorted_lists


def save_titles(list):
    with open("film_titles.txt", mode="w", encoding="utf-8") as fp:
        for item in list:
            fp.writelines(f"{item[0]})  \t{item[1]}\n")


#  NOTE: We could use the slice() function, or [::-1] slice operator to reverse the list,
#    e.g. movie_titles = title_texts[::-1] ... creates a new list movie_titles

if __name__ == "__main__":
    result = read_web_file()
    print(f"result = {result}")
    titles = get_all_titles(result)
    # print(f"titles = {titles}")
    sorted_titles = sort_results(titles)
    # print(f"sorted_titles = {sorted_titles}")
    save_titles(sorted_titles)
