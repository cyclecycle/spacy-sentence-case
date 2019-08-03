def sentence_case(doc, nlp):
    new_text = ''
    for token in doc:
        token_text = token.text_with_ws
        if token.i == 0:
            pass
        elif n_caps(token) > 1:
            pass
        else:
            token_text = token_text.lower()
        new_text += token_text
    new_doc = nlp(new_text)
    return new_doc


def n_caps(token):
    return token.shape_.count('X')
