# -*- coding: utf8 -*-
from locust import HttpLocust, TaskSet, task
import json


# locust -f ice/api/load/ml/locustio.py --host=http://localhost:4567


class PredictBehavior(TaskSet):
    @task(1)
    def predict(self):
        payload = {
            "data": [
                {
                    "Post ID": "925389023",
                    "postTitle": "Daily Update â€“ Energy Price for Close of Business: 3/21",
                    "summary": "",
                    "description": "",
                    "Client Identifier": "testIdentifier"
                },
                {
                    "Post ID": "32471535",
                    "postTitle": "Study: Emissions From Power Plants, Refineries May Be Far Higher Than Reported",
                    "summary": "",
                    "description": "",
                    "Client Identifier": "testIdentifier"
                },
                {
                    "Post ID": "-1783743912",
                    "postTitle": "Virginia to Utilize Old Coal Mines for Hydropower",
                    "summary": "The coal industry may be dying, but the skeletons left behind in the form of abandoned mines can provide new life. The water left behind by the once industrious business is planned to be used by the state of Virginia, in the development of pumped storage hydro-electric power plants. However, this particular strategy to source water has been receiving some criticism. The bill to support the building of the power plants received nearly unanimous support in both the state Senate and the House of Delegates. However, researchers, coal reclamation experts, and renewable energy advocates alike have voiced concerns, citing that the idea is yet to be proven. Pumped storage facilities do exist elsewhere in Virginia, but using water from abandoned coal mines is an innovation to be tested anywhere in the world. The proposed locations for the new mines are in seven counties in the western end of the state. These counties have had many coal mines close recently, and the local economies have suffered as a result. Tax revenues from the mines were used to fund public schools and other government services. The pumped hydroplants work by utilizing excess energy â€“ usually intermittent energy from fluctuating renewable energy sources â€“ to pump water uphill, where it is stored at higher elevations in a lake or reservoir. When demand for energy spikes, the water is allowed to flow downhill into a reservoir at a lower elevation, and the energy is recaptured using turbines. These types of facilities are in use around the world. Minnesota is similarly attempting to breathe life into abandoned infrastructure, but in the form of abandoned iron pits. However, assessments have revealed that the presence of iron and water oxidation threatens potential operations at that location. Similar concerns have been raised with regards to the Virginia plan â€“ critics continue to say that the coalfield region needs to be more geologically stable for these power plants to work. Some experts are hopeful, looking at the relatively low level of iron found in the coalmines as support for the project. Moreover, a similar pumped hydro project in Southern California has been recently licensed, and if all goes smoothly there, it would provide a worthy precedent for supporters of the Virginian counterpart. This proposal is being looked at in conjunction with plans to build wind farms in Virginia â€“ these types of storage systems are the battery component necessary to make renewable energy sources feasible. This concern is especially relevant as we approach the summer months where demand for electricity skyrockets, and an ever increasing appetite for new renewable energy in Virginia remains. Indeed, the largest pumped-storage facility in the world happens to be in Virginia, in operation since the 1980â€™s. Unlike any other types of power plants, pumped hydro plants are free from many of the rules, regulations, and license requirements that traditionally govern the establishment and building processes. But despite these benefits that come from the language of the bills in question, the companies that would build these facilities would not do so without extensive research. The biggest issue, then, is cost. A recent series of studies concluded that a 100-MW pumped storage facility would cost approximately $120 million. The benefits are attractive, hundreds of jobs would be created at the construction site of each new facility, new sources of tax revenue would be found for local economies, and the transition to renewable energy becomes much easier for the state legislative body.",
                    "description": "The coal industry may be dying, but the skeletons left behind in the form of abandoned mines can provide new life. The water left behind by the once industrious business is planned to be used by the state of Virginia, in the development of pumped storage hydro-electric power plants.However, this particular strategy to source water has been receiving some criticism. The bill to support the building of the power plants received nearly unanimous support in both the state Senate and the House of Delegates. However, researchers, coal reclamation experts, and renewable energy advocates alike have voiced concerns, citing that the idea is yet to be proven. Pumped storage facilities do exist elsewhere in Virginia, but using water from abandoned coal mines is an innovation to be tested anywhere in the world.The proposed locations for the new mines are in seven counties in the western end of the state. These counties have had many coal mines close recently, and the local economies have suffered as a result. Tax revenues from the mines were used to fund public schools and other government services.The pumped hydroplants work by utilizing excess energy â€“ usually intermittent energy from fluctuating renewable energy sources â€“ to pump water uphill, where it is stored at higher elevations in a lake or reservoir. When demand for energy spikes, the water is allowed to flow downhill into a reservoir at a lower elevation, and the energy is recaptured using turbines.These types of facilities are in use around the world. Minnesota is similarly attempting to breathe life into abandoned infrastructure, but in the form of abandoned iron pits. However, assessments have revealed that the presence of iron and water oxidation threatens potential operations at that location. Similar concerns have been raised with regards to the Virginia plan â€“ critics continue to say that the coalfield region needs to be more geologically stable for these power plants to work.Some experts are hopeful, looking at the relatively low level of iron found in the coalmines as support for the project. Moreover, a similar pumped hydro project in Southern California has been recently licensed, and if all goes smoothly there, it would provide a worthy precedent for supporters of the Virginian counterpart.This proposal is being looked at in conjunction with plans to build wind farms in Virginia â€“ these types of storage systems are the battery component necessary to make renewable energy sources feasible. This concern is especially relevant as we approach the summer months where demand for electricity skyrockets, and an ever increasing appetite for new renewable energy in Virginia remains. Indeed, the largest pumped-storage facility in the world happens to be in Virginia, in operation since the 1980â€™s.Unlike any other types of power plants, pumped hydro plants are free from many of the rules, regulations, and license requirements that traditionally govern the establishment and building processes. But despite these benefits that come from the language of the bills in question, the companies that would build these facilities would not do so without extensive research. The biggest issue, then, is cost. A recent series of studies concluded that a 100-MW pumped storage facility would cost approximately $120 million.The benefits are attractive, hundreds of jobs would be created at the construction site of each new facility, new sources of tax revenue would be found for local economies, and the transition to renewable energy becomes much easier for the state legislative body.",
                    "Client Identifier": "testIdentifier"
                },
                {
                    "Post ID": "1162123218",
                    "postTitle": "Trump Administration Not Including Climate Change in New Decisions",
                    "summary": "",
                    "description": "",
                    "Client Identifier": "testIdentifier"
                },
                {
                    "Post ID": "-410428556",
                    "postTitle": "Long-Term Power Supply Issue Still Present in Australia Even After Offer from Teslaâ€™s Musk",
                    "summary": "",
                    "description": "",
                    "Client Identifier": "testIdentifier"
                },
                {
                    "Post ID": "1394910789",
                    "postTitle": "Expected Growth of Lithium-ion Battery Production puts Cobalt at Center Stage",
                    "summary": "",
                    "description": "",
                    "Client Identifier": "testIdentifier"
                },
                {
                    "Post ID": "1015096197",
                    "postTitle": "Sigora Haiti Sheds Light on the Energy Business in Frontier Markets",
                    "summary": "",
                    "description": "",
                    "Client Identifier": "testIdentifier"
                },
                {
                    "Post ID": "1549474474",
                    "postTitle": "Daily Update â€“ Energy Prices for Close of Business: 3/22",
                    "summary": "",
                    "description": "",
                    "Client Identifier": "testIdentifier"
                },
                {
                    "Post ID": "-374885247",
                    "postTitle": "100 Days: Access To Arctic Energy Key To U.S. Security",
                    "summary": "",
                    "description": "",
                    "Client Identifier": "testIdentifier"
                },
                {
                    "Post ID": "-671655231",
                    "postTitle": "Two Bankruptcies, One Signal to Investors?",
                    "summary": "TheÂ recent bankruptcies of two clean energy companies has kept the renewable energy sector on its toes. While these events may not be enough to provide a clear trend in the sector, it is keeping clean energy investors on their toes for what is to come in this industry.Â  This past week has been difficultÂ for clean energy due to the fact that two clean energy companies have filed for bankruptcy: Aquion, a saltwater battery maker, and Sungevity, a residential solar installer. These two instances of failure call into question the stability of the clean energy market, and reaffirm that there is not a wide margin for error for new companies in this space. In Aquionâ€™s beginning, their perceived potential was high enough that even Bill Gates contributed to the $190 million raised by investors on the promise that the company would be a shock to the advanced storage industry. The companyâ€™s supposed competitive advantage came in the form of nonflammable, nontoxic chemistry as an alternative to the industry standard of lithium-ion. The factory established in Pennsylvania was capable of producing 200 megawatt-hours per year. Unfortunately, only approximately 36 megawatt-hours had been produced by the end of 2016. Despite the numerous deals that Aquion boasted, the wind was sucked from its sails rather quickly. For instance, as recently as February 27th, the company announced a deal with Japanese Kyushu Electric Power to manufacture a solar-plus-storage system. Within merely two weeks, Aquion had filed for bankruptcy and is now searching for a buyer of its operating assets. The Aquion bankruptcy is a demonstration of the dangers of fundraising in energy innovation. Per usual, the Department of Energy funded the initial research phase at Carnegie Mellon University. As it scaled, the company began to attract high-profile investors. This combination of high growth potential and speedy financing are age-old ingredients in a recipe to grow too large too fast. Indeed, one piece of evidence supporting this overly-ambitious growth has already been mentioned in this article: Aquion owned a factory with a 200 megawatt-hour capacity â€“ yet it was only producing 36 MWh. Demand was therefore far lower than anticipated, and the overhead costs of such a large factory were expensive. It is the lack of demand that is the final peg in the coffin for these companies. The market for long-duration storage batteries that Aquion was in the business of producing does not really exist. This is perhaps due to the ubiquitous lithium-ion battery; it is not cost-effective to use lithium-ion batteries for more than a 5 hour duration, and the market does not seek alternatives where they are not needed. Further still, the cost of lithium-ion batteries has been falling as of late. Next on the chopping block was Sungevity. Once again, investors dreamt of a nationwide solar-plus-storage channel. This vision ceasedÂ when the sources of funding for the company dried up before it was profitable. Issuing a Series E was not possible for Sungevity, and leadership also decided against releasing an IPO. Instead, management decided on a reverse merger with a Wall Street shell company in return for $200 million which was pushed back until the window of opportunity passed at the end of 2016. Before the company announced bankruptcy, two thirds of the workforce was laid off â€“ and this is after a group of staff was just terminated in January. What this says about the residential solar model is not yet clear, but the message does not seem to be fatal. While Sungevity followed in the footsteps of previous leaders in residential solar by remaining unprofitable for so long, this single instance is not enough to prove a trend. It is clear, however, that clean energy investors are impatient with regards to profitability setbacks. And as the market changes, profitability is ever-fleeting. They say bad news comes in threes. So, whoâ€™s next?",
                    "description": "The recent bankruptcies of two clean energy companies has kept the renewable energy sector on its toes. While these events may not be enough to provide a clear trend in the sector, it is keeping clean energy investors on their toes for what is to come in this industry.This past week has been difficult for clean energy due to the fact that two clean energy companies have filed for bankruptcy: Aquion, a saltwater battery maker, and Sungevity, a residential solar installer. These two instances of failure call into question the stability of the clean energy market, and reaffirm that there is not a wide margin for error for new companies in this space.In Aquionâ€™s beginning, their perceived potential was high enough that even Bill Gates contributed to the $190 million raised by investors on the promise that the company would be a shock to the advanced storage industry.The companyâ€™s supposed competitive advantage came in the form of nonflammable, nontoxic chemistry as an alternative to the industry standard of lithium-ion. The factory established in Pennsylvania was capable of producing 200 megawatt-hours per year. Unfortunately, only approximately 36 megawatt-hours had been produced by the end of 2016.Despite the numerous deals that Aquion boasted, the wind was sucked from its sails rather quickly. For instance, as recently as February 27th, the company announced a deal with Japanese Kyushu Electric Power to manufacture a solar-plus-storage system. Within merely two weeks, Aquion had filed for bankruptcy and is now searching for a buyer of its operating assets.The Aquion bankruptcy is a demonstration of the dangers of fundraising in energy innovation. Per usual, the Department of Energy funded the initial research phase at Carnegie Mellon University. As it scaled, the company began to attract high-profile investors. This combination of high growth potential and speedy financing are age-old ingredients in a recipe to grow too large too fast.Indeed, one piece of evidence supporting this overly-ambitious growth has already been mentioned in this article: Aquion owned a factory with a 200 megawatt-hour capacity â€“ yet it was only producing 36 MWh. Demand was therefore far lower than anticipated, and the overhead costs of such a large factory were expensive.It is the lack of demand that is the final peg in the coffin for these companies. The market for long-duration storage batteries that Aquion was in the business of producing does not really exist. This is perhaps due to the ubiquitous lithium-ion battery; it is not cost-effective to use lithium-ion batteries for more than a 5 hour duration, and the market does not seek alternatives where they are not needed. Further still, the cost of lithium-ion batteries has been falling as of late.Next on the chopping block was Sungevity. Once again, investors dreamt of a nationwide solar-plus-storage channel. This vision ceased when the sources of funding for the company dried up before it was profitable.Issuing a Series E was not possible for Sungevity, and leadership also decided against releasing an IPO. Instead, management decided on a reverse merger with a Wall Street shell company in return for $200 million which was pushed back until the window of opportunity passed at the end of 2016.Before the company announced bankruptcy, two thirds of the workforce was laid off â€“ and this is after a group of staff was just terminated in January.What this says about the residential solar model is not yet clear, but the message does not seem to be fatal. While Sungevity followed in the footsteps of previous leaders in residential solar by remaining unprofitable for so long, this single instance is not enough to prove a trend.It is clear, however, that clean energy investors are impatient with regards to profitability setbacks. And as the market changes, profitability is ever-fleeting. They say bad news comes in threes. So, whoâ€™s next?",
                    "Client Identifier": "testIdentifier"
                }
            ],
            "services": [
                # "FUbeeECsFTojsoB5LER13AJhIWi9tB4HxVWQqdlbwME",
                # "Z4Fq0TB1H77VU5DG8qXS8os1ayjdiSTqKVMxrWMvtj0",
                # "wZbDHxLoPqhTu8VIHvIHcztXihdCWf1OAA4VIOscDfY"
                "vbkY76AUSkOuVto0vt3yDHILWVEaHQACrIFauJYUsCc",
                "GDDIzK6gRdELHRgFR0CqyuM2a072TQI1zL28V2U6aXM",
                "z5uk2JhNQbFzdI3Ju5P9Th7D5tA8ZFWlb7Eycy8qQA4"
            ],
            "labels": [
                "category",
                "renewables",
                "techtrends"
            ]
        }
        headers = {'content-type': 'application/json'}

        self.client.post("/api/classifier/predict", data=json.dumps(payload), headers=headers)

    @task(2)
    def text_extract(self):
        payload = {
            "url": "http://www.cio.com/article/3052271/videos/twitter-beats-out-verizon-amazon-for-nfl-streaming-deal.html"
        }
        headers = {'content-type': 'application/json'}

        self.client.post("/api/text/extract", data=json.dumps(payload), headers=headers)

    @task(3)
    def keywords(self):
        payload = {
            "data": [
                {
                    "Post ID": 1,
                    "Post Title": "",
                    "Post Summary": "",
                    "Post Description": "Let’s face it. There is not going to be political or social revolution in Malaysia anytime soon—not for at least one generation. Here are the facts. Nearly 60% of Malaysians are apathetic to politics, with more than 70% of Malaysian youth aged between 19 to 24 years declared themselves as simply ‘not interested in politics’. Moreover,",
                    "Client Identifier": "Might"
                },
                {
                    "Post ID": 2,
                    "Post Title": "",
                    "Post Summary": "",
                    "Post Description": "THE SUSTAINABLE MANUFACTURING INNOVATION ALLIANCE WILL LEAD $140 MILLION INSTITUTE IN ROCHESTER, NEW YORK TO IMPROVE COMPETITIVENESS OF U.S. MANUFACTURING WASHINGTON — As part of the Manufacturing USA initiative, today the Energy Department announced its new Reducing Embodied-energy and Decreasing Emissions (REMADE) Institute, which will be headquartered in Rochester, New York and led by the",
                    "Client Identifier": "Might"
                }
            ],
            "column": "Post Description"
        }
        headers = {'content-type': 'application/json'}

        self.client.post("/api/parse/keywords", data=json.dumps(payload), headers=headers)


class WebsiteUser(HttpLocust):
    task_set = PredictBehavior
    min_wait = 5000
    max_wait = 10000
