from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'Aza',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, I do not understand. I am still learning. Here is a list of what i can help you with type (LIST)',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

# Training with Personal Ques & Ans 

trainer = ListTrainer(chatbot)

manual=[

    "List",
    "what do you want to know about ? just type it in (Hotels)(accommodations)(Places)(currency)(activities)(weather)(tours)(food)(nature)(History)(shopping)(transport)(culture)(nature)",


]

conversation = [
    "Hi",
    "Hello! how can i help you ?",
    "Hello", 
    "Hi there",
    "Hello",
    "Hi there! how can i help you ?",
    "How are you doing?",
    "great",
    "That is good to hear"
    "I'm doing great.",
    "That is good to hear",
    "Thank you",
    "You're welcome",
    "Glad to help, is there anything else you are looking for ?",
    "yes",
    "I am here to help 😊",
    "what is your name ?",
    "My name is Aza",
    "Are you a robot?",
    "Yes, My name is Aza",
    "Are you a bot?",
    "Yes, My name is Aza",
    "Are you a chatbot?",
    "Yes, My name is Aza",
    "Are you real?",
    "I am a ChatBot, My name is Aza",
    "What is your name?",
    "My name is Aza",
    "What do you do?",
    "I am made to give answers and help you in terms of tourism in salalah.", 
    "who made you ?",
    "That is a secret :)",
    "glad",
    "Thank you",
]

facts = [
    "How much is the population in salalah ?",
    "The total population is 374,000",

    "what should i know about salalah?",
    "Salalah is the capital city of Oman's southern Zufar and Dhofar region. It is often considered to be the second city of the Sultanate, although some of this designation is probably due to its distinction as Sultan Qaboos birthplace. The region is famous for its khareef (monsoon), Many locals will in fact be quite surprised to see non-Arab visitors at other times of year.",
    
    "travel tip",
    "Salalah is at its busiest during the khareef season, so make sure you book your hotel as far in advance as possible. If driving around the region during the monsoon, be prepared for the rapid onset of thick fog.",
    
    "what is the city famous for?",
    "Salalah is known for its unique Khareef (monsoon) season, in which the whole city turns green and attracts visitors from all around the world. Nevertheless, there is more to this mind-blowing gem in terms of natural beauty and architectural wonder.",
    
    "How big is salalah ?",
    "Salalah is the second largest city of Sultanate of Oman.",
    
    "can you tell me about salalah?",
    "Salalah City receives its visitors with large vistas of grass and water mist, opening its arms to them and spreading the shade of its palm trees (locally called Coconut). The smell of frankincense wafts through the city. This is the same frankincense that has been portrayed on the walls of ancient Pharaonic temples ever since Hatshepsut journeyed to Oman’s fertile lands. Salalah is famous for its lights that sparkle through the night’s lyrical breezes and the day’s sun rays beating down on the waves that dance in celebration of Salalah’s eternal spring.",
    
    "what is the main language in salalah ?",
    "The main language is arabic, but most people can speak english too.",
    
    "where is salalah located?",
    "it is located in the south of oman",
    
    "tell me about kareef salalah",
    "Dhofar Governorate is famous for its seasonal weather, locally known as monsoon or “Khareef” , when it witnesses its best period, clothed in lush greenery and its hills surrounded by white fog. Light rains drizzle to cool the air. During this time, it is frequented by many visitors, especially from within Oman and the neighbouring countries. Salalah Tourism Festival takes place from 15 July to 31 August every year. The festival is part of Khareef(monsoon) that extends from the end of July until the beginning of September.",
    
    "when is the kareef season ?",
    "It starts from about June to early September.",

    "How is the weather in salalah ?",
    "The warmest month (with the highest average high temperature) is May (32.4°C). The month with the lowest average high temperature is August (27.3°C). The month with the highest average low temperature is June (26.5°C). The coldest month (with the lowest average low temperature) is January (17.9°C). make sure to visit <a href= ""https://weather.com/weather/today/l/17.02,54.11?par=google&temp=c"">Here</a> if you want to know the weather in real time ",

    "tell me about the history of salalah ?",
    "Salalah is one of the most historic cities in the region due to the role it played in the frankincense trade. Evidence of this can still be found today at many of the region’s fascinating archeological sites.Samharam was a city and port that acted as one the Dhofar region’s links to the world. Today only the ruins of the 5,000-year-old city remain, but you can still get a sense of its former importance. Built on a hill, it looks out onto an unspoilt stretch of beach and the ocean.On the outskirts of Salalah is Al Balid City, which was an important port during the same time as Samharam. It’s a sprawling site that was only rediscovered in 1930, with pathways winding through the clearly defined foundations of ancient buildings.",

    "how is the weather there?",
    "Most visitors come to Salalah during July and August to enjoy the annual khareef, when the nearby wadis are full of water. Occasionally streets flood, and ocean currents are too strong for swimming or diving. The crowds leave in September along with the rains, but the vegetation is still green, and hotel prices have started to come down. Diving is only possible during the dry season, from October to the end of May, and this is also the optimal time for bird watching. May and especially June are the hottest months of the year, with humidity steadily increasing until the rains bring relief again in late June or early July.",



]

