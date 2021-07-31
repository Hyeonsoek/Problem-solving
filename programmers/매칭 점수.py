import re
from collections import defaultdict

def calculate_network_point():
    global network, back_network ,network_base_score

    network_match_score = defaultdict(int)

    for key in network_base_score:
        network_match_score[key] = network_base_score[key]

    for key in network:
        for url in back_network[key]:
            if url in network:
                network_match_score[key] += \
                        network_base_score[url]/int(len(network[url]))

    return network_match_score


def solution(word, pages):
    meta_content = re.compile('<meta property="og:url" content="https://\S+"')
    a_href = re.compile('<a href="https://\S+">')
    url_pattern = re.compile('"https://\S+"')

    word = word.lower()

    global network, back_network, network_base_score
    network = defaultdict(list)
    back_network = defaultdict(list)
    network_base_score = defaultdict(int)
    index = defaultdict(int)

    for idx, page in enumerate(pages):
        page_html = meta_content.search(page).group()
        page_url = url_pattern.search(page_html).group()[1:-1]

        page_hrefs = a_href.findall(page)
        print(page_hrefs)
        for href in page_hrefs:
            href_url = url_pattern.search(href).group()[1:-1]
            network[page_url].append(href_url)
            back_network[href_url].append(page_url)

        start = re.search(r'<body>', page).span()[1]
        end = re.search(r'</body>', page).span()[0]

        body = page[start:end].lower()
        body = re.sub('[^a-zA-Z]',' ',body).split(' ')

        base_score = 0

        for w in body:
            if w == word:
                base_score+=1

        network_base_score[page_url] = base_score
        index[page_url] = idx

    network_match_score = calculate_network_point()
    answer = []

    for x in network_match_score:
        answer.append([network_match_score[x], x])
    answer = sorted(answer, key=lambda x : -x[0])

    if not answer:
        return 0
    
    return index[answer[0][1]]