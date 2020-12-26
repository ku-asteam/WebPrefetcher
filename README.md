# WebPrefetcher
Predictive Prefetching Engine for Web Applications

## Introduction

Predictive Prefetching Engine in WebPrefetcher is an implementation of *a*STEAM Project (Next-Generation Information Computing Development Program through the National Research Foundation of Korea (NRF) funded by the Ministry of Science and ICT; <https://asteam.korea.ac.kr>) 's Web prefetching engine over Browsertime. The function of this software is to preload the contents of prefetching targets by utilizing user iteraction data for predictions.

## Requirements and Dependencies

* *Browsertime*: The version of `7.2.2` is recommended
* *Prefetching Scenario Data* after preprocessed and transformed into the form suitable for pre-scripts executed by Browsertime
* Other Python packages should be installed and imported properly

## Instructions

* Prepare the prefetching scenario data in the `scenario` directory
* Set the parameters for network profile, prefetching type, Web browser, number of iterations, viewport size, etc.
* Execute `run.py` to launch Web page loading with predictive prefetching for each scenario and check the results for various quality of experience (QoE) metrics
* See the example of executing WebProfiler (top_k=3, network_profile=cable, prefetching_type=prefetch, iter_opt=3):
```
[run.py] Starting Docker networks                                                                         
575f6f2ef36aa0a2c81de2fdbdf5c143a0c502cd5ecaa4fe0c88c6aac3822cc3                                          
69474f77623b43edffcd0faf9dd48c77b956694b733cd1e34b3fdbfce7be2669                                          
4b2b6ff53ec506b0a2e51ca952bf4f7872d0a237a3aa4e0cea4560c9846c6bc0                                          
cef607adbf94abb5d2516de0a961ea513e52f4f86e1c9c4d6470ce84b352fc80                                          
[run.py] Scenario file loaded: ./scenario/top3_scenario.json                                              
[run.py]  - top_k: 3                                                                                      
[run.py]  - n_scenario: 5                                                                                 
[run.py]  - test_precition: 0.800000                                                                      
[run.py]  - test_recall: 0.800000                                                                         
[run.py]  - test_f-measure: 0.800000                                                                      
[run.py] ********* (cable, 1/5) - Start *********                                                         
[run.py] ********* (cable, prefetch) - Start *********                                                    
Google Chrome 78.0.3904.87                                                                                
Mozilla Firefox 70.0                                                                                      
[2020-12-26 01:15:12] INFO: Running tests using Chrome - 3 iteration(s)                                   
[2020-12-26 01:15:12] INFO: Starting the preScript of pre.js                                              
[2020-12-26 01:15:12] INFO: Prefetch lisetd URLs as the given scenario                                    
[2020-12-26 01:15:12] INFO: Inputs loaded: 3 URLs [https://www.daum.net/,https://nyaa.si/,https://www.nave
r.com/] (19 - 1 = 18ms)                                                                                   
[2020-12-26 01:15:12] INFO: Main window: about:blank (CDwindow-F6CAF9188A75CFD4842F91DA0B43DEF6)          
[2020-12-26 01:15:14] INFO: After prefetching (partial & predict): 1559 ms                                
[2020-12-26 01:15:14] INFO: Finishing the preScript of pre.js                                             
[2020-12-26 01:15:14] INFO: Testing url https://www.daum.net/ iteration 1                                 
[2020-12-26 01:15:37] INFO: https://www.daum.net/ BackEndTime: 101 DomInteractiveTime: 548 DomContentLoade
dTime: 548 FirstPaint: 352 PageLoadTime: 831                                                              
[2020-12-26 01:15:37] INFO: VisualMetrics FirstVisualChange: 334 SpeedIndex: 897 PerceptualSpeedIndex: 537
 ContentfulSpeedIndex: 753 LastVisualChange: 4134                                                         
[2020-12-26 01:15:38] INFO: Starting the preScript of pre.js                                              
[2020-12-26 01:15:38] INFO: Prefetch lisetd URLs as the given scenario                                    
[2020-12-26 01:15:38] INFO: Inputs loaded: 3 URLs [https://www.daum.net/,https://nyaa.si/,https://www.nave
r.com/] (19 - 1 = 18ms)                                                                                   
[2020-12-26 01:15:38] INFO: Main window: about:blank (CDwindow-0C7D616D90E9D208F1B5A99ADFC954A1)          
[2020-12-26 01:15:40] INFO: After prefetching (partial & predict): 1852 ms                                
[2020-12-26 01:15:40] INFO: Finishing the preScript of pre.js                                             
[2020-12-26 01:15:40] INFO: Testing url https://www.daum.net/ iteration 2                                 
[2020-12-26 01:16:05] INFO: https://www.daum.net/ BackEndTime: 35 DomInteractiveTime: 361 DomContentLoaded
Time: 361 FirstPaint: 274 PageLoadTime: 2471                                                              
[2020-12-26 01:16:05] INFO: VisualMetrics FirstVisualChange: 300 SpeedIndex: 724 PerceptualSpeedIndex: 575
 ContentfulSpeedIndex: 694 LastVisualChange: 7500                                                         
[2020-12-26 01:16:06] INFO: Starting the preScript of pre.js                                              
[2020-12-26 01:16:06] INFO: Prefetch lisetd URLs as the given scenario                                    
[2020-12-26 01:16:06] INFO: Inputs loaded: 3 URLs [https://www.daum.net/,https://nyaa.si/,https://www.nave
r.com/] (19 - 1 = 18ms)                                                                                   
[2020-12-26 01:16:06] INFO: Main window: about:blank (CDwindow-7EACFC7B406C76FA6D6CFBE1830997C8)          
[2020-12-26 01:16:07] INFO: After prefetching (partial & predict): 1469 ms                                
[2020-12-26 01:16:07] INFO: Finishing the preScript of pre.js                                             
[2020-12-26 01:16:07] INFO: Testing url https://www.daum.net/ iteration 3                                 
[2020-12-26 01:16:36] INFO: https://www.daum.net/ BackEndTime: 35 DomInteractiveTime: 477 DomContentLoaded
Time: 477 FirstPaint: 371 PageLoadTime: 2111                                                              
[2020-12-26 01:16:36] INFO: VisualMetrics FirstVisualChange: 400 SpeedIndex: 963 PerceptualSpeedIndex: 603
 ContentfulSpeedIndex: 817 LastVisualChange: 4133                                                         
[2020-12-26 01:16:36] INFO: https://www.daum.net/ 131 requests, backEndTime: 57ms (±17.96ms), firstPaint: 
332ms (±24.23ms), firstVisualChange: 345ms (±23.97ms), DOMContentLoaded: 462ms (±44.50ms), Load: 1.80s (±4
06.32ms), speedIndex: 861 (±58.18), visualComplete85: 1.58s (±168.04ms), lastVisualChange: 5.26s (±916.25m
s), rumSpeedIndex: 3056 (±36.31) (3 runs)                                                                 
[2020-12-26 01:16:36] INFO: Wrote data to output/top3_cable_prefetch_0                                    
[run.py] ********* (cable, 1/5) - End *********
```
...
```
[run.py] ********* (cable, 5/5) - Start *********                                                         
[run.py] ********* (cable, prefetch) - Start *********                                                    
Google Chrome 78.0.3904.87                                                                                
Mozilla Firefox 70.0                                                                                      
[2020-12-26 01:20:09] INFO: Running tests using Chrome - 3 iteration(s)                                   
[2020-12-26 01:20:10] INFO: Starting the preScript of pre.js                                              
[2020-12-26 01:20:10] INFO: Prefetch lisetd URLs as the given scenario                                    
[2020-12-26 01:20:10] INFO: Inputs loaded: 3 URLs [https://www.daum.net/,https://www.google.com/search,htt
p://www.yes24.com/Main/default.aspx] (2414 - 0 = 2414ms)                                                  
[2020-12-26 01:20:10] INFO: Main window: about:blank (CDwindow-9ADBAB6264C723A23ADF6F09D1C69858)          
[2020-12-26 01:20:13] INFO: After prefetching (partial & predict): 2589 ms                                
[2020-12-26 01:20:13] INFO: Finishing the preScript of pre.js                                             
[2020-12-26 01:20:13] INFO: Testing url https://www.daum.net/ iteration 1                                 
[2020-12-26 01:20:41] INFO: https://www.daum.net/ BackEndTime: 490 DomInteractiveTime: 1692 DomContentLoad
edTime: 1692 FirstPaint: 1219 PageLoadTime: 2959                                                          
[2020-12-26 01:20:41] INFO: VisualMetrics FirstVisualChange: 1200 SpeedIndex: 1756 PerceptualSpeedIndex: 1
409 ContentfulSpeedIndex: 1613 LastVisualChange: 5234                                                     
[2020-12-26 01:20:42] INFO: Starting the preScript of pre.js                                              
[2020-12-26 01:20:42] INFO: Prefetch lisetd URLs as the given scenario                                    
[2020-12-26 01:20:42] INFO: Inputs loaded: 3 URLs [https://www.daum.net/,https://www.google.com/search,htt
p://www.yes24.com/Main/default.aspx] (2414 - 0 = 2414ms)                                                  
[2020-12-26 01:20:42] INFO: Main window: about:blank (CDwindow-214C850320AE1267D9C38FF4950135B9)          
[2020-12-26 01:20:44] INFO: After prefetching (partial & predict): 2564 ms                                
[2020-12-26 01:20:44] INFO: Finishing the preScript of pre.js                                             
[2020-12-26 01:20:44] INFO: Testing url https://www.daum.net/ iteration 2                                 
[2020-12-26 01:21:05] INFO: https://www.daum.net/ BackEndTime: 300 DomInteractiveTime: 762 DomContentLoade
dTime: 762 FirstPaint: 637 PageLoadTime: 1051                                                             
[2020-12-26 01:21:05] INFO: VisualMetrics FirstVisualChange: 667 SpeedIndex: 1165 PerceptualSpeedIndex: 85
1 ContentfulSpeedIndex: 1047 LastVisualChange: 4400                                                       
[2020-12-26 01:21:06] INFO: Starting the preScript of pre.js                                              
[2020-12-26 01:21:06] INFO: Prefetch lisetd URLs as the given scenario                                    
[2020-12-26 01:21:06] INFO: Inputs loaded: 3 URLs [https://www.daum.net/,https://www.google.com/search,htt
p://www.yes24.com/Main/default.aspx] (2414 - 0 = 2414ms)                                                  
[2020-12-26 01:21:06] INFO: Main window: about:blank (CDwindow-43CEA659BF17DAD44BBB621FE7E8299E)          
[2020-12-26 01:21:08] INFO: After prefetching (partial & predict): 2597 ms                                
[2020-12-26 01:21:08] INFO: Finishing the preScript of pre.js                                             
[2020-12-26 01:21:08] INFO: Testing url https://www.daum.net/ iteration 3                                 
[2020-12-26 01:21:29] INFO: https://www.daum.net/ BackEndTime: 141 DomInteractiveTime: 792 DomContentLoade
dTime: 792 FirstPaint: 664 PageLoadTime: 1089                                                             
[2020-12-26 01:21:29] INFO: VisualMetrics FirstVisualChange: 667 SpeedIndex: 1207 PerceptualSpeedIndex: 86
2 ContentfulSpeedIndex: 1047 LastVisualChange: 4433                                                       
[2020-12-26 01:21:29] INFO: https://www.daum.net/ 119 requests, backEndTime: 310ms (±82.37ms), firstPaint:
 840ms (±154.86ms), firstVisualChange: 845ms (±145.06ms), DOMContentLoaded: 1.08s (±249.13ms), Load: 1.70s
 (±514.20ms), speedIndex: 1376 (±155.45), visualComplete85: 1.99s (±229.17ms), lastVisualChange: 4.69s (±2
22.63ms), rumSpeedIndex: 1893 (±682.19) (3 runs)                                                          
[2020-12-26 01:21:29] INFO: Wrote data to output/top3_cable_prefetch_4                                    
[run.py] ********* (cable, 5/5) - End *********                                                           
[run.py] Stopping Docker networks                                                                         
cable                                                                                                     
3g                                                                                                        
3gfast                                                                                                    
3gslow
```
