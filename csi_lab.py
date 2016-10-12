dna = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

hair_black = "CCAGCAATCGC"
hair_brown = "GCCAGTGCCG"
hair_blonde ="TTAGCTATCGC"

face_square = "GCCACGG"
face_round = "ACCACAA"
face_oval = "AGGCCTCA"

eye_blue ="TTGTGGTGGC"
eye_green = "GGGAGGTGGC"
eye_brown = "AAGTAGTGAC"

female = "TGAAGGACCTTC"
male = "TGCAGGAACTTC"

race_white = "AAAACCTCA"
race_black = "CGACTACAG"
race_asian = "CGCGGGCCG"

if (dna.find(hair_blonde)>=0) and (dna.find(face_oval)>=0) and (dna.find(eye_blue)>=0) and (dna.find(female)>=0) and (dna.find(race_white)>=0):
    print ("LISA ate the ice cream.")

if (dna.find(hair_brown)>=0) and (dna.find(face_oval)>=0) and (dna.find(eye_brown)>=0) and (dna.find(female)>=0) and (dna.find(race_white)>=0):
    print ("LARISA ate the ice cream.")

if (dna.find(hair_black)>=0) and (dna.find(face_oval)>=0) and (dna.find(eye_blue)>=0) and (dna.find(male)>=0) and (dna.find(race_white)>=0):
    print ("MATEJ ate the ice cream.")

if (dna.find(hair_brown)>=0) and (dna.find(face_square)>=0) and (dna.find(eye_green)>=0) and (dna.find(male)>=0) and (dna.find(race_white)>=0):
    print ("MIHA ate the ice cream.")
