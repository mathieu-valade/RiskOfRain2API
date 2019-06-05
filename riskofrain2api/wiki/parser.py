import re


def parse_description(text):
    sep = re.findall(r'[-+]?\d+(?:\.\d+)?', text)

    text = re.sub(r'\([^)]*\)', '', text)

    param = 0

    params = []
    multipliers = []

    for i in range(len(sep)):
        if sep[i][0] == '+' or sep[i][0] == '-':
            text = text.replace(sep[i - 1], '{' + str(param) + '}')
            params.append(sep[i - 1])
            multipliers.append(sep[i])
            param += 1

    text = re.sub(r' +', ' ', text)
    text = re.sub(r' \.', '.', text)
    text = re.sub(r'\.\.', '.', text)

    description = {
        "text": text,
        "param": params,
        "multi": multipliers
    }
    return description
