import os
import random
import re
import sys
from collections import defaultdict


DAMPING = 0.85
SAMPLES = 100000



def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor,counts):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """


    pages = list(corpus.keys())

    def main_selector(page):
        possible_functions = [random_selector, path_finder]
        probabilities = [1-0.85, 0.85]
        if len(corpus[page])!=0:
            chosen_function = random.choices(possible_functions, weights=probabilities, k=1)[0]
        else:
            chosen_function = random_selector
        new_page=chosen_function(page)
        return new_page

    def random_selector(page):

        random_key = random.choice(pages)
        # counts[random_key] += 1
        page = random_key
        return page


    def path_finder(page):

        linked_pages = list(corpus[page])
        random_value = random.choice(linked_pages)
        # counts[random_value] += 1

        page = random_value
        return page


    new_page=main_selector(page)
    return new_page



def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page = random.choice(list(corpus.keys()))


    x=1
    counts = defaultdict(int)


    while x < n:
        counts[page] += 1
        next_page=transition_model(corpus,page,DAMPING,counts)
        page=next_page
        x += 1

    for key in counts:
        counts[key] = counts[key] / n

    print(counts)
    return counts


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    # Create a new corpus to avoid modifying the original
    processed_corpus = {}
    all_pages = set(corpus.keys())

    for page, links in corpus.items():
        # If a page has no links, treat it as linking to all pages
        if not links:
            processed_corpus[page] = all_pages
        else:
            processed_corpus[page] = links

    corpus=processed_corpus
    incoming_links = {}

    d = damping_factor

    # Initialize with all pages and empty sets
    for page in corpus:
        incoming_links[page] = set()

    # Iterate through the original corpus to populate incoming_links
    for page, outgoing_links in corpus.items():
        # If a page links to nothing, it's handled by the initialization
        if not outgoing_links:
            continue
        # For each outgoing link, add the current page as an incoming link
        for linked_page in outgoing_links:
            incoming_links[linked_page].add(page)



    answers = {}
    N = len(incoming_links)

    for page in incoming_links.keys():
        answers[page] = 1 / N



    def PR(p, new_ans):


        answer = ((1 - d) / N) + (d * sum([(answers[i] / len(corpus[i])) for i in incoming_links[p]]))
        new_ans[p] = answer

    n = 1

    while n < 100000:
        new_ans = {}
        for i in answers:
            PR(i, new_ans)
        answers = new_ans
        n += 1

    return answers


if __name__ == "__main__":
    main()
