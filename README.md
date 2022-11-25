

**IoT-based Predictive Oxygen Inventory Management**


**CONTENTS**


|**Chapter No.**|**Chapter Name**|**Page Number**|
| :-: | :-: | :-: |
|1|Introduction|1|
|2|Literature Review|2|
|3|Problem Statement|4|
|4|System Design and Requirements|5|
|5|Data Analytics Algorithm|7|
|6|Results|8|
|7|Conclusion and Future Scope|13|
||References|14|


**List of Abbreviations**


|**Sr. No.**|**Abbreviation**|**Full Form**|
| :-: | :-: | :-: |
|1.|LMIC|Low and Middle-Income Countries|
|2.|EKG|Electrocardiogram|
|3.|CSIO|Central Scientific Instruments Organization|



**List of Figures**


|**Fig. No.**|**Figure Name**|**Page No.**|
| :-: | :-: | :-: |
|4.1.1|System Description Workflow|5|
|6.1|Ubidots Interface|8|
|6.2|Ubidots history of POST values|9|
|6.3|Console Output on IOT device (Raspberry Pi)|10|
|6.4|Real time hypoxia count prediction|11|



**List of Tables**


|**Table. No.**|**Table Name**|**Page No.**|
| :-: | :-: | :-: |
|2.1|Review of Literature Summary|3|
|4.2.1|Requirements for Hardware Components|6|
|4.2.2|Requirements for Software Components|6|






**Chapter 1**

**Introduction** 


During the COVID-19 crisis, [1] India required about 8000 metric tonnes of medical oxygen per day Industrial oxygen up to an additional 6000 MT per day was diverted for medical use. The unprecedented numbers of preventable oxygen starvation deaths during the COVID-19 pandemic have highlighted that the current model [1] of obtaining medical oxygen is unsound and dysfunctional. The Ministry of Health and Family Welfare states [2] because supplies are fixed in the very near term, prices may increase significantly, making oxygen unaffordable and increasing the mortality rate among the really poor. As a result, an IoT-based predictor model that can foresee oxygen requirements can be utilized to help the supply chain get ready for future demand, which can help prevent catastrophic harm to human life during an unforeseen emergency.

Access to affordable, reliable oxygen in low- and middle-income nations has become more difficult since the pandemic's beginning. With hospitals in many LMICs running out of oxygen, COVID-19 has put enormous pressure on health systems, leading to avoidable fatalities and hospitalized patients' families having to pay more for limited oxygen supply.

Despite being a necessary drug for the effective treatment of COVID-19 hospital patients, access to oxygen is restricted in LMICs because of the expense, lack of infrastructure, and logistical challenges. Health care institutions frequently lack access to the oxygen they need, which results in needless fatalities.

[5] The Access to COVID Tools Accelerator Therapeutics pillar (co-led by Unitaid and Wellcome) is taking on a new role to coordinate and advocate for increased supply of oxygen, and, in partnership with a WHO-led consortium, is today announcing the launch of a COVID-19 Oxygen Emergency Taskforce. This is done in recognition of the central importance of sustainable oxygen supply - along with therapeutic products like dexamethasone - for the treatment of COVID. The developed model seeks to assist agencies like the COVID-19 emergency task force in determining a hospital's oxygen needs.


**Chapter 2**

**Literature Review**


`		`[1] Physician's role is to provide assurance of oxygen delivery to vital organs. State of the art monitoring extends to following indirect parameters of oxygen transport such as heart rate via EKG or plethymograph. The commercial availability of solid state components such as the microprocessor, light emitting diodes, and miniaturized photo-detectors has made possible the application of classical spectrophotometric techniques of measuring oxygen saturation.

`		`[2] CSIO has developed a pulse oximeter that measures the oxygen saturation (SaO/sub 2/) of arterial blood and pulse rate. The ratio of red and infrared signals after normalization is calculated and is related to arterial oxygen saturation. System operates at 400 Hz which is locked with power line frequency. It also gives alarm conditions if the probe is accidentally disconnected from the finger. MAX-30100 sensor works on the same principle for calculating arterial oxygen saturation. It works on the I2C protocol; it combines 2 LEDs a photo detector, optimized optics and a low noise analog signal processing circuit to detect pulse oximetry and heart rate signals.

