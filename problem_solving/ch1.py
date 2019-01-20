cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']


def pleaseConform(caps):
    start = forward = backward = 0
    intervals = []
    caps = caps + ["END"]
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            intervals.append((start, i-1, caps[start]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            if t[0] != t[1]:
                print('People in positions', t[0], 'through', t[1], 'flip your caps!')
            else:
                print('Person at position', t[0], 'flip your cap!')


pleaseConform(cap1)
pleaseConform(cap2)


def pleaseConformOnepass(caps):
    if len(caps) == 0:
        pass
    else:
        caps = caps + [caps[0]]
        for i in range(1, len(caps)):
            if caps[i] != caps[i-1]:
                if i == len(caps):
                    print('Person at position', caps[i], 'flip your cap!')
                else:
                    if caps[i] != caps[0]:
                        print('People in positions', i, end='')
                    else:
                        print(' through', i-1, 'flip your cap!')

pleaseConformOnepass(cap1)
pleaseConformOnepass(cap2)

cap3 = ['F', 'F', 'B', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'F', 'F']

def ex3(caps):
    start = forward = backward = 0
    intervals = []
    caps = caps + ["END"]
    for i in range(len(caps)):
        if caps[i] == 'H':
            caps[i] = caps[0]
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            intervals.append((start, i-1, caps[start]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            if t[0] != t[1]:
                print('People in positions', t[0], 'through', t[1], 'flip your caps!')
            else:
                print('Person at position', t[0], 'flip your cap!')

ex3(cap3)


s = 'BWWWWWBWWWW'
def runLengthEncoding(text):
    if not text:
        return ""
    else:
        i = 0
        while i < len(text) and text[0] == text[i]:
            i += 1
        return str(i) + text[0] + runLengthEncoding(text[i:])

print(runLengthEncoding(s))

encoded = runLengthEncoding(s)

def runLengthDecoding(text):
    if not text:
        return ""
    else:
        return int(text[0]) * text[1] + runLengthDecoding(text[2:])

print(runLengthDecoding(encoded))

def encode(text):
    if not text:
        return ""
    else:
        i = 0
        while i < len(text) and text[0] == text[i]:
            i += 1
        return str(i) + text[0] + encode(text[i:])
print(encode(s))
