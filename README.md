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
 
See the /V2.2526_Hardware/ folder for further details.

>>> LOOK >>> Also, be advised that this set of configs requires manual installation of two components
on top of a fresh install of Klipper - Kiauh's 'shell_commands' unofficial extension is required, as is
'z_calibration'.  Shell_Commands is used herein to facilitate execution of config_blah.sh scripts which
enables the automagic push and pull of these config files, as well as my nozzle cam v4l2 settings, and
some other UI goodness such as macro buttons to kick off curl commands to control external devices such
as my Wyze Cam day/night modes and smart outlets for the printer and the external enclosure I have.

With Alex's help (Discord @ALEX#8260, THANK YOU!), I was able to get an automated construct setup such that:

1) On every boot, the config_pull.sh script runs (see _startup_autoexec.cfg) and pulls down changes from the git repo.
  - in case I make changes that are pushed directly to the repo from elsewhere other than the printer config_push.sh script.
  - If config changes are indeed downloaded as a result of the check, upon completion of the download, Klipper service restarts.
  
2) On print_end event, the config_push.sh script runs to push a snapshot of the printer's current config out to the git repo.
  - I am still cogitating on what other, if any, events to use to trigger a config backup.
  
These activities are codified in those scripts and the associated backups of the various .cfgs they impute a backup of, as
evidenced in the contents herein.

As info (more for my recollection more than anything) there are three Klippy files I have overtly edited to keep console noise to a minimum:

	1) probe.py, I commented out the probe: open/TRIGGERED and the probe at console messages
		# gcmd.respond_info("probe: %s" % (["open", "TRIGGERED"][not not res],))
	        # self.gcode.respond_info("probe at %.3f,%.3f is z=%.6f" % (epos[0], epos[1], epos[2]))
	2) save_variables.py, I commented out the save_variable console message "Variable Saved"
		# gcmd.respond_info("Variable Saved")
	3) extruder.py, I commented out the pressure advance/smooth time messages
		# gcmd.respond_info(msg, log=False)

Of note, there is one .cfg I have overtly nix'd from herein - Moonraker's Telegram Bot's .conf.  If an example is desired to look at,
take a peek at the initial commit's history and you'll see it therein.  The token has since been revoked, so don't spin yer wheels. ;)
https://github.com/TodWulff/V2.2526_Config/commit/8ac0f96c20a67e028ace10987d7467840370a18f#diff-2f205e9c312fdeaf31e98c2e4242087f788b99c51a2f2b692e8175073f6e4cf8

Enjoy and Happy Printing!

~MHz
