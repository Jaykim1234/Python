# Group member
# 11968850, JINHYUN,KIM
# Link for explaination: https://drive.google.com/file/d/1kVAZ5uD2QocMMLN8ajSdu8O9J0vO_8lV/view?usp=sharing


import random

area = {    "Russia": 16995800,    "Antarctica": 14000000,    "China": 9326410,    "United States": 9161923,    "Canada": 9093507,    "Brazil": 8456510,    "Australia": 7617930,    "India": 2973190,    "Argentina": 2736690,    "Kazakhstan": 2669800,    "Algeria": 2381740,    "Sudan": 1886068,    "South Sudan": 619746,    "Democratic Republic of the Congo": 2267600,    "Greenland": 2166086,    "Saudi Arabia": 2149690,    "Mexico": 1923040,    "Indonesia": 1826440,    "Libya": 1759540,    "Iran": 1636000,    "Peru": 1280000,    "Niger": 1266700,    "Chad": 1259200,    "Angola": 1246700,    "Mali": 1220000,    "South Africa": 1219912,    "Ethiopia": 1119683,    "Bolivia": 1084390,    "Colombia": 1038700,    "Mauritania": 1030400,    "Egypt": 995450,    "Nigeria": 910768,    "Tanzania": 886037,    "Venezuela": 882050,    "Namibia": 825418,    "Mozambique": 784090,    "Pakistan": 778720,    "Turkey": 770760,    "Chile": 748800,    "Zambia": 740724,    "Burma": 657740,    "Afghanistan": 647500,    "France": 640053,    "Somalia": 627337,    "Central African Republic": 622984,    "Ukraine": 603700,    "Botswana": 585370,    "Madagascar": 581540,    "Kenya": 569250,    "Yemen": 527970,    "Thailand": 511770,    "Spain": 499542,    "Turkmenistan": 488100,    "Cameroon": 469440,    "Papua New Guinea": 452860,    "Morocco": 446300,    "Iraq": 432162,    "Uzbekistan": 425400,
    "Sweden": 410934,    "Paraguay": 397300,    "Zimbabwe": 386670,    "Japan": 374744,    "Germany": 349223,    "Republic of the Congo": 341500,    "Malaysia": 328550,    "Vietnam": 325360,    "Cote d'Ivoire": 318000,    "Norway": 307442,    "Finland": 304473,    "Poland": 304465,    "Philippines": 298170,    "Italy": 294020,    "Ecuador": 276840,    "Burkina Faso": 273800,    "New Zealand": 268021,    "Western Sahara": 266000,    "Gabon": 257667,    "Guinea": 245857,    "United Kingdom": 241590,    "Ghana": 230940,    "Laos": 230800,    "Romania": 230340,    "Oman": 212460,    "Belarus": 207600,    "Uganda": 199710,    "Guyana": 196850,    "Senegal": 192000,    "Kyrgyzstan": 191300,    "Syria": 184050,    "Cambodia": 176520,    "Uruguay": 173620,    "Suriname": 161470,    "Tunisia": 155360,    "Nepal": 143181,    "Tajikistan": 142700,    "Bangladesh": 133910,    "Greece": 130800,    "Eritrea": 121320,    "North Korea": 120410,    "Nicaragua": 120254,    "Honduras": 111890,    "Cuba": 110860,    "Benin": 110620,    "Bulgaria": 110550,    "Guatemala": 108430,    "Serbia and Montenegro": 102136,    "Iceland": 100250,    "South Korea": 98190,    "Liberia": 96320,    "Malawi": 94080,    "Hungary": 92340,    "Jordan": 91971,    "Portugal": 91951,    "French Guiana": 89150,    "Azerbaijan": 86100,    "United Arab Emirates": 83600,    "Austria": 82444,    "Sweden": 410934,    "Paraguay": 397300,    "Zimbabwe": 386670,    "Japan": 374744,    "Germany": 349223,    "Republic of the Congo": 341500,    "Malaysia": 328550,    "Vietnam": 325360,    "Cote d'Ivoire": 318000,    "Norway": 307442,    "Finland": 304473,    "Poland": 304465,    "Philippines": 298170,    "Italy": 294020,    "Ecuador": 276840,    "Burkina Faso": 273800,    "New Zealand": 268021,    "Western Sahara": 266000,    "Gabon": 257667,    "Guinea": 245857,    "United Kingdom": 241590,    "Ghana": 230940,    "Laos": 230800,    "Romania": 230340,    "Oman": 212460,    "Belarus": 207600,    "Uganda": 199710,    "Guyana": 196850,    "Senegal": 192000,    "Kyrgyzstan": 191300,    "Syria": 184050,    "Cambodia": 176520,    "Uruguay": 173620,    "Suriname": 161470,    "Tunisia": 155360,    "Nepal": 143181,    "Tajikistan": 142700,    "Bangladesh": 133910,    "Greece": 130800,    "Eritrea": 121320,    "North Korea": 120410,    "Nicaragua": 120254,    "Honduras": 111890,    "Cuba": 110860,    "Benin": 110620,    "Bulgaria": 110550,    "Guatemala": 108430,    "Serbia and Montenegro": 102136,    "Iceland": 100250,    "South Korea": 98190,    "Liberia": 96320,    "Malawi": 94080,    "Hungary": 92340,    "Jordan": 91971,    "Portugal": 91951,    "French Guiana": 89150,    "Azerbaijan": 86100,    "United Arab Emirates": 83600,    "Austria": 82444,
    "Czech Republic": 77276,    "Panama": 75990,    "Sierra Leone": 71620,    "Georgia": 69700,    "Ireland": 68890,    "Sri Lanka": 64740,    "Latvia": 63589,    "Svalbard": 61020,    "Croatia": 56414,    "Togo": 54385,    "Bosnia and Herzegovina": 51129,    "Costa Rica": 50660,    "Slovakia": 48800,    "Dominican Republic": 48380,    "Bhutan": 47000,    "Estonia": 43211,    "Denmark": 42394,    "Switzerland": 39770,    "Netherlands": 33883,    "Moldova": 33371,    "Taiwan": 32260,    "Lesotho": 30355,    "Belgium": 30278,    "Armenia": 28400,    "Equatorial Guinea": 28051,    "Guinea-Bissau": 28000,    "Haiti": 27560,    "Solomon Islands": 27540,    "Albania": 27398,    "Burundi": 25650,    "Rwanda": 24948,    "North Macedonia": 24856,    "Djibouti": 22980,    "Belize": 22806,    "El Salvador": 20720,    "Israel": 20330,    "Slovenia": 20151,    "New Caledonia": 18575,    "Fiji": 18270,    "Kuwait": 17820,    "Eswatini (Swaziland)": 17203,    "Vanuatu": 12200,    "Falkland Islands (Islas Malvinas)": 12173,    "Qatar": 11437,    "Jamaica": 10831,    "Lebanon": 10230,    "The Bahamas": 10070,    "The Gambia": 10000,    "Cyprus": 9240,}

