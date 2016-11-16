# PYTHON SCRIPT, tested on v3.5.2
# ADD person to group NEW and WRITE results/errors to file
import psycopg2
import sys
import datetime

	# Create new log file
		filename = "log - "+datetime.datetime.now().strftime("%Y%m%d-%H%M%S"+".txt")
		f = open(filename, 'w+')

	
	# Try to connect
		try:
			conn=psycopg2.connect("dbname='test' user='test' password='test' host='hostname' port='port'")
		except:
			f.write ("I am unable to connect to the database.")
		
		
	# Print rows selected to update
	cur = conn.cursor()
	
	res = cur.execute
		# Print sum of rows 
	("SELECT count(*) FROM a.person p JOIN h.person h ON p.person_id = h.id WHERE date_part('year',age(h.birth_date))>= 15 and person_group_id <>1")
	
	f.write ("Liczba wierszy do zmiany: " + str(cur.fetchone())+ '\n')
	
		# Print data 
	res = cur.execute("SELECT h.id FROM a.person p JOIN hr.person h ON p.person_id = h.id WHERE date_part('year',age(h.birth_date))>= 15 and person_group_id <>1")
	
	f.write ("Lista [person_ID]: \n")
		for res in cur.fetchall():
			f.write (str(res)+ '\n')
	
	
	# Update transaction
		try:
			res = cur.execute("UPDATE a.person as p SET peron_group_id=14 FROM h.person h WHERE p.person_id h.id and date_part('year',age(h.birth_date))>= 15 and person_group_id <>1")
		except:
			f.write ("I am unable to UPDATE."+ '\n')
		try:
			conn.commit()
		except:
			f.write ("I am unable to commit()."+ '\n')
			
	# close connection and logfile
	f.close()
	cur.close()
	conn.close()
	raise SystemExit()
