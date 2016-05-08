
import os
import controllers
from resources import *




#for testing get requests
api.add_resource(controllers.index,'/api/v1.0/index')
#for testing get requests that would make sure that it is connected to the database
api.add_resource(controllers.check_connection,'/api/v1.0/connect')
#for getting all the airports details (GET Request)
#Required Parameters :NONE
#OUTPUT : JSON array which contains all the airports and details


api.add_resource(controllers.get_airports,'/api/v1.0/get_airport')
#for getting no of airports (GET Request))
#Required Parameters :NONE
#OUTPUT : JSON array which contains The total no of airports

api.add_resource(controllers.total_airports,'/api/v1.0/total_airports')

#for searching (GET Request)
#Required Parameters :id
#OUTPUT : JSON array which searches on the basis of id

api.add_resource(controllers.search,'/api/v1.0/search')



#examle api url for api.add_resource(controllers.post_request,'/api/v1.0/post_req',methods=['POST','PUT'])

#url for checking login


