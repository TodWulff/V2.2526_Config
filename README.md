# V2.2526_Config
Repo for the Klipper Config directory of my Voron V2.4 (not v2.4r2) SN 2526, a 350^3 model built by ~MHz (myself) in 4Q21.

03MAR23 blurb:

-	refactored the code trace instrumenting approach - instead of a jinja
	conditional wrapping a call to the _start_proc (and _end_proc macros)
	in. every. macro., I decided to nix all those conditional and have a
	single conditional in _start_proc/_end_proc.  While it makes for prettier code,
	I fear the overhead of calling a proc that has the conditional vs wrapping the
	gazillion calls with conditionals will have detrimental performance impacts,
	if what happens under the hood is as I perceive it to be.  We'll see.
	I migrated back to a typical SBC as my klipper host during these refactoring
	efforts, just to not have a issue masked by using a x86 host.

01MAR23 Update Brief:
1)	Added delayed gcode macros to every .cfg to validate load/sequencing.
	This can be disabled in the Printer_Vars variables (...cfgload: 0).
	I was having an issue with sequencing the load and a silly syntax AND
	logic error caused a module to load but not run a specific macro, I had
	thought my edits borked the cfg loading, but it was just the macro that
	was failing silently... (A Klipper Behavior Feature they say ;-)
2)	Added ability for Klipper to synthesize voice by way of pico2wave on the
	host.  I'll make a separate readme for those who might be interested.  As
	a result of this capability, I threaded speech synthesis commands into a
	lot of the macros.  I've been missing TTS since I switch to Klipper from
	Octoprint (Jneliii has the M117VoiceSynthesis plugin that I loved and got
	used to hearing as the machine did it's thing).  Beeping just doesn't cut
	it after one gets used to the verbal emissions (at least for me...).
3)	Working to add code to stall a print starting if host cpu utilization is
	\>1.0.  This is relevant if one automagically generates timelapses and one
	tries to start a new print after a longer print completed and a timelapse
	is being built by the host.  Can you say Timer-Too-Close.?.
4)	There are other things I continue to work or polish or refactor or break.
5)	I got curious what the composite cfg looks like once it is loaded by Klipper
	If you are curious and want to see a config that is nearly 13K LOC:
	https://gist.github.com/TodWulff/a8c6e04c5518768006bb266694994f11
6)	I commissioned Brody (yes, I've taken to naming my printers after sentient
	AIs from my other passion in life - SciFi Audio Books) back in NOV21, was
	TDY professionally for 9 consecutive months earlier that year (it was brutal
	in Middle TN during the summer months - couldn't wait to come home.  Did so,
	and got hooked by the Voron bug.  Ordered the Kit in September and had it
	completed sometime in November.  Then, in 2022, I got tasked with more travel
	on an OCONUS gig (to the DR for a USG Program on an Aerial ISR Platform that
	we modified and certified under a WPAFB administered SOUTHCOM FMS program).
	That lasted from early JUL22 thru AUG22.  I came back from DR and was here for
	a week+ when, on/about 01SEP, I was voluntold that I needed to go assist the
	MRO's Avionics division as they had a program larger than they were prepared for.
	I drove from Upper MI to Middle TN on Labor Day 2022, and was able to get back
	here (to my home orifice) just a few weeks ago.  Needless to say, it is good
	to be back here and to be knee-deep in snow, printers, Klipper, Mainsail, Discord
	and all that is this wonderful hobby and community. 9+2+5 = 16+ months deployed
	since JAN21. I hope I can be home for a while this time around. Am in the middle
	of a v0.1 build (my 2nd, having gifted my first (Skippy) to my son's family).
	I am printing parts to turn the kit into a Tri-Zero as I never got comfortable
	with the cantilevered beds on the stock v0.1s.  Anyways, I've rambled on much
	too long.  Peace and Love Peeps.  I'm out for now.  ~MHz

Useful Links:
- https://jinja.palletsprojects.com/en/2.10.x/templates/
- https://www.klipper3d.org/Overview.html
- https://github.com/Klipper3d/klipper
- https://github.com/VoronDesign/Voron-2/raw/Voron2.4/Manual/Assembly_Manual_2.4r2.pdf
- https://docs.vorondesign.com/
- https://klipper.discourse.group/
- Nice Klipper macro tutorial from Mental: https://klipper.discourse.group/t/macro-creation-tutorial/30
- Current Wiring: https://github.com/TodWulff/V2.2526_Config/blob/main/V2.2526_Hardware/__WDM/V2.2526%20Wiring%20Diagram.pdf

Spring 2022 Update:  Be advised that I continue to muck with things related to the ERCF.  One of my findings
is that repeatedly yanking hot filament up through the hot end contributes to heat creep.  After having
fought heat creep with my Dragon HF HE on a traditional AB setup, having installed 'the dragon duct' to
ward off heat creep in a non-ercf context, I was good.  However, with the ERCF install, it has come back.
As such, I have installed a Dragon WHF - a water cooled HF HE.  One can glean a bit of info in Discord:
https://discord.com/channels/877549316913365083/928716501480009768/963178294424006767 and
https://discord.com/channels/460117602945990666/830395563094442044/966138287905443880 (VD's Phaetus Ch)
https://i.imgur.com/eYwYVdl.png <-- image of my mainsail instance.

I also just installed an Orbiter v2 (23May22).

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

C) LED_Effects by Hagbard

D) Git (done at host's OS level)

Also, with Alex's help (Discord @ALEX#8260, THANK YOU!), I was able to get an automated construct setup such that:

1) On every boot, the config_pull.sh script runs (see _startup_autoexec.cfg) and pulls down changes from the git repo.
  - in case I make changes that are pushed directly to the repo from elsewhere other than the printer config_push.sh script.
  - If config changes are indeed downloaded as a result of the check, upon completion of the download, Klipper service restarts.

2) On print_end event, the config_push.sh script runs to push a snapshot of the printer's current config out to the git repo.
  - I am still cogitating on what other, if any, events to use to trigger a config backup.

3) Macro buttons on Mainsail enables manual initiation of either a push or pull from Klipper's Mainsail UI.

These activities are codified in those scripts and the associated backups of the various .cfgs they impute a backup of, as evidenced in the contents herein.

Of note, there is one .cfg I have overtly nix'd from herein - Moonraker's Telegram Bot's .conf.  If an example is desired to look at, take a peek at the initial commit's history and you'll see it therein.  The token has since been revoked, so don't spin yer wheels. ;)
https://github.com/TodWulff/V2.2526_Config/commit/8ac0f96c20a67e028ace10987d7467840370a18f#diff-2f205e9c312fdeaf31e98c2e4242087f788b99c51a2f2b692e8175073f6e4cf8

I've also elected to ignore the save_variables file that houses configuration data for the ERCF, etc. so that old config data doesn't overwright current data.

Enjoy and Happy Printing!

~MHz

Also, https://i.imgur.com/IHALDMd.png  Making use of Mainsail's console filtering to quiet the noise... ;)

Useful Tidbits:
	NPP Regex to fix copy/pastes from Mailsail Console:
		Win Find:  ^([0-9][0-9]:[0-9][0-9]:[0-9][0-9])\r\n(.*)$
		Replace:   \1 \2

		*nix Find:  ^([0-9][0-9]:[0-9][0-9]:[0-9][0-9])\n(.*)$
		Replace:    \1 \2

