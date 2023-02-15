## Data Analysis Nanodegree

---
## Project 2: Investigate a dataset
#### Created by: Juanita Smith
#### Last date: 5 October 2022

---



## Predicting no-show appointments

<img src="images/img.png" alt="drawing" width="600"/>

## Project Overview
This project is completed as part of the 'Data Analyst' nanodegree with Udacity. 
The dataset, provided by Kaggle, collects information from 100k medical appointments in Brazil. It is focused 
on the question of whether or not patients show up for their appointment. 
A number of characteristics about the patient are included in each row.

The goal of the project was to demonstrate data analysis skills of questioning, wrangling, exploring, analysing and communicating data using numpy, pandas and matplotlib libraries.

Udacity's instructions:
Conduct own analysis of the dataset and brainstorm what questions the dataset could answer. Use pandas and NumPy to answer the questions most interesting, and create a report sharing the conclusions.


Note: Idea of the project was not use inferential statistics or machine learning to answer the questions, but to explore the features manually purely with pandas and numpy to practise plotting and data analysis skills

   
## Data

- Data were supplied by Kaggle through Udacity and can be downloaded from [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/July/5b57919a_data-set-options/data-set-options.pdf)
- Read more information about the features directly in Kaggle [here](https://www.kaggle.com/datasets/joniarroba/noshowappointments)

### Data Dictionary

The data contain 14 features:

*1) PatientId:* Identification of a patient

*2) AppointmentID:* Identification of each appointment

*3) Gender:* Male (M) or Female (F).  
Female is the greater proportion, woman takes way more care of they health in comparison to man.

*4) ScheduledDay:* The date and time the patient setup their appointment

*5) AppointmentDay:* The date of the actual appointment (no time is present)

*6) Age:* How old is the patient.

*7) Neighbourhood:* Location of the hospital where the appointment takes place

*8) Scholarship:* True (1) of False (0).

Indicates whether or not the patient is enrolled in Brasilian welfare program.
Read more about the [Bolsa Família here](https://en.wikipedia.org/wiki/Bolsa_Fam%C3%ADlia)

*9) Hipertension:* True (1) or False (0)
Also known as high blood pressure

*10) Diabetes:* True (1) or False (0)

*11) Alcoholism:* True (1) or False (0)

*12) Handcap:* Values 0 - 4

- 0 means patient have no disabilitly, 1 means patient 1 disability, 2 means patient have 2 disabilities and so on

*13) SMS_received:* True (1) or False (0)

- 1 or more messages were sent to the patient

*14) No-show:* True (1) or False (0)

- Be careful about the encoding of the last column: it says ‘No’ if the patient showed up to their appointment, and ‘Yes’ if they did not show up.


## Requirements
- Python 3 (Python 3.9 interpreter was used)
- Libraries needed:
    - pandas==1.4.4
    - numpy==1.21.5
    - seaborn==0.11.2
    - matplotlib==3.5.2
    - jupyter notebook=1.0.0
    - nb_conda=2.2.1


## Installation

To clone the repository: 'https://github.com/JuanitaSmith/medical_noshows.git'

Refer to 'requirements.txt' for all related dependencies and versions used


## Resources used:

https://stackoverflow.com/questions/13851535/how-to-delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression
https://stackoverflow.com/questions/34615854/seaborn-countplot-with-normalized-y-axis-per-group

