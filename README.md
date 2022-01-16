# V2.2526_Config
Repo for the Klipper Config directory of my Voron V2.4 SN 2526, a 350^3 model built by myself in 4Q21.

Printer Details, for those who may be interested:
- 7OW/PT1000 AB Print Head housing a Phaetus Dragon HF HE with an Orbiter Extruder fitted thereto.
- An accelerometerized AB Toolhead PCB was designed, built and installed.
- The thermistor that is normally on the TH PCB has been removed, with wires affixed thereto to allow
  for the placement of the PCB Chamber Temp Sens=0805 10K 1% B=3950K(25/50C) in the AB duct by way
  of a JST connector pair.
- HE0=HE_HTR, HE3=HOUR_METER
- M0=B, M1=A, M2.1=Z0, M3=Z1, M4=Z2, M5=Z3, M6=E
- F0=PCF, F1=HEF
- DIAG0=XES, DIAG1=YES, DIAG2=ZES, DIAG3=PL-08 Bed Sens (blocking diode on AB PCB)
- DIAG4=SFS
- RGB LED IO (PB0) unused
- TB=BED, T0=HE, T1=AB_PCB(CHAMBER)
- Display Aural Xdcr on uC IO PE8
- RP2040 installed as MCU2:  ADXL I/F, I/F for 228ea DotStar LEDs for chamber lighting, and Power Switch's RGB Halo Light Control
 
See the /V2.2526_Hardware/ folder for further details

With Alex's help (Discord @ALEX#8260), I was able to get an automated construct setup such that:

1) On every boot, the config_pull.sh script runs (see _startup_autoexec.cfg) and pulls down changes from the git repo.
  - in case I make changes that are pushed directly to the repo from elsewhere other than the printer config_push.sh script.
  
2) On ___ event, the config_push.sh script runs to push a snapshot of the printer's current config out to the git repo.
  - I am still cogitating on what event to use to trigger the config backup.
  - Right now I've a macro button that does so.
  - And I may add an automated backup to my print start script, causing the backup to happen, with any changes being backed up
    at the start of each print (if no changes exist, nothing happens (it is how git works)
  
These activities are codified in those scripts and the associated backups of the various .cfgs they impute a backup of, as
evidenced in the contents herein.

Of note, there is one .cfg I have overtly nix'd from herein - Moonraker's Telegram Bot's .conf.  If an example is desired to look at,
take a peek at the initial commit's history and you'll see it therein.  The token has since been revoked, so don't spin yer wheels. ;)