accommodations = [
    "I am looking for accommodations in salalah ?",
    "what about your budget (Mid-Range options)(Low-budget)(Luxury)? are you (alone) or with (family) ?",

    "Low-budget",
    "Check the list of the cheapest hotels <a href=""https://www.tripadvisor.com/SmartDeals-g298419-Salalah_Dhofar_Governorate-Hotel-Deals.html"">Here</a>",
    
    "Mid-Range options",
    "Check the list for mid-range hotels <a href=>Here</a>",
    
    "Luxury",
    "Check the list of luxury hotels <a href =""https://www.booking.com/luxury/city/om/salalah.en-gb.html"">Here</a>",
    
    "best accommodations in salalah ?", 
    "are you alone or with family ?",
    
    "Looking for accommodations in salalah ?", 
    "Sure! are you alone or with family ?",
    
    "alone",
    "The best choices would be, Salalah gardens hotel, it is close to everything you might need for a solo vist and it costs only 36 OMR a night, The Millennium Resort, which costs 50 OMR and Anantara Resort which is a more luxurious option. There is also the Haffa house which is a cheaper option, only 15 OMR per day. <a href= ""https://www.booking.com/accommodation/city/om/salalah.html""> read more here </a>",
    
    "family", 
    "Some of the best choices for salalah family visits are, Juweira resort, crowne hotel, Salalah gardens mall, Al nile hotel and others. visit <a href= ""https://www.booking.com/accommodation/city/om/salalah.html""> THIS </a> for more info, Or do you want to list hotels based on you budget (Mid-Range options)(Cheaper options)(Luxury) ?",


]