dic_continent ={'Antarctica': ['Antarctica'],
 'South America': ['Argentina',
  'Bolivia (Plurinational State of)',
  'Bouvet Island',
  'Brazil',
  'Chile',
  'Colombia',
  'Ecuador',
  'Falkland Islands (Malvinas)',
  'French Guiana',
  'Guyana',
  'Paraguay',
  'Peru',
  'South Georgia and the South Sandwich Islands',
  'Suriname',
  'Uruguay',
  'Venezuela (Bolivarian Republic of)'],
 'Africa': ['Algeria',
  'Angola',
  'Benin',
  'Botswana',
  'British Indian Ocean Territory',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cameroon',
  'Central African Republic',
  'Chad',
  'Comoros',
  'Congo',
  'Côte d’Ivoire',
  'Democratic Republic of the Congo',
  'Djibouti',
  'Egypt',
  'Equatorial Guinea',
  'Eritrea',
  'Eswatini',
  'Ethiopia',
  'French Southern Territories',
  'Gabon',
  'Gambia',
  'Ghana',
  'Guinea',
  'Guinea-Bissau',
  'Kenya',
  'Lesotho',
  'Liberia',
  'Libya',
  'Madagascar',
  'Malawi',
  'Mali',
  'Mauritania',
  'Mauritius',
  'Mayotte',
  'Morocco',
  'Mozambique',
  'Namibia',
  'Niger',
  'Nigeria',
  'Réunion',
  'Rwanda',
  'Saint Helena',
  'Sao Tome and Principe',
  'Senegal',
  'Seychelles',
  'Sierra Leone',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Sudan',
  'Togo',
  'Tunisia',
  'Uganda',
  'United Republic of Tanzania',
  'Western Sahara',
  'Zambia',
  'Zimbabwe'],
 'Europe': ['Åland Islands',
  'Albania',
  'Andorra',
  'Austria',
  'Belarus',
  'Belgium',
  'Bosnia and Herzegovina',
  'Bulgaria',
  'Croatia',
  'Czechia',
  'Denmark',
  'Estonia',
  'Faroe Islands',
  'Finland',
  'France',
  'Germany',
  'Gibraltar',
  'Greece',
  'Guernsey',
  'Holy See',
  'Hungary',
  'Iceland',
  'Ireland',
  'Isle of Man',
  'Italy',
  'Jersey',
  'Latvia',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Malta',
  'Monaco',
  'Montenegro',
  'Netherlands',
  'North Macedonia',
  'Norway',
  'Poland',
  'Portugal',
  'Republic of Moldova',
  'Romania',
  'Russian Federation',
  'San Marino',
  'Sark',
  'Serbia',
  'Slovakia',
  'Slovenia',
  'Spain',
  'Svalbard and Jan Mayen Islands',
  'Sweden',
  'Switzerland',
  'Ukraine',
  'United Kingdom of Great Britain and Northern Ireland'],
 'Oceania': ['American Samoa',
  'Australia',
  'Christmas Island',
  'Cocos (Keeling) Islands',
  'Cook Islands',
  'Fiji',
  'French Polynesia',
  'Guam',
  'Heard Island and McDonald Islands',
  'Kiribati',
  'Marshall Islands',
  'Micronesia (Federated States of)',
  'Nauru',
  'New Caledonia',
  'New Zealand',
  'Niue',
  'Norfolk Island',
  'Northern Mariana Islands',
  'Palau',
  'Papua New Guinea',
  'Pitcairn',
  'Samoa',
  'Solomon Islands',
  'Tokelau',
  'Tonga',
  'Tuvalu',
  'United States Minor Outlying Islands',
  'Vanuatu',
  'Wallis and Futuna Islands'],
 'North America': ['Anguilla',
  'Antigua and Barbuda',
  'Aruba',
  'Bahamas',
  'Barbados',
  'Belize',
  'Bermuda',
  'Bonaire, Sint Eustatius and Saba',
  'British Virgin Islands',
  'Canada',
  'Cayman Islands',
  'Costa Rica',
  'Cuba',
  'Curaçao',
  'Dominica',
  'Dominican Republic',
  'El Salvador',
  'Greenland',
  'Grenada',
  'Guadeloupe',
  'Guatemala',
  'Haiti',
  'Honduras',
  'Jamaica',
  'Martinique',
  'Mexico',
  'Montserrat',
  'Nicaragua',
  'Panama',
  'Puerto Rico',
  'Saint Barthélemy',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Martin (French Part)',
  'Saint Pierre and Miquelon',
  'Saint Vincent and the Grenadines',
  'Sint Maarten (Dutch part)',
  'Trinidad and Tobago',
  'Turks and Caicos Islands',
  'United States of America',
  'United States Virgin Islands'],
 'Asia': ['Afghanistan',
  'Armenia',
  'Azerbaijan',
  'Bahrain',
  'Bangladesh',
  'Bhutan',
  'Brunei Darussalam',
  'Cambodia',
  'China',
  'China, Hong Kong Special Administrative Region',
  'China, Macao Special Administrative Region',
  'Cyprus',
  "Democratic People's Republic of Korea",
  'Georgia',
  'India',
  'Indonesia',
  'Iran (Islamic Republic of)',
  'Iraq',
  'Israel',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kuwait',
  'Kyrgyzstan',
  "Lao People's Democratic Republic",
  'Lebanon',
  'Malaysia',
  'Maldives',
  'Mongolia',
  'Myanmar',
  'Nepal',
  'Oman',
  'Pakistan',
  'Philippines',
  'Qatar',
  'Republic of Korea',
  'Saudi Arabia',
  'Singapore',
  'Sri Lanka',
  'State of Palestine',
  'Syrian Arab Republic',
  'Tajikistan',
  'Thailand',
  'Timor-Leste',
  'Turkey',
  'Turkmenistan',
  'United Arab Emirates',
  'Uzbekistan',
  'Viet Nam',
  'Yemen']}

