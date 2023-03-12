#Program to change cm-m & m-cm viceversa using Dictionary

m_cm = { x : x*100 for x in range( 1, 11) }
temp = m_cm.values()
cm_m = { x : x/100 for x in temp }

print( " Meters : Centimeters ", m_cm)
print( " Centimeters : Meters ", cm_m)