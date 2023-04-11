In [ercf] module enable section
encoder_resolution: 1.346348 # 1000 11

In save variables file
ercf_calib_0 = 1.0
ercf_calib_1 = 0.997799885869
ercf_calib_10 = 0.99711646129
ercf_calib_11 = 0.999855792227
ercf_calib_2 = 1.00054297834
ercf_calib_3 = 1.00054297834
ercf_calib_4 = 0.998484247931
ercf_calib_5 = 1.00123110969
ercf_calib_6 = 1.00054297834
ercf_calib_7 = 0.999855792227
ercf_calib_8 = 1.0026102159
ercf_calib_9 = 0.999855792227
ercf_calib_ref = 1147.088496


NOW:
In [ercf] module enable section
encoder_resolution: 1.411233 # per ERCF_CALIBRATE_ENCODER on 06APR23  https://i.imgur.com/zbv04FR.png

In save variables file
ercf_calib_0 =   1.0
ercf_calib_1 =   0.9984842479308441
ercf_calib_10 =  1.0039931265401176
ercf_calib_11 =  1.001231109685812
ercf_calib_2 =   1.0005429783389488
ercf_calib_3 =   1.001231109685812
ercf_calib_4 =   0.9998557922274524
ercf_calib_5 =   1.001231109685812
ercf_calib_6 =   1.0033011946817165
ercf_calib_7 =   1.0005429783389488
ercf_calib_8 =   1.0053798573778803
ercf_calib_9 =   1.0039931265401176
ercf_calib_ref = 1151.1275400000002


RESTART
ERCF_HOME
ERCF_TEST_LOAD_SEQ to verify that all is right with the filament and carts
https://i.imgur.com/BQFZxJV.png

ERCF_HOME
ERCF_SELECT_TOOL_dbg TOOL=0
ERCF_CALIBRATE_ENCODER
https://i.imgur.com/dHK82zF.png
manually apply the resultant value to ERCF Enablement in MCU file(s)

RESTART
ERCF_HOME
ERCF_CALIBRATE
https://i.imgur.com/qacYXEA.png
RESTART when prompted
New calib figures now in svv

doing some maths on the results: https://i.imgur.com/x1HZErJ.png