# V2.2526_Config
Repo for the Klipper Config directory of my Voron V2.4 (not v2.4r2) SN 2526, a 350^3 model built by ~MHz (myself) in 4Q21.

Useful Links:
- https://jinja.palletsprojects.com/en/2.10.x/templates/
- https://www.klipper3d.org/Overview.html
- https://github.com/Klipper3d/klipper
- https://github.com/VoronDesign/Voron-2/raw/Voron2.4/Manual/Assembly_Manual_2.4r2.pdf
- https://docs.vorondesign.com/
- https://klipper.discourse.group/
- Nice Klipper macro tutorial from Mental: https://klipper.discourse.group/t/macro-creation-tutorial/30

Spring 2022:  Be advised that I continue to muck with things related to the ERCF.  One of my findings
is that repeatedly yanking hot filament up through the hot end contributes to heat creep.  After having
fought heat creep with my Dragon HF HE on a traditional AB setup, having installed 'the dragon duct' to
ward off heat creep in a non-ercf context, I was good.  However, with the ERCF install, it has come back.
As such, I have installed a Dragon WHF - a water cooled HF HE.  One can glean a bit of info in Discord:
https://discord.com/channels/877549316913365083/928716501480009768/963178294424006767 and
https://discord.com/channels/460117602945990666/830395563094442044/966138287905443880 (VD's Phaetus Ch)
https://i.imgur.com/eYwYVdl.png <-- image of my mainsail instance.

Voron Kit Feedback Server Invite:  https://bit.ly/3igPTpJ (resolves to https://discord.com/invite/RyAGnb9y3G)
My Formbot printer kit feedback ch: https://discord.com/channels/877549316913365083/885942140012744744
My ERCF DFH Kit feedback ch: https://discord.com/channels/877549316913365083/928716501480009768

FYSA (24Feb2022):  Be advised that these configs are a big Work In Process (WIP).  The printer is a new
build in Nov 2021.  Further, I recently added a 12-cart ERCF with ERCPs.  And, commensurate with the ERCF,
I have migrated over to Prusa Slicer from Cura Slicer (which I have used for years), so I am working to 
massage these config files to conform to the workflow that I had initially established with Cura.  Just
so y'all know about same...  Usual disclaimers apply.  YMMV.  blah blah blah.

DISCLAIMER:  I am not at fault if your use of these info/data/code/macros/configs result in injury/damage/issues/etc.
Your use of these info/data/code/macros/configs acknowledges these risks and indicates a full imdemnification
of myself from any potential outcomes of your decision to use the info/data/code/macros/configs presented herein.

Printer Details, for those who may be interested:
- Watercooled Phaetus WHF High Flow Hot End, with Phaetus WaterCooler Pump/Radiator/Fan Kit
  - I supplemented the latter with a stand-alone temp sensor/indicator ()
  - And I've added sensors to enable programmatic indication of the 'H2O' cooling system in Klipper
  - Further, I changed the kit wiring to enable PWM of the pump and to provide pump tach feedback to Klipper
  - Finally (I think), I replaced the kit fan (2-wire 92mm, loud AF) with a Noctua () which is MUCH quieter. 
- 12-cart ERCF with ERCPs - ERCF mounted to back, ERCPs are on a rack collocated IVO printer
- ERCP imputed use of a tool-head filament detector switch which I folded into the design of the
  Orbiter v1.5 adapter
- 7OW/PT1000 AB Print Head housing a Phaetus Dragon HF HE with an Orbiter Extruder fitted thereto.
- An accelerometerized AB Toolhead PCB was designed, built and installed, oriented to clear stuffs
- The thermistor that is normally on the TH PCB has been removed, with wires affixed thereto to allow for the placement of the PCB Chamber Temp Sens=0805 10K 1% B=3950K(25/50C) in the AB duct by way of a JST connector pair - have fan set to default to 10% to keep air flowing over the sensor
- HE0=HE_HTR, HE3=HOUR_METER
- M0=B, M1=A, M2.1=Z0, M3=Z1, M4=Z2, M5=Z3, M6=E
- F0=PCF, F1=HEF, F2=Aft Chassis (MCU), F3=Fore Chassis (PS), F4=Exhaust, F5=Filter/Stir, F6=5VDC PS (12V), F6=StepperDriver (12V)
- DIAG0=XES, DIAG1=YES, DIAG2=ZES, DIAG3=PL-08 Bed Sens (blocking diode on AB PCB)
- DIAG4=SFS
- RGB LED IO (PB0) used for 'dashboard' neopixels
- TB=BED, T0=HE, T1=AB_PCB(CHAMBER), T2=3950 bead @ top of chamber ivo exhaust, T3=3950 bead @ unswitched 5VDC PS
- Display Aural Xdcr on uC IO PE8
- RP2040 installed as MCU2:  ADXL I/F, I/F for 228ea DotStar LEDs for chamber lighting, data for ERCF Neopixels, and Power Switch's RGB Halo Light Control
 
See the /V2.2526_Hardware/ folder for further details.

>>> LOOK >>> Also, be advised that this set of configs requires manual installation of some components on top of a fresh install of the host OS and Klipper/Moonraker/Mainsail:

A) Kiauh's 'shell_commands' [an unofficial extension], 
  - Shell_Commands is used herein to facilitate execution of config_blah.sh scripts which enables the automagic push and pull of these config files, as well as my nozzle cam v4l2 settings, and some other UI goodness such as macro buttons to kick off curl commands to control external devices such as my Wyze Cam day/night modes and smart outlets for the printer and the external enclosure I have.

B) Klicky & the related 'z_calibration',

C) LED_Effects, (31mar22 - recent klipper LED updates breaks LED effects - reportedly to be worked on in the coming days to fix it)

D) Git (done at host's OS level)

Also, with Alex's help (Discord @ALEX#8260, THANK YOU!), I was able to get an automated construct setup such that:

1) On every boot, the config_pull.sh script runs (see _startup_autoexec.cfg) and pulls down changes from the git repo.
  - in case I make changes that are pushed directly to the repo from elsewhere other than the printer config_push.sh script.
  - If config changes are indeed downloaded as a result of the check, upon completion of the download, Klipper service restarts.
  
2) On print_end event, the config_push.sh script runs to push a snapshot of the printer's current config out to the git repo.
  - I am still cogitating on what other, if any, events to use to trigger a config backup.
  
These activities are codified in those scripts and the associated backups of the various .cfgs they impute a backup of, as evidenced in the contents herein.

Of note, there is one .cfg I have overtly nix'd from herein - Moonraker's Telegram Bot's .conf.  If an example is desired to look at, take a peek at the initial commit's history and you'll see it therein.  The token has since been revoked, so don't spin yer wheels. ;)
https://github.com/TodWulff/V2.2526_Config/commit/8ac0f96c20a67e028ace10987d7467840370a18f#diff-2f205e9c312fdeaf31e98c2e4242087f788b99c51a2f2b692e8175073f6e4cf8

I've also elected to ignore the save_variables file that houses configuration data for the ERCF, etc. so that old config data doesn't overwright current data.

Enjoy and Happy Printing!

~MHz