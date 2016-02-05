region_names = {
     0: 'afghanistan',
     1: 'alaska',
     2: 'alberta',
     3: 'argentina',
     4: 'brazil',
     5: 'central-america',
     6: 'china',
     7: 'congo',
     8: 'east-africa',
     9: 'eastern-australia',
     10: 'eastern-united-states',
     11: 'egypt',
     12: 'great-britain',
     13: 'greenland',
     14: 'iceland',
     15: 'india',
     16: 'indonesia',
     17: 'irkutsk',
     18: 'japan',
     19: 'kamchatka',
     20: 'madagascar',
     21: 'middle-east',
     22: 'mongolia',
     23: 'new-guinea',
     24: 'north-africa',
     25: 'northern-europe',
     26: 'northwest-territory',
     27: 'ontario',
     28: 'peru',
     29: 'quebec',
     30: 'scandinavia',
     31: 'siam',
     32: 'siberia',
     33: 'south-africa',
     34: 'southern-europe',
     35: 'ukraine',
     36: 'ural',
     37: 'venezuela',
     38: 'western-australia',
     39: 'western-europe',
     40: 'western-united-states',
     41: 'yakutsk' }

region_neighbors = {
     0: [35, 36, 6, 15, 21],
     1: [26, 2, 19],
     2: [1, 26, 27, 40],
     3: [4, 28],
     4: [24, 3, 28, 37],
     5: [40, 10, 37],
     6: [31, 15, 0, 32, 36, 22],
     7: [8, 33, 24],
     8: [11, 21, 20, 33, 7, 24],
     9: [23, 38],
     10: [5, 40, 27, 29],
     11: [34, 21, 8, 24],
     12: [14, 25, 30, 39],
     13: [26, 27, 29, 14],
     14: [13, 12, 30],
     15: [6, 31, 21, 0],
     16: [31, 23, 38],
     17: [41, 22, 32, 19],
     18: [19, 22],
     19: [18, 1, 17, 22, 41],
     20: [8, 33],
     21: [8, 11, 35, 0, 15, 34],
     22: [18, 6, 32, 17, 19],
     23: [9, 16, 38],
     24: [39, 11, 8, 7, 4],
     25: [30, 35, 34, 39, 12],
     26: [1, 2, 13, 27],
     27: [2, 10, 13, 26, 29, 40],
     28: [4, 37, 3],
     29: [10, 13, 27],
     30: [35, 25, 12, 14],
     31: [16, 15, 6],
     32: [17, 41, 22, 6, 36],
     33: [7, 8, 20],
     34: [11, 39, 25, 35, 21],
     35: [36, 0, 21, 34, 25, 30],
     36: [32, 6, 0, 35],
     37: [28, 4, 5],
     38: [9, 16, 23],
     39: [12, 24, 34, 25],
     40: [2, 5, 10, 27],
     41: [19, 17, 32]}

region_locations = {
     0: [1140, 430],
     1: [135, 180],
     2: [270, 260],
     3: [470, 890],
     4: [550, 730],
     5: [270, 500],
     6: [1330, 510],
     7: [910, 830],
     8: [985, 750],
     9: [1540, 920],
     10: [400, 420],
     11: [910, 640],
     12: [700, 350],
     13: [600, 120],
     14: [740, 230],
     15: [1225, 580],
     16: [1355, 800],
     17: [1360, 280],
     18: [1530, 395],
     19: [1510, 150],
     20: [1060, 970],
     21: [1050, 560],
     22: [1360, 395],
     23: [1500, 760],
     24: [805, 683],
     25: [855, 385],
     26: [300, 180],
     27: [390, 280],
     28: [450, 770],
     29: [500, 290],
     30: [880, 200],
     31: [1355, 630],
     32: [1260, 200],
     33: [930, 960],
     34: [860, 470],
     35: [1010, 290],
     36: [1170, 270],
     37: [430, 630],
     38: [1445, 970],
     39: [720, 540],
     40: [280, 400],
     41: [1390, 135]}

continent_names = {
     0: 'africa',
     1: 'asia',
     2: 'europe',
     3: 'north-america',
     4: 'oceania',
     5: 'south-america'}

continent_bonuses = {0: 3, 1: 7, 2: 5, 3: 5, 4: 2, 5: 2}

continent_regions = {
     0: [7, 8, 11, 20, 24, 33],
     1: [0, 6, 15, 17, 18, 19, 21, 22, 31, 32, 36, 41],
     2: [12, 14, 25, 30, 34, 35, 39],
     3: [1, 2, 5, 10, 13, 26, 27, 29, 40],
     4: [9, 16, 23, 38],
     5: [3, 4, 28, 37]}

player_colors = {
     0: 'red',
     1: 'blue',
     2: 'green',
     3: 'yellow',
     4: 'pink',
     5: 'black',
     None: None }

starting_armies = { 
    2: 40,
    3: 35,
    4: 30,
    5: 25,
    6: 20 }