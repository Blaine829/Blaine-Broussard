import breezypythongui
import datetime
import urllib.request
import json
from breezypythongui import EasyFrame
from tkinter import PhotoImage

class weather(breezypythongui.EasyFrame):
    def __init__(self):
        super().__init__(self)
       
        self.city_label = self.addLabel(text = "Spartanburg SC", row = 0, column = 0, columnspan = 2, sticky = "NSEW")
        
        self.temp_label = self.addLabel(text = "temp", row = 1, column = 0, columnspan = 1, sticky = "NSEW")
        self.image_label = self.addLabel(text = "image", row = 1, column = 1, columnspan = 1, sticky = "NSEW")
        self.date_label = self.addLabel(text = datetime.datetime.now(), row = 2, column = 0, columnspan = 3, sticky = "NSEW")
        self.button = self.addButton(text = "Refresh", row = 0, column = 3, columnspan = 1, command = self.refresh)
        self.refresh()
        
    def refresh(self):
        
        u = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=Spartanburg,SC,USA&appid=bd8a12003a32ab5f89a6e6ac3bda2d0f&units=imperial')
        byte_data = u.read()

        
        json_data = json.loads(byte_data)
        
        image_data = str(json_data['weather'][0]['icon'])
        temp_data = str(json_data['main']['temp'])
        # json_data
        # '{"coord":{"lon":-81.93,"lat":34.95},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"base":"stations","main":{"temp":52.34,"pressure":1017,"humidity":87,"temp_min":50,"temp_max":55.94},"visibility":16093,"wind":{"speed":4.7,"deg":210},"clouds":{"all":40},"dt":1542682500,"sys":{"type":1,"id":2418,"message":0.0043,"country":"US","sunrise":1542715624,"sunset":1542752364},"id":4597200,"name":"Spartanburg","cod":200def main():

        # update the labels
        
        self.image = PhotoImage(file = image_data+".gif")
        self.image_label["image"] = self.image

        self.temp_label["text"] = temp_data

        self.date_label["text"] = datetime.datetime.now()

def main():
    weather().mainloop()
        
        
if __name__ == "__main__":
    main()
