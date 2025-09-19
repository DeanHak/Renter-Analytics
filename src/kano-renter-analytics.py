# -*- coding: utf-8 -*-
"""Kano_Residency_Reshaped.ipynb


# Importing Data
"""

pip install XlsxWriter

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# inputting the csv file
df = pd.read_csv('/content/Residency Reshaped_September 4, 2024_10.55.csv')
df.head()

df.info()

dq=df # creating a duplicate

"""Cleaning the data and setting column headers

# Cleaning Data
"""

dq.columns = dq.iloc[0]
dq = dq.drop([0, 1])

dq.head()

"""# **Column Names**"""

# get a list of all the questions
dq.columns.values.tolist()

d_cor = dq[['Please select your age range:',
 'What is your current living situation?',
 "How long have you been renting in total, across all the places you've lived?",

 'How much do you currently pay in rent each month (excluding bills and utilities)?',
 'How long have you been a resident of your current property?',
 'How would you rate your overall satisfaction with your current apartment?',
 'How many bedrooms does your current apartment have?',
 'What type of building is your apartment in?',
 'What best describes your current living arrangement? - Selected Choice',

 'How many roommates or family members currently live with you?',
 'What types of pets do you have, how many, and how do they impact where you choose to live?',
 'Please rank the following factors in order of importance when choosing your current apartment. (1=most important, 7=least important) - Price + Affordability',
 'Please rank the following factors in order of importance when choosing your current apartment. (1=most important, 7=least important) - Amenities ',
 'Please rank the following factors in order of importance when choosing your current apartment. (1=most important, 7=least important) - Location',
 'Please rank the following factors in order of importance when choosing your current apartment. (1=most important, 7=least important) - Reputation + Management',
 'Please rank the following factors in order of importance when choosing your current apartment. (1=most important, 7=least important) - Community + Lifestyle',
 'Please rank the following factors in order of importance when choosing your current apartment. (1=most important, 7=least important) - Safety + Security',
 'Please rank the following factors in order of importance when choosing your current apartment. (1=most important, 7=least important) - Design + Layout',


 'Please rank the following reasons in order of importance for why you plan to stay in your current unit or building property. (1=most important, 10=least important) - I am satisfied with the size of my current unit ',
 'Please rank the following reasons in order of importance for why you plan to stay in your current unit or building property. (1=most important, 10=least important) - I am satisfied with the design of my current unit',
 'Please rank the following reasons in order of importance for why you plan to stay in your current unit or building property. (1=most important, 10=least important) - The rent is affordable',
 'Please rank the following reasons in order of importance for why you plan to stay in your current unit or building property. (1=most important, 10=least important) - The location is convenient',
 'Please rank the following reasons in order of importance for why you plan to stay in your current unit or building property. (1=most important, 10=least important) - I don’t want to move',
 'Please rank the following reasons in order of importance for why you plan to stay in your current unit or building property. (1=most important, 10=least important) - I like the amenities',
 'Please rank the following reasons in order of importance for why you plan to stay in your current unit or building property. (1=most important, 10=least important) - I have a good relationship with the management',
 'Please rank the following reasons in order of importance for why you plan to stay in your current unit or building property. (1=most important, 10=least important) - I feel safe and secure',
 'Please rank the following reasons in order of importance for why you plan to stay in your current unit or building property. (1=most important, 10=least important) - I feel like a member of the community and have friends here',



 'Are you planning to own an electric car in the future?',
 'How do you typically commute to work or school? Select the option that best describes your primary mode of transportation.',

 'Do you work remotely, either full-time, part-time, or occasionally?',

 'How satisfied are you with your current remote work setup in your home or apartment?',
 'How much more would you be willing to pay per month for an apartment with your desired in-unit amenities?',
 'Please indicate which of the following smart home devices you currently have in your apartment an... - Current - Smart thermostat',
 'Please indicate which of the following smart home devices you currently have in your apartment an... - Current - Smart lighting',
 'Please indicate which of the following smart home devices you currently have in your apartment an... - Current - Smart locks and security systems',
 'Please indicate which of the following smart home devices you currently have in your apartment an... - Current - Voice-activated assistants (e.g., Amazon Echo, Google Home)',
 'Please indicate which of the following smart home devices you currently have in your apartment an... - Current - Smart Appliances (e.g., smart refrigerators, smart ovens)',
 'Please indicate which of the following smart home devices you currently have in your apartment an... - Current - High-speed internet',
 'Please indicate which of the following smart home devices you currently have in your apartment an... - Current - Home automation systems',
 'Please indicate which of the following smart home devices you currently have in your apartment an... - Current - Smart energy management systems',


 'Please indicate which of the following smart home devices you currently have in your apartment an... - Future - Smart thermostat',
 'Please indicate which of the following smart home devices you currently have in your apartment an... - Future - Smart lighting',
 'Please indicate which of the following smart home devices you currently have in your apartment an... - Future - Smart locks and security systems',
 'Please indicate which of the following smart home devices you currently have in your apartment an... - Future - Voice-activated assistants (e.g., Amazon Echo, Google Home)',
 'Please indicate which of the following smart home devices you currently have in your apartment an... - Future - Smart Appliances (e.g., smart refrigerators, smart ovens)',
 'Please indicate which of the following smart home devices you currently have in your apartment an... - Future - High-speed internet',
 'Please indicate which of the following smart home devices you currently have in your apartment an... - Future - Home automation systems',
 'Please indicate which of the following smart home devices you currently have in your apartment an... - Future - Smart energy management systems',

 'Are there any new spaces, technologies, or innovations you’d like to see in your apartment building?',
 'How satisfied are you with the following aspects of building management? Please rate each item on a scale of 1-5. - Communication with management',
 'How satisfied are you with the following aspects of building management? Please rate each item on a scale of 1-5. - Response time to maintenance requests',
 'How satisfied are you with the following aspects of building management? Please rate each item on a scale of 1-5. - Quality of maintenance and repairs',
 'How satisfied are you with the following aspects of building management? Please rate each item on a scale of 1-5. - Availability of virtual tours and leasing information',
 'How satisfied are you with the following aspects of building management? Please rate each item on a scale of 1-5. - Friendliness and professionalism of staff',
 'How satisfied are you with the following aspects of building management? Please rate each item on a scale of 1-5. - Availability of digital portals for rent payment and service requests',
 'How satisfied are you with the following aspects of building management? Please rate each item on a scale of 1-5. - Community events and engagement initiatives',
 'How satisfied are you with the following aspects of building management? Please rate each item on a scale of 1-5. - Overall management of the property',
 'Please describe any specific suggestions you have for how apartment buildings or building management can better meet your needs.',
 'How do you identify in terms of gender?',
 'Which of the following best describes your ethnic group?']]





Neighborhood_amenity_list = ['Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Bars and nightlife venues (e.g., live music halls)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Bike lanes and bike-friendly streets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Childcare',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Coffee shops',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Doctors’ offices',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Farmer’s markets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Fitness centers and gyms',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Green space/nature',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Grocery stores',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Libraries',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Pet-friendly areas (e.g., dog parks)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Public transportation access',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Restaurants',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Shopping options',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)',

 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Bars and nightlife venues (e.g., live music halls)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Bike lanes and bike-friendly streets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Childcare',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Coffee shops',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Doctors’ offices',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Farmer’s markets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Fitness centers and gyms',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Green space/nature',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Grocery stores',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Libraries',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Pet-friendly areas (e.g., dog parks)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Public transportation access',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Restaurants',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Shopping options',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)']

dq[neighborhood_amenity_importance]

Importance_Neighborhood = pd.DataFrame()

# Iterate through each column in the dataframe
for column in dq[neighborhood_amenity_importance].columns:

    # Get the value counts for the column
    counts = dq[neighborhood_amenity_importance][column].value_counts()

    # Add the counts to the new dataframe
    Importance_Neighborhood[column] = counts

Importance_Neighborhood.head()

Importance_Neighborhood.to_excel("/content/Importance_Neighborhood.xlsx")



"""# Shared"""

shared_amentiy_importance = ['How important is it for you to have access to this shared amenity? - Access to food or beverages (e.g., vending machines, coffee bar, snack stations)',
 'How important is it for you to have access to this shared amenity? - Bicycle storage and repair station',
 'How important is it for you to have access to this shared amenity? - Community lounge or clubhouse',
 'How important is it for you to have access to this shared amenity? - Controlled access and security features (e.g., cameras, key fobs)',
 'How important is it for you to have access to this shared amenity? - Concierge or front desk services',
 'How important is it for you to have access to this shared amenity? - Coworking space',
 'How important is it for you to have access to this shared amenity? - Dog park/run',
 'How important is it for you to have access to this shared amenity? - Entertainment space (e.g., movie theater)',
 'How important is it for you to have access to this shared amenity? - EV charging stations',
 'How important is it for you to have access to this shared amenity? - Fitness center/gym',
 'How important is it for you to have access to this shared amenity? - Game or recreation room (e.g., billiards, ping-pong, golf simulators)',
 'How important is it for you to have access to this shared amenity? - High-speed internet in common areas',
 'How important is it for you to have access to this shared amenity? - Indoor or outdoor children’s play area',
 'How important is it for you to have access to this shared amenity? - On-site parking – dedicated parking spot',
 'How important is it for you to have access to this shared amenity? - On-site parking – gated/secure parking',
 'How important is it for you to have access to this shared amenity? - On-site parking – covered parking',
 'How important is it for you to have access to this shared amenity? - Outdoor grilling and picnic areas',
 'How important is it for you to have access to this shared amenity? - Package delivery and mailroom services',
 'How important is it for you to have access to this shared amenity? - Pet washing station',
 'How important is it for you to have access to this shared amenity? - Resident events and activities',
 'How important is it for you to have access to this shared amenity? - Rooftop deck or terrace',
 'How important is it for you to have access to this shared amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'How important is it for you to have access to this shared amenity? - Shared community resources/items (e.g., rentable printers, vacuum cleaners, tool kits, electric scooters)',
 'How important is it for you to have access to this shared amenity? - Shared garden or green space',
 'How important is it for you to have access to this shared amenity? - Shared laundry facilities',
 'How important is it for you to have access to this shared amenity? - Spa/sauna or wellness center',
 'How important is it for you to have access to this shared amenity? - Swimming pool',
 'How important is it for you to have access to this shared amenity? - Valet trash service']

Shared_amenity_list = ['Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Access to food or beverages (e.g., vending machines, coffee bar, snack stations)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Bicycle storage and repair station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Community lounge or clubhouse',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Controlled access and security features (e.g., cameras, key fobs)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Concierge or front desk services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Coworking space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Dog park/run',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Entertainment space (e.g., movie theater)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - EV charging stations',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Fitness center/gym',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Game or recreation room (e.g., billiards, ping-pong, golf simulators)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - High-speed internet in common areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Indoor or outdoor children’s play area',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - On-site parking – dedicated parking spot',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - On-site parking – gated/secure parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - On-site parking – covered parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Outdoor grilling and picnic areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Package delivery and mailroom services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Pet washing station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Resident events and activities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Rooftop deck or terrace',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Shared community resources/items (e.g., rentable printers, vacuum cleaners, tool kits, electric scooters)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Shared garden or green space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Shared laundry facilities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Spa/sauna or wellness center',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Swimming pool',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Valet trash service',

 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Access to food or beverages (e.g., vending machines, coffee bar, snack stations)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Bicycle storage and repair station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Community lounge or clubhouse',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Controlled access and security features (e.g., cameras, key fobs)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Concierge or front desk services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Coworking space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Dog park/run',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Entertainment space (e.g., movie theater)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - EV charging stations',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Fitness center/gym',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Game or recreation room (e.g., billiards, ping-pong, golf simulators)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - High-speed internet in common areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Indoor or outdoor children’s play area',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - On-site parking – dedicated parking spot',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - On-site parking – gated/secure parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - On-site parking – covered parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Outdoor grilling and picnic areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Package delivery and mailroom services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Pet washing station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Resident events and activities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Rooftop deck or terrace',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Shared community resources/items (e.g., rentable printers, vacuum cleaners, tool kits, electric scooters)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Shared garden or green space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Shared laundry facilities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Spa/sauna or wellness center',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Swimming pool',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Valet trash service']

dq[shared_amenity_importance]

Importance_Shared = pd.DataFrame()

# Iterate through each column in the dataframe
for column in dq[shared_amenity_importance].columns:

    # Get the value counts for the column
    counts = dq[shared_amenity_importance][column].value_counts()

    # Add the counts to the new dataframe
    Importance_Shared[column] = counts

Importance_shared.to_excel("/content/Importance_Shared.xlsx")

"""# In_Unit"""

Inunit_amenity_importance = ['How important is it for you to have access to this in-unit amenity? - Adequate storage space (e.g., closets, cabinets, built-ins)',
 'How important is it for you to have access to this in-unit amenity? - Central Air Conditioning + Heating',
 'How important is it for you to have access to this in-unit amenity? - Energy-efficient features (e.g., LED lighting, energy-efficient appliances)',
 'How important is it for you to have access to this in-unit amenity? - Enhanced security systems (e.g., cameras, alarms)',
 'How important is it for you to have access to this in-unit amenity? - High-end bathroom features (e.g., spa-like bathrooms, rain showers)',
 'How important is it for you to have access to this in-unit amenity? - High Quality Appliances',
 'How important is it for you to have access to this in-unit amenity? - In-unit laundry',
 'How important is it for you to have access to this in-unit amenity? - Large windows and natural lighting',
 'How important is it for you to have access to this in-unit amenity? - Modern finishes (e.g., hardwood floors, granite countertops)',
 'How important is it for you to have access to this in-unit amenity? - Office or dedicated workspace',
 'How important is it for you to have access to this in-unit amenity? - Private balconies or patios',
 'How important is it for you to have access to this in-unit amenity? - Provided high speed internet',
 'How important is it for you to have access to this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'How important is it for you to have access to this in-unit amenity? - Secure access (e.g., smart locks, keyless entry)',
 'How important is it for you to have access to this in-unit amenity? - Smart home features (e.g., smart thermostat, smart lights)',
 'How important is it for you to have access to this in-unit amenity? - Spacious Layouts (e.g., open floor plans, large rooms)']

