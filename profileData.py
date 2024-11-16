import requests
import WebPull
urlList = WebPull.linkList()
listOfInfo = []
api_key = 'cZhem_FvSZoBUNV_QZM1Ag'
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
def getInfo():
    for v in urlList:
        params = {'linkedin_profile_url': v,'skills': 'include',}
        response = requests.get(api_endpoint, params=params,headers=headers)
        profileData = response.json()
        full_Name = profileData['full_name']
        occupation = profileData['occupation']
        location = profileData['state']
        profilePic = profileData['profile_pic_url']
        industry = profileData['industry'] 
        listOfInfo.append([full_Name, occupation, location, profilePic, industry])

    return listOfInfo