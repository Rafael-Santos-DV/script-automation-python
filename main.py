import json
from pprint import pprint
from methods.methods import InformationOfAnime
from methods.verify import verifyItems
import requests as req

from service.api import SERVER

init = True;

while init: 
    response = InformationOfAnime();    
    verifyItems(response);
    question = input("All right? S/N");
    pprint(response);
    if question.upper() == "S": 
        print(json.dumps(response));
        res = req.post(f"{SERVER}/createNewAnime", json=response);
        print(res.json());
        init = False;
    


# Routes.get('/showAnimes', ControllersCrudAnimes.GetShowAnimes);
# Routes.get('/showAnime/:animeId', ControllersCrudAnimes.GetShowAnime);
# Routes.post('/createNewAnime', ControllersCrudAnimes.CreateNewAnimeData); 