places = [
    "Best place for sightseeing?",
    "jabel samhan, shaat, watching the dolpins in mirbat, Al Mughsail Beach, Ayn razat",
    
    "best places to relax ?", 
    "1- Al baleed resort (anantara) 2- crowne plaza resort 3- fanar hotel 4- Rotana resort 5- Hilton 6- Marriott resort, 7- Juweria Hotel. Which one are you interested to know more about ?",
    
    "Best resorts in salalah ?",
    "1- Al baleed resort (anantara), 2- crowne plaza resort, 3- fanar hotel, 4- Rotana resort, 5- Hilton, 6- Marriott resort, 7- Juweria Hotel. Which one are you interested to know more about ?",

    "Al  haffa souq",
    "Al Hafah Souq lies 3 kilometres from the city of Salalah in Dhofar Governorate. It is surrounded by lofty coconut trees and is the perfect place to buy the best kinds of gum and incense, not only in Dhofar, but also in the Sultanate.Al Hafah Souq is replete with a variety of products, including traditional textiles and clothing, gold and silver jewellery as well as many other traditional artefacts.<a href=""https://www.google.com/maps/place/17%C2%B000'09.2%22N+54%C2%B006'07.4%22E/@17.002553,54.1042467,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x0!8m2!3d17.002553!4d54.102058?hl=ar""> Location here</a>",

    "Wadi darbat",
    "his wadi carves its way through hills and highlands until it reaches Khawr Ruri, where it empties into the Arabian Gulf.During autumn, the wadi’s water descending from the mountains forms magnificent waterfalls cascading from a height of up to 30 metres (100 feet).",

    "Al balid city",
    "The Most Important Ancient Port on the Arabian Sea (Part of the Frankincense Trail) history dates back to before 2000 BC. Some archaeological research confirms that the city's prosperity dates back to the Iron Age. Much of this city’s remains lie in Dhofar Governorate.<a href =""https://omantourism.gov.om/wps/portal/mot/tourism/oman/details/!ut/p/a1/ldHJboMwEAbgZ-mBKx6zGKc3toALhKQuKvGlIhUlVARHhIY-fgnKpVvS-jbW90uzIIFyJNriWFdFX8u2aE61IE_p_YrPF74BEAUYmBb4S4w5NrExgvUI3MAODSsGACdygUX-KnrQEww2_m_eoBowzwk9a5YAMPK3PPzybLiW52WLHpGY2CyyfK4BgTR2LGA8CzEPHJ1ycgZkMY-XvochpXhsjtOEcO7qYFhXQGqewaVFfQHfNzGBC6PeIVE1cjOdbW23G51WSHTlS9mVnfrWjd_bvt8fbhVQYBgGtZKyakr1We4U-CmylYce5Z8l2u-yLH9nNXs1m2Ns33wAxioItQ!!/dl5/d5/L2dJQSEvUUt3QS80SmlFL1o2XzlLN0VTMjA2ME81NzEwSVNQUTBLRUwxR1A3/?WCM_GLOBAL_CONTEXT=/wps/wcm/connect/mot_english_lib/mot/experience/culture/archeological/baleed"">Read more here</a>",

    "Dhofar Lagoons", #
    "Lagoons abound in Dhofar Governorate, and vary in size from a few hectares to more than one hundred hectares. Some of these lagoons have been established as nature reserves. There are eight reserves, namely: Khawr Ruri, the largest reserve in the Governorate. Khawr Al Baleed, Khawr Al Maghsayl, Khawr Awqad, which is located in the Dhofar Governorate at the outskirts of the ancient Awqad <a href =""https://omantourism.gov.om/wps/portal/mot/tourism/oman/details/!ut/p/a1/ldHJboMwEAbgZ-mBKx6zGKc3toALhKQuKvGlIhUlVARHhIY-fgnKpVvS-jbW90uzIIFyJNriWFdFX8u2aE61IE_p_YrPF74BEAUYmBb4S4w5NrExgvUI3MAODSsGACdygUX-KnrQEww2_m_eoBowzwk9a5YAMPK3PPzybLiW52WLHpGY2CyyfK4BgTR2LGA8CzEPHJ1ycgZkMY-XvochpXhsjtOEcO7qYFhXQGqewaVFfQHfNzGBC6PeIVE1cjOdbW23G51WSHTlS9mVnfrWjd_bvt8fbhVQYBgGtZKyakr1We4U-CmylYce5Z8l2u-yLH9nNXs1m2Ns33wAxioItQ!!/dl5/d5/L2dJQSEvUUt3QS80SmlFL1o2XzlLN0VTMjA2ME81NzEwSVNQUTBLRUwxR1A3/?WCM_GLOBAL_CONTEXT=/wps/wcm/connect/mot_english_lib/mot/experience/nature/reserves/dohfar+lagoons"">Read more here</a>",
]

resturants = [
  "best resturants in salalah ?",
  "What about your budget (Mid-Range)(fastfood)(Splurge) ?",

  "Mid-Range",
  "Most of the choices are found in malls, passion change, Huff puff, big bin, if you like burgers and american cuisine and if you prefer arabian cuisines, there are labeneese and turkeish resturants as well",

  "fastfood",
  "You can find a wide varity of fast food resturants like KFC, pizza hut, mcdonalds, supway many others",

  "Splurge",
  "Mostly found in Hotels, such as anantara's, crowne's and you can also find some at salalah gardens mall, like anabi and others. Here is a list of the top resturants according to visitors <a href=""https://theculturetrip.com/middle-east/oman/articles/the-top-restaurants-in-salalah-oman/""></a>",  
]