`		`[3] Embedded software and IoT hardware prototypes have been produced in the past, but their costs have not been sufficiently reduced for widespread use. We created and evaluated a pulse rate and blood oxygen monitor using an Atmel ATmega 328P MCU and MAX30100 sensor package. In order to compare the results with a commercially available Rossmax SB150 pulse oximeter, we used the device on 12 participants. A minimal variance of 0.425% for blood oxygen and 0.8175% for pulse rate was found, confirming the precision of our algorithm and implementation. Cost study reveals that implementation can be completed for approximately $12.

`		`[4] The inventory control problem is to predict the demand variations in real-time. The work presents a novel solution using a reinforcement learning model that manages Internet of Things (IoT) devices. The accurate predictions of inventory variations play a key role in reducing the overhead of inventory management. The work presented in this paper aids in developing a model capable of predicting demand variations for oxygen in real time. 


**Table: 2.1** Review of Literature Summary

|**Sr No**|**IEEE Paper**|**Purpose**|
| :-: | :-: | :-: |
|[1]|Yelderman M., Corenmen J. (1983) Real Time Oximetry. In: Prakash O. (eds) Computing in Anesthesia and Intensive Care. Developments in Critical Care Medicine and Anesthesiology, vol 5. Springer, Dordrecht. https://doi.org/10.1007/978-94-009-6747-2\_26|To develop a monitor to accurately record data in real time and to measure arterial blood oxygen saturation.|
|[2]|R. C. Gupta, S. S. Ahluwalia and S. S. Randhawa, "Design and development of pulse oximeter," Proceedings of the First Regional Conference, IEEE Engineering in Medicine and Biology Society and 14th Conference of the Biomedical Engineering Society of India. An International Meet, 1995, pp. 1/13-1/16, doi: 10.1109/RCEMBS.1995.508670.|<p>To explain the working of Pulse Oximeter</p><p></p>|
|[3]|N. B. Ahmed, S. Khan, N. A. Haque and M. S. Hossain, "Pulse Rate and Blood Oxygen Monitor to Help Detect Covid-19: Implementation and Performance," 2021 IEEE International IOT, Electronics and Mechatronics Conference (IEMTRONICS), 2021, pp. 1-5, doi: 10.1109/IEMTRONICS52119.2021.9422520.|To implement the use case of Pulse Oximeter on a larger scale.|
|[4]|M. Naveed, M. Adnan, I. Ahmed and Y. Javed, "Smart IoT based Demand Variation Prediction Model," 2019 Sixth HCT Information Technology Trends (ITT), 2019, pp. 296-299, doi: 10.1109/ITT48889.2019.9075066.|Smart IoT based Demand Variation Prediction Model|















**Chapter 3**

**Problem Statement**


To create a predictive inventory management system based on the Internet of Things that will allow hospital oxygen demand to be forecasted based on pulse oximeter measurements.

- To develop and build an IoT based patient monitoring system.

- To create a predictor model that combines IoT and machine learning.

- To forecast inventory load using the predictor model























**Chapter 4**

**System Design and Requirements**


**4.1 System Design**

![](Aspose.Words.920432f0-e54b-4b99-b14f-5df87edef25c.002.png)

**Figure: 4.1.1** System Description workflow

The developed IoT system's system description is shown in figure 4.1.1. It is made up of three main parts: the Raspberry Pi (an Internet of Things device), Ubidots Cloud (a cloud service provider), and Flask Front End (Front end web server). The raspberry pi device is programmed to increase a counter variable named the "hypoxia counter" when the sensor detects a spo2 value below 90. The data production takes place at the maximum 30100 sensor and is powered by the raspberry pi. For 30 seconds, the machine will measure the patient once every second. This presumption is made in order to simulate a real-world scenario for the model that has been constructed. The 'hypoxia counter' variable is payloaded to the ubidots api and submitted to the ubidots cloud through an API POST request after the inner loop of 15 seconds is finished. The 'pulseoxy' device variable on the cloud is updated after a successful post. The front end web server sends a GET request to ubidots at the same time the device variable is updated, bringing real-time data into the server.

**4.2 Requirements**

**Hardware Components**

**Table: 4.2.1** Requirements for Hardware Components

|**Components**|**Quantity**|**Cost (in Rs)**|
| :-: | :-: | :-: |
|Raspberry Pi|1|2000|
|MAX30100 Module|1|300|
|Connecting Wires|10|20|
|||Total Cost = 2320|


**Software Components:**

**Table: 4.2.2** Requirements for Software Components

