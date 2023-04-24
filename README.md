# V2.2526_Config (I am Brody)
Repo for the Klipper Config directory of my Voron V2.4 (not v2.4r2) SN 2526, a 350^3 model built by ~MHz (myself) in 4Q21. Name: 'Brody'

24Apr23:

Ground through the klipper source and created wrappers for every identifiable organic klipper core, kinematic, and klippy extra command callable from user macros.  Ended up having to roll back some due to logging recursion.  Moved all previously wrapped firmware commands to their respective userWrap_blah.cfg.

Refactored all config gcode such that G0 is employed for non-extruding move and G1 is employed for moves that include extrusion.

Refactored _proc_start parameter passing to ensure that issue-imputing ', ", \\", and \\' were removed prior to calling _proc_start.

Changed manner in which instantaneous and fast cpu_idle information was collected (using top) to enable calculating CPU utilization in a seemingly robust manner - tested across three different class hosts (Raspberry Pi 3B+ (Raspbian), Acer CXI/CXI2 (Debian 11), and an HP EliteDesk 800 G3 (Debian 11)).

Employed use of a extra module I stumbled across when reading Reddit posts when looking for something that would do exactly this.  This: https://github.com/JeremyRuhland/klipper_network_status enables: https://i.imgur.com/ChF3R1p.png.  With my having multiple printers emitting to a single telegram channel or sending alerts to a common SMS recipient (my mobile device) then it help muh gray matter to know which printer is bitchin and how to connect to it moar quiker via VPN.  Yes, I use static IPs internally on my LAN, but this will be useful, I posit.

These configs are being structured to work on all of the hosts I have at my disposal.  Next will be to ensure these work on Libre Computer's SBCs.  But that will have to wait as I am departing this afternoon for a week long professional TDY.

05APR23:

(Because I am always looking for these:)
Unicode Symbols recommended for use in string variables w/in klipper configs:

- Ellipse use	…	instead of	...		(gTTS actually verbalizes 'dot dot dot' with the latter... lol!)
- LB/Hash use	♯	instead of	 #		(klipper parsers ignore everything after a # (comment symbol, ofc))
- Percent use	％	instead of	 %		(save_variables(/Jinja?) chokes on use of % w/in strings)

Took a break from getting smarter with Python:
- Implemented a cpu_load check at print start as, historically, when transcoding/encoding a time lapse, host saturates which could definitely 
affect any quick follow-on prints, until the transcode/encode is completed.
- Finally implemented a much needed fix for a long time nag with PS (first layer infill is over extruded, while perimeters are good), and
- Implemented a more robust Idle Timeout approach:
	- On Idle Timeout set a 2 min timer and give user an ability to decide what to do.
	- User has option to
		- Allow the shutdown, 
		- Can elect to push a config & shutdown, or 
		- Choose to reset the idle timeout (temps retained, motors stay engaged, ITO period reset to a 'default' (set in vars))
		- Defaults to doing the shutdown in case user is away
	- FIXME: I still desire to implement a HE cool down with PCF running, to help prevent duct warp-age at printer shutdown when hot.
Easy enough to do, I am just procrastinating...

Still cogitating on best way to suppress specific commands from being logged.  Started with adding a NOLOG=1 detection to any passed 
parameters that are included with the potential log entry.  Issue with this is that, on proc exits, params haven't been sent, so no means
to squelch those.  The now me is kicking my old self's shins for not considering this then.

Also, this whole proc depth thing feels like it's pretty fragile, and I've been mulling on how best to track/display same robustly.  However,
without macro entry/exit callback hooks within klipper, I fear that this might be the best means to an end, but will continue mull on it.

