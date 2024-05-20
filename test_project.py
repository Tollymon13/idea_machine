from project import add_startups_list
from project import this_that_generator
from project import hacker_news

def test_add_startups_list():
    assert add_startups_list("Reddit", "1 2 3 4 5 6 7", "test.csv") == str("Too long of a description")

def test_this_that_generator():
    assert this_that_generator(3) == 3

def test_hacker_news():
    assert hacker_news(5) == 5
