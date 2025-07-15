from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

responses = {
    "hello": "how are you doing today?",
    "what's up?": "I'm cool and you?",
    "good morning": "Same here",
    "good afternoon": "Same here",
    "good evening": "Same here",
    "thank you": "you're welcome",
    "qst": '''
1. A blood donor should have
    a. Hb of over 12g/dl for both men and women
    b. No pregnancy in last 6 months
    c. No blood transfusion in last 6 months
    d. No major operation in last 6 months
    e. No clinical malaria in past month living in endemic areas
ANS. (A)

2. Which of the following is true about bile
    A. Depends on active secretion
    B. Depends on hormones
    C. Depends on the stability of enterohepatic circulation
    D. Has only two secretion sites or so, I can't recall
    E. None of the above
ANS. (A)

3. Which of the following is not a pediatric emergency
    A. Testicular torsion
    B. Posterior urethral valve
    C. Intestinal obstruction
    D. Congenital pyloric stenosis
    E. Hypospadias
ANS. (E)

4. Which is correct about testicular torsion;
    a. it's a true urological emergency
    b. it's intravaginal in neonates
    c. diagnosis isn't reliable
ANS. (A)

5. All these are features of hypokalemia except
    A. vomiting
    B. nausea
    C. Ileus
ANS. (C)
    
6. Breast pain is associated with Breast cancer
    a.Lcis
    b.DCIS
    c.Sclerosing adenosis
    d.Breast cyst
ANS. (D)
    
7. A 55kg malnourished man was admitted for abdominal Surgery. Approximate the protein and carbohydrates required daily to feed him.
    a. 800 kcal of carbohydrates
    b. 80 kcal
    c. 50 kcal
    d. 3000 kcal
    e. 40 kcal
ANS. (A)
    
8. Hyperkalemia may occur in the following except
    a. Blood transfusion
    b. Rhandomyolysis
    c. Severe metabolic alkalosis
    d. Gastrointestinal hemorrhage
    e. Crush injury
ANS. (C)
    
9. The following are true of posterior urethra valve except
    a. Common cause of congenital bladder
    b. occurs only in males
    c. most common cause of renal failure and renal transplantation in pediatrics population
    d. 1 in 5k–8k
    e. polylhydrominos is a feature on uss
ANS. (E)
    
10. How can splenic injury be diagnosed in a descending order
    a) ultrasonography
    b) MRI
    c) CT
    d) peritoneal lavage
ANS. (C)
    
11. the following are components of the
    A. Femoral vein
    B. lateral border of the rectus sheath
    C. inguinal ligament
    D. inferior epigastric vessels
    E. B and C
ANS. (A)
    
12. Which of these does not facilitate interstitial fluid production
    A. Hypo proteinemia
    B. Hypernatremia
    C. Constrictive pericarditis
    D. Hypokalemia
    E. None of the above
ANS. (D)

13. Cardinal Symptoms of Intestinal Obstruction are the following except
    A. Crampy Abdominal Pain
    B. Billous Vomiting
    C. Abdominal Distention
    D. A and C only
    E. All of the above
ANS. (D)

14. The following are plasma expanders except
    a. Dextrose
    b. Dextran
    c. Albumin
    d. Stable plasma protein
    e. Synthetic colloid
ANS. (A)
    
15. The most common cause of mechanical obstruction of small bowel in Nigeria is?
    a. Adhesion
    b. Diverticulitis
    c. Volvulus
    d. Cancer
    e. Inguinal hernia
ANS. (A)
    
16. Shock is described as
    A. Hypotension
    B. Hypoxemia
    C. Hypoperfusion
    D. All of the above
ANS. (C)
    
17. A 32 year old woman with 35 weeks pregnancy prevented at emergency unit with fever, leucocytosis, nausea, vomiting and right sided abdominal tenderness. Regarding her management, which of the following is most appropriate?
    A. Treat with antibiotics to avoid operation
    B. Perform ultrasound
    C. Perform MRI (or CT, I'm not sure)
    D. Perform laparotomy immediately
    E. Perform laparotomy after delivery
ANS. (B)

18. Which of this condition is associated with meckel's diverticulitis
    A. GI bleeding
    B. Obstruction
    C. Cancer
    D. Diverticulitis
ANS. (A)

19. About omphalocele, which is correct?
    A. Common in 1in 2000
    B. Defect in anterior abdominal wall
    C. In exomphalos major, umbilical cord is attached at the centre
    D. In exomphalos minor, umbilicus is attached at the inferior border
ANS. (B)

20. Which of the following is true about appendiceal innervation
    a). The appendix gets its innervation from somatic and afferent neurons
    d). Ruptured appendix results in no pain
ANS. (A)

21. which is true of Antigen HLA
    a.it is found in all vertebrea
ANS. (A)

22. Which of the following will manage the nutrition of a patient except
    A. Microbiologyist
    B. Hospital administrator
    C. Otorhinolaryngologist
    D. Nutritionist
    E. Nurse
ANS. (C)

23. Which of the following organ can be donated the patient stops breathing and heart stops beating
    a. Heart valve
    b. Kidney
    c. Liver
ANS. (B)

24. A 2 yr old fell from a storey building and presented with vomiting, seizure and a GCS score of 12, which of the following does he have
    a. Severe head injury
    b. Moderate head injury
    c. Mid head injury
    d. subarachnoid hemorrhage
ANS. (B)

25. The which of the following hernia will reoccur after primary repair
    A. Epigastric hernia
    B. Spigelian hernia
    C. Indirect hernia
    D. Femoral hernia
    E. Incisional hernia
ANS. (E)

26. If the mucocele of an appendix is found during surgery, which of the following will be the management therapy?
    A. Biopsy then subsequent appendectomy if malignant....
    B. Needle aspiration cytology ....
    C. Appendectomy
    D. Close and observe
ANS. (C)

27. Which of the following is true about veniform appendicitis
    a). Its length is 1–30cm
ANS. (A)

28. Which of the following is CORRECT
    a. Testicular torsion is more prevalent in ages greater than 19 years
    b. Horizontal tests is not a risk factor
    c. In doppler ultrasonography, acute epididymorchitis indicates increased flow of blood
    d. Horizontal tests is not a risk factor for torsion
ANS. (C)
'''
}

def get_chatbot_response(user_input):
    user_input = user_input.lower().strip()
    for key in responses:
        if key in user_input:
            return responses[key]
        elif user_input == "yes":
            return responses["qst"]
    return "Awaiting upgrade..."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response")
def get_response():
    user_text = request.args.get("msg")
    return jsonify({"response": get_chatbot_response(user_text)})

if __name__ == "__main__":
    app.run(debug=True)