import resources.topics as topicrepo
from random import choice as choose

def generate_comic_dialog():
    dialog = []
    topic_choice = choose(topicrepo.topics)
    for plotpoint in topic_choice["plot"]:
        dialog.append(choose(topicrepo.options[plotpoint]))
    return dialog