Logging...  I am mulling on the threading/queue approach still, and also how best to consider adding additional logs without hard-coding for
them.  Klipper has a one to many capability with a module import, and sub-instantiations (ugh on the terms) of module elements.  It would be
uber nice to be able to spin up n logs from a user's config by just adding a [userlog blah] section after the [userlogging] module is asserted.
One might reasonably ask: "Seriously?  What for?  You've already got 4+1 logs going.?."  'ERCF.' is my knee-jerk response - that whole thing
is a large set of macros, hardware, and configs, in and of itself and, I posit, that merits an ability to have dedicated log(s) for same.  
It would have been uber nice when I was cutting my teeth and fighting things when building, configuring, and tuning it...

~MHz


29MAR23:

A lot has transpired these last couple of weeks.  Most notably is that I drafted the initial pass as a Klipper Extras Module entitled 
userlogger.py.  The userLogger module enables logging to files rather than by way of the console (or a hugely failed attempt to write to 
files via shell_commands [100ms blocks on each message entry - way painful to watch]).  The goal here was to instantiate a means to have 
logging on at restart, capturing everything printer/Klipper 'boot' related, to log files, and to do so in a manner that yields no effect 
on the printer or Klipper.  This endeavor is partially successful in that I got the logging module instantiated and functional as designed.  
I have a snap-shot of it here in, in the root config folder (needs to be moved to the Klipper/Klipper/extras ifin a user wishes to muck 
around with it).

There were a lot of shiny things that reared their heads that I played whack-a-mole with (I mean, Mutable Focus Systems is muh d/b/a for a 
reason - lol).  Anyways, in no certain order:

-	Created a macro that, when it's button in the Mainsail UI is clicked on, emits to the console a set of 5 URLs that enable work-flow 
efficient access to the logs.  The links are possible by my trapping FW M118, and imputing use of action_respond_info vs. FW's implementation
(supports numeric/special char starts/inclusion and, I've discovered, a much more expressive use of the console in that this approach allows 
writing console emissions from macros that contain HTML that is actually rendered in Mainsail's console) - see _gcode_macros.cfg for that 
specific (painfully simple) M118 implementation.  I don't know if that was ultimately unintended or not, but Meteyou seemed surprised and, 
I perceive, to be nodding in acknowledgment that doing so wasn't objectionable.  So I hope that this ability doesn't get quashed by Kevin, 
Arksine, or the Mainsail crew...
-	The links to the logs are just a piece of the overall puzzle, however.
	-	Those links are instantiated by way of custom URL Protocol handlers.  See the Mainsail_Linking_To_UserLogs.zip archive for additional 
details and copies of the .reg files that inject these handlers into one's registry, so that the various schemes will be honored (sorry Linux 
clients, I don't know how to do so on a Linux box - if it gets figured out, I'd like to know, however).
	-	I had initially worked this solution up with windows putty, but that proved to have an undocumented 'feature' (or windows does?) where 
the loading and display of the logs via an ssh session hung hard.  I migrated over to using MobaXterm (MXT hereinafter) as the SSH client that, 
while a bit of a sledgehammer vs. flyswatter I posit, seems to be working well and reliably.  Time will tell.
	-	I created sessions in MXT that enables connection to the Klipper host via stored key generated by putty's Pageant tool.  I was using 
the pageant tool's generated keys during the putty efforts and when I adopted the use of MXT, pointing the MXT ssh client to the pageant 
generated keys, it just worked <shrugg>.
	-	Once the sessions were created, I configured them with starting commands that, ultimately, instantiate a tail -f -n100 log file session,