travel_info = [
    "what currency is used in salalah ?",
    "Omani rial (OMR)",
    
    "How to get a visa for oman ?",
    "Most nationalities can buy an Oman tourist visa on arrival: 30-day visa: 21 rials or 60USD. 10-day visa: 5 rials or 13USD Multiple-entry visa, valid for 1 year: 50 rials or 130USD. If possible, try to pay in either Omani Rials or with a credit card, because the price in USD is higher than the actual exchange rate. You can also buy your Omani visa online through this portal at a discounted price (around 1 rial), which is 2-3USD, for the 30-day visa at least. ",
    
    "Daily budget for salalah ?",
    "At Salalah, you will probably spend around OMR 30 (USD 77) per day.",
    
    "where to exchange money in salalah ?", 
    "The best places to exchange money is at the Oman UAE exchange centres. There are many small centres in and around Salalah.",
    
    "Do you need to join a tour in Salalah ?",
    "Salalah is a difficult city to move around, basically, because you hardly find public transportation. Therefore, to travel in Oman, you need to either rent a car or go on a tour. Read <a href= ""https://www.tripadvisor.com/Attractions-g298419-Activities-c42-Salalah_Dhofar_Governorate.html""> Here </a> to learn more about what tours are offered in salalah.",

    "How can i travel around in salalah ?",
    "the most ideal way for tourists to get around either within Salalah or when travelling to the numerous locations outside of town, is by taxi, by hiring a driver, or by hiring a car.",

]

