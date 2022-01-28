v4l2-ctl -d0 --set-ctrl=brightness=8				# (int)  min=0 max=15 step=1 default=8#
v4l2-ctl -d0 --set-ctrl=contrast=8				# (int)  min=0 max=15 step=1 default=8
v4l2-ctl -d0 --set-ctrl=saturation=7				# (int)  min=0 max=15 step=1 default=7
v4l2-ctl -d0 --set-ctrl=hue=0					# (int)  min=-10 max=10 step=1 default=0
v4l2-ctl -d0 --set-ctrl=white_balance_temperature_auto=1	# (bool) default=1
v4l2-ctl -d0 --set-ctrl=gamma=10				# (int)  min=1 max=10 step=1 default=10
v4l2-ctl -d0 --set-ctrl=power_line_frequency=2			# (menu) min=0 max=2 default=2  0:Disabled 1:50Hz 2:60Hz
#v4l2-ctl -d0 --set-ctrl=white_balance_temperature=2800		# (int)  min=2800 max=6500 step=1 default=2800 flags=inactive
v4l2-ctl -d0 --set-ctrl=sharpness=6				# (int)  min=0 max=15 step=1 default=6 value=6
v4l2-ctl -d0 --set-ctrl=backlight_compensation=1		# (int)  min=0 max=1 step=1 default=1 value=1
v4l2-ctl -d0 --set-ctrl=exposure_auto=3				# (menu) min=0 max=3 default=3 0:???  1:Manual 2:? 3:AperturePriority
#v4l2-ctl -d0 --set-ctrl=exposure_absolute=1250			# (int)  min=39 max=5000 step=1 default=1250 flags=inactive
v4l2-ctl -d0 --set-ctrl=focus_auto=0				# (bool) default=1
v4l2-ctl -d0 --set-ctrl=focus_absolute=23			# (int)  min=0 max=23 step=1 default=16 flags=inactive