which has a pipe redirection to grcat to affect regex driven log colorization of the logs, on a log by log basis. Those terminal commands are 
also included in the aforementioned archive.
-	Colorization of messages, by log filename (employed use of grcat on the host) - where each has a separate /home/user/pi/.grc/grcat_blah.conf 
file to apply color decorations to each log file's messages when rendered.  Most are pretty benign (muting date/time visually, and applying a 
consistent color for the messages).  However, the one for the trace log is a bit more dynamic in that the coloring is applied based on proc 
depth (denoted therein by way of back-ticks).  The regex is, regardless, pretty easily understood.  These grc_blah.conf files are too in the 
aforementioned archive.
-	Lastly, I, being the strange man behind the curtain, decided that this wasn't enough automation and, as a fall back into bed with a long 
time lover, employed use of an AHK script to detect the MXT ssh sessions opening, netting automagic positioning and resizing of those terminal 
session on my desktop in a consistent eye-pleasing/intuitive manner:  https://i.imgur.com/FOgMqCW.png
-	A related item I wish to implement on this front is the automatic detection and clicking of the chrome prompt to run an external executable 
(MXT in this case), but that is a battle for another time.  What has my immediate focus is
-	Morphing the userlogger.py extra module to make use of threading.threads and queue.queue modules and have the messages-to-queue and 
queue-to-log be running on a background thread such that, even when Klipper is task saturated (i.e. at printer startup/klipper restart/etc.) 
that the logging takes a backseat to whatever else is transpiring in Klipper's world.

SO...

I have just purchased and enrolled into an on-line training course via Udemy - Complete Python Developer in 2023: Zero to Mastery.  
My stumbling through getting the current instantiation of userlogger.py running bore a lot of forehead banging and scarring.  
I need to be smarter in the python realm and am taking the steps to do so, at least to get through enough of the course to allow me to 
leverage python's concurrency capabilities on the userlogger extras module.  That will have my focus for the near term.  Wish me luck.

~MHz


15MAR23:

-	fixed recursion error due to latest 'instrumentation' efforts - 
	the just a wee bit old me was smarter than the just now me.
-	added module state stuff for shell_commands and TTS
-	added logic to macros say and say_wait to annunciate if shell_commands is MIA - 
	they emit stdout and error dialog to temp files
-	tail and GREP are my new friends, seriously. **fukin besties**.
-	made it so that the TTS scripts on the host emit back into klipper what is being said,
	as a console message to the user (in event speakers off, deafness, being remote, etc.)
-	split off separate cfgs for _debug_userlogs, _host_control, _tts, _temp_capture, and fought
	the OS for a while getting TTS goin:

this worked well out of the gate with Raspiban hosts.  However, on Debian, it was not so
ended up with a bloody forehead before piping output to temp log and tailing that with
tail -f -n40 temp_gtts.log  and  tail -f -n40 temp_cvlc.log then discovered CVLC was squawking:
       ALSA lib pcm_dmix.c:1075:(snd_pcm_dmix_open) unable to open slave
giggled my way to success:
https://dev.to/setevoy/linux-alsa-lib-pcmdmixc1108sndpcmdmixopen-unable-to-open-slave-38on
missing modprobe.d conf file...  seriously, WTF - why work from CLI but not when klipper called the same damn scripts.  ugh.  anyways, it is
fixed.