hotels = [

    "List of hotels",
    "There are many hotels in the city, but the best options would be hotels located centerally, for example, salalah gardens mall, the hilton resort, and millinum.. Do you have a specific preference when it comes to the budget (Mid-Range options)(Cheaper options)(Luxury)? ",

    "Al baleed resort",
    "Nestled between a private beach and freshwater lagoon, Al Baleed Resort Salalah by Anantara celebrates cultural treasures, while being the first and only luxury pool villa resort among Salalah hotels.Majestic design reflects Oman’s coastal fortresses. Garden walkways are lush with palms and water features. Relax at the infinity pool or on white sands. Explore archaeological ruins – or soak up Salalah’s precious frankincense in exclusive spa rituals. <a href= ""http://www.anantara.com/en/al-baleed-salalah""> read more here </a>",

    "anantara",
    "Nestled between a private beach and freshwater lagoon, Al Baleed Resort Salalah by Anantara celebrates cultural treasures, while being the first and only luxury pool villa resort among Salalah hotels.Majestic design reflects Oman’s coastal fortresses. Garden walkways are lush with palms and water features. Relax at the infinity pool or on white sands. Explore archaeological ruins – or soak up Salalah’s precious frankincense in exclusive spa rituals. <a href= ""http://www.anantara.com/en/al-baleed-salalah""> read more here </a>",

    "Juweria Hotel",
    "a popular destination to tourists who are attracted by its incredible climate and vistas. Elegant and understated, the 4-star Juweira Boutique Hotel was designed in a classic oriental theme. Creative dining, best escape to nature, quite place with great comfort and service, close to the Salalah town. <a href=""here:www.juweirahotel.com"">Read more here</a>",
    
    "crowne plaza resort",
    "Located 1.2 mi away from Salalah, Crowne Plaza Resort Salalah is surrounded by lush tropical gardens. The hotel has a large outdoor pool, overlooking the Indian Ocean and the sandy beach.Crown Plaza features modern rooms with a satellite TV. All the air-conditioned rooms have wooden furniture and a work desk. Each of them has mini-bar and a coffee maker. Salalah International Airport is only a 10-minute drive from the hotel. Free private parking and a car rental service are available on site.",

    "fanar hotel",
    "Fanar Hotel & Residences is set in Salalah directly on the beach. Guests can enjoy the buffet restaurant or Aubergine a Mediterranean à la carte restaurant. You will find a 24-hour front desk, babysitting service, gift shop and entertainment at the property. During khareef, bike rental services are available at a surcharge. This hotel has a private beach area and car hire are available. You can play tennis at the hotel or join water activities. Enjoy nearby Hawana Aqua Park, the largest aquapark in Oman. RATING: Couples particularly like the location — they rated it 8.1 for a two-person trip.",

    "Rotana resort",
    "he upscale hotel’s Omani-inspired architecture features a series of clusters surrounding the main building, housing major public facilities and amenities. All guest rooms have a balcony or terrace with ocean views, canal views or garden views and are furnished with flat screen Televisions, mini bar, tea or coffee making amenities and more. Conveniently located with close proximity to major attractions including Museum of the Land of Frankincense, Haffah Souq and the Sultan's Palace, Salalah Rotana Resort is a scenic 20 km drive from Salalah Airport.",

    "Hilton",
    "This hotel is a good choice. It’s right on the sand, but located just on the outskirts of Salalah, and has a collection of bars and restaurants. <a href ="" www3.hilton.com"">read more here </a>",

    "Marriott resort",
    "On peaceful Mirbat Cove, the 5-star Kairaba Mirbat Resort has direct access to a white-sand beach. It features a 2,000-m² freeform pool, a diving centre and a tennis court. Guests can lounge around the lagoon-style pool or the beach. The spa offers traditional Balinese massages. The resort also offers a hot tub and a 24-hour gym. Kairaba Mirbat Resort has an international restaurant and an Arabic specialty restaurant. Light snacks are available from the Wharf Pool Bar. The Piano Lounge offers a range of drinks and freshly baked pastries. The city centre and Salalah International Airport are just a 1-hour drive from the hotel. The UNESCO-listed ruins of Khor Rori and the famous Wadi Darbat are just 25 km from the resort. <a href= ""https://www.booking.com/hotel/om/salalah-resort-salalah.html""> Learn more here </a>",


    "Where can i stay in salalah ?",
    "Salalah is home to a number of luxurious hotels, such as the Crowne Plaza Resort Salalah, the Hilton Salalah Resort and the Al Baleed Resort Salalah by Anantara, which are all located relatively centrally. The Salalah Rotana Resort lies a little way out of Salalah. In the town of Mirbat, which is around an hour’s drive from Salalah, is the Marriot Hotel. Al Busaidi advised tourists however to stay in hotels located within the city of Salalah, due to the services that the city has to offer. I would personally like to advise you to stay in Salalah, as it’s lively and has a great deal of things going on, unlike some of the other smaller towns. Mirbat for example doesn’t have as many facilities as Salalah and hence tourists should look to base themselves in Salalah. Moreover, for those looking for a cheaper option, there are hotel apartments that you can rent out for the duration of your stay. <a href= ""https://www.atheer.om/en/37769/need-know-travelling-salalah-khareef/#ixzz6bDfquiPC""> read more here </a>", 

    "family hotels",
    "Some of the best choices for salalah family visits are, Juweira resort, crowne hotel, Salalah gardens mall, Al nile hotel and others. visit <a href= ""https://www.booking.com/accommodation/city/om/salalah.html""> THIS </a> for more info, Or do you want to list hotels based on you budget (Mid-Range options)(Cheaper options)(Luxury) ?",



]
activities = [

    "Boat trips in salalah ?",
    "Enjoy the crystal waters of the Sea of Oman, and the surrounding beautiful mountains and white sandy beaches of Salalah through a trip in a local wooden Omani boat. Whether a short or long trip, a boat journey will offer a unique experience, where you can relax and watch the pure natural beauty of Salalah and the Dhofar region.", 

    "best places for shopping ?",
    "The best places to go shopping in the city are, Salalah gardens mall, Al Saadah City Mall and Souq Al Haffa for traditional goods. find the locations here <a href= ""https://www.google.com/search?newwindow=1&sxsrf=ALeKk036hH0wRzNa1TADysa2xbj9NGHEZA:1604251262202&ei=E-yeX8bFIdu91fAP36GF2AU&q=shopping%20in%20salalah&oq=shopping+in+salalah&gs_lcp=CgZwc3ktYWIQAzIGCAAQBxAeMgYIABAHEB4yAggAMgQIABAeMgYIABAFEB4yBggAEAUQHjIGCAAQBRAeOgcIIxCwAhAnULrCEFiDzRBgk9AQaABwAHgAgAGJAogBmg-SAQUwLjIuN5gBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=2ahUKEwiNnvTU7eHsAhURaRUIHZZgCXYQvS4wAHoECBIQKw&uact=5&npsic=0&rflfq=1&rlha=0&rllag=17024141,54114308,5450&tbm=lcl&rldimm=7816026422240269555&lqi=ChNzaG9wcGluZyBpbiBzYWxhbGFoSOOAjIn9rICACFolCghzaG9wcGluZxAAGAAYAiITc2hvcHBpbmcgaW4gc2FsYWxhaA&phdesc=URPEg4aImr8&rldoc=1&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:10&rlst=f#rlfi=hd:;si:7816026422240269555,l,ChNzaG9wcGluZyBpbiBzYWxhbGFoSOOAjIn9rICACFolCghzaG9wcGluZxAAGAAYAiITc2hvcHBpbmcgaW4gc2FsYWxhaA,y,URPEg4aImr8;mv:[[17.0559709,54.1728053],[16.998636899999997,54.0133685]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:10"">Location here</a>",

    "Things to Do in Salalah ?", 
    "There are many activities to do in salalah, especially if you love nature and sightseeing. There are a varity of tours that help you too - type (tours) if interested - you can also go on safari's, boat trips (water activities) and hiking. in addition to that, Salalah is a good place to camp because of it's nature and many mountains. if you are interested in other things like shopping, spas and luxury experinace you can find that too. check our list of (luxury) hotels.",

    "camping",
    "The diverse environment of Salalah allows many options when it comes to camping. Camping is mostly enjoyed in The Empty Quarter in Dhofar or camping in one of the secluded beaches that spread in salalah Governorate. In addition to the camps created for tourists in each of these areas, visitors are allowed to pitch their own tents in each of these places, as well as in many others.",

    "Dolphin watching", ##
    "Just like Muscat and Musandam are famous for dolphin watching, Dhofar is too. Dolphin shoals visit the shores of salalah in large numbers.",

    "",
    "",
]
keywords =[

    "Salalah",
    "Salalah City receives its visitors with large vistas of grass and water mist, opening its arms to them and spreading the shade of its palm trees (locally called Coconut). The smell of frankincense wafts through the city. This is the same frankincense that has been portrayed on the walls of ancient Pharaonic temples ever since Hatshepsut journeyed to Oman’s fertile lands. Salalah is famous for its lights that sparkle through the night’s lyrical breezes and the day’s sun rays beating down on the waves that dance in celebration of Salalah’s eternal spring.",

    "hotels",   
    "Salalah is home to a number of luxurious hotels, such as the Crowne Plaza Resort Salalah, the Hilton Salalah Resort and the Al Baleed Resort Salalah by Anantara, which are all located relatively centrally. The Salalah Rotana Resort lies a little way out of Salalah. In the town of Mirbat, which is around an hour’s drive from Salalah, is the Marriot Hotel. Al Busaidi advised tourists however to stay in hotels located within the city of Salalah, due to the services that the city has to offer. I would personally like to advise you to stay in Salalah, as it’s lively and has a great deal of things going on, unlike some of the other smaller towns. Mirbat for example doesn’t have as many facilities as Salalah and hence tourists should look to base themselves in Salalah. Moreover, for those looking for a cheaper option, there are hotel apartments that you can rent out for the duration of your stay. <a href= ""https://www.atheer.om/en/37769/need-know-travelling-salalah-khareef/#ixzz6bDfquiPC""> read more here </a>",
    
    "accommodations",
    "what about your budget (Mid-Range options)(Cheaper options)(Luxury)?",
    
    "activites",
    "Read <a href= ""https://www.tripadvisor.com/Attractions-g298419-Activities-Salalah_Dhofar_Governorate.html""> Here </a> to know more about what activities you can do in salalah.",

    "Resturants",
    "What Resturants are you more interested in (Mid-Range)(cheap)(Splurge) ?",

    "kareef",
    "Dhofar Governorate is famous for its seasonal weather, locally known as monsoon or “Khareef” , when it witnesses its best period, clothed in lush greenery and its hills surrounded by white fog. Light rains drizzle to cool the air. During this time, it is frequented by many visitors, especially from within Oman and the neighbouring countries. Salalah Tourism Festival takes place from 15 July to 31 August every year. The festival is part of Khareef(monsoon) that extends from the end of July until the beginning of September.",

    "Tours",
    "Read <a href= ""https://www.tripadvisor.com/Attractions-g298419-Activities-c42-Salalah_Dhofar_Governorate.html""> Here </a> to learn more about what tours are offered in salalah.",

    "weather",
    "The warmest month (with the highest average high temperature) is May (32.4°C). The month with the lowest average high temperature is August (27.3°C). The month with the highest average low temperature is June (26.5°C). The coldest month (with the lowest average low temperature) is January (17.9°C). make sure to visit <a href= ""https://weather.com/weather/today/l/17.02,54.11?par=google&temp=c"">Here</a> if you want to know the weather in real time ",

    "transport",
    "the most ideal way for tourists to get around either within Salalah or when travelling to the numerous locations outside of town, is by taxi, by hiring a driver, or by hiring a car.",

    "Shopping",
    "The best places to go shopping in the city are, Salalah gardens mall, Al Saadah City Mall and Souq Al Haffa for traditional goods. find the locations here <a href= ""https://www.google.com/search?newwindow=1&sxsrf=ALeKk036hH0wRzNa1TADysa2xbj9NGHEZA:1604251262202&ei=E-yeX8bFIdu91fAP36GF2AU&q=shopping%20in%20salalah&oq=shopping+in+salalah&gs_lcp=CgZwc3ktYWIQAzIGCAAQBxAeMgYIABAHEB4yAggAMgQIABAeMgYIABAFEB4yBggAEAUQHjIGCAAQBRAeOgcIIxCwAhAnULrCEFiDzRBgk9AQaABwAHgAgAGJAogBmg-SAQUwLjIuN5gBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=2ahUKEwiNnvTU7eHsAhURaRUIHZZgCXYQvS4wAHoECBIQKw&uact=5&npsic=0&rflfq=1&rlha=0&rllag=17024141,54114308,5450&tbm=lcl&rldimm=7816026422240269555&lqi=ChNzaG9wcGluZyBpbiBzYWxhbGFoSOOAjIn9rICACFolCghzaG9wcGluZxAAGAAYAiITc2hvcHBpbmcgaW4gc2FsYWxhaA&phdesc=URPEg4aImr8&rldoc=1&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:10&rlst=f#rlfi=hd:;si:7816026422240269555,l,ChNzaG9wcGluZyBpbiBzYWxhbGFoSOOAjIn9rICACFolCghzaG9wcGluZxAAGAAYAiITc2hvcHBpbmcgaW4gc2FsYWxhaA,y,URPEg4aImr8;mv:[[17.0559709,54.1728053],[16.998636899999997,54.0133685]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:10""></a>",

    "history",
    "Salalah is one of the most historic cities in the region due to the role it played in the frankincense trade. Evidence of this can still be found today at many of the region’s fascinating archeological sites.Samharam was a city and port that acted as one the Dhofar region’s links to the world. Today only the ruins of the 5,000-year-old city remain, but you can still get a sense of its former importance. Built on a hill, it looks out onto an unspoilt stretch of beach and the ocean.On the outskirts of Salalah is Al Balid City, which was an important port during the same time as Samharam. It’s a sprawling site that was only rediscovered in 1930, with pathways winding through the clearly defined foundations of ancient buildings.",

    "Currency",
    "1 OMR = 0.38 USD",

    "Places", 
    "There are many places to visit in salalah, you can go for a trip to the jabal or visit the Mueseum of frankincense and the traditional souq. you can also enjoy the weather and view in wadi darbat and salalah's beautiful beaches. <a href=""https://www.holidify.com/places/salalah/sightseeing-and-things-to-do.html"">Click here for more info</a>",

    "activites",
    "There are many activities to do in salalah, especially if you love nature and sightseeing. There are a varity of tours that help you too - type (tours) if interested - you can also go on safari's, boat trips (water activities) and hiking. in addition to that, Salalah is a good place to camp because of it's nature and many mountains. if you are interested in other things like shopping, spas and luxury experinace you can find that too. check our list of (luxury) hotels.",

    "Beaches",
    "Salalah is home to the Taqah Beach, Al Fazayah Beach, Al Haffa, Al Mughsail, and Al Dahariz beaches. These beaches in Salalah line the East and the South-East coast of Oman overlooking the Arabian Sea. Most of them have soft white sand while some have rocky and rugged terrain. Nonetheless, all of them are scenic, clean and, therefore, are visited by locals all through the year for recreational activities.",

    "Food",
    "",

    "nature", ##
    "Dhofar Governorate stretches over an area of one third of Oman and forms the Sultanate’s southern part. Dhofar includes a distinctive natural diversity where the coast blends with the mountains and the desert in wonderful harmony so that the mountains look like a fertile crescent, rising to a height of 1,500 metres and then descending into a flat plain that embraces sandy beaches stretching for hundreds of kilometres.",

    "culture",
    "History and culture play pivotal roles in delineating the features of Salalah people, and the city’s nature and culture. Studies and research carried out by a number of scholars point to the ancient history of this city. This is evidenced by the various writings and inscriptions found on artefacts belonging to a succession of civilisations that have risen and fallen in this land and which still have their impact to the present day. Excavations are still under way to determine the exact historic timeline of these civilisations, including the Al Bilayd civilization which dates back to between the twelfth and sixteenth centuries, and the archaeological finds indicate the existence of much business activity <a href =""https://omantourism.gov.om/wps/portal/mot/tourism/oman/details/!ut/p/a1/lZFNU4MwEIZ_DVey4SvUG18FDBQwMtJcHOogxaHQoVj8-VKGi1Wp5raZ59mdfRdxlCHe5OeqzPuqbfL6UnPtOXpI2HrjKADUxeBLrhNjzLCKlRHYjoDlGp5CAgAwqQU-dRL6KIcYDPxfX9El8G3Ts8kqBPC1v_nwyzNg8leUOEwCDSKVjD6LE6BOgN2YzP4CcGM-Kxr0hPjVmMAkY5fUw8w1ZZ1pM6Bt1kHs2BgiHY_LMT3UGLNkUMgNIFJnYCnoK-B7khOwENU94mXd7qazb41mJ-sl4l3xWnRFJ7534_e-74-nOwEEGIZBLNu2rAvxpT0I8JOyb089yr6S6HhI0zT78Cv_Ta3PgfEJZNjlCA!!/dl5/d5/L2dJQSEvUUt3QS80SmlFL1o2XzlLN0VTMjA2ME81NzEwSVNQUTBLRUwxR1A3/?WCM_GLOBAL_CONTEXT=/wps/wcm/connect/mot_english_lib/mot/experience/culture/cites/salalah"">Read more here</a> ",
    
    "Salalah city",
    "The unique climatic factors make Salalah a magical spot and the jewel of the Arabian Sea. Here you will enjoy monsoon (khareef) amidst the green carpet woven by nature in Salalah, and marvel at the steep mountain views, bathed in the colours of sunset and sunrise that visitors enjoy every day, and marvel at the abundance of rare types of birds.",
   
   "Mountains",
   "Salalah has a number of beautiful mountains, but Ittin is easily accessible from Salalah city and within 5 minutes, you can reach to the mountain for a great view of Beautiful Salalah City. The view is stunning at night!<a href=""https://www.google.com/maps/dir/17.0812959,54.1561049/salalah+ittin/@17.0730746,54.180312,12z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x3dd15f744941a8fd:0x6648fd77b3985d07!2m2!1d54.0668244!2d17.0656765"">Location here</a> ",

]

