import json

with open('output2.json') as f:
    data = json.load(f)

raw_text = data['textAnnotations'][0]['description']

raw_text = raw_text.split('\n')

def contains_date(text_entity):
    Date = False
    Date = Date or "January" in text_entity
    Date = Date or "February" in text_entity
    Date = Date or "March" in text_entity
    Date = Date or "April" in text_entity
    Date = Date or "May" in text_entity
    Date = Date or "June" in text_entity
    Date = Date or "July" in text_entity
    Date = Date or "August" in text_entity
    Date = Date or "September" in text_entity
    Date = Date or "October" in text_entity
    Date = Date or "November" in text_entity
    Date = Date or "December" in text_entity
    return Date

def is_date(text_entity):
    Date = False
    Date = Date or "January" == text_entity
    Date = Date or "February" == text_entity
    Date = Date or "March" == text_entity
    Date = Date or "April" == text_entity
    Date = Date or "May" == text_entity
    Date = Date or "June" == text_entity
    Date = Date or "July" == text_entity
    Date = Date or "August" == text_entity
    Date = Date or "September" == text_entity
    Date = Date or "October" == text_entity
    Date = Date or "November" == text_entity
    Date = Date or "December" == text_entity
    return Date

dates = []

for text_entity in raw_text:
    if contains_date(text_entity) == True:
        dates.append(text_entity)


immunizations = []
y_range_and_dates = []
x_range_and_vaccines = []

for text in data['textAnnotations']:
    selections = []
    dates_coords = {}
    if is_date(text['description']):
        y_range = (text['boundingPoly']['vertices'][0]['y'], text['boundingPoly']['vertices'][3]['y'])
        for date in dates:
            if text['description'] in date:
                y_range_and_date = [date,  y_range]
                y_range_and_dates.append(y_range_and_date)
                print(y_range_and_date)
    if text['description'] == 'Flu':
        corners = []
        for elem in text['boundingPoly']['vertices']:
            temp = (elem['x'],elem['y'])
            corners.append(temp)
        sorted_corners = sorted(corners, key=lambda x: x[1])
        x_range = (sorted_corners[0][0], sorted_corners[1][0])
        print(x_range)
        x_range_and_vaccine = ('Flu', x_range)
        x_range_and_vaccines.append(x_range_and_vaccine)
    if text['description'] == 'Polio':
        corners = []
        for elem in text['boundingPoly']['vertices']:
            temp = (elem['x'],elem['y'])
            corners.append(temp)
        sorted_corners = sorted(corners, key=lambda x: x[1])
        x_range = (sorted_corners[0][0], sorted_corners[1][0])
        # print(x_range)
        x_range_and_vaccine = ('Polio', x_range)
        x_range_and_vaccines.append(x_range_and_vaccine)
    if text['description'] == 'Pertussis':
        corners = []
        for elem in text['boundingPoly']['vertices']:
            temp = (elem['x'],elem['y'])
            corners.append(temp)
        sorted_corners = sorted(corners, key=lambda x: x[1])
        x_range = (sorted_corners[0][0], sorted_corners[1][0])
        # print(x_range)
        x_range_and_vaccine = ('Pertussis', x_range)
        x_range_and_vaccines.append(x_range_and_vaccine)
    if text['description'] == 'Tetanus':
        corners = []
        for elem in text['boundingPoly']['vertices']:
            temp = (elem['x'],elem['y'])
            corners.append(temp)
        sorted_corners = sorted(corners, key=lambda x: x[1])
        x_range = (sorted_corners[0][0], sorted_corners[1][0])
        # print(x_range)
        x_range_and_vaccine = ('Tetanus', x_range)
        x_range_and_vaccines.append(x_range_and_vaccine)
    if text['description'] == 'Diphtheria':
        corners = []
        for elem in text['boundingPoly']['vertices']:
            temp = (elem['x'],elem['y'])
            corners.append(temp)
        sorted_corners = sorted(corners, key=lambda x: x[1])
        x_range = (sorted_corners[0][0], sorted_corners[1][0])
        # print(x_range)
        x_range_and_vaccine = ('Diphtheria', x_range)
        x_range_and_vaccines.append(x_range_and_vaccine)


for text in data['textAnnotations']:
    if text['description'] == 'YES':
        xAvg = (text['boundingPoly']['vertices'][0]['x'] + text['boundingPoly']['vertices'][1]['x'])/2
        yAvg = (text['boundingPoly']['vertices'][0]['y'] + text['boundingPoly']['vertices'][3]['y'])/2
        selections.append((xAvg,yAvg))
        for x in x_range_and_vaccines:
            if xAvg > (x[1][0] - 21) and xAvg < (x[1][1] + 21):
                print(x[0])
        for y in y_range_and_dates:
            if yAvg > y[1][0] and yAvg < y[1][1]:
                print(y[0])




    # if text['description'] == 'Polio':
    #     print(text['boundingPoly'])

vaccines = []

# print(text['description'])
