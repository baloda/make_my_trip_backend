import json
from flask.ext.restful import Resource
from flask import request 
from connection import *



class check_connection(Resource):
	def get(self):
		if connect() != False:
	    		return {"connect":True,"succes":True}
		else:
			return {"connect":False,"succes":True}


class search(Resource):
	def get(self):
		conn=connect()
		id=request.headers.get('id')
		print (id)
		query = "select * from mmt where name='{0}' or code='{0}' or country='{0}'".format(id)
		cursor=conn.cursor()
		cursor.execute(query)
		row=cursor.fetchall()
		result=dict()
		final_result=[]
		length_of_dict=len(row)
		for i in range(0,length_of_dict):
			result['id']=row[i][0]
			result['code']=row[i][1]
			result['lat']=row[i][2]
			result['lon']=row[i][3]
			result['name']=row[i][4]
			result['rating']=row[i][5]
			result['city']=row[i][6]
			result['state']=row[i][7]
			result['country']=row[i][8]
			result['tz']=row[i][9]
			result['type']=row[i][10]
			result['url']=row[i][11]
			final_result.append(result)
		conn.close()
		return final_result



class index(Resource):
	def get(self):
    		return {"message":"another end point","succes":True}


class get_airports(Resource):
	def get(self):
		url = "https://raw.githubusercontent.com/hjnilsson/country-flags/master/png250px/"
		conn=connect()
		query = "select * from mmt order by code limit 100"
		cursor=conn.cursor()
		cursor.execute(query)
		row=cursor.fetchall()

		final_result=[]
		length_of_dict=len(row)
		for i in range(0,length_of_dict,1):
			result=dict()
			result['id']=row[i][0]
			result['code']=row[i][1]
			result['lat']=row[i][2]
			result['lon']=row[i][3]
			result['name']=row[i][4]
			result['rating']=row[i][5]
			result['city']=row[i][6]
			result['state']=row[i][7]
			result['country']=row[i][8]
			result['tz']=row[i][9]
			result['type']=row[i][10]
			result['url']=row[i][11]
			result['elevation']=row[i][12]
			result['direct_flight']=row[i][13]
			image=result['code'][1:]

			result['image']=url+image.lower()+".png"

			final_result.append(result)
		conn.close()
		return final_result


class total_airports(Resource):
	def get(self):
		conn=connect()
		query = "select count(*) from mmt where type='Airports'"
		cursor=conn.cursor()
		cursor.execute(query)
		row=cursor.fetchall()
		print (row)
		return {"succes":True,"data":row[0][0]}



class second_class(Resource):
	def get(self):
		return {"data":"this is the second class","succes":True}

