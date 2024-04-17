n=int(input("Enter your Choic : "))
D={0:"""Q1. Who is father of our nation?
a. Mahatma Gandhi
b. Subash Chandra Bosh
c. Dr. Rajendra Prashad
d. LAl Bahadur Shastri\n""",
1:"""\nQ2. Who invented Computer?
a. Dennis Ritchie
b. Alan Turing
c. Charles Babbage
d. James Gosling \n""",
2:"""\nQ3. Who is the father of C language?
a. Steve Jobs
b. James Gosling
c. Dennis Ritchie
d. Rasmus Lerdorf\n""",
3:"""\nQ4. Who developed the Python language?
a. Zim Den
b. Guido van Rossum
c. Niene Stom
d. Wick van Rossum\n""",
4:"""\nQ5. In which year was the Python language developed?
a. 1995
b. 1972
c. 1981
d. 1989\n""",
5:"""\nQ6. Which one of the following is the correct extension of the Python file?
a. .py
b. .python
c. .p
d. None of these\n""",
6:"""\nQ7. What is the method inside the class in python language?
a. Object
b. Function
c. Attribute,
d. Argument\n""",
7:"""\nQ8. Which of the following is not a keyword in Python language?
a. val
b. raise
c. try
d. with\n""",
8:"""\nQ9. Which one of the following has the highest precedence in the expression?
a. Division
b. Subtraction
c. Power
d. Parentheses\n""",
9:"""\nQ10. Which of the following option is not a core data type in the python language?
a. Dictionary
b. Class
c. Lists
d. All of the above\n""",
10:"""Q11. Which one of the following river flows between Vindhyan and Satpura ranges?
(a) Narmada
(b) Mahanadi
(c) Son
(d) Netravati\n""",

11:"""Q12. The Central Rice Research Station is situated in?
(a) Chennai
(b) Cuttack
(c) Bangalore
(d) Quilon\n""",
12:"""Q13. Who among the following wrote Sanskrit grammar?
(a) Kalidasa
(b) Charak
(c) Panini
(d) Aryabhatt\n""",
13:"""Q14. Which among the following headstreams meets the Ganges in last?
(a) Alaknanda
(b) Pindar
(c) Mandakini
(d) Bhagirathi\n""",
14:"""Q15. The metal whose salts are sensitive to light is?
(a) Zinc
(b) Silver
(c) Copper
(d) Aluminum\n""",
15:"""Q16. Patanjali is well known for the compilation of –
(a) Yoga Sutra
(b) Panchatantra
(c) Brahma Sutra
(d) Ayurveda\n""",
16:"""Q17. River Luni originates near Pushkar and drains into which one of the following?
(a) Rann of Kachchh
(b) Arabian Sea
(c) Gulf of Cambay
(d) Lake Sambhar\n""",
17:"""Q18. Which one of the following rivers originates in Brahmagiri range of Western Ghats?
(a) Pennar
(b) Cauvery
(c) Krishna
(d) Tapti\n""",

18:"""Q19. The country that has the highest in Barley Production?
(a) China
(b) India
(c) Russia
(d) France\n""",
19:"""Q20. Tsunamis are not caused by
(a) Hurricanes
(b) Earthquakes
(c) Undersea landslides
(d) Volcanic eruptions\n""",

20:"""Q21. Chambal river is a part of 
(a) Sabarmati basin
(b) Ganga basin
(c) Narmada basin
(d) Godavari basin\n""",
21:"""Q22. D.D.T. was invented by?
(a) Mosley
(b) Rudolf
(c) Karl Benz
(d) Dalton\n""",
22:"""Q23. Volcanic eruption do not occur in the
(a) Baltic sea
(b) Black sea
(c) Caribbean sea
(d) Caspian sea\n""",
23:"""Q24. Indus river originates in 
(a) Kinnaur
(b) Ladakh
(c) Nepal
(d) Tibet\n""",

24:"""Q25. The hottest planet in the solar system?
(a) Mercury
(b) Venus
(c) Mars
(d) Jupiter\n""",
25:"""Q26. With which of the following rivers does Chambal river merge?
(a) Banas
(b) Ganga
(c) Narmada
(d) Yamuna\n""",

26:"""Q27. Where was the electricity supply first introduced in India 
(a) Mumbai
(b) Dehradun
(c) Darjeeling
(d) Chennai\n""",
27:"""Q28. Amravati, Bhavani, Hemavati and Kabini are tributaries of which one of the following rivers?
(a) Mahanadi
(b) Godawari
(c) Cauvery
(d) Krishna\n""",

28:"""Q29. Which of the following is related to Bharat Nirman Scheme?
(a) Foodgrain production self sufficiency
(b) Family welfare programme
(c) Infrastructure development
(d) Employment generation program\n""",
29:"""Q30. Which peninsular river is least seasonal in flow?
(a) Narmada
(b) Krishna
(c) Godavari
(d) Cauvery\n""",
30:"""Q31. Which one of the following ports is the oldest port in India?
(a) Mumbai Port
(b) Chennai Port
(c) Kolkata Port
(d) Vishakhapatnam Port\n""",

31:"""Q32. At which one of the following places do the rivers Alaknanda and Bhagirathi merge to form Ganga?
(a) Devprayag
(b) Rudra Prayag
(c) Karnaprayag
(d) Vishnuprayag\n""",

32:"""Q33. Which of the following is not a nuclear power center?
(a) Narora
(b) Kota
(c) Chamera
(d) Kakrapara\n""",
33:"""Q34. When was the first human heart transplant operation, which was performed by Dr. Christian Bernard on Louis Washkansky conducted?
a) 1943
b) 1988
c) 1967
d) 1963\n""",
34:"""Q35. Which is the religion for which the Fire temple is the place of worship?
a) Hinduism
b) Jainism
c) Zoroastrianism
d) Buddhism\n""",
35:"""Q36. Where can Coral reefs be found in India?
a) The Malabar Coast
b) Rameshwaram
c) Trivandrum
d) Mahabalipuram\n""",
36:"""Q37. The United Nations Organization has its Headquarters at
a) Bali
b) Hague
c) New York, USA
d) Washington DC\n""",
37:"""Q38. Objects at the surface of water can be viewed from a submarine under water by using this instrument.
a) Stethescope
b) Periscope
c) Kaleidoscope
d) Telescope\n""",
38:"""Q39. Professor Amartya Sen received the Nobel Prize in this field.
a) Literature
b) Electronics
c) Economics
d) Geology\n""",
39:"""Q40. Which of the following musical instruments is played by Amjad Ali Khan?
a) Veena
b) Tabla
c) Sarod
d) Guitar\n""",
40:"""Q41. Greta Garbo is associated with
a) Classical dance
b) Music
c) Acting
d) Literature\n""",
41:"""Q42. Dr. V. Kurien is famous in the field of _________.
a) Atomic power
b) Dairy development
c) Economic reforms
d) Poultry farms\n""",
42:"""Q43. Ms. Meera Sahib Fathima Beevi has the distinction of being the first lady
a) Prime minister of Pakisthan
b) Judge of the District Court
c) Chief Minister of a State
d) Judge of Supreme Court\n""",
43:"""Q44. Who created the famous Rock Garden of Chandigarh?
a) Gaudi
b) Saarinen
c) Krishnarao Jaisim
d) Nek Chand\n""",
44:"""Q45. The 'Lady with the Lamp' was the name given to?
a) Vijayalakshmi Pandit
b) Queen Elizabeth
c) Florence Nightingale
d) Princess Diana Florence Nightingale\n""",
45:"""Q46. The biggest part of the brain is
a) Spinal cord
b) Cerebellum
c) Cerebrum
d) Brain Stem\n""",
46:"""Q47. NASA's most famous space telescope goes by the name?
a) Muble Satellite Telescope
b) Hubble Space Telescope
c) Humble Space Telescope
d) Galaxy Satellite Telescope\n""",
47:"""Q48. At room temperature, which is the only metal that is in liquid form?
a) Iron
b) Aluminum
c) Mercury
d) Silver\n""",
48:"""Q49. This scientist is well known for his theory of relativity. Who is he?
a) Thomas Alva Edison
b) Albert Einstein
c) Marconi
d) James Watt\n""",
49:"""Q50. A change of the DNA of an organism resulting in a new trait is known as a ________.
a) Mitosis
b) Meiosis
c) Mutation
d) Morphosis\n""",
}

a=['a','c','c','b','d','a','a','a','d','b','a','b','c','d','b','a','a','b','c','a','c','a','a','d','b','d','c','c','c','c','b','a','c','c','c','b','c','b','c','c','c','b','d','d','c','c','b','d','b','c']
j=0
score=0
for k in range(n):
    print("\n",D[k])
    ans=input("Ans. ")
    if ans==a[k]:
        print("Your Answer Is Right")
        print("You Get 10 point")
        score=score+2
    else:
        print(f"Your Answer Is Wrong\nRight Ans. {a[k]}\nYou Loss 5 points")
        score=score-1
        
print("\nYou Gain Total Score = ",score)