The above drama is related to migrating back to my amd64 Chromebox.  I've simply too much shite going on for a small SBC to keep up.  Decided
to install a headless Debian 11 OS thereon (hadn't done so before, so yeah, learnz) all was right with the effort, except TTS. 
Wow, ignorance == PITA.

Part of harmonization is the adoption of 4 macros common in every .cfg being loaded (still a WIP -
I've a shitte tonne of modules...)
-	[delayed_gcode _module_name_loaded] <-- this is a macro that is auto-run at (4.501) seconds after loading, for startup annunciation, 
logging, etc.  (the three digit is for simple find and replace purposes)
-	[gcode_macro _info_module_name] <-- a macro that is not intended to be used, but rather is a common place for module documentation
-	[gcode_macro _module_name_vars] <-- module specific variables are to be plopped herein
-	[delayed_gcode _module_name_start] <-- is to fire off at 0.5s after loading, to init module variables and globals (i.e. module loaded 
and module err flag)
-	Then, further on in the module, will be klipper enablement sections, if needed, for contextually relevant modules that are to be loaded.
-	Finally, contextually relevant gcode macros and shell commands, etc., are to exist therein. 

-	moar useful bits
tail -f ~/temp/temp_gtts.log  <-- after redirected from /dev/null to a temp file
tail -f ~/temp/temp_cvlc.log  <-- after redirected from /dev/null to a temp file

tail -f ~/printer_data/logs/klippy.log | grep -v -E "^Stats|^received|^mcu "  <-- to find the trees in the forest

14MAR23:

-	Implemented framework for logging (Code/SVV/Gmove/State traces) to be
	written to log files or the console - using a _printer_var to control
-	Implemented colorization to user input prompts and console debug output
	(this was a long time desire that I finally figured out how to implement)
-	Have decided to create a single repository for all of my printers which
	will make use of conditional includes (via Jinja w/ home brew 'predicates')
	This will be a drawn out WIP effort as I figure out how best to implement
-	Started the Harmonization efforts between config repositories with white
	space cleanup (horiz, vertical, trailing, etc.)
-	Went through and validated that EVERY gcode block was instrumented (except
	where uncontrolled recursion would occur), including non-macro blocks - 
	I expect to have some of these efforts bite me in the backside, but as of
	now, it all boots and non-exhaustive tests indicate that the stars aligned
-	Nifty stats: 426 gcode macros, 523 gcode blocks (not all blocks are macros)
	10,046 no-BS Lines of Config (no comments, no vertical whitespace) with over
	380K characters (no excess horizontal whitespace either) - I've probably stroked
	the keys over a million times (no BS)- peeps can attest to the fact that I 
	can get OVERLY verbose in my comments, guidance, and other 'elucidations' :)
-	Oh, yeah, also have nix'd the useless commit messages that were automagically
	used in the scripts when the configs automatically updated this repo (had been
	triggering them on each successful print completion) - now the print_end proc
	queries the user, after optional filament unload and heater setting retention
	queries, if the configs are to be pushed up to the repo and, if so, enforces
	input of a proper commit summary vs useless diatribe - ima work to honor the
	spirit of documenting the pushes as they should have been to begin with -
	future me, and anyone else who stumbles across this, will hopefully benefit...

03MAR23 blurb:

-	Refactored the code trace instrumenting approach - instead of a Jinja
	conditional wrapping a call to the _start_proc (and _end_proc macros)
	in. every. macro., I decided to nix all those conditional and have a
	single conditional in _start_proc/_end_proc. While it makes for prettier code,
	I fear the overhead of calling a proc that has the conditional vs wrapping the
	gazillion calls with conditionals will have detrimental performance impacts,
	if what happens under the hood is as I perceive it to be. We'll see.
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
	host. I'll make a separate readme for those who might be interested. As
	a result of this capability, I threaded speech synthesis commands into a
	lot of the macros. I've been missing TTS since I switch to Klipper from
	Octoprint (Jneliii has the M117VoiceSynthesis plug-in that I loved and got
	used to hearing as the machine did it's thing). Beeping just doesn't cut
	it after one gets used to the verbal emissions (at least for me...).
3)	Working to add code to stall a print starting if host CPU utilization is
	\>1.0. This is relevant if one automagically generates timelapses and one
	tries to start a new print after a longer print completed and a timelapse
	is being built by the host. Can you say Timer-Too-Close.?.
4)	There are other things I continue to work or polish or refactor or break.
5)	I got curious what the composite cfg looks like once it is loaded by Klipper
	If you are curious and want to see a config that is nearly 13K LOC:
	https://gist.github.com/TodWulff/a8c6e04c5518768006bb266694994f11