##################################################################################3


print(24*"#")
print("# Welcome to GeoGuess! #")
print(24 * "#")

print("Would you like to play an easy or a difficult game?")
difficult_game = None

while difficult_game is None:
    difficult_game = None
    while difficult_game is None:   
        game_type = input("Type D for difficult or E for easy: ")
        # Here I have added 'upper()' option  to allow lower letter as an input
        if game_type.upper() == "D":
            difficult_game = True
            print("\nOkay, difficult it is!")

        # Here I have added 'upper()' option  to allow lower letter as an input
        elif game_type.upper() == "E":
            difficult_game = False
            print("\nOkay, easy it is!")

print("Would you like to pick a continent to play with?")
print('\n< list of Continents >')
print('North America,','Asia,','South America,','Africa,','Europe,','Oceania')
print('\n# Note: There is only one country in Antarctica. So, it is not included')

continent = None
while continent not in ['North America','Asia','South America','Africa','Europe','Oceania','No_selection']:
    continent_type = input("\nType continent you like to play with, (Type X when you don't want to pick): ")
    
    # Here I have added 'upper()' option  to allow lower letter as an input
    if continent_type == 'North America':
        continent = 'North America'
        print("\nOkay, North America!")
    
    elif continent_type == 'Asia':
        continent = 'Asia'
        print("\nOkay, Asia!")
    
    elif continent_type == 'South America':
        continent = 'South America'
        print("\nOkay, South America!")
    
    elif continent_type == 'Africa':
        continent = 'Africa'
        print("\nOkay, Africa!")
    
    elif continent_type == 'Europe':
        continent = 'Europe'
        print("\nOkay, Europe!")
    
    elif continent_type == 'Oceania':
        continent = 'Oceania'
        print("\nOkay, Europe!")

    elif continent_type.upper() == "X":
        continent = 'No_selection'
        print("\nOkay, No specific continent!")