CQuestions =[
   "Where to stay",
    "You can choose between resort hotels or budget friendly hotels. Want to know more, type (hotels)",

    "where to go",
    "Thre many places to visit in salalah. you can go for a walk in the nature and park, go to the beach and enjoy the beautiful weather. Shopping malls are also a great place to buy souviners before you leave ... Type (places) for more info on that.",

    "where to eat",
    "You can eat at resturants, coffee shops. There are variety of cuisines you can find here, american, turkeish, chinese, and traditional omani food. Tell me What Resturants are you more interested in (Mid-Range)(cheap)(Splurge) for more info ?",

    "what to do",
    "There are many activities to do in salalah, especially if you love nature and sightseeing. There are a varity of tours that help you too - type (tours) if interested - you can also go on safari's, boat trips (water activities) and hiking. in addition to that, Salalah is a good place to camp because of it's nature and many mountains. if you are interested in other things like shopping, spas and luxury experinace you can find that too. check our list of (luxury) hotels.",

]
chatbot.storage.drop() #drop the previous trained data
list_trainer = ListTrainer(chatbot)

for item in (conversation, facts, accommodations, activities, travel_info, resturants, places, hotels, keywords, CQuestions, manual):
    list_trainer.train(item)

# Training it with English Corpus Data 
#trainer_corpus = ChatterBotCorpusTrainer(chatbot)
#trainer_corpus.train(
#    'chatterbot.corpus.english',
#    "chatterbot.corpus.english.greetings",
#    "chatterbot.corpus.english.conversations"
#) 

#sudo pip install numpy --upgrade scikit-learn