Inunit_amenity_list = [ 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Adequate storage space (e.g., closets, cabinets, built-ins)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Central Air Conditioning + Heating',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Energy-efficient features (e.g., LED lighting, energy-efficient appliances)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Enhanced security systems (e.g., cameras, alarms)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - High-end bathroom features (e.g., spa-like bathrooms, rain showers)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - High Quality Appliances',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - In-unit laundry',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Large windows and natural lighting',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Modern finishes (e.g., hardwood floors, granite countertops)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Office or dedicated workspace',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Private balconies or patios',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Provided high speed internet',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Secure access (e.g., smart locks, keyless entry)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Smart home features (e.g., smart thermostat, smart lights)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Spacious Layouts (e.g., open floor plans, large rooms)',


 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Adequate storage space (e.g., closets, cabinets, built-ins)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Central Air Conditioning + Heating',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Energy-efficient features (e.g., LED lighting, energy-efficient appliances)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Enhanced security systems (e.g., cameras, alarms)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - High-end bathroom features (e.g., spa-like bathrooms, rain showers)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - High Quality Appliances',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - In-unit laundry',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Large windows and natural lighting',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Modern finishes (e.g., hardwood floors, granite countertops)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Office or dedicated workspace',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Private balconies or patios',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Provided high speed internet',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Secure access (e.g., smart locks, keyless entry)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Smart home features (e.g., smart thermostat, smart lights)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Spacious Layouts (e.g., open floor plans, large rooms)',
]

dq[Inunit_amenity_importance]

Importance_Inunit = pd.DataFrame()

# Iterate through each column in the dataframe
for column in dq[Inunit_amenity_importance].columns:

    # Get the value counts for the column
    counts = dq[Inunit_amenity_importance][column].value_counts()

    # Add the counts to the new dataframe
    Importance_Inunit[column] = counts

Importance_Inunit.to_excel("/content/Importance_Inunit.xlsx")







"""# **Kano_Overall_Neighborhood**

Functional
"""

Func_OV_N= dq[['Response ID',
               'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Bars and nightlife venues (e.g., live music halls)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Bike lanes and bike-friendly streets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Childcare',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Coffee shops',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Doctors’ offices',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Farmer’s markets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Fitness centers and gyms',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Green space/nature',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Grocery stores',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Libraries',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Pet-friendly areas (e.g., dog parks)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Public transportation access',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Restaurants',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Shopping options',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)',
               ]]

new_columns = Func_OV_N.columns.str.replace('Please answer the following questions regarding neighborhood assets near where you live. - ', '')
Func_OV_N.columns = new_columns

Func_OV_N.head()

Func_OV_N.info()

Func_OV_N.to_excel("/content/Func_OV_N.xlsx")

"""Dysfunctional"""

Dysfunc_OV_N = dq[['Response ID',
                   'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Bars and nightlife venues (e.g., live music halls)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Bike lanes and bike-friendly streets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Childcare',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Coffee shops',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Doctors’ offices',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Farmer’s markets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Fitness centers and gyms',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Green space/nature',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Grocery stores',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Libraries',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Pet-friendly areas (e.g., dog parks)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Public transportation access',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Restaurants',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Shopping options',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)',
                   ]]

new_columns = Dysfunc_OV_N.columns.str.replace('Please answer the following questions regarding neighborhood assets near where you live. - ', '')
Dysfunc_OV_N.columns = new_columns

Dysfunc_OV_N.info()

Dysfunc_OV_N.to_excel("/content/Dysunc_OV_N.xlsx")

"""Importance"""

Imp_OV_N =dq[['Response ID',
'How important is it for you to have access to this neighborhood asset? - Bars and nightlife venues (e.g., live music halls)',
 'How important is it for you to have access to this neighborhood asset? - Bike lanes and bike-friendly streets',
 'How important is it for you to have access to this neighborhood asset? - Childcare',
 'How important is it for you to have access to this neighborhood asset? - Coffee shops',
 'How important is it for you to have access to this neighborhood asset? - Doctors’ offices',
 'How important is it for you to have access to this neighborhood asset? - Farmer’s markets',
 'How important is it for you to have access to this neighborhood asset? - Fitness centers and gyms',
 'How important is it for you to have access to this neighborhood asset? - Green space/nature',
 'How important is it for you to have access to this neighborhood asset? - Grocery stores',
 'How important is it for you to have access to this neighborhood asset? - Libraries',
 'How important is it for you to have access to this neighborhood asset? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'How important is it for you to have access to this neighborhood asset? - Pet-friendly areas (e.g., dog parks)',
 'How important is it for you to have access to this neighborhood asset? - Public transportation access',
 'How important is it for you to have access to this neighborhood asset? - Restaurants',
 'How important is it for you to have access to this neighborhood asset? - Shopping options',
 'How important is it for you to have access to this neighborhood asset? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)']]

Imp_OV_N.head()

Imp_OV_N.info()

Imp_OV_N.to_excel("/content/Importacne_OV_N.xlsx")

Neighborhood_Overall = pd.merge(pd.merge(Func_OV_N, Dysfunc_OV_N, on='Response ID', how='inner'), Imp_OV_N, on='Response ID', how='inner')

Neighborhood_Overall.info()

Neighborhood_Overall.head()

Neighborhood_Overall.to_excel("/content/Neighborhood_Overall.xlsx")

Kano_N_OV = pd.read_excel("/content/Kano_Neighborhood_Overall.xlsx",sheet_name="Kano_Result",skiprows=1)

Kano_N_OV["Neighborhood_Codes"] = ['N_C' + str(i + 1) for i in range(len(Kano_N_OV))]

Kano_N_OV.head()

Kano_N_OV.info()

pip install adjustText

from adjustText import adjust_text
# Set up the figure with a larger size

# Define a color map for your categories using hex codes or RGB values
category_colors = {
    'Attractive': '#1f77b4',  # Blue
    'Indifferent': '#ff7f0e',  # Orange
    'Performance': '#2ca02c',  # Green
    'Must-Have': '#d62728',  # Red
}




fig, ax = plt.subplots(figsize=(16, 8))  # Change fig size here (width, height)
# Create a scatter plot with Seaborn
sns.scatterplot(
    x=Kano_N_OV['Dysfunctional (X)'],
    y=Kano_N_OV['Functional (Y)'],
    hue=Kano_N_OV['Category'],  # Define column for legend (color)
    palette=category_colors,    # Apply the custom color palette
    size=Kano_N_OV['Importance (Z)'],     # Define column for point sizes
    sizes=(50, 200), # Set the range of marker sizes
    ax= ax  # Add the scatter plot to the axis
)

# Set x and y axis limits
ax.set_xlim(1, 2.5)   # Set x-axis limits from 0 to 6
ax.set_ylim(1, 2.5)  # Set y-axis limits from 4 to 10


# Add a title to the plot
ax.set_title('Kano Analysis for Neighborhood Amenities_Overall', fontsize=16)

# Add labels to the x and y axes
ax.set_xlabel('Dysfunctional (X)', fontsize=14)
ax.set_ylabel('Functional (Y)', fontsize=14)

# Move the legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)


# Add labels to each point with an offset
texts = []
for i in range(Kano_N_OV.shape[0]):
    texts.append(
      ax.text(
        Kano_N_OV['Dysfunctional (X)'][i],  # Offset X position by 0.1 units to the right
        Kano_N_OV['Functional (Y)'][i],  # Offset Y position by 0.1 units upwards
         Kano_N_OV['Neighborhood_Codes'][i],    # Label points with values from the 'Labels' column
        fontsize=10,          # Adjust font size of the labels
        ha='center',          # Center align the text
        va='bottom'           # Align text to the bottom to avoid overlap with the point
      )
    )

# Automatically adjust text to avoid overlap
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

# Display the plot
plt.tight_layout()
plt.show()

"""# **Kano_Overall_Shared**"""



"""Functional"""