|**Components**|**Quantity**|**Cost (in Rs)**|
| :-: | :-: | :-: |
|Python IDLE|1|0|
|Google Colab|1|0|
|UbiDots|1|0|
|Flask|1|0|









**Chapter 5**

**Data Analytics**


**5.1 Data Analytics**

To perform regression analysis on the dataset generated by OurWorldInData.org for India during the Covid-19 pandemic. The front end server is equipped with a recurrent neural network model which was trained on a modified dataset from world statistics. It consists of real world data of Covid-19 pandemic cases from 2020-2022. The following modifications were performed on the dataset, and added a new column called rate of change of hypoxia cases. This was done in order to find a pattern to train the RNN model in such a way that it is able to predict future cases by understanding the pattern of previous count of hypoxia patients.

The flask server after performing a get request pushes the value into an Int Array. This population mechanism continues for a duration of 15 seconds, after the population is completed. The RNN model is called with the populated array as input, the returned result is then used for calculating the predicted oxygen requirement for the hospital. The timeout of 15 seconds on the flask server and timeout of 15 seconds on the IoT device creates a total timeout of 30 seconds. This time window is used to a scaled simulation of the developed model in a real world hospital scenario.

**5.2 Algorithm**

**Recurrent Neural Network**

Recurrent Neural Network(RNN) is a type of Neural Network where the output from the previous step is fed as input to the current step. In traditional neural networks, all the inputs and outputs are independent of each other, but in cases like when it is required to predict the next word of a sentence, the previous words are required and hence there is a need to remember the previous words. Thus RNN came into existence, which solved this issue with the help of a Hidden Layer. The main and most important feature of RNN is the Hidden state, which remembers some information about a sequence.

RNN has a “memory” which remembers all information about what has been calculated. It uses the same parameters for each input as it performs the same task on all the inputs or hidden layers to produce the output. This reduces the complexity of parameters, unlike other neural networks.

**Chapter 6**

**Results**


![](Aspose.Words.920432f0-e54b-4b99-b14f-5df87edef25c.003.png)

**Fig 6.1:** Ubidots Interface


The dashboard in the ubidots interface displays the most recent activity and summary for each IoT device label. As seen in figure 6.1, a device variable called "pulseoxy" was generated with the recent hypoxia count of 102, which was posted to the ubidots cloud 11 minutes prior to the time of capture. The data in-stream or variable status can be checked using this interface on the ubidots cloud server in real time.


![](Aspose.Words.920432f0-e54b-4b99-b14f-5df87edef25c.004.png)

**Fig 6.2:** Ubidots history of POST values


A line graph representing a summary of the variable data is shown in figure 6.2. The dashboard window displays the previous 30 post data obtained from the IoT device through the help of ubidots api. There are four columns in the summary table: date, value, context, and actions. The date and GMT time, converted to IST, are given in the date column. The value column displays the variable data for that specific time period. The context column is empty because the context string was left out of the post request to the ubidots cloud via the API.

![](Aspose.Words.920432f0-e54b-4b99-b14f-5df87edef25c.005.png)

**Fig 6.3:** Console Output on IOT device (Raspberry Pi)


Figure 6.3 shows the Raspberry Pi-based Internet of Things device's Python shell prompt. The system is set up so that it counts the number of times a SpO2 reading of 89 or lower is observed and increases the variable hypoxia for 15 seconds. This was done in order to simulate the functionality of the created IoT system and neural network model in an actual environment. The IoT device therefore assumes that each patient is being monitored for exactly one second, and this cycle repeats for 15 seconds, which is assumed to be one day's worth of measurements from a fictitious hospital. The ubidots api is then used to package this as a POST request to the ubidots cloud. Every 15 seconds, a successful post request is made, and with it comes a print statement with the API status code, which is either 200 for success or 400 for failure.

![](Aspose.Words.920432f0-e54b-4b99-b14f-5df87edef25c.006.png)

![](Aspose.Words.920432f0-e54b-4b99-b14f-5df87edef25c.007.png)

**Fig 6.4:** Real time hypoxia count prediction graph