correct_guesses = 0
Wrong_questions = []
Check_tendency_from_mistake = []
total_guesses   = 0 
hint_number = 10
comparison_countries = []

while True:
    if continent == 'No_selection': # Play chose X (Do not want to pick continent)
        selected_countries = list(area.keys()) # list of country is all the countries
    else:
        selected_countries = dic_continent[continent] # list of countries with selected continent

    # There are more countries in Continent dictionary. 
    # I have added this to prevent key error
    check = None
    while check is None: 
        country1 = random.choice(selected_countries)
        if country1 in area.keys(): # Break when randomly selected country is in the given 'area' dictionary
            check = True

    # List of countries that have similiar size of area with country 1

    Hint_country1 = []
    for country_other in area.keys():
        relative_difference = 1- area[country_other]/area[country1]

    # Selected countries that has relative area differece of 30%    
        if abs(relative_difference) < 0.3:
            Hint_country1.append(country_other)

    area1 = area[country1]    
    
    for other_country in area.keys(): 
        # Go only when countries are in a area dictionary 
        if other_country in selected_countries:
            larger_area = max(area1, area[other_country])        
            smaller_area = min(area1, area[other_country])        
            relative_difference = 1 - smaller_area / larger_area        
            if ((difficult_game and 0 < relative_difference < 0.25) or  (not difficult_game and relative_difference > 0.25)):
                comparison_countries.append(other_country) 
        else:
            continue
    
    # Small change from canvas
    # I have changed comparison_countries list to contain all the countries that meet conditions
    # So I deleted this

    # if len(comparison_countries) ==0 :        
    #     continue  

    country2 = random.choice(comparison_countries)    

    # List of countries that have similiar size of area with country2
    Hint_country2 = []
    for country_other in area.keys():
        relative_difference = 1- area[country_other]/area[country2]
        
    # Selected countries that has relative area differece of 30%    
        if abs(relative_difference) < 0.3:
            Hint_country2.append(country_other)

    correct_answer = "1" if area[country1] > area[country2] else "2"

    print("\nWhich country is larger?")    
    print("1: " + country1)    
    print("2: " + country2)    

    print("\nDo you want hint?")
    reply = None
    # Ask whether they want hint only when hints are available
    while reply not in ["y", "Y", "n",'N'] and hint_number != 0:   
            reply = input("Type Y for yes, N for no: ") 
            if reply.upper() == 'Y':
                print('< Countries with similar area of country1 >')
                print(Hint_country1)
                print('\n< Countries with similar area of country2 >')
                print(Hint_country2)
                hint_number -= 1

    guess = None    

    while guess not in ["1", "2", "X",'x']:   # Here I have added option to allow lower letter
        guess = input("\nMake a guess: 1 or 2? (Type X to exit.) ")    
    
    if guess.upper() == "X":
        # In case of people didn't solve anything, I have added a condition
        if total_guesses == 0:
            print('You did not solve anything bye!')
            break
        
        # Show  a list that contains wrong questions
        print('\n< Answers for wrong questions >\n')
        for question in Wrong_questions: 
            print(question)

        print("\nYour tendeny to learn by rate")
        print('-100% mean you learn really well')
        print('-0% means learning tendency is not good ')

        lst2= [Check_tendency_from_mistake.count(i) for i in set(Check_tendency_from_mistake)]
        lst3= [num for num in lst2 if num>1]

        percentage = str(100- sum(lst3)/sum(lst2)*100) + '%'
        print('\n# Your learning tendency score is', percentage)

        percent_correct = round(100 * correct_guesses / total_guesses)
        print("\n# You were " + str(percent_correct) + "% correct. Bye! #")        
        break    
        
    elif guess == correct_answer:        
        total_guesses += 1        
        correct_guesses += 1        
        print("\nYou are correct!") 
        print('\nThe number of hints that are left :', hint_number)  

    elif guess != correct_answer:        
        total_guesses += 1
        # Save wrong questions here
        # Answers will be contained as a string
        print(country1)
        print(country2)

        if correct_answer == "1":
            Wrong_questions.append(f'{country1} > {country2}')
        else:
            Wrong_questions.append(f'{country1} < {country2}')

        # Add countires into wrong answers list 
        # We will check learning tendency by checking the 
        # frequency of Countries
        # If the frequency of countires is high, this means learning tendency is low 
        
        Check_tendency_from_mistake.append(country1)
        Check_tendency_from_mistake.append(country2)

        print("\nThat's wrong, sorry!")
        print('\nThe number of hints that are left :', hint_number)

