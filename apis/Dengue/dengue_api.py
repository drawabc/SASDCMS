from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
import pprint
import googlemaps
import json


class Dengue():
    def __init__(self):
        def get_alphabets(s):
            special = ['(','/']
            for i in range(len(s)):
                if s[i] in special:
                    i-=1
                    return s[:i+1]        
        my_url = 'https://www.nea.gov.sg/dengue-zika/dengue/dengue-clusters'
        uclient = ureq(my_url)
        page_html = uclient.read()
        uclient.close()

        page_soup = soup(page_html,"html.parser")
        table = page_soup.findAll("table",{"class":"table surveillance-table two-row-head"})[0]

        rows = table.findAll("tr")
        rows = rows[2:]

        parsed_row_data = []
        row_data=[]
        for i in range(len(rows)):


            if len(rows[i]['class'])!=0 and rows[i]['class'][0]=="hashlink":

                parsed_row_data.append(row_data)

                title = get_alphabets(rows[i]['id'])
                row_data = [[title],[[rows[i+1].findAll("td",{"style":"text-align:center"})[3].text,int(rows[i+1].findAll("td",{"style":"text-align:center"})[0].text)]]]

                colour = i+1

            elif i == colour:
                c= rows[i].findAll("td")[1].div['class'][0]
                row_data[0].append(c)

            else :
                row_data[1].append([rows[i].findAll("td",{"style":"text-align:center"})[0].text,int(rows[i].findAll("td",{"style":"text-align:center"})[1].text)])

                skip = 0

        self.date = page_soup.findAll("div",{"id":"mainContent_mainContent_TFA5CC790007_Col00"})[0].p.text.strip()

        self.parsed_row_data = parsed_row_data[1:]



    def convert_to_json(self,li,date):
        api_key = 'AIzaSyCMwtsOxNlEec_9SI_FgkpSlpWwMtZUOKA'
        gm = googlemaps.Client(key = api_key)
        cluster_data = {'clusters':[]}
        cluster_data['updated_time'] = date

        for item in li:
            
            cluster = {}
            cluster['name'] = item[0][0]
            cluster['intensity'] = item[0][1]
            cluster['locations'] = []
            for address in item[1]:
                addr = {}
                addr['name'] = address[0]
                addr['coordinates'] = gm.geocode(address[0]+", Singapore")[0]['geometry']['location']
                addr['no_of_reports'] = address[1]
                cluster['locations'].append(addr)
            cluster_data['clusters'].append(cluster)

        return cluster_data

    def get_polygon_data(self):
        self.j_data = self.convert_to_json(self.parsed_row_data,self.date)
        clusters = self.j_data['clusters']
        polygons = []
        for cluster in clusters:
            points = cluster['locations']
            points_data = []
            for point in points:
                points_data.append(point['coordinates'])
            polygons.append(points_data)

        return polygons

    def write_json_file(self,title):
        try:
            with open(title,'w') as json_file:
                json.dump(self.j_data,json_file)
            return "Json file saved successfully"
        except:
            return "Json file not saved, an error has occured"

if __name__=='__main__':
    dengue_api = Dengue()
    pprint.pprint(dengue_api.get_polygon_data())