The Fig. 6.4 is a real time performance descriptor which is displayed on the front end web server. It is generated in real time by use of stream processing technique, by fetching real time data from ubidots cloud through API-GET request. It has two major functional components, blue line which is predicted cases generated by the RNN which tries to predict future demand on the hospital by the help of the IoT device values, which is depicted by the red line. The number of days is shown on the x-axis, while the number of hypoxia instances is shown on the y-axis. The graph is a visual performance description that displays how well the recurrent neural network model performs. The original cases line (red), which was constructed using real-time data from the IoT device, must match exactly with the forecasted cases line (blue). It is clear that as the model grows and develops with more cases, the predicted values match those of the original cases.

The recurrent neural network model has a bias of estimating the hypoxia cases to be really high at the start of the prediction time cycle. This is due to the fact that, in 2020 the covid pandemic saw an exponential increase in hypoxia patients in a really short period of time, Hence it developed the mentioned bias during the initial prediction cycle. This bias is gradually removed as the cycle continues and the model matures and learns the patterns of the new incoming data.

**Chapter 7**

**Conclusion and Future Scope** 


**7.1 Conclusion**

The economical pulse oximeter is proposed and developed to store real-time SpO2 and oximetry vitals that will subsequently be utilized to perform regression analysis and forecast the hospital's oxygen needs. The telemetry data is sent to the web server through the means of stream processing, the results are then shown on an Flask Web Server. The cost-efficient pulse oximeter could be recreated with ease with the provided technical and theoretical resources as mentioned above. The device may be upgraded with new features because the Raspberry Pi it uses is reprogrammable. 

The sensor's accuracy is confirmed by the data and analysis and is about 97.11% to 98.84%. More parameters might be integrated to create a larger monitoring and detection system to combat Pneumonia and Covid. The device is affordable, according to the cost study. This paper is likely to contribute to the development of cheap health-parameter measurement technology.

**7.2 Future Scope**

A real-time clock or a timer, which might be added for a schedule checking, are examples of future scope. By creating a dataset with a day-by-day rate of change in the number of hypoxia patients, the model can be improved and ensure more precise demand forecasting. 

The system should ideally be a comprehensive mesh network of pulse oximeters supplying real-time oximetry results to a central web server in order to predict the future need of the hospitals, however we have used a single sensor node to demonstrate the system's shortcomings.

The developed smart pulse oximeter is based on Raspberry Pi with a breadboard base for connection, which is not a portable model. Hence the smart pulse oximeter is not portable.

**References** 


[1] Yelderman M., Corenmen J. (1983) Real Time Oximetry. In: Prakash O. (eds) Computing in Anesthesia and Intensive Care. Developments in Critical Care Medicine and Anesthesiology, vol 5. Springer, Dordrecht. https://doi.org/10.1007/978-94-009-6747-2\_26

[2] R. C. Gupta, S. S. Ahluwalia and S. S. Randhawa, "Design and development of pulse oximeter," Proceedings of the First Regional Conference, IEEE Engineering in Medicine and Biology Society and 14th Conference of the Biomedical Engineering Society of India. An International Meet, 1995, pp. 1/13-1/16, doi: 10.1109/RCEMBS.1995.508670.

[3] N. B. Ahmed, S. Khan, N. A. Haque and M. S. Hossain, "Pulse Rate and Blood Oxygen Monitor to Help Detect Covid-19: Implementation and Performance," 2021 IEEE International IOT, Electronics and Mechatronics Conference (IEMTRONICS), 2021, pp. 1-5, doi: 10.1109/IEMTRONICS52119.2021.9422520.

[4] M. Naveed, M. Adnan, I. Ahmed and Y. Javed, "Smart IoT based Demand Variation Prediction Model," 2019 Sixth HCT Information Technology Trends (ITT), 2019, pp. 296-299, doi: 10.1109/ITT48889.2019.9075066.

[5] WHO, [online]., Available:

https://www.who.int/news/item/25-02-2021-covid-19-oxygen-emergency-impacting-more-than-half-a-million-people-in-low--and-middle-income-countries-every-day-as-demand-surges

(Accessed: September 20, 2022)

[6] Scroll Investigation, [online]. Available:

https://scroll.in/article/992928/how-grave-is-indias-oxygen-emergency-worse-than-the-government-admits (Accessed: July 19, 2022)

[7] Ministry of Health and Family Welfare, [online]. Available:

https://pib.gov.in/PressReleasePage.aspx?PRID=1711922 (Accessed: July 19, 2022)

[8] HowToElectronics, [online]. Available:

https://how2electronics.com/blood-oxygen-heart-rate-monitor-max30100-arduino/ (Accessed: July 17, 2022)
