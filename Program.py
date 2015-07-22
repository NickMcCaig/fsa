from __future__ import print_function
import mysql.connector
import json
import urllib2
from mysql.connector import errorcode
cnx = mysql.connector.connect(user='Admin', password='red123',host='127.0.0.1',database='test')
cursor = cnx.cursor()
def listing(XXstr):
    add_business = ("INSERT INTO fsadata "
               "(FHRSID, BusinessName, BusinessType, RateingValue, AddressLine1, AddressLine2, AddressLine3, AddressLine4,Postcode,LocalAuthorityBusinessID,BusinessTypeID, RatingKey, LocalAuthorityCode, LocalAuthorityName, NewRatingPending ) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    FHRSID = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['FHRSID'])
    FHRSID = FHRSID.replace('"',"")
    BusinessName = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['BusinessName'])
    BusinessName = BusinessName.replace('"','')
    BusinessType = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['BusinessType'])
    BusinessType = BusinessType.replace('"','')
    RateingValue = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['RatingValue'])
    RateingValue = RateingValue.replace('"','')
    AddressLine1 = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['AddressLine1'])
    AddressLine1 = AddressLine1.replace('"','')
    if AddressLine1 == 'null':
        AddressLine1 = ''
    AddressLine2 = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['AddressLine2'])
    AddressLine2 = AddressLine2.replace('"','')
    if AddressLine2 == 'null':
        AddressLine2 = ''
    AddressLine3 = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['AddressLine3'])
    AddressLine3 = AddressLine3.replace('"','')
    if AddressLine3 == 'null':
        AddressLine3 = ''
    AddressLine4 = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['AddressLine4'])
    AddressLine4 = AddressLine4.replace('"','')
    if AddressLine4 == 'null':
        AddressLine4 = ''
    Postcode = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['PostCode'])
    Postcode = Postcode.replace('"','')
    LocalAuthorityBusinessID = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['LocalAuthorityBusinessID'])
    LocalAuthorityBusinessID = LocalAuthorityBusinessID.replace('"','')
    BusinessTypeID = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['BusinessTypeID'])
    BusinessTypeID = BusinessTypeID.replace('"','')
    RatingKey = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['RatingKey'])
    RatingKey = RatingKey.replace('"','')
    LocalAuthorityCode = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['LocalAuthorityCode'])
    LocalAuthorityCode = Postcode.replace('"','')
    LocalAuthorityName = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['LocalAuthorityName'])
    LocalAuthorityName = LocalAuthorityName.replace('"','')
    NewRatingPending = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['NewRatingPending'])
    NewRatingPending = NewRatingPending.replace('"','')
    data_business = (FHRSID, BusinessName, BusinessType, RateingValue, AddressLine1, AddressLine2, AddressLine3, AddressLine4,Postcode,LocalAuthorityBusinessID,BusinessTypeID, RatingKey, LocalAuthorityCode, LocalAuthorityName, NewRatingPending)
    cursor.execute(add_business, data_business)
#try:
for x in range(0, 1000):
    x += 1 # Same as a = a + 1
    astr = str(x)
    if not x % 1:
        print("the program has searched:" + str(x) + ' pages')
        url = 'http://ratings.food.gov.uk/enhanced-search/en-GB/%5E/%5E/Relevance/0/%5E/%5E/1/'+ astr +'/2500/json'
    print(url)
    req = urllib2.Request(url)
    opener =  urllib2.build_opener()
    f = opener.open(req)
    jsona = json.load(f)
    for XX in range(0, 2500):
        XXstr = XX
        rateingvalue = json.dumps(jsona['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail'][XXstr]['RatingValue'])
        listing(XXstr)
        XX += 1 # Same as a = a + 1
        astr = str(XX)
#except:
 #   print('The program has reached the end of the search')
    cnx.commit()
cursor.close()
cnx.close()