Func_OV_SH= dq[['Response ID',
                'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Access to food or beverages (e.g., vending machines, coffee bar, snack stations)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Bicycle storage and repair station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Community lounge or clubhouse',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Controlled access and security features (e.g., cameras, key fobs)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Concierge or front desk services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Coworking space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Dog park/run',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Entertainment space (e.g., movie theater)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - EV charging stations',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Fitness center/gym',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Game or recreation room (e.g., billiards, ping-pong, golf simulators)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - High-speed internet in common areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Indoor or outdoor children’s play area',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - On-site parking – dedicated parking spot',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - On-site parking – gated/secure parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - On-site parking – covered parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Outdoor grilling and picnic areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Package delivery and mailroom services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Pet washing station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Resident events and activities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Rooftop deck or terrace',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Shared community resources/items (e.g., rentable printers, vacuum cleaners, tool kits, electric scooters)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Shared garden or green space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Shared laundry facilities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Spa/sauna or wellness center',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Swimming pool',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Valet trash service']]

new_columns = Func_OV_SH.columns.str.replace('Please answer the following questions regarding shared amenities in your apartment building/prope... - ', '')
Func_OV_SH.columns = new_columns

Func_OV_SH.head()

"""Dysfunctional"""

Dysfunc_OV_SH = dq[['Response ID',
                    'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Access to food or beverages (e.g., vending machines, coffee bar, snack stations)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Bicycle storage and repair station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Community lounge or clubhouse',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Controlled access and security features (e.g., cameras, key fobs)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Concierge or front desk services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Coworking space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Dog park/run',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Entertainment space (e.g., movie theater)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - EV charging stations',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Fitness center/gym',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Game or recreation room (e.g., billiards, ping-pong, golf simulators)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - High-speed internet in common areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Indoor or outdoor children’s play area',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - On-site parking – dedicated parking spot',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - On-site parking – gated/secure parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - On-site parking – covered parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Outdoor grilling and picnic areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Package delivery and mailroom services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Pet washing station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Resident events and activities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Rooftop deck or terrace',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Shared community resources/items (e.g., rentable printers, vacuum cleaners, tool kits, electric scooters)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Shared garden or green space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Shared laundry facilities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Spa/sauna or wellness center',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Swimming pool',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Valet trash service']]

new_columns = Dysfunc_OV_SH.columns.str.replace('Please answer the following questions regarding shared amenities in your apartment building/prope... - ', '')
Dysfunc_OV_SH.columns = new_columns

"""Importance"""

Imp_OV_SH =dq[['Response ID',
               'How important is it for you to have access to this shared amenity? - Access to food or beverages (e.g., vending machines, coffee bar, snack stations)',
 'How important is it for you to have access to this shared amenity? - Bicycle storage and repair station',
 'How important is it for you to have access to this shared amenity? - Community lounge or clubhouse',
 'How important is it for you to have access to this shared amenity? - Controlled access and security features (e.g., cameras, key fobs)',
 'How important is it for you to have access to this shared amenity? - Concierge or front desk services',
 'How important is it for you to have access to this shared amenity? - Coworking space',
 'How important is it for you to have access to this shared amenity? - Dog park/run',
 'How important is it for you to have access to this shared amenity? - Entertainment space (e.g., movie theater)',
 'How important is it for you to have access to this shared amenity? - EV charging stations',
 'How important is it for you to have access to this shared amenity? - Fitness center/gym',
 'How important is it for you to have access to this shared amenity? - Game or recreation room (e.g., billiards, ping-pong, golf simulators)',
 'How important is it for you to have access to this shared amenity? - High-speed internet in common areas',
 'How important is it for you to have access to this shared amenity? - Indoor or outdoor children’s play area',
 'How important is it for you to have access to this shared amenity? - On-site parking – dedicated parking spot',
 'How important is it for you to have access to this shared amenity? - On-site parking – gated/secure parking',
 'How important is it for you to have access to this shared amenity? - On-site parking – covered parking',
 'How important is it for you to have access to this shared amenity? - Outdoor grilling and picnic areas',
 'How important is it for you to have access to this shared amenity? - Package delivery and mailroom services',
 'How important is it for you to have access to this shared amenity? - Pet washing station',
 'How important is it for you to have access to this shared amenity? - Resident events and activities',
 'How important is it for you to have access to this shared amenity? - Rooftop deck or terrace',
 'How important is it for you to have access to this shared amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'How important is it for you to have access to this shared amenity? - Shared community resources/items (e.g., rentable printers, vacuum cleaners, tool kits, electric scooters)',
 'How important is it for you to have access to this shared amenity? - Shared garden or green space',
 'How important is it for you to have access to this shared amenity? - Shared laundry facilities',
 'How important is it for you to have access to this shared amenity? - Spa/sauna or wellness center',
 'How important is it for you to have access to this shared amenity? - Swimming pool',
 'How important is it for you to have access to this shared amenity? - Valet trash service']]

Shared_Overall = pd.merge(pd.merge(Func_OV_SH, Dysfunc_OV_SH, on='Response ID', how='inner'), Imp_OV_SH, on='Response ID', how='inner')

Shared_Overall.to_excel("/content/Shared_Overall.xlsx")





Kano_SH_OV = pd.read_excel("/content/Kano_Shared_Overall .xlsx",sheet_name="Kano_Result",skiprows=1)

Kano_SH_OV["Shared_Codes"] = ['SH_C' + str(i + 1) for i in range(len(Kano_SH_OV))]

Kano_SH_OV.head()

from adjustText import adjust_text
# Set up the figure with a larger size

# Define a color map for your categories using hex codes or RGB values
category_colors = {
    'Attractive': '#1f77b4',  # Blue
    'Indifferent': '#ff7f0e',  # Orange
    'Performance': '#2ca02c',  # Green
    'Must-Have': '#d62728',  # Red
}




fig, ax = plt.subplots(figsize=(16, 8))  # Change fig size here (width, height)
# Create a scatter plot with Seaborn
sns.scatterplot(
    x=Kano_SH_OV['Dysfunctional (X)'],
    y=Kano_SH_OV['Functional (Y)'],
    hue=Kano_SH_OV['Category'],  # Define column for legend (color)
    palette=category_colors,    # Apply the custom color palette
    size=Kano_SH_OV['Importance (Z)'],     # Define column for point sizes
    sizes=(50, 200), # Set the range of marker sizes
    ax= ax  # Add the scatter plot to the axis
)

# Set x and y axis limits
ax.set_xlim(1, 2.5)   # Set x-axis limits from 0 to 6
ax.set_ylim(1, 2.5)  # Set y-axis limits from 4 to 10


# Add a title to the plot
ax.set_title('Kano Analysis for Shared Amenities_Overall', fontsize=16)

# Add labels to the x and y axes
ax.set_xlabel('Dysfunctional (X)', fontsize=14)
ax.set_ylabel('Functional (Y)', fontsize=14)

# Move the legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)


# Add labels to each point with an offset
texts = []
for i in range(Kano_SH_OV.shape[0]):
    texts.append(
      ax.text(
        Kano_SH_OV['Dysfunctional (X)'][i],  # Offset X position by 0.1 units to the right
        Kano_SH_OV['Functional (Y)'][i],  # Offset Y position by 0.1 units upwards
        Kano_SH_OV['Shared_Codes'][i],    # Label points with values from the 'Labels' column
        fontsize=10,          # Adjust font size of the labels
        ha='center',          # Center align the text
        va='bottom'           # Align text to the bottom to avoid overlap with the point
      )
    )

# Automatically adjust text to avoid overlap
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

# Display the plot
plt.tight_layout()
plt.show()

"""# **Kano_Overall_InUnit**"""



"""Functional"""

Func_OV_IU= dq[['Response ID',
                'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Adequate storage space (e.g., closets, cabinets, built-ins)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Central Air Conditioning + Heating',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Energy-efficient features (e.g., LED lighting, energy-efficient appliances)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Enhanced security systems (e.g., cameras, alarms)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - High-end bathroom features (e.g., spa-like bathrooms, rain showers)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - High Quality Appliances',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - In-unit laundry',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Large windows and natural lighting',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Modern finishes (e.g., hardwood floors, granite countertops)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Office or dedicated workspace',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Private balconies or patios',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Provided high speed internet',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Secure access (e.g., smart locks, keyless entry)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Smart home features (e.g., smart thermostat, smart lights)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Spacious Layouts (e.g., open floor plans, large rooms)']]

new_columns = Func_OV_IU.columns.str.replace('Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - ', '')
Func_OV_IU.columns = new_columns

Func_OV_IU.head()

"""Dysfunctional"""

Dysfunc_OV_IU = dq[['Response ID',
                    'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Adequate storage space (e.g., closets, cabinets, built-ins)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Central Air Conditioning + Heating',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Energy-efficient features (e.g., LED lighting, energy-efficient appliances)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Enhanced security systems (e.g., cameras, alarms)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - High-end bathroom features (e.g., spa-like bathrooms, rain showers)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - High Quality Appliances',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - In-unit laundry',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Large windows and natural lighting',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Modern finishes (e.g., hardwood floors, granite countertops)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Office or dedicated workspace',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Private balconies or patios',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Provided high speed internet',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Secure access (e.g., smart locks, keyless entry)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Smart home features (e.g., smart thermostat, smart lights)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Spacious Layouts (e.g., open floor plans, large rooms)']]

new_columns = Dysfunc_OV_IU.columns.str.replace('Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - ', '')
Dysfunc_OV_IU.columns = new_columns

"""Importance"""

Imp_OV_IU =dq[['Response ID',
               'How important is it for you to have access to this in-unit amenity? - Adequate storage space (e.g., closets, cabinets, built-ins)',
 'How important is it for you to have access to this in-unit amenity? - Central Air Conditioning + Heating',
 'How important is it for you to have access to this in-unit amenity? - Energy-efficient features (e.g., LED lighting, energy-efficient appliances)',
 'How important is it for you to have access to this in-unit amenity? - Enhanced security systems (e.g., cameras, alarms)',
 'How important is it for you to have access to this in-unit amenity? - High-end bathroom features (e.g., spa-like bathrooms, rain showers)',
 'How important is it for you to have access to this in-unit amenity? - High Quality Appliances',
 'How important is it for you to have access to this in-unit amenity? - In-unit laundry',
 'How important is it for you to have access to this in-unit amenity? - Large windows and natural lighting',
 'How important is it for you to have access to this in-unit amenity? - Modern finishes (e.g., hardwood floors, granite countertops)',
 'How important is it for you to have access to this in-unit amenity? - Office or dedicated workspace',
 'How important is it for you to have access to this in-unit amenity? - Private balconies or patios',
 'How important is it for you to have access to this in-unit amenity? - Provided high speed internet',
 'How important is it for you to have access to this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'How important is it for you to have access to this in-unit amenity? - Secure access (e.g., smart locks, keyless entry)',
 'How important is it for you to have access to this in-unit amenity? - Smart home features (e.g., smart thermostat, smart lights)',
 'How important is it for you to have access to this in-unit amenity? - Spacious Layouts (e.g., open floor plans, large rooms)']]



Inunit_Overall = pd.merge(pd.merge(Func_OV_IU, Dysfunc_OV_IU, on='Response ID', how='inner'), Imp_OV_IU, on='Response ID', how='inner')

Inunit_Overall.to_excel("/content/Inunit_Overall.xlsx")





Kano_IU_OV = pd.read_excel("/content/Kano_Inunit_Overall.xlsx",sheet_name="Kano_Result",skiprows=1)

Kano_IU_OV["Inunit_Codes"] = ['IU_C' + str(i + 1) for i in range(len(Kano_IU_OV))]

Kano_IU_OV.head()

from adjustText import adjust_text
# Set up the figure with a larger size

# Define a color map for your categories using hex codes or RGB values
category_colors = {
    'Attractive': '#1f77b4',  # Blue
    'Indifferent': '#ff7f0e',  # Orange
    'Performance': '#2ca02c',  # Green
    'Must-Have': '#d62728',  # Red
}




fig, ax = plt.subplots(figsize=(16, 8))  # Change fig size here (width, height)
# Create a scatter plot with Seaborn
sns.scatterplot(
    x=Kano_IU_OV['Dysfunctional (X)'],
    y=Kano_IU_OV['Functional (Y)'],
    hue=Kano_IU_OV['Category'],  # Define column for legend (color)
    palette=category_colors,    # Apply the custom color palette
    size=Kano_IU_OV['Importance (Z)'],     # Define column for point sizes
    sizes=(50, 200), # Set the range of marker sizes
    ax= ax  # Add the scatter plot to the axis
)

# Set x and y axis limits
ax.set_xlim(1, 2.5)   # Set x-axis limits from 0 to 6
ax.set_ylim(1, 2.5)  # Set y-axis limits from 4 to 10


# Add a title to the plot
ax.set_title('Kano Analysis for In unit Amenities_Overall', fontsize=16)

# Add labels to the x and y axes
ax.set_xlabel('Dysfunctional (X)', fontsize=14)
ax.set_ylabel('Functional (Y)', fontsize=14)

# Move the legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)


# Add labels to each point with an offset
texts = []
for i in range(Kano_IU_OV.shape[0]):
    texts.append(
      ax.text(
        Kano_IU_OV['Dysfunctional (X)'][i],  # Offset X position by 0.1 units to the right
        Kano_IU_OV['Functional (Y)'][i],  # Offset Y position by 0.1 units upwards
        Kano_IU_OV['Inunit_Codes'][i],    # Label points with values from the 'Labels' column
        fontsize=10,          # Adjust font size of the labels
        ha='center',          # Center align the text
        va='bottom'           # Align text to the bottom to avoid overlap with the point
      )
    )

# Automatically adjust text to avoid overlap
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

# Display the plot
plt.tight_layout()
plt.show()

"""# **Kano_Age_Neighborhood**"""

dq["Please select your age range:"].unique()

dq.info()



"""Functional"""

Func_Age1_N= dq[['Response ID',
                 "Please select your age range:",
               'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Bars and nightlife venues (e.g., live music halls)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Bike lanes and bike-friendly streets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Childcare',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Coffee shops',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Doctors’ offices',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Farmer’s markets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Fitness centers and gyms',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Green space/nature',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Grocery stores',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Libraries',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Pet-friendly areas (e.g., dog parks)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Public transportation access',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Restaurants',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Shopping options',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)',
               ]]

new_columns = Func_Age1_N.columns.str.replace('Please answer the following questions regarding neighborhood assets near where you live. - ', '')
Func_Age1_N.columns = new_columns

Func_Age1_N.head()

"""Dysfunctional"""

Dysfunc_Age1_N = dq[['Response ID',
                     "Please select your age range:",
                   'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Bars and nightlife venues (e.g., live music halls)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Bike lanes and bike-friendly streets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Childcare',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Coffee shops',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Doctors’ offices',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Farmer’s markets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Fitness centers and gyms',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Green space/nature',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Grocery stores',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Libraries',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Pet-friendly areas (e.g., dog parks)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Public transportation access',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Restaurants',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Shopping options',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)',
                   ]]

new_columns = Dysfunc_Age1_N.columns.str.replace('Please answer the following questions regarding neighborhood assets near where you live. - ', '')
Dysfunc_Age1_N.columns = new_columns

Imp_Age1_N =dq[['Response ID',
                "Please select your age range:",
'How important is it for you to have access to this neighborhood asset? - Bars and nightlife venues (e.g., live music halls)',
 'How important is it for you to have access to this neighborhood asset? - Bike lanes and bike-friendly streets',
 'How important is it for you to have access to this neighborhood asset? - Childcare',
 'How important is it for you to have access to this neighborhood asset? - Coffee shops',
 'How important is it for you to have access to this neighborhood asset? - Doctors’ offices',
 'How important is it for you to have access to this neighborhood asset? - Farmer’s markets',
 'How important is it for you to have access to this neighborhood asset? - Fitness centers and gyms',
 'How important is it for you to have access to this neighborhood asset? - Green space/nature',
 'How important is it for you to have access to this neighborhood asset? - Grocery stores',
 'How important is it for you to have access to this neighborhood asset? - Libraries',
 'How important is it for you to have access to this neighborhood asset? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'How important is it for you to have access to this neighborhood asset? - Pet-friendly areas (e.g., dog parks)',
 'How important is it for you to have access to this neighborhood asset? - Public transportation access',
 'How important is it for you to have access to this neighborhood asset? - Restaurants',
 'How important is it for you to have access to this neighborhood asset? - Shopping options',
 'How important is it for you to have access to this neighborhood asset? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)']]

Age_Neighborhood_Overall = pd.merge(pd.merge(Func_Age1_N, Dysfunc_Age1_N, on='Response ID', how='inner'), Imp_Age1_N, on='Response ID', how='inner')

Age_Neighborhood_Overall = Age_Neighborhood_Overall.sort_values(by=["Please select your age range:"], ascending=[True])

Age_Neighborhood_Overall.to_excel("/content/Age_Neighborhood_Overall.xlsx")



"""# Scatterplot"""

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from adjustText import adjust_text

# Directory containing the Excel files
directory = '/content/Age_Neighborhood'

# Define a color map for your categories using hex codes or RGB values
category_colors = {
    'Attractive': '#1f77b4',  # Blue
    'Indifferent': '#ff7f0e',  # Orange
    'Performance': '#2ca02c',  # Green
    'Must-Have': '#d62728',  # Red
}

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):  # Adjust the file extension if necessary
        file_path = os.path.join(directory, filename)

        # Extract the word after "__" from the filename
        #city_name = filename.split("_")[1].split(".")[0]  # Split by '__' and get the word before the '.xlsx'
        # Extract the word after the second "_" and before ".xlsx"
        parts = filename.split("_")
        if len(parts) > 2:
            city_name = parts[2].split(".")[0]  # Get the word after the second "_" and before ".xlsx"
        else:
            city_name = "Unknown"  # Default to "Unknown" if the expected pattern isn't met

        # Read each Excel file with the desired sheet and skipping rows
        df = pd.read_excel(file_path, sheet_name="Kano_Result", skiprows=1)
                # Add the 'Shared_Codes' column to each DataFrame
        df["Neighborhood_Codes"] = ['N_C' + str(i + 1) for i in range(len(df))]

        # Assign colors based on the 'Category' column
        df['Color'] = df['Category'].map(category_colors)

        # Set up the figure with a larger size
        fig, ax = plt.subplots(figsize=(20, 12))  # Change fig size here (width, height)

        # Create a scatter plot with Seaborn
        scatter = sns.scatterplot(
            x=df['Dysfunctional (X)'],
            y=df['Functional (Y)'],
            hue=df['Category'],  # Define column for legend (color)
            palette=category_colors,  # Use the custom color palette
            size=df['Importance (Z)'],  # Define column for point sizes
            sizes=(50, 200),  # Set the range of marker sizes
            ax=ax  # Add the scatter plot to the axis
        )

        # Set x and y axis limits
        ax.set_xlim(1, 4)  # Set x-axis limits
        ax.set_ylim(1, 4)  # Set y-axis limits

        # Add a title to the plot using the extracted city name
        ax.set_title(f'Kano Analysis for Neighborhood Amenities_{city_name}', fontsize=16)

        # Add labels to the x and y axes
        ax.set_xlabel('Dysfunctional (X)', fontsize=14)
        ax.set_ylabel('Functional (Y)', fontsize=14)

        # Move the legend outside the plot
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

        # Add labels to each point with an offset
        texts = []
        for i in range(df.shape[0]):
            texts.append(
              ax.text(
                df['Dysfunctional (X)'][i],  # X position
                df['Functional (Y)'][i],  # Y position
                df['Neighborhood_Codes'][i],  # Label points with 'Shared_Codes' column
                fontsize=10,  # Font size for labels
                ha='center',  # Horizontal alignment
                va='bottom'  # Vertical alignment
              )
            )

        # Automatically adjust text to avoid overlap
        adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

        # Display the plot for each file
        plt.tight_layout()
        plt.show()

"""# **Kano_Age_Shared**"""



"""Functional"""

Func_Age_SH= dq[['Response ID',
                 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Access to food or beverages (e.g., vending machines, coffee bar, snack stations)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Bicycle storage and repair station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Community lounge or clubhouse',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Controlled access and security features (e.g., cameras, key fobs)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Concierge or front desk services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Coworking space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Dog park/run',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Entertainment space (e.g., movie theater)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - EV charging stations',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Fitness center/gym',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Game or recreation room (e.g., billiards, ping-pong, golf simulators)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - High-speed internet in common areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Indoor or outdoor children’s play area',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - On-site parking – dedicated parking spot',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - On-site parking – gated/secure parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - On-site parking – covered parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Outdoor grilling and picnic areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Package delivery and mailroom services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Pet washing station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Resident events and activities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Rooftop deck or terrace',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Shared community resources/items (e.g., rentable printers, vacuum cleaners, tool kits, electric scooters)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Shared garden or green space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Shared laundry facilities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Spa/sauna or wellness center',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Swimming pool',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Valet trash service',
               'Please select your age range:']]

new_columns = Func_Age_SH.columns.str.replace('Please answer the following questions regarding shared amenities in your apartment building/prope... - ', '')
Func_Age_SH.columns = new_columns

Func_Age_SH.head()

Func_Age_SH[Func_Age_SH.isna().any(axis=1)]

Func_Age_SH=Func_Age_SH.dropna()

"""Dysfunctional"""

Dysfunc_Age_SH = dq[['Response ID',
                     'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Access to food or beverages (e.g., vending machines, coffee bar, snack stations)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Bicycle storage and repair station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Community lounge or clubhouse',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Controlled access and security features (e.g., cameras, key fobs)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Concierge or front desk services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Coworking space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Dog park/run',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Entertainment space (e.g., movie theater)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - EV charging stations',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Fitness center/gym',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Game or recreation room (e.g., billiards, ping-pong, golf simulators)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - High-speed internet in common areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Indoor or outdoor children’s play area',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - On-site parking – dedicated parking spot',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - On-site parking – gated/secure parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - On-site parking – covered parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Outdoor grilling and picnic areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Package delivery and mailroom services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Pet washing station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Resident events and activities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Rooftop deck or terrace',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Shared community resources/items (e.g., rentable printers, vacuum cleaners, tool kits, electric scooters)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Shared garden or green space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Shared laundry facilities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Spa/sauna or wellness center',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Swimming pool',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Valet trash service',
               'Please select your age range:']]

new_columns = Dysfunc_Age_SH.columns.str.replace('Please answer the following questions regarding shared amenities in your apartment building/prope... - ', '')
Dysfunc_Age_SH.columns = new_columns

Dysfunc_Age_SH.head()



Dysfunc_Age_SH[Dysfunc_Age_SH.isna().any(axis=1)]

Dysfunc_Age_SH=Dysfunc_Age_SH.dropna()

"""Importance"""

Imp_Age_SH =dq[['Response ID',
                'How important is it for you to have access to this shared amenity? - Access to food or beverages (e.g., vending machines, coffee bar, snack stations)',
 'How important is it for you to have access to this shared amenity? - Bicycle storage and repair station',
 'How important is it for you to have access to this shared amenity? - Community lounge or clubhouse',
 'How important is it for you to have access to this shared amenity? - Controlled access and security features (e.g., cameras, key fobs)',
 'How important is it for you to have access to this shared amenity? - Concierge or front desk services',
 'How important is it for you to have access to this shared amenity? - Coworking space',
 'How important is it for you to have access to this shared amenity? - Dog park/run',
 'How important is it for you to have access to this shared amenity? - Entertainment space (e.g., movie theater)',
 'How important is it for you to have access to this shared amenity? - EV charging stations',
 'How important is it for you to have access to this shared amenity? - Fitness center/gym',
 'How important is it for you to have access to this shared amenity? - Game or recreation room (e.g., billiards, ping-pong, golf simulators)',
 'How important is it for you to have access to this shared amenity? - High-speed internet in common areas',
 'How important is it for you to have access to this shared amenity? - Indoor or outdoor children’s play area',
 'How important is it for you to have access to this shared amenity? - On-site parking – dedicated parking spot',
 'How important is it for you to have access to this shared amenity? - On-site parking – gated/secure parking',
 'How important is it for you to have access to this shared amenity? - On-site parking – covered parking',
 'How important is it for you to have access to this shared amenity? - Outdoor grilling and picnic areas',
 'How important is it for you to have access to this shared amenity? - Package delivery and mailroom services',
 'How important is it for you to have access to this shared amenity? - Pet washing station',
 'How important is it for you to have access to this shared amenity? - Resident events and activities',
 'How important is it for you to have access to this shared amenity? - Rooftop deck or terrace',
 'How important is it for you to have access to this shared amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'How important is it for you to have access to this shared amenity? - Shared community resources/items (e.g., rentable printers, vacuum cleaners, tool kits, electric scooters)',
 'How important is it for you to have access to this shared amenity? - Shared garden or green space',
 'How important is it for you to have access to this shared amenity? - Shared laundry facilities',
 'How important is it for you to have access to this shared amenity? - Spa/sauna or wellness center',
 'How important is it for you to have access to this shared amenity? - Swimming pool',
 'How important is it for you to have access to this shared amenity? - Valet trash service',
            'Please select your age range:']]

Imp_Age_SH[Imp_Age_SH.isna().any(axis=1)]

Imp_Age_SH=Imp_Age_SH.dropna()



Age_Shared_Overall = pd.merge(pd.merge(Func_Age_SH, Dysfunc_Age_SH, on='Response ID', how='inner'), Imp_Age_SH, on='Response ID', how='inner')

Age_Shared_Overall = Age_Shared.sort_values(by=["Please select your age range:"], ascending=[True])

Age_Shared_Overall.to_excel("/content/Age_Shared_Overall.xlsx")







"""# Age 25-29"""



Kano_SH_AG_25 = pd.read_excel("/content/Shared/Kano_Shared__Age_25-29.xlsx",sheet_name="Kano_Result",skiprows=1)

Kano_SH_AG_25["Shared_Codes"] = ['SH_C' + str(i + 1) for i in range(len(Kano_SH_AG_25))]

Kano_SH_AG_25.head()

from adjustText import adjust_text
# Set up the figure with a larger size
fig, ax = plt.subplots(figsize=(20, 12))  # Change fig size here (width, height)
# Create a scatter plot with Seaborn
sns.scatterplot(
    x=Kano_SH_AG_25['Dysfunctional (X)'],
    y=Kano_SH_AG_25['Functional (Y)'],
    hue=Kano_SH_AG_25['Category'],  # Define column for legend (color)
    size=Kano_SH_AG_25['Importance (Z)'],     # Define column for point sizes
    sizes=(50, 200), # Set the range of marker sizes
    ax= ax  # Add the scatter plot to the axis
)

# Set x and y axis limits
ax.set_xlim(1, 3.5)   # Set x-axis limits from 0 to 6
ax.set_ylim(1, 3.5)  # Set y-axis limits from 4 to 10


# Add a title to the plot
ax.set_title('Kano Analysis for Shared Amenities_Age 25-29', fontsize=16)

# Add labels to the x and y axes
ax.set_xlabel('Dysfunctional (X)', fontsize=14)
ax.set_ylabel('Functional (Y)', fontsize=14)

# Move the legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)


# Add labels to each point with an offset
texts = []
for i in range(Kano_SH_AG_25.shape[0]):
    texts.append(
      ax.text(
        Kano_SH_AG_25['Dysfunctional (X)'][i],  # Offset X position by 0.1 units to the right
        Kano_SH_AG_25['Functional (Y)'][i],  # Offset Y position by 0.1 units upwards
        Kano_SH_AG_25['Shared_Codes'][i],    # Label points with values from the 'Labels' column
        fontsize=10,          # Adjust font size of the labels
        ha='center',          # Center align the text
        va='bottom'           # Align text to the bottom to avoid overlap with the point
      )
    )

# Automatically adjust text to avoid overlap
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

# Display the plot
plt.tight_layout()
plt.show()

"""# Age 30-34"""



Kano_SH_AG_30 = pd.read_excel("/content/Shared/Kano_Shared__Age_30-34.xlsx",sheet_name="Kano_Result",skiprows=1)

Kano_SH_AG_30["Shared_Codes"] = ['SH_C' + str(i + 1) for i in range(len(Kano_SH_AG_30))]

Kano_SH_AG_30.head()

from adjustText import adjust_text
# Set up the figure with a larger size
fig, ax = plt.subplots(figsize=(20, 12))  # Change fig size here (width, height)
# Create a scatter plot with Seaborn
sns.scatterplot(
    x=Kano_SH_AG_30['Dysfunctional (X)'],
    y=Kano_SH_AG_30['Functional (Y)'],
    hue=Kano_SH_AG_30['Category'],  # Define column for legend (color)
    size=Kano_SH_AG_30['Importance (Z)'],     # Define column for point sizes
    sizes=(50, 200), # Set the range of marker sizes
    ax= ax  # Add the scatter plot to the axis
)

# Set x and y axis limits
ax.set_xlim(1, 3.5)   # Set x-axis limits from 0 to 6
ax.set_ylim(1, 3.5)  # Set y-axis limits from 4 to 10


# Add a title to the plot
ax.set_title('Kano Analysis for Shared Amenities_Age 30-34', fontsize=16)

# Add labels to the x and y axes
ax.set_xlabel('Dysfunctional (X)', fontsize=14)
ax.set_ylabel('Functional (Y)', fontsize=14)

# Move the legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)


# Add labels to each point with an offset
texts = []
for i in range(Kano_SH_AG_30.shape[0]):
    texts.append(
      ax.text(
        Kano_SH_AG_30['Dysfunctional (X)'][i],  # Offset X position by 0.1 units to the right
        Kano_SH_AG_30['Functional (Y)'][i],  # Offset Y position by 0.1 units upwards
        Kano_SH_AG_30['Shared_Codes'][i],    # Label points with values from the 'Labels' column
        fontsize=10,          # Adjust font size of the labels
        ha='center',          # Center align the text
        va='bottom'           # Align text to the bottom to avoid overlap with the point
      )
    )

# Automatically adjust text to avoid overlap
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

# Display the plot
plt.tight_layout()
plt.show()

"""# Age 35-39"""



Kano_SH_AG_35 = pd.read_excel("/content/Shared/Kano_Shared__Age_35-39.xlsx",sheet_name="Kano_Result",skiprows=1)

Kano_SH_AG_35["Shared_Codes"] = ['SH_C' + str(i + 1) for i in range(len(Kano_SH_AG_35))]

Kano_SH_AG_35.head()

from adjustText import adjust_text
# Set up the figure with a larger size
fig, ax = plt.subplots(figsize=(20, 12))  # Change fig size here (width, height)
# Create a scatter plot with Seaborn
sns.scatterplot(
    x=Kano_SH_AG_35['Dysfunctional (X)'],
    y=Kano_SH_AG_35['Functional (Y)'],
    hue=Kano_SH_AG_35['Category'],  # Define column for legend (color)
    size=Kano_SH_AG_35['Importance (Z)'],     # Define column for point sizes
    sizes=(50, 200), # Set the range of marker sizes
    ax= ax  # Add the scatter plot to the axis
)

# Set x and y axis limits
ax.set_xlim(1, 3.5)   # Set x-axis limits from 0 to 6
ax.set_ylim(1, 3.5)  # Set y-axis limits from 4 to 10


# Add a title to the plot
ax.set_title('Kano Analysis for Shared Amenities_Age 35-39', fontsize=16)

# Add labels to the x and y axes
ax.set_xlabel('Dysfunctional (X)', fontsize=14)
ax.set_ylabel('Functional (Y)', fontsize=14)

# Move the legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)


# Add labels to each point with an offset
texts = []
for i in range(Kano_SH_AG_35.shape[0]):
    texts.append(
      ax.text(
        Kano_SH_AG_35['Dysfunctional (X)'][i],  # Offset X position by 0.1 units to the right
        Kano_SH_AG_35['Functional (Y)'][i],  # Offset Y position by 0.1 units upwards
        Kano_SH_AG_35['Shared_Codes'][i],    # Label points with values from the 'Labels' column
        fontsize=10,          # Adjust font size of the labels
        ha='center',          # Center align the text
        va='bottom'           # Align text to the bottom to avoid overlap with the point
      )
    )

# Automatically adjust text to avoid overlap
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

# Display the plot
plt.tight_layout()
plt.show()

"""# Age 40-45"""



Kano_SH_AG_40 = pd.read_excel("/content/Shared/Kano_Shared__Age_40-45.xlsx",sheet_name="Kano_Result",skiprows=1)

Kano_SH_AG_40["Shared_Codes"] = ['SH_C' + str(i + 1) for i in range(len(Kano_SH_AG_40))]

Kano_SH_AG_40.head()

from adjustText import adjust_text
# Set up the figure with a larger size
fig, ax = plt.subplots(figsize=(20, 12))  # Change fig size here (width, height)
# Create a scatter plot with Seaborn
sns.scatterplot(
    x=Kano_SH_AG_40['Dysfunctional (X)'],
    y=Kano_SH_AG_40['Functional (Y)'],
    hue=Kano_SH_AG_40['Category'],  # Define column for legend (color)
    size=Kano_SH_AG_40['Importance (Z)'],     # Define column for point sizes
    sizes=(50, 200), # Set the range of marker sizes
    ax= ax  # Add the scatter plot to the axis
)

# Set x and y axis limits
ax.set_xlim(1, 3.5)   # Set x-axis limits from 0 to 6
ax.set_ylim(1, 3.5)  # Set y-axis limits from 4 to 10


# Add a title to the plot
ax.set_title('Kano Analysis for Shared Amenities_Age 40-45', fontsize=16)

# Add labels to the x and y axes
ax.set_xlabel('Dysfunctional (X)', fontsize=14)
ax.set_ylabel('Functional (Y)', fontsize=14)

# Move the legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)


# Add labels to each point with an offset
texts = []
for i in range(Kano_SH_AG_40.shape[0]):
    texts.append(
      ax.text(
        Kano_SH_AG_40['Dysfunctional (X)'][i],  # Offset X position by 0.1 units to the right
        Kano_SH_AG_40['Functional (Y)'][i],  # Offset Y position by 0.1 units upwards
        Kano_SH_AG_40['Shared_Codes'][i],    # Label points with values from the 'Labels' column
        fontsize=10,          # Adjust font size of the labels
        ha='center',          # Center align the text
        va='bottom'           # Align text to the bottom to avoid overlap with the point
      )
    )

# Automatically adjust text to avoid overlap
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

# Display the plot
plt.tight_layout()
plt.show()

"""# **Kano_Age_InUnit**"""



"""Functional"""

Func_Age_IU= dq[['Response ID',
                 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Adequate storage space (e.g., closets, cabinets, built-ins)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Central Air Conditioning + Heating',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Energy-efficient features (e.g., LED lighting, energy-efficient appliances)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Enhanced security systems (e.g., cameras, alarms)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - High-end bathroom features (e.g., spa-like bathrooms, rain showers)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - High Quality Appliances',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - In-unit laundry',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Large windows and natural lighting',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Modern finishes (e.g., hardwood floors, granite countertops)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Office or dedicated workspace',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Private balconies or patios',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Provided high speed internet',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Secure access (e.g., smart locks, keyless entry)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Smart home features (e.g., smart thermostat, smart lights)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Spacious Layouts (e.g., open floor plans, large rooms)',
               'Please select your age range:']]

new_columns = Func_Age_IU.columns.str.replace('Please answer the following questions regarding in-unit amenities. - ', '')
Func_Age_IU.columns = new_columns

Func_Age_IU.head()

Func_Age_IU[Func_Age_IU.isna().any(axis=1)]

Func_Age_IU=Func_Age_IU.dropna()

"""Dysfunctional"""

Dysfunc_Age_IU = dq[['Response ID',
                     'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Adequate storage space (e.g., closets, cabinets, built-ins)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Central Air Conditioning + Heating',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Energy-efficient features (e.g., LED lighting, energy-efficient appliances)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Enhanced security systems (e.g., cameras, alarms)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - High-end bathroom features (e.g., spa-like bathrooms, rain showers)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - High Quality Appliances',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - In-unit laundry',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Large windows and natural lighting',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Modern finishes (e.g., hardwood floors, granite countertops)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Office or dedicated workspace',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Private balconies or patios',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Provided high speed internet',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Secure access (e.g., smart locks, keyless entry)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Smart home features (e.g., smart thermostat, smart lights)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Spacious Layouts (e.g., open floor plans, large rooms)',
               'Please select your age range:']]

new_columns = Dysfunc_Age_IU.columns.str.replace('Please answer the following questions regarding in-unit amenities. - ', '')
Dysfunc_Age_IU.columns = new_columns

Dysfunc_Age_IU.head()

Dysfunc_Age_IU[Dysfunc_Age_IU.isna().any(axis=1)]

Dysfunc_Age_IU=Dysfunc_Age_IU.dropna()

"""Importance"""

Imp_Age_IU =dq[['Response ID',
                'How important is it for you to have access to this in-unit amenity? - Adequate storage space (e.g., closets, cabinets, built-ins)',
 'How important is it for you to have access to this in-unit amenity? - Central Air Conditioning + Heating',
 'How important is it for you to have access to this in-unit amenity? - Energy-efficient features (e.g., LED lighting, energy-efficient appliances)',
 'How important is it for you to have access to this in-unit amenity? - Enhanced security systems (e.g., cameras, alarms)',
 'How important is it for you to have access to this in-unit amenity? - High-end bathroom features (e.g., spa-like bathrooms, rain showers)',
 'How important is it for you to have access to this in-unit amenity? - High Quality Appliances',
 'How important is it for you to have access to this in-unit amenity? - In-unit laundry',
 'How important is it for you to have access to this in-unit amenity? - Large windows and natural lighting',
 'How important is it for you to have access to this in-unit amenity? - Modern finishes (e.g., hardwood floors, granite countertops)',
 'How important is it for you to have access to this in-unit amenity? - Office or dedicated workspace',
 'How important is it for you to have access to this in-unit amenity? - Private balconies or patios',
 'How important is it for you to have access to this in-unit amenity? - Provided high speed internet',
 'How important is it for you to have access to this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'How important is it for you to have access to this in-unit amenity? - Secure access (e.g., smart locks, keyless entry)',
 'How important is it for you to have access to this in-unit amenity? - Smart home features (e.g., smart thermostat, smart lights)',
 'How important is it for you to have access to this in-unit amenity? - Spacious Layouts (e.g., open floor plans, large rooms)',
            'Please select your age range:']]

Imp_Age_IU[Imp_Age_IU.isna().any(axis=1)]

Imp_Age_IU=Imp_Age_IU.dropna()



Age_Inunit_Overall= pd.merge(pd.merge(Func_Age_IU, Dysfunc_Age_IU, on='Response ID', how='inner'), Imp_Age_IU, on='Response ID', how='inner')

Age_Inunit_Overall = Age_Inunit_Overall.sort_values(by=["Please select your age range:"], ascending=[True])

Age_Inunit_Overall.to_excel("/content/Age_Inunit_Overall.xlsx")







"""# Scatterplot"""

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from adjustText import adjust_text

# Directory containing the Excel files
directory = '/content/Age_Inunit'

# Define a color map for your categories using hex codes or RGB values
category_colors = {
    'Attractive': '#1f77b4',  # Blue
    'Indifferent': '#ff7f0e',  # Orange
    'Performance': '#2ca02c',  # Green
    'Must-Have': '#d62728',  # Red
}

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):  # Adjust the file extension if necessary
        file_path = os.path.join(directory, filename)

        # Extract the word after "__" from the filename
        #city_name = filename.split("_")[1].split(".")[0]  # Split by '__' and get the word before the '.xlsx'
        # Extract the word after the second "_" and before ".xlsx"
        parts = filename.split("_")
        if len(parts) > 2:
            city_name = parts[2].split(".")[0]  # Get the word after the second "_" and before ".xlsx"
        else:
            city_name = "Unknown"  # Default to "Unknown" if the expected pattern isn't met

        # Read each Excel file with the desired sheet and skipping rows
        df = pd.read_excel(file_path, sheet_name="Kano_Result", skiprows=1)
                # Add the 'Shared_Codes' column to each DataFrame
        df["Inunit_Codes"] = ['IU_C' + str(i + 1) for i in range(len(df))]

        # Assign colors based on the 'Category' column
        df['Color'] = df['Category'].map(category_colors)

        # Set up the figure with a larger size
        fig, ax = plt.subplots(figsize=(20, 12))  # Change fig size here (width, height)

        # Create a scatter plot with Seaborn
        scatter = sns.scatterplot(
            x=df['Dysfunctional (X)'],
            y=df['Functional (Y)'],
            hue=df['Category'],  # Define column for legend (color)
            palette=category_colors,  # Use the custom color palette
            size=df['Importance (Z)'],  # Define column for point sizes
            sizes=(50, 200),  # Set the range of marker sizes
            ax=ax  # Add the scatter plot to the axis
        )

        # Set x and y axis limits
        ax.set_xlim(1, 4.5)  # Set x-axis limits
        ax.set_ylim(1, 4.5)  # Set y-axis limits

        # Add a title to the plot using the extracted city name
        ax.set_title(f'Kano Analysis for In-unit Amenities_{city_name}', fontsize=16)

        # Add labels to the x and y axes
        ax.set_xlabel('Dysfunctional (X)', fontsize=14)
        ax.set_ylabel('Functional (Y)', fontsize=14)

        # Move the legend outside the plot
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

        # Add labels to each point with an offset
        texts = []
        for i in range(df.shape[0]):
            texts.append(
              ax.text(
                df['Dysfunctional (X)'][i],  # X position
                df['Functional (Y)'][i],  # Y position
                df['Inunit_Codes'][i],  # Label points with 'Shared_Codes' column
                fontsize=10,  # Font size for labels
                ha='center',  # Horizontal alignment
                va='bottom'  # Vertical alignment
              )
            )

        # Automatically adjust text to avoid overlap
        adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

        # Display the plot for each file
        plt.tight_layout()
        plt.show()

"""# **Kano_State_Neighborhood**"""



"""Functional"""

Func_CT_N= dq[['Response ID',
               'Which city do you currently live in?',
               'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Bars and nightlife venues (e.g., live music halls)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Bike lanes and bike-friendly streets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Childcare',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Coffee shops',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Doctors’ offices',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Farmer’s markets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Fitness centers and gyms',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Green space/nature',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Grocery stores',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Libraries',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Pet-friendly areas (e.g., dog parks)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Public transportation access',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Restaurants',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Shopping options',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)',
               ]]

new_columns = Func_CT_N.columns.str.replace('Please answer the following questions regarding neighborhood assets near where you live. - ', '')
Func_CT_N.columns = new_columns

Func_CT_N.head()

"""Dysfunctional"""

Dysfunc_CT_N = dq[['Response ID',
                   'Which city do you currently live in?',
                   'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Bars and nightlife venues (e.g., live music halls)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Bike lanes and bike-friendly streets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Childcare',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Coffee shops',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Doctors’ offices',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Farmer’s markets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Fitness centers and gyms',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Green space/nature',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Grocery stores',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Libraries',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Pet-friendly areas (e.g., dog parks)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Public transportation access',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Restaurants',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Shopping options',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)',
                   ]]

new_columns = Dysfunc_CT_N.columns.str.replace('Please answer the following questions regarding neighborhood assets near where you live. - ', '')
Dysfunc_CT_N.columns = new_columns

"""Importance"""

Imp_CT_N =dq[['Response ID',
              'Which city do you currently live in?',
'How important is it for you to have access to this neighborhood asset? - Bars and nightlife venues (e.g., live music halls)',
 'How important is it for you to have access to this neighborhood asset? - Bike lanes and bike-friendly streets',
 'How important is it for you to have access to this neighborhood asset? - Childcare',
 'How important is it for you to have access to this neighborhood asset? - Coffee shops',
 'How important is it for you to have access to this neighborhood asset? - Doctors’ offices',
 'How important is it for you to have access to this neighborhood asset? - Farmer’s markets',
 'How important is it for you to have access to this neighborhood asset? - Fitness centers and gyms',
 'How important is it for you to have access to this neighborhood asset? - Green space/nature',
 'How important is it for you to have access to this neighborhood asset? - Grocery stores',
 'How important is it for you to have access to this neighborhood asset? - Libraries',
 'How important is it for you to have access to this neighborhood asset? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'How important is it for you to have access to this neighborhood asset? - Pet-friendly areas (e.g., dog parks)',
 'How important is it for you to have access to this neighborhood asset? - Public transportation access',
 'How important is it for you to have access to this neighborhood asset? - Restaurants',
 'How important is it for you to have access to this neighborhood asset? - Shopping options',
 'How important is it for you to have access to this neighborhood asset? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)']]

Neighborhood_City_Overall = pd.merge(pd.merge(Func_CT_N, Dysfunc_CT_N, on='Response ID', how='inner'), Imp_CT_N, on='Response ID', how='inner')

Neighborhood_City_Overall = Neighborhood_City_Overall.sort_values(by=['Which city do you currently live in?'], ascending=[True])

Neighborhood_City_Overall.to_excel("/content/Neighborhood_City.xlsx")







"""# Scatterplot"""

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from adjustText import adjust_text

# Directory containing the Excel files
directory = '/content/City_Neighborhood'

# Define a color map for your categories using hex codes or RGB values
category_colors = {
    'Attractive': '#1f77b4',  # Blue
    'Indifferent': '#ff7f0e',  # Orange
    'Performance': '#2ca02c',  # Green
    'Must-Have': '#d62728',  # Red
}

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):  # Adjust the file extension if necessary
        file_path = os.path.join(directory, filename)

        # Extract the word after "__" from the filename
        #city_name = filename.split("_")[1].split(".")[0]  # Split by '__' and get the word before the '.xlsx'
        # Extract the word after the second "_" and before ".xlsx"
        parts = filename.split("_")
        if len(parts) > 2:
            city_name = parts[2].split(".")[0]  # Get the word after the second "_" and before ".xlsx"
        else:
            city_name = "Unknown"  # Default to "Unknown" if the expected pattern isn't met

        # Read each Excel file with the desired sheet and skipping rows
        df = pd.read_excel(file_path, sheet_name="Kano_Result", skiprows=1)
                # Add the 'Shared_Codes' column to each DataFrame
        df["Neighborhood_Codes"] = ['N_C' + str(i + 1) for i in range(len(df))]

        # Assign colors based on the 'Category' column
        df['Color'] = df['Category'].map(category_colors)

        # Set up the figure with a larger size
        fig, ax = plt.subplots(figsize=(20, 12))  # Change fig size here (width, height)

        # Create a scatter plot with Seaborn
        scatter = sns.scatterplot(
            x=df['Dysfunctional (X)'],
            y=df['Functional (Y)'],
            hue=df['Category'],  # Define column for legend (color)
            palette=category_colors,  # Use the custom color palette
            size=df['Importance (Z)'],  # Define column for point sizes
            sizes=(50, 200),  # Set the range of marker sizes
            ax=ax  # Add the scatter plot to the axis
        )

        # Set x and y axis limits
        ax.set_xlim(1, 4)  # Set x-axis limits
        ax.set_ylim(1, 4)  # Set y-axis limits

        # Add a title to the plot using the extracted city name
        ax.set_title(f'Kano Analysis for Neighborhood Amenities_{city_name}', fontsize=16)

        # Add labels to the x and y axes
        ax.set_xlabel('Dysfunctional (X)', fontsize=14)
        ax.set_ylabel('Functional (Y)', fontsize=14)

        # Move the legend outside the plot
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

        # Add labels to each point with an offset
        texts = []
        for i in range(df.shape[0]):
            texts.append(
              ax.text(
                df['Dysfunctional (X)'][i],  # X position
                df['Functional (Y)'][i],  # Y position
                df['Neighborhood_Codes'][i],  # Label points with 'Shared_Codes' column
                fontsize=10,  # Font size for labels
                ha='center',  # Horizontal alignment
                va='bottom'  # Vertical alignment
              )
            )

        # Automatically adjust text to avoid overlap
        adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

        # Display the plot for each file
        plt.tight_layout()
        plt.show()

"""# **Kano_State_Shared**"""



"""Functional"""

Func_CT_SH= dq[['Response ID',
               'Which city do you currently live in?',
                                'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Access to food or beverages (e.g., vending machines, coffee bar, snack stations)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Bicycle storage and repair station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Community lounge or clubhouse',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Controlled access and security features (e.g., cameras, key fobs)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Concierge or front desk services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Coworking space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Dog park/run',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Entertainment space (e.g., movie theater)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - EV charging stations',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Fitness center/gym',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Game or recreation room (e.g., billiards, ping-pong, golf simulators)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - High-speed internet in common areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Indoor or outdoor children’s play area',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - On-site parking – dedicated parking spot',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - On-site parking – gated/secure parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - On-site parking – covered parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Outdoor grilling and picnic areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Package delivery and mailroom services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Pet washing station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Resident events and activities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Rooftop deck or terrace',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Shared community resources/items (e.g., rentable printers, vacuum cleaners, tool kits, electric scooters)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Shared garden or green space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Shared laundry facilities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Spa/sauna or wellness center',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Swimming pool',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Valet trash service',
               ]]

new_columns = Func_CT_SH.columns.str.replace('Please answer the following questions regarding neighborhood assets near where you live. - ', '')
Func_CT_SH.columns = new_columns

Func_CT_SH.head()

"""Dysfunctional"""

Dysfunc_CT_SH = dq[['Response ID',
                   'Which city do you currently live in?',
                                     'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Access to food or beverages (e.g., vending machines, coffee bar, snack stations)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Bicycle storage and repair station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Community lounge or clubhouse',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Controlled access and security features (e.g., cameras, key fobs)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Concierge or front desk services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Coworking space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Dog park/run',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Entertainment space (e.g., movie theater)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - EV charging stations',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Fitness center/gym',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Game or recreation room (e.g., billiards, ping-pong, golf simulators)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - High-speed internet in common areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Indoor or outdoor children’s play area',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - On-site parking – dedicated parking spot',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - On-site parking – gated/secure parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - On-site parking – covered parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Outdoor grilling and picnic areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Package delivery and mailroom services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Pet washing station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Resident events and activities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Rooftop deck or terrace',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Shared community resources/items (e.g., rentable printers, vacuum cleaners, tool kits, electric scooters)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Shared garden or green space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Shared laundry facilities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Spa/sauna or wellness center',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Swimming pool',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Valet trash service',
                   ]]

new_columns = Dysfunc_CT_SH.columns.str.replace('Please answer the following questions regarding neighborhood assets near where you live. - ', '')
Dysfunc_CT_SH.columns = new_columns

"""Importance"""

Imp_CT_SH =dq[['Response ID',
               'Which city do you currently live in?',
              'How important is it for you to have access to this shared amenity? - Access to food or beverages (e.g., vending machines, coffee bar, snack stations)',
 'How important is it for you to have access to this shared amenity? - Bicycle storage and repair station',
 'How important is it for you to have access to this shared amenity? - Community lounge or clubhouse',
 'How important is it for you to have access to this shared amenity? - Controlled access and security features (e.g., cameras, key fobs)',
 'How important is it for you to have access to this shared amenity? - Concierge or front desk services',
 'How important is it for you to have access to this shared amenity? - Coworking space',
 'How important is it for you to have access to this shared amenity? - Dog park/run',
 'How important is it for you to have access to this shared amenity? - Entertainment space (e.g., movie theater)',
 'How important is it for you to have access to this shared amenity? - EV charging stations',
 'How important is it for you to have access to this shared amenity? - Fitness center/gym',
 'How important is it for you to have access to this shared amenity? - Game or recreation room (e.g., billiards, ping-pong, golf simulators)',
 'How important is it for you to have access to this shared amenity? - High-speed internet in common areas',
 'How important is it for you to have access to this shared amenity? - Indoor or outdoor children’s play area',
 'How important is it for you to have access to this shared amenity? - On-site parking – dedicated parking spot',
 'How important is it for you to have access to this shared amenity? - On-site parking – gated/secure parking',
 'How important is it for you to have access to this shared amenity? - On-site parking – covered parking',
 'How important is it for you to have access to this shared amenity? - Outdoor grilling and picnic areas',
 'How important is it for you to have access to this shared amenity? - Package delivery and mailroom services',
 'How important is it for you to have access to this shared amenity? - Pet washing station',
 'How important is it for you to have access to this shared amenity? - Resident events and activities',
 'How important is it for you to have access to this shared amenity? - Rooftop deck or terrace',
 'How important is it for you to have access to this shared amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'How important is it for you to have access to this shared amenity? - Shared community resources/items (e.g., rentable printers, vacuum cleaners, tool kits, electric scooters)',
 'How important is it for you to have access to this shared amenity? - Shared garden or green space',
 'How important is it for you to have access to this shared amenity? - Shared laundry facilities',
 'How important is it for you to have access to this shared amenity? - Spa/sauna or wellness center',
 'How important is it for you to have access to this shared amenity? - Swimming pool',
 'How important is it for you to have access to this shared amenity? - Valet trash service']]

Shared_City_Overall_Raw_data= pd.merge(pd.merge(Func_CT_SH, Dysfunc_CT_SH, on='Response ID', how='inner'), Imp_CT_SH, on='Response ID', how='inner')

Shared_City_Overall_Raw_data = Shared_City_Overall_Raw_data.sort_values(by=['Which city do you currently live in?'], ascending=[True])

Shared_City_Overall_Raw_data.to_excel("/content/Shared_City_Raw_data.xlsx")





"""# Scatterplot"""



import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from adjustText import adjust_text

# Directory containing the Excel files
directory = '/content/City_Shared'

# Define a color map for your categories using hex codes or RGB values
category_colors = {
    'Attractive': '#1f77b4',  # Blue
    'Indifferent': '#ff7f0e',  # Orange
    'Performance': '#2ca02c',  # Green
    'Must-Have': '#d62728',  # Red
}

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):  # Adjust the file extension if necessary
        file_path = os.path.join(directory, filename)

        # Extract the word after "__" from the filename
        #city_name = filename.split("_")[1].split(".")[0]  # Split by '__' and get the word before the '.xlsx'
        # Extract the word after the second "_" and before ".xlsx"
        parts = filename.split("_")
        if len(parts) > 2:
            city_name = parts[2].split(".")[0]  # Get the word after the second "_" and before ".xlsx"
        else:
            city_name = "Unknown"  # Default to "Unknown" if the expected pattern isn't met

        # Read each Excel file with the desired sheet and skipping rows
        df = pd.read_excel(file_path, sheet_name="Kano_Result", skiprows=1)
                # Add the 'Shared_Codes' column to each DataFrame
        df["Shared_Codes"] = ['SH_C' + str(i + 1) for i in range(len(df))]

        # Assign colors based on the 'Category' column
        df['Color'] = df['Category'].map(category_colors)

        # Set up the figure with a larger size
        fig, ax = plt.subplots(figsize=(20, 12))  # Change fig size here (width, height)

        # Create a scatter plot with Seaborn
        scatter = sns.scatterplot(
            x=df['Dysfunctional (X)'],
            y=df['Functional (Y)'],
            hue=df['Category'],  # Define column for legend (color)
            palette=category_colors,  # Use the custom color palette
            size=df['Importance (Z)'],  # Define column for point sizes
            sizes=(50, 200),  # Set the range of marker sizes
            ax=ax  # Add the scatter plot to the axis
        )

        # Set x and y axis limits
        ax.set_xlim(1, 4)  # Set x-axis limits
        ax.set_ylim(1, 4)  # Set y-axis limits

        # Add a title to the plot using the extracted city name
        ax.set_title(f'Kano Analysis for Shared Amenities_{city_name}', fontsize=16)

        # Add labels to the x and y axes
        ax.set_xlabel('Dysfunctional (X)', fontsize=14)
        ax.set_ylabel('Functional (Y)', fontsize=14)

        # Move the legend outside the plot
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

        # Add labels to each point with an offset
        texts = []
        for i in range(df.shape[0]):
            texts.append(
              ax.text(
                df['Dysfunctional (X)'][i],  # X position
                df['Functional (Y)'][i],  # Y position
                df['Shared_Codes'][i],  # Label points with 'Shared_Codes' column
                fontsize=10,  # Font size for labels
                ha='center',  # Horizontal alignment
                va='bottom'  # Vertical alignment
              )
            )

        # Automatically adjust text to avoid overlap
        adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

        # Display the plot for each file
        plt.tight_layout()
        plt.show()

"""# **Kano_State_InUnit**"""



"""Functional"""

Func_CT_IU= dq[['Response ID',
               'Which city do you currently live in?',
                 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Adequate storage space (e.g., closets, cabinets, built-ins)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Central Air Conditioning + Heating',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Energy-efficient features (e.g., LED lighting, energy-efficient appliances)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Enhanced security systems (e.g., cameras, alarms)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - High-end bathroom features (e.g., spa-like bathrooms, rain showers)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - High Quality Appliances',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - In-unit laundry',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Large windows and natural lighting',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Modern finishes (e.g., hardwood floors, granite countertops)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Office or dedicated workspace',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Private balconies or patios',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Provided high speed internet',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Secure access (e.g., smart locks, keyless entry)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Smart home features (e.g., smart thermostat, smart lights)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Spacious Layouts (e.g., open floor plans, large rooms)']]

new_columns = Func_CT_IU.columns.str.replace('Please answer the following questions regarding in-unit amenities. - ', '')
Func_CT_IU.columns = new_columns

Func_CT_IU.head()

Func_CT_IU[Func_CT_IU.isna().any(axis=1)]

Func_CT_IU=Func_CT_IU.dropna()

"""Dysfunctional"""

Dysfunc_CT_IU = dq[['Response ID',
               'Which city do you currently live in?',
                     'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Adequate storage space (e.g., closets, cabinets, built-ins)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Central Air Conditioning + Heating',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Energy-efficient features (e.g., LED lighting, energy-efficient appliances)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Enhanced security systems (e.g., cameras, alarms)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - High-end bathroom features (e.g., spa-like bathrooms, rain showers)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - High Quality Appliances',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - In-unit laundry',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Large windows and natural lighting',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Modern finishes (e.g., hardwood floors, granite countertops)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Office or dedicated workspace',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Private balconies or patios',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Provided high speed internet',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Secure access (e.g., smart locks, keyless entry)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Smart home features (e.g., smart thermostat, smart lights)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Spacious Layouts (e.g., open floor plans, large rooms)']]

new_columns = Dysfunc_CT_IU.columns.str.replace('Please answer the following questions regarding in-unit amenities. - ', '')
Dysfunc_CT_IU.columns = new_columns

Dysfunc_CT_IU.head()

Dysfunc_CT_IU[Dysfunc_CT_IU.isna().any(axis=1)]

Dysfunc_CT_IU=Dysfunc_CT_IU.dropna()

"""Importance"""

Imp_CT_IU =dq[['Response ID',
               'Which city do you currently live in?',
                'How important is it for you to have access to this in-unit amenity? - Adequate storage space (e.g., closets, cabinets, built-ins)',
 'How important is it for you to have access to this in-unit amenity? - Central Air Conditioning + Heating',
 'How important is it for you to have access to this in-unit amenity? - Energy-efficient features (e.g., LED lighting, energy-efficient appliances)',
 'How important is it for you to have access to this in-unit amenity? - Enhanced security systems (e.g., cameras, alarms)',
 'How important is it for you to have access to this in-unit amenity? - High-end bathroom features (e.g., spa-like bathrooms, rain showers)',
 'How important is it for you to have access to this in-unit amenity? - High Quality Appliances',
 'How important is it for you to have access to this in-unit amenity? - In-unit laundry',
 'How important is it for you to have access to this in-unit amenity? - Large windows and natural lighting',
 'How important is it for you to have access to this in-unit amenity? - Modern finishes (e.g., hardwood floors, granite countertops)',
 'How important is it for you to have access to this in-unit amenity? - Office or dedicated workspace',
 'How important is it for you to have access to this in-unit amenity? - Private balconies or patios',
 'How important is it for you to have access to this in-unit amenity? - Provided high speed internet',
 'How important is it for you to have access to this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'How important is it for you to have access to this in-unit amenity? - Secure access (e.g., smart locks, keyless entry)',
 'How important is it for you to have access to this in-unit amenity? - Smart home features (e.g., smart thermostat, smart lights)',
 'How important is it for you to have access to this in-unit amenity? - Spacious Layouts (e.g., open floor plans, large rooms)']]

Imp_CT_IU[Imp_CT_IU.isna().any(axis=1)]

Imp_CT_IU=Imp_CT_IU.dropna()

City_Inunit_Overall= pd.merge(pd.merge(Func_CT_IU, Dysfunc_CT_IU, on='Response ID', how='inner'), Imp_CT_IU, on='Response ID', how='inner')

City_Inunit_Raw_data = City_Inunit_Overall.sort_values(by=['Which city do you currently live in?'], ascending=[True])

City_Inunit_Raw_data.to_excel("/content/City_Inunit_Raw_data.xlsx")



"""# Scatterplot"""

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from adjustText import adjust_text

# Directory containing the Excel files
directory = '/content/City_In_Unit'

# Define a color map for your categories using hex codes or RGB values
category_colors = {
    'Attractive': '#1f77b4',  # Blue
    'Indifferent': '#ff7f0e',  # Orange
    'Performance': '#2ca02c',  # Green
    'Must-Have': '#d62728',  # Red
}

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):  # Adjust the file extension if necessary
        file_path = os.path.join(directory, filename)

        # Extract the word after "__" from the filename
        #city_name = filename.split("_")[1].split(".")[0]  # Split by '__' and get the word before the '.xlsx'
        # Extract the word after the second "_" and before ".xlsx"
        parts = filename.split("_")
        if len(parts) > 2:
            city_name = parts[2].split(".")[0]  # Get the word after the second "_" and before ".xlsx"
        else:
            city_name = "Unknown"  # Default to "Unknown" if the expected pattern isn't met

        # Read each Excel file with the desired sheet and skipping rows
        df = pd.read_excel(file_path, sheet_name="Kano_Result", skiprows=1)
                # Add the 'Shared_Codes' column to each DataFrame
        df["Inunit_Codes"] = ['IU_C' + str(i + 1) for i in range(len(df))]

        # Assign colors based on the 'Category' column
        df['Color'] = df['Category'].map(category_colors)

        # Set up the figure with a larger size
        fig, ax = plt.subplots(figsize=(20, 12))  # Change fig size here (width, height)

        # Create a scatter plot with Seaborn
        scatter = sns.scatterplot(
            x=df['Dysfunctional (X)'],
            y=df['Functional (Y)'],
            hue=df['Category'],  # Define column for legend (color)
            palette=category_colors,  # Use the custom color palette
            size=df['Importance (Z)'],  # Define column for point sizes
            sizes=(50, 200),  # Set the range of marker sizes
            ax=ax  # Add the scatter plot to the axis
        )

        # Set x and y axis limits
        ax.set_xlim(1, 4)  # Set x-axis limits
        ax.set_ylim(1, 4)  # Set y-axis limits

        # Add a title to the plot using the extracted city name
        ax.set_title(f'Kano Analysis for In-unit Amenities_{city_name}', fontsize=16)

        # Add labels to the x and y axes
        ax.set_xlabel('Dysfunctional (X)', fontsize=14)
        ax.set_ylabel('Functional (Y)', fontsize=14)

        # Move the legend outside the plot
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

        # Add labels to each point with an offset
        texts = []
        for i in range(df.shape[0]):
            texts.append(
              ax.text(
                df['Dysfunctional (X)'][i],  # X position
                df['Functional (Y)'][i],  # Y position
                df['Inunit_Codes'][i],  # Label points with 'Shared_Codes' column
                fontsize=10,  # Font size for labels
                ha='center',  # Horizontal alignment
                va='bottom'  # Vertical alignment
              )
            )

        # Automatically adjust text to avoid overlap
        adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

        # Display the plot for each file
        plt.tight_layout()
        plt.show()

"""# **Kano_Lease Status_Neighborhood**"""





"""Functional"""

Func_LS_N= dq[['Response ID',
               'What do you plan to do when your current lease ends? - Selected Choice',
               'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Bars and nightlife venues (e.g., live music halls)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Bike lanes and bike-friendly streets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Childcare',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Coffee shops',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Doctors’ offices',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Farmer’s markets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Fitness centers and gyms',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Green space/nature',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Grocery stores',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Libraries',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Pet-friendly areas (e.g., dog parks)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Public transportation access',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Restaurants',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Shopping options',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)',
               ]]

new_columns = Func_LS_N.columns.str.replace('Please answer the following questions regarding neighborhood assets near where you live. - ', '')
Func_LS_N.columns = new_columns

Func_LS_N.head()

"""Dysfunctional"""

Dysfunc_LS_N = dq[['Response ID',
                   'What do you plan to do when your current lease ends? - Selected Choice',
                   'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Bars and nightlife venues (e.g., live music halls)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Bike lanes and bike-friendly streets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Childcare',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Coffee shops',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Doctors’ offices',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Farmer’s markets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Fitness centers and gyms',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Green space/nature',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Grocery stores',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Libraries',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Pet-friendly areas (e.g., dog parks)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Public transportation access',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Restaurants',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Shopping options',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)',
                   ]]

new_columns_1 = Dysfunc_LS_N.columns.str.replace('Please answer the following questions regarding neighborhood assets near where you live. - ', '')
Dysfunc_LS_N.columns = new_columns_1

"""Importance"""

Imp_LS_N =dq[['Response ID',
              'What do you plan to do when your current lease ends? - Selected Choice',
'How important is it for you to have access to this neighborhood asset? - Bars and nightlife venues (e.g., live music halls)',
 'How important is it for you to have access to this neighborhood asset? - Bike lanes and bike-friendly streets',
 'How important is it for you to have access to this neighborhood asset? - Childcare',
 'How important is it for you to have access to this neighborhood asset? - Coffee shops',
 'How important is it for you to have access to this neighborhood asset? - Doctors’ offices',
 'How important is it for you to have access to this neighborhood asset? - Farmer’s markets',
 'How important is it for you to have access to this neighborhood asset? - Fitness centers and gyms',
 'How important is it for you to have access to this neighborhood asset? - Green space/nature',
 'How important is it for you to have access to this neighborhood asset? - Grocery stores',
 'How important is it for you to have access to this neighborhood asset? - Libraries',
 'How important is it for you to have access to this neighborhood asset? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'How important is it for you to have access to this neighborhood asset? - Pet-friendly areas (e.g., dog parks)',
 'How important is it for you to have access to this neighborhood asset? - Public transportation access',
 'How important is it for you to have access to this neighborhood asset? - Restaurants',
 'How important is it for you to have access to this neighborhood asset? - Shopping options',
 'How important is it for you to have access to this neighborhood asset? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)']]

Neighborhood_Lease_Overall = pd.merge(pd.merge(Func_LS_N, Dysfunc_LS_N, on='Response ID', how='inner'), Imp_LS_N, on='Response ID', how='inner')

Neighborhood_Lease_Overall = Neighborhood_Lease_Overall.sort_values(by=['What do you plan to do when your current lease ends? - Selected Choice',], ascending=[True])

Neighborhood_Lease_Overall.to_excel("/content/Neighborhood_Lease_Raw Data.xlsx")

"""# **Kano_Lease Status_Shared**

# **Kano_Lease Status_InUnit**

# **Functional_Amount of Rent**

# **Dysfunctional_Amount of Rent**

# **Kano_Living Arrangement_Neighborhood**

Hyp: people living with more occupants look for more shared amenity
"""



"""Functional"""

Func_LA_N= dq[['Response ID',
               'What best describes your current living arrangement? - Selected Choice',
               'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Bars and nightlife venues (e.g., live music halls)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Bike lanes and bike-friendly streets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Childcare',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Coffee shops',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Doctors’ offices',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Farmer’s markets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Fitness centers and gyms',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Green space/nature',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Grocery stores',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Libraries',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Pet-friendly areas (e.g., dog parks)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Public transportation access',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Restaurants',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Shopping options',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)',
               ]]

new_columns = Func_LA_N.columns.str.replace('Please answer the following questions regarding neighborhood assets near where you live. - ', '')
Func_LA_N.columns = new_columns

Func_LA_N.head()

"""Dysfunctional"""

Dysfunc_LA_N = dq[['Response ID',
                  'What best describes your current living arrangement? - Selected Choice',
                   'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Bars and nightlife venues (e.g., live music halls)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Bike lanes and bike-friendly streets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Childcare',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Coffee shops',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Doctors’ offices',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Farmer’s markets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Fitness centers and gyms',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Green space/nature',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Grocery stores',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Libraries',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Pet-friendly areas (e.g., dog parks)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Public transportation access',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Restaurants',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Shopping options',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)',
                   ]]

new_columns_1 = Dysfunc_LA_N.columns.str.replace('Please answer the following questions regarding neighborhood assets near where you live. - ', '')
Dysfunc_LA_N.columns = new_columns_1

"""Importance"""

Imp_LA_N =dq[['Response ID',
             'What best describes your current living arrangement? - Selected Choice',
'How important is it for you to have access to this neighborhood asset? - Bars and nightlife venues (e.g., live music halls)',
 'How important is it for you to have access to this neighborhood asset? - Bike lanes and bike-friendly streets',
 'How important is it for you to have access to this neighborhood asset? - Childcare',
 'How important is it for you to have access to this neighborhood asset? - Coffee shops',
 'How important is it for you to have access to this neighborhood asset? - Doctors’ offices',
 'How important is it for you to have access to this neighborhood asset? - Farmer’s markets',
 'How important is it for you to have access to this neighborhood asset? - Fitness centers and gyms',
 'How important is it for you to have access to this neighborhood asset? - Green space/nature',
 'How important is it for you to have access to this neighborhood asset? - Grocery stores',
 'How important is it for you to have access to this neighborhood asset? - Libraries',
 'How important is it for you to have access to this neighborhood asset? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'How important is it for you to have access to this neighborhood asset? - Pet-friendly areas (e.g., dog parks)',
 'How important is it for you to have access to this neighborhood asset? - Public transportation access',
 'How important is it for you to have access to this neighborhood asset? - Restaurants',
 'How important is it for you to have access to this neighborhood asset? - Shopping options',
 'How important is it for you to have access to this neighborhood asset? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)']]

Neighborhood_LivingArrangemet_Overall = pd.merge(pd.merge(Func_LA_N, Dysfunc_LA_N, on='Response ID', how='inner'), Imp_LA_N, on='Response ID', how='inner')

Neighborhood_LivingArrangemet_Overall = Neighborhood_LivingArrangemet_Overall.sort_values(by=['What best describes your current living arrangement? - Selected Choice'], ascending=[True])

Neighborhood_LivingArrangemet_Overall.to_excel("/content/Neighborhood_Living-arrangement_Raw Data.xlsx")

"""Functional"""

Func_LA_N= dq[['Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Bars and nightlife venues (e.g., live music halls)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Bike lanes and bike-friendly streets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Childcare',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Coffee shops',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Doctors’ offices',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Farmer’s markets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Fitness centers and gyms',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Green space/nature',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Grocery stores',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Libraries',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Pet-friendly areas (e.g., dog parks)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Public transportation access',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Restaurants',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Shopping options',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you have this in-unit amenity? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)',
              'What best describes your current living arrangement? - Selected Choice' ]]

new_columns = Func_LA_N.columns.str.replace('Please answer the following questions regarding neighborhood assets near where you live. - ', '')
Func_LA_N.columns = new_columns

Func_LA_N.head()

Neighborhood_Living_Arrangement_Functional = pd.DataFrame()

# Iterate through each column in the dataframe
for column in Func_LA_N.columns:

    # Get the value counts for the column
    counts = Func_LA_N.groupby('What best describes your current living arrangement? - Selected Choice')[column].value_counts()

    # Add the counts to the new dataframe
    Neighborhood_Living_Arrangement_Functional[column] = counts

"""Dysfunctional"""

Dysfunc_LA_N = dq[['Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Bars and nightlife venues (e.g., live music halls)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Bike lanes and bike-friendly streets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Childcare',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Coffee shops',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Doctors’ offices',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Farmer’s markets',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Fitness centers and gyms',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Green space/nature',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Grocery stores',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Libraries',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Pet-friendly areas (e.g., dog parks)',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Public transportation access',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Restaurants',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Shopping options',
 'Please answer the following questions regarding neighborhood assets near where you live. - How do you feel if you do not have this in-unit amenity? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)',
                   'What best describes your current living arrangement? - Selected Choice']]

new_columns = Dysfunc_LA_N.columns.str.replace('Please answer the following questions regarding neighborhood assets near where you live. - ', '')
Dysfunc_LA_N.columns = new_columns

Neighborhood_Living_Arrangement_DysFunctional = pd.DataFrame()

# Iterate through each column in the dataframe
for column in Dysfunc_LA_N.columns:

    # Get the value counts for the column
    counts = Dysfunc_LA_N.groupby('What best describes your current living arrangement? - Selected Choice')[column].value_counts()

    # Add the counts to the new dataframe
    Neighborhood_Living_Arrangement_DysFunctional[column] = counts

"""Importance"""

Imp_LA_N =dq[['How important is it for you to have access to this neighborhood asset? - Bars and nightlife venues (e.g., live music halls)',
 'How important is it for you to have access to this neighborhood asset? - Bike lanes and bike-friendly streets',
 'How important is it for you to have access to this neighborhood asset? - Childcare',
 'How important is it for you to have access to this neighborhood asset? - Coffee shops',
 'How important is it for you to have access to this neighborhood asset? - Doctors’ offices',
 'How important is it for you to have access to this neighborhood asset? - Farmer’s markets',
 'How important is it for you to have access to this neighborhood asset? - Fitness centers and gyms',
 'How important is it for you to have access to this neighborhood asset? - Green space/nature',
 'How important is it for you to have access to this neighborhood asset? - Grocery stores',
 'How important is it for you to have access to this neighborhood asset? - Libraries',
 'How important is it for you to have access to this neighborhood asset? - Outdoor trails or sports courts (e.g., tennis, pickleball, basketball)',
 'How important is it for you to have access to this neighborhood asset? - Pet-friendly areas (e.g., dog parks)',
 'How important is it for you to have access to this neighborhood asset? - Public transportation access',
 'How important is it for you to have access to this neighborhood asset? - Restaurants',
 'How important is it for you to have access to this neighborhood asset? - Shopping options',
 'How important is it for you to have access to this neighborhood asset? - Walkability and easy access to nearby assets (e.g., shops, restaurants, transportation)',
              'What best describes your current living arrangement? - Selected Choice']]

Neighborhood_Living_Arrangement_Importance = pd.DataFrame()

# Iterate through each column in the dataframe
for column in Dysfunc_LA_N.columns:

    # Get the value counts for the column
    counts = Dysfunc_LA_N.groupby('What best describes your current living arrangement? - Selected Choice')[column].value_counts()

    # Add the counts to the new dataframe
    Neighborhood_Living_Arrangement_Importance[column] = counts

# Specify the file path for the Excel file
file_path = '/content/Kano_Living_Arrangement_Neiborhood_Python_Input.xlsx'

# Write each dataframe to a different sheet in the same Excel file
with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
    Neighborhood_Living_Arrangement_Functional.to_excel(writer, sheet_name='Functional', index=True)
    Neighborhood_Living_Arrangement_DysFunctional.to_excel(writer, sheet_name='Dysfunctional', index=True)
    Neighborhood_Living_Arrangement_Importance.to_excel(writer, sheet_name='Importance', index=True)





"""# Scatterplot"""

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from adjustText import adjust_text

# Directory containing the Excel files
directory = '/content/Living Arrangement_Neighborhood'

# Define a color map for your categories using hex codes or RGB values
category_colors = {
    'Attractive': '#1f77b4',  # Blue
    'Indifferent': '#ff7f0e',  # Orange
    'Performance': '#2ca02c',  # Green
    'Must-Have': '#d62728',  # Red
}

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):  # Adjust the file extension if necessary
        file_path = os.path.join(directory, filename)

        # Extract the word after "__" from the filename
        #city_name = filename.split("_")[1].split(".")[0]  # Split by '__' and get the word before the '.xlsx'
        # Extract the word after the second "_" and before ".xlsx"
        parts = filename.split("_")
        if len(parts) > 2:
            city_name = parts[2].split(".")[0]  # Get the word after the second "_" and before ".xlsx"
        else:
            city_name = "Unknown"  # Default to "Unknown" if the expected pattern isn't met

        # Read each Excel file with the desired sheet and skipping rows
        df = pd.read_excel(file_path, sheet_name="Kano_Result", skiprows=1)
                # Add the 'Shared_Codes' column to each DataFrame
        df["Neighborhood_Codes"] = ['N_C' + str(i + 1) for i in range(len(df))]

        # Assign colors based on the 'Category' column
        df['Color'] = df['Category'].map(category_colors)

        # Set up the figure with a larger size
        fig, ax = plt.subplots(figsize=(20, 12))  # Change fig size here (width, height)

        # Create a scatter plot with Seaborn
        scatter = sns.scatterplot(
            x=df['Dysfunctional (X)'],
            y=df['Functional (Y)'],
            hue=df['Category'],  # Define column for legend (color)
            palette=category_colors,  # Use the custom color palette
            size=df['Importance (Z)'],  # Define column for point sizes
            sizes=(50, 200),  # Set the range of marker sizes
            ax=ax  # Add the scatter plot to the axis
        )

        # Set x and y axis limits
        ax.set_xlim(1, 4)  # Set x-axis limits
        ax.set_ylim(1, 4)  # Set y-axis limits

        # Add a title to the plot using the extracted city name
        ax.set_title(f'Kano Analysis for Neighborhood Amenities_{city_name}', fontsize=16)

        # Add labels to the x and y axes
        ax.set_xlabel('Dysfunctional (X)', fontsize=14)
        ax.set_ylabel('Functional (Y)', fontsize=14)

        # Move the legend outside the plot
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

        # Add labels to each point with an offset
        texts = []
        for i in range(df.shape[0]):
            texts.append(
              ax.text(
                df['Dysfunctional (X)'][i],  # X position
                df['Functional (Y)'][i],  # Y position
                df['Neighborhood_Codes'][i],  # Label points with 'Shared_Codes' column
                fontsize=10,  # Font size for labels
                ha='center',  # Horizontal alignment
                va='bottom'  # Vertical alignment
              )
            )

        # Automatically adjust text to avoid overlap
        adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

        # Display the plot for each file
        plt.tight_layout()
        plt.show()

"""# **Kano_Living Arrangement_Shared**"""



"""Functional"""

Func_LA_SH= dq[['Response ID',
               'What best describes your current living arrangement? - Selected Choice',
                                'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Access to food or beverages (e.g., vending machines, coffee bar, snack stations)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Bicycle storage and repair station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Community lounge or clubhouse',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Controlled access and security features (e.g., cameras, key fobs)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Concierge or front desk services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Coworking space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Dog park/run',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Entertainment space (e.g., movie theater)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - EV charging stations',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Fitness center/gym',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Game or recreation room (e.g., billiards, ping-pong, golf simulators)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - High-speed internet in common areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Indoor or outdoor children’s play area',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - On-site parking – dedicated parking spot',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - On-site parking – gated/secure parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - On-site parking – covered parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Outdoor grilling and picnic areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Package delivery and mailroom services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Pet washing station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Resident events and activities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Rooftop deck or terrace',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Shared community resources/items (e.g., rentable printers, vacuum cleaners, tool kits, electric scooters)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Shared garden or green space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Shared laundry facilities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Spa/sauna or wellness center',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Swimming pool',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you have this in-unit amenity? - Valet trash service',
               ]]

new_columns = Func_LA_SH.columns.str.replace('Please answer the following questions regarding neighborhood assets near where you live. - ', '')
Func_LA_SH.columns = new_columns

Func_LA_SH.head()

"""Dysfunctional"""

Dysfunc_LA_SH = dq[['Response ID',
                   'What best describes your current living arrangement? - Selected Choice',
                                     'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Access to food or beverages (e.g., vending machines, coffee bar, snack stations)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Bicycle storage and repair station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Community lounge or clubhouse',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Controlled access and security features (e.g., cameras, key fobs)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Concierge or front desk services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Coworking space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Dog park/run',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Entertainment space (e.g., movie theater)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - EV charging stations',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Fitness center/gym',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Game or recreation room (e.g., billiards, ping-pong, golf simulators)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - High-speed internet in common areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Indoor or outdoor children’s play area',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - On-site parking – dedicated parking spot',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - On-site parking – gated/secure parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - On-site parking – covered parking',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Outdoor grilling and picnic areas',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Package delivery and mailroom services',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Pet washing station',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Resident events and activities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Rooftop deck or terrace',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Shared community resources/items (e.g., rentable printers, vacuum cleaners, tool kits, electric scooters)',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Shared garden or green space',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Shared laundry facilities',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Spa/sauna or wellness center',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Swimming pool',
 'Please answer the following questions regarding shared amenities in your apartment building/prope... - How do you feel if you do not have this in-unit amenity? - Valet trash service',
                   ]]

new_columns = Dysfunc_LA_SH.columns.str.replace('Please answer the following questions regarding neighborhood assets near where you live. - ', '')
Dysfunc_LA_SH.columns = new_columns

"""Importance"""

Imp_LA_SH =dq[['Response ID',
              'What best describes your current living arrangement? - Selected Choice',
              'How important is it for you to have access to this shared amenity? - Access to food or beverages (e.g., vending machines, coffee bar, snack stations)',
 'How important is it for you to have access to this shared amenity? - Bicycle storage and repair station',
 'How important is it for you to have access to this shared amenity? - Community lounge or clubhouse',
 'How important is it for you to have access to this shared amenity? - Controlled access and security features (e.g., cameras, key fobs)',
 'How important is it for you to have access to this shared amenity? - Concierge or front desk services',
 'How important is it for you to have access to this shared amenity? - Coworking space',
 'How important is it for you to have access to this shared amenity? - Dog park/run',
 'How important is it for you to have access to this shared amenity? - Entertainment space (e.g., movie theater)',
 'How important is it for you to have access to this shared amenity? - EV charging stations',
 'How important is it for you to have access to this shared amenity? - Fitness center/gym',
 'How important is it for you to have access to this shared amenity? - Game or recreation room (e.g., billiards, ping-pong, golf simulators)',
 'How important is it for you to have access to this shared amenity? - High-speed internet in common areas',
 'How important is it for you to have access to this shared amenity? - Indoor or outdoor children’s play area',
 'How important is it for you to have access to this shared amenity? - On-site parking – dedicated parking spot',
 'How important is it for you to have access to this shared amenity? - On-site parking – gated/secure parking',
 'How important is it for you to have access to this shared amenity? - On-site parking – covered parking',
 'How important is it for you to have access to this shared amenity? - Outdoor grilling and picnic areas',
 'How important is it for you to have access to this shared amenity? - Package delivery and mailroom services',
 'How important is it for you to have access to this shared amenity? - Pet washing station',
 'How important is it for you to have access to this shared amenity? - Resident events and activities',
 'How important is it for you to have access to this shared amenity? - Rooftop deck or terrace',
 'How important is it for you to have access to this shared amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'How important is it for you to have access to this shared amenity? - Shared community resources/items (e.g., rentable printers, vacuum cleaners, tool kits, electric scooters)',
 'How important is it for you to have access to this shared amenity? - Shared garden or green space',
 'How important is it for you to have access to this shared amenity? - Shared laundry facilities',
 'How important is it for you to have access to this shared amenity? - Spa/sauna or wellness center',
 'How important is it for you to have access to this shared amenity? - Swimming pool',
 'How important is it for you to have access to this shared amenity? - Valet trash service']]

Shared_LivingArrangement_Overall_Raw_data= pd.merge(pd.merge(Func_LA_SH, Dysfunc_LA_SH, on='Response ID', how='inner'), Imp_LA_SH, on='Response ID', how='inner')

Shared_LivingArrangement_Overall_Raw_data = Shared_LivingArrangement_Overall_Raw_data.sort_values(by=['What best describes your current living arrangement? - Selected Choice'], ascending=[True])

Shared_LivingArrangement_Overall_Raw_data.to_excel("/content/Shared_Living Arrangement_Raw_data.xlsx")





"""# Scatterplot"""

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from adjustText import adjust_text

# Directory containing the Excel files
directory = '/content/Living Arrangement_Shared'

# Define a color map for your categories using hex codes or RGB values
category_colors = {
    'Attractive': '#1f77b4',  # Blue
    'Indifferent': '#ff7f0e',  # Orange
    'Performance': '#2ca02c',  # Green
    'Must-Have': '#d62728',  # Red
}

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):  # Adjust the file extension if necessary
        file_path = os.path.join(directory, filename)

        # Extract the word after "__" from the filename
        #city_name = filename.split("_")[1].split(".")[0]  # Split by '__' and get the word before the '.xlsx'
        # Extract the word after the second "_" and before ".xlsx"
        parts = filename.split("_")
        if len(parts) > 2:
            city_name = parts[2].split(".")[0]  # Get the word after the second "_" and before ".xlsx"
        else:
            city_name = "Unknown"  # Default to "Unknown" if the expected pattern isn't met

        # Read each Excel file with the desired sheet and skipping rows
        df = pd.read_excel(file_path, sheet_name="Kano_Result", skiprows=1)
                # Add the 'Shared_Codes' column to each DataFrame
        df["Shared_Codes"] = ['SH_C' + str(i + 1) for i in range(len(df))]

        # Assign colors based on the 'Category' column
        df['Color'] = df['Category'].map(category_colors)

        # Set up the figure with a larger size
        fig, ax = plt.subplots(figsize=(20, 12))  # Change fig size here (width, height)

        # Create a scatter plot with Seaborn
        scatter = sns.scatterplot(
            x=df['Dysfunctional (X)'],
            y=df['Functional (Y)'],
            hue=df['Category'],  # Define column for legend (color)
            palette=category_colors,  # Use the custom color palette
            size=df['Importance (Z)'],  # Define column for point sizes
            sizes=(50, 200),  # Set the range of marker sizes
            ax=ax  # Add the scatter plot to the axis
        )

        # Set x and y axis limits
        ax.set_xlim(1, 4)  # Set x-axis limits
        ax.set_ylim(1, 4)  # Set y-axis limits

        # Add a title to the plot using the extracted city name
        ax.set_title(f'Kano Analysis for Shared Amenities_{city_name}', fontsize=16)

        # Add labels to the x and y axes
        ax.set_xlabel('Dysfunctional (X)', fontsize=14)
        ax.set_ylabel('Functional (Y)', fontsize=14)

        # Move the legend outside the plot
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

        # Add labels to each point with an offset
        texts = []
        for i in range(df.shape[0]):
            texts.append(
              ax.text(
                df['Dysfunctional (X)'][i],  # X position
                df['Functional (Y)'][i],  # Y position
                df['Shared_Codes'][i],  # Label points with 'Shared_Codes' column
                fontsize=10,  # Font size for labels
                ha='center',  # Horizontal alignment
                va='bottom'  # Vertical alignment
              )
            )

        # Automatically adjust text to avoid overlap
        adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

        # Display the plot for each file
        plt.tight_layout()
        plt.show()

"""Functional

# **Kano_Living Arrangement_InUnit**
"""



"""Functional"""

Func_LA_IU= dq[['Response ID',
               'What best describes your current living arrangement? - Selected Choice',
                 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Adequate storage space (e.g., closets, cabinets, built-ins)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Central Air Conditioning + Heating',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Energy-efficient features (e.g., LED lighting, energy-efficient appliances)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Enhanced security systems (e.g., cameras, alarms)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - High-end bathroom features (e.g., spa-like bathrooms, rain showers)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - High Quality Appliances',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - In-unit laundry',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Large windows and natural lighting',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Modern finishes (e.g., hardwood floors, granite countertops)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Office or dedicated workspace',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Private balconies or patios',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Provided high speed internet',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Secure access (e.g., smart locks, keyless entry)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Smart home features (e.g., smart thermostat, smart lights)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you have this in-unit amenity? - Spacious Layouts (e.g., open floor plans, large rooms)']]

new_columns = Func_LA_IU.columns.str.replace('Please answer the following questions regarding in-unit amenities. - ', '')
Func_LA_IU.columns = new_columns

Func_LA_IU.head()

"""Dysfunctional"""

Dysfunc_LA_IU = dq[['Response ID',
               'What best describes your current living arrangement? - Selected Choice',
                     'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Adequate storage space (e.g., closets, cabinets, built-ins)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Central Air Conditioning + Heating',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Energy-efficient features (e.g., LED lighting, energy-efficient appliances)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Enhanced security systems (e.g., cameras, alarms)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - High-end bathroom features (e.g., spa-like bathrooms, rain showers)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - High Quality Appliances',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - In-unit laundry',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Large windows and natural lighting',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Modern finishes (e.g., hardwood floors, granite countertops)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Office or dedicated workspace',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Private balconies or patios',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Provided high speed internet',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Secure access (e.g., smart locks, keyless entry)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Smart home features (e.g., smart thermostat, smart lights)',
 'Please answer the following questions regarding in-unit amenities. - How do you feel if you do not have this in-unit amenity? - Spacious Layouts (e.g., open floor plans, large rooms)']]

new_columns = Dysfunc_LA_IU.columns.str.replace('Please answer the following questions regarding in-unit amenities. - ', '')
Dysfunc_LA_IU.columns = new_columns

Dysfunc_LA_IU.head()

"""Importance"""

Imp_LA_IU =dq[['Response ID',
               'What best describes your current living arrangement? - Selected Choice',
                'How important is it for you to have access to this in-unit amenity? - Adequate storage space (e.g., closets, cabinets, built-ins)',
 'How important is it for you to have access to this in-unit amenity? - Central Air Conditioning + Heating',
 'How important is it for you to have access to this in-unit amenity? - Energy-efficient features (e.g., LED lighting, energy-efficient appliances)',
 'How important is it for you to have access to this in-unit amenity? - Enhanced security systems (e.g., cameras, alarms)',
 'How important is it for you to have access to this in-unit amenity? - High-end bathroom features (e.g., spa-like bathrooms, rain showers)',
 'How important is it for you to have access to this in-unit amenity? - High Quality Appliances',
 'How important is it for you to have access to this in-unit amenity? - In-unit laundry',
 'How important is it for you to have access to this in-unit amenity? - Large windows and natural lighting',
 'How important is it for you to have access to this in-unit amenity? - Modern finishes (e.g., hardwood floors, granite countertops)',
 'How important is it for you to have access to this in-unit amenity? - Office or dedicated workspace',
 'How important is it for you to have access to this in-unit amenity? - Private balconies or patios',
 'How important is it for you to have access to this in-unit amenity? - Provided high speed internet',
 'How important is it for you to have access to this in-unit amenity? - Scenic views (e.g., cityscape, waterfront, nature)',
 'How important is it for you to have access to this in-unit amenity? - Secure access (e.g., smart locks, keyless entry)',
 'How important is it for you to have access to this in-unit amenity? - Smart home features (e.g., smart thermostat, smart lights)',
 'How important is it for you to have access to this in-unit amenity? - Spacious Layouts (e.g., open floor plans, large rooms)']]

LivingArrangement_Inunit_Overall= pd.merge(pd.merge(Func_LA_IU, Dysfunc_LA_IU, on='Response ID', how='inner'), Imp_LA_IU, on='Response ID', how='inner')

LivingArrangement_Inunit_Overall = LivingArrangement_Inunit_Overall.sort_values(by=['What best describes your current living arrangement? - Selected Choice'], ascending=[True])

LivingArrangement_Inunit_Overall.to_excel("/content/Living Arrangement_Inunit_Raw_data.xlsx")





"""# Scatterplot"""

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from adjustText import adjust_text

# Directory containing the Excel files
directory = '/content/Living Arrangement_Inunit'

# Define a color map for your categories using hex codes or RGB values
category_colors = {
    'Attractive': '#1f77b4',  # Blue
    'Indifferent': '#ff7f0e',  # Orange
    'Performance': '#2ca02c',  # Green
    'Must-Have': '#d62728',  # Red
}

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):  # Adjust the file extension if necessary
        file_path = os.path.join(directory, filename)

        # Extract the word after "__" from the filename
        #city_name = filename.split("_")[1].split(".")[0]  # Split by '__' and get the word before the '.xlsx'
        # Extract the word after the second "_" and before ".xlsx"
        parts = filename.split("_")
        if len(parts) > 2:
            city_name = parts[2].split(".")[0]  # Get the word after the second "_" and before ".xlsx"
        else:
            city_name = "Unknown"  # Default to "Unknown" if the expected pattern isn't met

        # Read each Excel file with the desired sheet and skipping rows
        df = pd.read_excel(file_path, sheet_name="Kano_Result", skiprows=1)
                # Add the 'Shared_Codes' column to each DataFrame
        df["Inunit_Codes"] = ['IU_C' + str(i + 1) for i in range(len(df))]

        # Assign colors based on the 'Category' column
        df['Color'] = df['Category'].map(category_colors)

        # Set up the figure with a larger size
        fig, ax = plt.subplots(figsize=(20, 12))  # Change fig size here (width, height)

        # Create a scatter plot with Seaborn
        scatter = sns.scatterplot(
            x=df['Dysfunctional (X)'],
            y=df['Functional (Y)'],
            hue=df['Category'],  # Define column for legend (color)
            palette=category_colors,  # Use the custom color palette
            size=df['Importance (Z)'],  # Define column for point sizes
            sizes=(50, 200),  # Set the range of marker sizes
            ax=ax  # Add the scatter plot to the axis
        )

        # Set x and y axis limits
        ax.set_xlim(1, 4)  # Set x-axis limits
        ax.set_ylim(1, 4)  # Set y-axis limits

        # Add a title to the plot using the extracted city name
        ax.set_title(f'Kano Analysis for In-unit Amenities_{city_name}', fontsize=16)

        # Add labels to the x and y axes
        ax.set_xlabel('Dysfunctional (X)', fontsize=14)
        ax.set_ylabel('Functional (Y)', fontsize=14)

        # Move the legend outside the plot
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

        # Add labels to each point with an offset
        texts = []
        for i in range(df.shape[0]):
            texts.append(
              ax.text(
                df['Dysfunctional (X)'][i],  # X position
                df['Functional (Y)'][i],  # Y position
                df['Inunit_Codes'][i],  # Label points with 'Shared_Codes' column
                fontsize=10,  # Font size for labels
                ha='center',  # Horizontal alignment
                va='bottom'  # Vertical alignment
              )
            )

        # Automatically adjust text to avoid overlap
        adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

        # Display the plot for each file
        plt.tight_layout()
        plt.show()