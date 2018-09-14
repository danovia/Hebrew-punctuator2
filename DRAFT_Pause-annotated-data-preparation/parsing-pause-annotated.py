from collections import OrderedDict
import csv
punct = (',','.','?','!','"','-')

with open('/home/danzu/mmn16/resources/623-text/623.csv') as asrFile:
    asr = csv.DictReader(asrFile)
    asrList = []
    for line in asr:
        asrList.append(line)

with open('/home/danzu/mmn16/resources/623-text/623-humanPunctWithQuote.csv') as humanPunctFile:
    humanPunct = csv.DictReader(humanPunctFile)
    humanPunctList = []
    for line in humanPunct:
        humanPunctList.append(line)
    # print(humanPunctList[0]['HumanWord'])

with open('/home/danzu/mmn16/resources/623-text/623-diff.csv') as diffFile:
    diff = csv.DictReader(diffFile)
    diffList = []
    for line in diff:
        diffList.append(line)

asrIndex = 0
humanIndex = 0
resultList = []
for diffIndex, line in enumerate(diffList):
    # add time annotations
    if line['AsrWord'] == asrList[asrIndex]['AsrWord']:
        resultLine = OrderedDict([
            ('FromTime',    asrList[asrIndex]['FromTime']),
            ('TillTime',    asrList[asrIndex]['TillTime']),
            ('Diff',        line['Diff']),
            ('WordDuration', float(asrList[asrIndex]['TillTime']) - float(asrList[asrIndex]['FromTime'])),
            ('ResultWord',  line['HumanWord'] if line['HumanWord'] != '' else '@WORD-GAP'),
            ('PauseToNextWord',
             float(asrList[asrIndex + 1]['FromTime']) - float(asrList[asrIndex]['TillTime'])
             if len(asrList) > asrIndex + 1 else 0)
        ])
        resultList.append(resultLine)
        asrIndex += 1
    # elif line['HumanWord'] == humanPunctList[humanIndex]['HumanWord']:
    #     resultLine = OrderedDict([
    #         ('FromTime', asrList[asrIndex]['FromTime']),
    #         ('TillTime', asrList[asrIndex]['TillTime']),
    #         ('Diff', line['Diff']),
    #         ('WordDuration', float(asrList[asrIndex]['TillTime']) - float(asrList[asrIndex]['FromTime'])),
    #         ('ResultWord', line['HumanWord'] if line['HumanWord'] != '' else '@WORD-GAP'),
    #         ('PauseToNextWord',
    #          float(asrList[asrIndex + 1]['FromTime']) - float(asrList[asrIndex]['TillTime'])
    #          if len(asrList) > asrIndex + 1 else 0)
    #     ])
    #     resultList.append(resultLine)
    #     asrIndex += 1

humanIndex = 0
for resultIndex, line in enumerate(resultList):
    # add punctuation, should be the last thing
    if line['ResultWord'] == humanPunctList[humanIndex]['HumanWord']:
        humanIndex += 1
        if humanPunctList[humanIndex]['HumanWord'] in punct:
            resultLine = OrderedDict([
                ('Diff', 'Punct'),
                ('ResultWord', humanPunctList[humanIndex]['HumanWord'])
            ])
            resultList.insert(resultIndex + 1, resultLine)
            humanIndex += 1

nonGapIndex = -1
for i, line in enumerate(resultList):
    try:
        # a gap should be skipped if it's close to a minor, and there is no punctuation around
        if ((line['ResultWord'] == '@WORD-GAP')
                & (' **Minor ' in (resultList[i-1]['Diff'], resultList[i+1]['Diff']))
                & ('Punct' not in (resultList[i-1]['Diff'], resultList[i+1]['Diff']))
        ):
            nonGapIndex = -1
            line['Diff'] += 'current gap NOT fixed '
            continue
        # enters to a strike of gaps, saves the non-gap index
        if (line['ResultWord'] == '@WORD-GAP') & (nonGapIndex == -1):
            if all(diff not in resultList[i-1]['Diff'] for diff in ('Punct', ' ** Gap ** ')):
                nonGapIndex = i-1
                resultList[nonGapIndex]['Diff'] += 'trying to gap fix... '
        # when finished a strike of gaps and punctuation marks
        if all(diff not in line['Diff'] for diff in ('Punct', ' ** Gap ** ')) \
                & (nonGapIndex != -1):
            resultList[nonGapIndex]['PauseToNextWord'] = \
                    float(line['FromTime']) - float(resultList[nonGapIndex]['TillTime'])
            resultList[nonGapIndex]['Diff'] += 'next gap/s fixed! '
            nonGapIndex = -1
    except IndexError:
        print('IndexError while fixing gaps, reached index boundries. index:' + str(i))
        nonGapIndex = -1
        continue


with open('output.csv', 'w') as outFile:
    fieldnames = ('FromTime', 'TillTime', 'WordDuration', 'Diff', 'ResultWord', 'PauseToNextWord')
    writer = csv.DictWriter(outFile, fieldnames=fieldnames)

    writer.writeheader()
    for line in resultList:
        writer.writerow(line)