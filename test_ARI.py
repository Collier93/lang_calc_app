# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 20:00:41 2022

@author: Jordan.Collier
"""

import string


def test_demo():
    # Test the demo string as a unit test
    s = """As we wound on our endless way, and the sun sank lower and lower behind us,
    the shadows of the evening began to creep round us. 
    This was emphasized by the fact that the snowy mountain-top still held the sunset,
    and seemed to glow out with a delicate cool pink. Here and there we passed Cszeks and slovaks,
    all in picturesque attire, but I noticed that goitre was painfully prevalent.
    By the roadside were many crosses, and as we swept by, my companions all
    crossed themselves. Here and there was a peasant man or woman kneeling before
    a shrine, who did not even turn round as we approached, but seemed in the
    self-surrender of devotion to have neither eyes nor ears for the outer world.
    There were many things new to me. For instance, hay-ricks in the trees, and
    here and there very beautiful masses of weeping birch, their white stems
    shining like silver through the delicate green of the leaves."""
    sentence_count = s.count('.')
    # account for a single sentence with no full stop at the end
    if sentence_count == 0:
        sentence_count = 1
    # remove punctuation
    s = s.translate(str.maketrans('', '', string.punctuation))
    # split string into individual words
    word_list = s.split()
    # count words
    word_count = len(word_list)
    # count non-space characters
    character_count = 0
    for word in word_list:
        character_count += len(word)
    # apply formula
    score = 4.71 * (character_count / word_count) + 0.5 * (word_count / sentence_count) - 21.43
    score = round(score)
    
    assert score == 11
    
def test_ellipsis():
    # Test the demo string as a unit test
    s = """And we shouldn’t be here at all, if we’d known more about it before we started. 
    But I suppose it’s often that way... The brave things in the old tales and songs... Mr. Frodo: adventures... 
    as I used to call them. I used to think that they were things the wonderful folk of the stories went out and 
    looked for, because they wanted them, because they were exciting and life was a bit dull, a kind of a sport... 
    as you might say... But that’s not the way, as you put it. But I expect they had lots of chances, like us, 
    of turning back, only they didn’t. And if they had, we shouldn’t know, because they’d have been forgotten. 
    We hear about those as just went on... and not all to a good end... mind you; at least not to what 
    folk inside a story and not outside it call a good end. You know, coming home, and finding things all right, 
    though not quite the same – like old Mr. Bilbo. But those aren’t always the best tales to hear... though they may 
    be the best tales to get landed in! I wonder what sort of a tale we’ve fallen into?"""
    sentence_count = s.count('.')
    # account for a single sentence with no full stop at the end
    if sentence_count == 0:
        sentence_count = 1
    # remove punctuation
    s = s.translate(str.maketrans('', '', string.punctuation))
    # split string into individual words
    word_list = s.split()
    # count words
    word_count = len(word_list)
    # count non-space characters
    character_count = 0
    for word in word_list:
        character_count += len(word)
    # apply formula
    score = 4.71 * (character_count / word_count) + 0.5 * (word_count / sentence_count) - 21.43
    score = round(score)
    
    assert score == 0
    
    
def test_complex():
    

     # Test the demo string as a unit test
     s = """This exceeding trifling witling, considering ranting criticizing concerning adopting fitting
     wording being exhibiting transcending learning, was displaying, notwithstanding ridiculing, surpassing
     boasting swelling reasoning, respecting correcting erring writing, and touching detecting deceiving
     arguing during debating"""
     sentence_count = s.count('.')
     # account for a single sentence with no full stop at the end
     if sentence_count == 0:
         sentence_count = 1
     # remove punctuation
     s = s.translate(str.maketrans('', '', string.punctuation))
     # split string into individual words
     word_list = s.split()
     # count words
     word_count = len(word_list)
     # count non-space characters
     character_count = 0
     for word in word_list:
         character_count += len(word)
     # apply formula
     score = 4.71 * (character_count / word_count) + 0.5 * (word_count / sentence_count) - 21.43
     score = round(score)
     
    
     
     assert score == 34
     

     
