from sentence_case import sentence_case
import spacy


cases = [
    {
        'input': 'L-theanine and Caffeine Improve Sustained Attention, Impulsivity and Cognition in Children with Attention Deficit Hyperactivity Disorders by Decreasing Mind Wandering.',
        'expected': 'L-theanine and caffeine improve sustained attention, impulsivity and cognition in children with attention deficit hyperactivity disorders by decreasing mind wandering.',
    }
]

nlp = spacy.load('en_core_web_sm')


def test_sentence_case():
    for case in cases:
        input_ = case['input']
        expected = case['expected']
        doc = nlp.make_doc(input_)
        doc = sentence_case(doc, nlp)
        assert doc.text == expected
