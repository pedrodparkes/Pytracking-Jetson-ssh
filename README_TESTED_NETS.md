





### Start visdom http://192.168.1.149:8097/
```shell
ssh jetson
visdom
```

TaMOs (WACV 2024)
```shell
tamos tamos_resnet50
tamos tamos_swin_base

  File "/home/pedro/Pytracking-Jetson-ssh/pytracking/evaluation/tracker.py", line 395, in run_video_generic
    out = tracker.track(frame, info)
  File "/home/pedro/Pytracking-Jetson-ssh/pytracking/tracker/tamos/tamos.py", line 157, in track
    self.frame_num += 1
AttributeError: 'TaMOs' object has no attribute 'frame_num'
```
    
    

RTS (ECCV 2022), 
    rts rts50 /tmp/3.mov --debug 2

ToMP (CVPR 2022) 
```shell
tomp tomp50 /tmp/3.mov --debug 2
tomp tomp101 /tmp/3.mov --debug 2
```

KeepTrack (ICCV 2021) - failing often
```shell
keep_track default /tmp/3.mov --debug 2
keep_track default_fast /tmp/3.mov --debug 2
```

LWL (ECCV 2020)
```shell
keep_track default /tmp/3.mov --debug 2
keep_track default_fast /tmp/3.mov --debug 2
```

KYS (ECCV 2020)
```shell
kys default /tmp/3.mov --debug 2

  File "/home/pedro/Pytracking-Jetson-ssh/ltr/models/kys/cost_volume.py", line 5, in <module>
    from spatial_correlation_sampler import SpatialCorrelationSampler
ModuleNotFoundError: No module named 'spatial_correlation_sampler'
```
PrDiMP (CVPR 2020) 

DiMP (ICCV 2019)
```shell
dimp dimp18 /tmp/3.mov --debug 2
dimp dimp50 default_fast /tmp/3.mov --debug 2
```

DiMP_Simple
```shell
dimp super_dimp_simple /tmp/3.mov --debug 2
```

ATOM (CVPR 2019)