6)	I commissioned Brody (yes, I've taken to naming my printers after sentient
	AIs from my other passion in life - SciFi Audio Books) back in NOV21, was
	TDY professionally for 9 consecutive months earlier that year (it was brutal
	in Middle TN during the summer months - couldn't wait to come home. Did so,
	and got hooked by the Voron bug. Ordered the Kit in September and had it
	completed sometime in November. Then, in 2022, I got tasked with more travel
	on an OCONUS gig (to the DR for a USG Program on an Aerial ISR Platform that
	we modified and certified under a WPAFB administered SOUTHCOM FMS program).
	That lasted from early JUL22 thru AUG22. I came back from DR and was here for
	a week+ when, on/about 01SEP, I was voluntold that I needed to go assist the
	MRO's Avionics division as they had a program larger than they were prepared for.
	I drove from Upper MI to Middle TN on Labor Day 2022, and was able to get back
	here (to my home orifice) just a few weeks ago. Needless to say, it is good
	to be back here and to be knee-deep in snow, printers, Klipper, Mainsail, Discord
	and all that is this wonderful hobby and community. 9+2+5 = 16+ months deployed
	since JAN21. I hope I can be home for a while this time around. Am in the middle
	of a v0.1 build (my 2nd, having gifted my first (Skippy) to my son's family).
	I am printing parts to turn the kit into a Tri-Zero as I never got comfortable
	with the cantilevered beds on the stock v0.1s. Anyways, I've rambled on much
	too long. Peace and Love Peeps. I'm out for now. ~MHz

Useful Links:
- https://Jinja.palletsprojects.com/en/2.10.x/templates/
- https://www.klipper3d.org/Overview.html
- https://github.com/Klipper3d/klipper
- https://github.com/VoronDesign/Voron-2/raw/Voron2.4/Manual/Assembly_Manual_2.4r2.pdf
- https://docs.vorondesign.com/
- https://klipper.discourse.group/
- Nice Klipper macro tutorial from Mental: https://klipper.discourse.group/t/macro-creation-tutorial/30
- Current Wiring: https://github.com/TodWulff/V2.2526_Config/blob/main/V2.2526_Hardware/__WDM/V2.2526%20Wiring%20Diagram.pdf

Spring 2022 Update: Be advised that I continue to muck with things related to the ERCF. One of my findings
is that repeatedly yanking hot filament up through the hot end contributes to heat creep. After having
fought heat creep with my Dragon HF HE on a traditional AB setup, having installed 'the dragon duct' to
ward off heat creep in a non-ercf context, I was good. However, with the ERCF install, it has come back.
As such, I have installed a Dragon WHF - a water cooled HF HE. One can glean a bit of info in Discord:
https://discord.com/channels/877549316913365083/928716501480009768/963178294424006767 and
https://discord.com/channels/460117602945990666/830395563094442044/966138287905443880 (VD's Phaetus Ch)
https://i.imgur.com/eYwYVdl.png <-- image of my mainsail instance.

I also just installed an Orbiter v2 (23May22).

Voron Kit Feedback Server Invite: https://bit.ly/3igPTpJ (resolves to https://discord.com/invite/RyAGnb9y3G)
My Formbot printer kit feedback ch: https://discord.com/channels/877549316913365083/885942140012744744
My ERCF DFH Kit feedback ch: https://discord.com/channels/877549316913365083/928716501480009768

FYSA (24Feb2022): Be advised that these configs are a big Work In Process (WIP). The printer is a new
build in Nov 2021. Further, I recently added a 12-cart ERCF with ERCPs. And, commensurate with the ERCF,
I have migrated over to Prusa Slicer from Cura Slicer (which I have used for years), so I am working to
massage these config files to conform to the work-flow that I had initially established with Cura. Just
so y'all know about same... Usual disclaimers apply. YMMV. blah blah blah.

DISCLAIMER: I am not at fault if your use of these info/data/code/macros/configs result in injury/damage/issues/etc.
Your use of these info/data/code/macros/configs acknowledges these risks and indicates a full indemnification
of myself from any potential outcomes of your decision to use the info/data/code/macros/configs presented herein.

Printer Details, for those who may be interested:
- Water-cooled Phaetus WHF High Flow Hot End, with Phaetus WaterCooler Pump/Radiator/Fan Kit
	- I supplemented the latter with a stand-alone temp sensor/indicator ()
	- And I've added sensors to enable programmatic indication of the 'H2O' cooling system in Klipper
	- Further, I changed the kit wiring to enable PWM of the pump and to provide pump tach feedback to Klipper
	- Finally (I think), I replaced the kit fan (2-wire 92mm, loud AF) with a Noctua () which is MUCH quieter.
- 12-cart ERCF with ERCPs - ERCF mounted to back, ERCPs are on a rack collocated IVO printer
- ERCP imputed use of a tool-head filament detector switch which I folded into the design of the
	Orbiter v1.5 adapter
- 7OW/PT1000 AB Print Head housing a Phaetus Dragon HF HE with an Orbiter Extruder fitted thereto.
- An accelerometerized AB Toolhead PCB was designed, built and installed, oriented to clear stuffs
- The thermistor that is normally on the TH PCB has been removed, with wires affixed thereto to allow for the placement of the PCB 
Chamber Temp Sens=0805 10K 1% B=3950K(25/50C) in the AB duct by way of a JST connector pair - have fan set to default to 10% to keep 
air flowing over the sensor
- HE0=HE_HTR, HE3=HOUR_METER
- M0=B, M1=A, M2.1=Z0, M3=Z1, M4=Z2, M5=Z3, M6=E
- F0=PCF, F1=HEF, F2=Aft Chassis (MCU), F3=Fore Chassis (PS), F4=Exhaust, F5=Filter/Stir, F6=5VDC PS (12V), F6=StepperDriver (12V)
- DIAG0=XES, DIAG1=YES, DIAG2=ZES, DIAG3=PL-08 Bed Sens (blocking diode on AB PCB)
- DIAG4=SFS
- RGB LED IO (PB0) used for 'dashboard' neopixels
- TB=BED, T0=HE, T1=AB_PCB(CHAMBER), T2=3950 bead @ top of chamber IVO exhaust, T3=3950 bead @ unswitched 5VDC PS
- Display Aural Xdcr on uC IO PE8
- RP2040 installed as MCU2: ADXL I/F, I/F for 228ea DotStar LEDs for chamber lighting, data for ERCF Neopixels, and Power Switch's RGB 
Halo Light Control

See the /V2.2526_Hardware/ folder for further details.

>>> LOOK >>> Also, be advised that this set of configs requires manual installation of some components on top of a fresh install of the 
host OS and Klipper/Moonraker/Mainsail:

A) Kiauh's 'shell_commands' [an unofficial extension],
	- Shell_Commands is used herein to facilitate execution of config_blah.sh scripts which enables the automagic push and pull of these 
config files, as well as my nozzle cam v4l2 settings, and some other UI goodness such as macro buttons to kick off curl commands to control 
external devices such as my Wyze Cam day/night modes and smart outlets for the printer and the external enclosure I have.

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

These activities are codified in those scripts and the associated backups of the various .cfgs they impute a backup of, as evidenced in the 
contents herein.

Of note, there is one .cfg I have overtly nix'd from herein - Moonraker's Telegram Bot's .conf. If an example is desired to look at, take 
a peek at the initial commit's history and you'll see it therein. The token has since been revoked, so don't spin yer wheels. ;)
https://github.com/TodWulff/V2.2526_Config/commit/8ac0f96c20a67e028ace10987d7467840370a18f#diff-2f205e9c312fdeaf31e98c2e4242087f788b99c51a2f2b692e8175073f6e4cf8

I've also elected to ignore the save_variables file that houses configuration data for the ERCF, etc. so that old config data doesn't overwrite
current data.

Enjoy and Happy Printing!

~MHz

Also, https://i.imgur.com/IHALDMd.png Making use of Mainsail's console filtering to quiet the noise... ;)

Useful Tidbits:
	NPP Regex to fix copy/pastes from Mainsail Console:
		Win Find: ^([0-9][0-9]:[0-9][0-9]:[0-9][0-9])\r\n(.*)$
		Replace: \1 \2

		*nix Find: ^([0-9][0-9]:[0-9][0-9]:[0-9][0-9])\n(.*)$
		Replace: \1 \2

