
#########################################################################
# Logrotate is employed outside of this module. Made use of Kiauh shell_
# commands to kick off a script on the host to rotate the logs and urge
# restart of klipper thereafter so it lets go of old file handles and
# picks up the new file handles after logrotate does it's thing.
# didn't programmatically force klipper reset in case printing when logs
# get rotated. Manual rotation via user macros urges klipper restart too
#
# Next effort is to migrate this to a threaded/queued implementation so
# that it doesn't block during intense operations by Klipper Runtime...
#########################################################################

import os
import configparser
import logging
import logging.handlers  # , threading, queue, time

# LOG MSG DECORATION GLOBALS
trace_color = ''
savar_color = ''
state_color = ''
gmove_color = ''
cmpst_color = ''
reset_color = ''


class UserLogger:
    def __init__(self, config):
        global trace_color, savar_color, state_color, \
            gmove_color, cmpst_color, reset_color

        self.printer = config.get_printer()

        # GET USER CONFIG-ASSERTED LOG FILE PATH/NAME
        self.cmpst_log_filename = os.path.expanduser(
            config.get('cmpst_log_filename'))
        self.trace_log_filename = os.path.expanduser(
            config.get('trace_log_filename'))
        self.savar_log_filename = os.path.expanduser(
            config.get('savar_log_filename'))
        self.state_log_filename = os.path.expanduser(
            config.get('state_log_filename'))
        self.gmove_log_filename = os.path.expanduser(
            config.get('gmove_log_filename'))

        # GET USER CONFIG-ASSERTED LOG ENTRY FORMATS
        self.cmpst_log_format = config.get('cmpst_log_format')
        self.trace_log_format = config.get('trace_log_format')
        self.savar_log_format = config.get('savar_log_format')
        self.state_log_format = config.get('state_log_format')
        self.gmove_log_format = config.get('gmove_log_format')

        # GET USER CONFIG-ASSERTED LOG ENTRY DECORATIONS, SETTING THE GLOBALS
        trace_color = config.get('cmpst_color_trace')
        savar_color = config.get('cmpst_color_savar')
        state_color = config.get('cmpst_color_state')
        gmove_color = config.get('cmpst_color_gmove')
        cmpst_color = config.get('cmpst_color_cmpst')
        reset_color = config.get('cmpst_color_reset')

        # CREATE COMPOSITE LOGGER (THIS IS A MOCK ROOT LOGGER)
        cmpst_logger = logging.getLogger("user_cmpst")
        # overtly nix any preexisting handlers (case: klipper soft 'restart')
        cmpst_logger.handlers = []
        # prevent user logs from causing klipper.log swell
        cmpst_logger.propagate = False
        cmpst_logger.setLevel(logging.DEBUG)
        cmpst_fhandler = logging.FileHandler(self.cmpst_log_filename)
        cmpst_fhandler.setLevel(logging.DEBUG)
        cmpst_formatter = logging.Formatter(self.cmpst_log_format)
        cmpst_fhandler.setFormatter(cmpst_formatter)
        cmpst_logger.addHandler(cmpst_fhandler)

        # CREATE TRACE LOGGER
        trace_logger = logging.getLogger("user_trace")
        # overtly nix any preexisting handlers (case: klipper soft 'restart')
        trace_logger.handlers = []
        # prevent user logs from causing klipper.log swell
        trace_logger.propagate = False
        trace_logger.setLevel(logging.DEBUG)
        trace_fhandler = logging.FileHandler(self.trace_log_filename)
        trace_fhandler.setLevel(logging.DEBUG)
        trace_formatter = logging.Formatter(self.trace_log_format)
        trace_fhandler.setFormatter(trace_formatter)
        trace_logger.addHandler(trace_fhandler)

        # REGISTER TRACE LOGGER COMMANDS W/ KLIPPER
        gcode = self.printer.lookup_object('gcode')
        gcode.register_command('TRACE_LOG', self.cmd_TRACE_LOG,
                               desc=self.cmd_TRACE_LOG_help)

        # CREATE STATE LOGGER
        state_logger = logging.getLogger("user_state")
        # overtly nix any preexisting handlers (case: klipper soft 'restart')
        state_logger.handlers = []
        # prevent user logs from causing klipper.log swell
        state_logger.propagate = False
        state_logger.setLevel(logging.DEBUG)
        state_fhandler = logging.FileHandler(self.state_log_filename)
        state_fhandler.setLevel(logging.DEBUG)
        state_formatter = logging.Formatter(self.state_log_format)
        state_fhandler.setFormatter(state_formatter)
        state_logger.addHandler(state_fhandler)

        # REGISTER STATE LOGGER COMMANDS W/ KLIPPER
        gcode = self.printer.lookup_object('gcode')
        gcode.register_command('STATE_LOG', self.cmd_STATE_LOG,
                               desc=self.cmd_STATE_LOG_help)

        # CREATE SAVE VAR LOGGER
        savar_logger = logging.getLogger("user_savar")
        # overtly nix any preexisting handlers (case: klipper soft 'restart')
        savar_logger.handlers = []
        # prevent user logs from causing klipper.log swell
        savar_logger.propagate = False
        savar_logger.setLevel(logging.DEBUG)
        savar_fhandler = logging.FileHandler(self.savar_log_filename)
        savar_fhandler.setLevel(logging.DEBUG)
        savar_formatter = logging.Formatter(self.savar_log_format)
        savar_fhandler.setFormatter(savar_formatter)
        savar_logger.addHandler(savar_fhandler)

        # REGISTER SAVE VAR LOGGER COMMANDS W/ KLIPPER
        gcode = self.printer.lookup_object('gcode')
        gcode.register_command('SAVAR_LOG', self.cmd_SAVAR_LOG,
                               desc=self.cmd_SAVAR_LOG_help)

        # CREATE GMOVE LOGGER
        gmove_logger = logging.getLogger("user_gmove")
        # overtly nix any preexisting handlers (case: klipper soft 'restart')
        gmove_logger.handlers = []
        # prevent user logs from causing klipper.log swell
        gmove_logger.propagate = False
        gmove_logger.setLevel(logging.DEBUG)
        gmove_fhandler = logging.FileHandler(self.gmove_log_filename)
        gmove_fhandler.setLevel(logging.DEBUG)
        gmove_formatter = logging.Formatter(self.gmove_log_format)
        gmove_fhandler.setFormatter(gmove_formatter)
        gmove_logger.addHandler(gmove_fhandler)

        # REGISTER GMOVE LOGGER COMMANDS W/ KLIPPER
        gcode = self.printer.lookup_object('gcode')
        gcode.register_command('GMOVE_LOG', self.cmd_GMOVE_LOG,
                               desc=self.cmd_GMOVE_LOG_help)

        # CMPST LOG SPAWN ENTRIES
        cmpst_logger.debug('=================================================')
        cmpst_logger.debug('COMPOSITE LOGGER SPAWNED')
        cmpst_logger.debug('Filename: ' + self.cmpst_log_filename)
        cmpst_logger.debug('=================================================')

        # TRACE LOG SPAWN ENTRIES
        trace_logger.debug('=================================================')
        trace_logger.debug('TRACE Logger Spawned')
        trace_logger.debug('Filename: ' + self.trace_log_filename)
        trace_logger.debug('=================================================')

        cmpst_logger.debug(
            trace_color + '=================================================' + reset_color)
        cmpst_logger.debug(trace_color + 'TRACE: ' +
                           'TRACE Logger Spawned' + reset_color)
        cmpst_logger.debug(trace_color + 'TRACE: ' +
                           'Filename: ' + self.trace_log_filename + reset_color)
        cmpst_logger.debug(
            trace_color + '=================================================')

        # STATE LOG SPAWN ENTRIES
        state_logger.debug('=================================================')
        state_logger.debug('STATE Logger Spawned')
        state_logger.debug('Filename: ' + self.state_log_filename)
        state_logger.debug('=================================================')

        cmpst_logger.debug(
            state_color + '=================================================' + reset_color)
        cmpst_logger.debug(state_color + 'STATE: ' +
                           'STATE Logger Spawned' + reset_color)
        cmpst_logger.debug(state_color + 'STATE: ' +
                           'Filename: ' + self.state_log_filename + reset_color)
        cmpst_logger.debug(
            state_color + '=================================================' + reset_color)

        # SAVAR LOG SPAWN ENTRIES
        savar_logger.debug('=================================================')
        savar_logger.debug('SAVAR Logger Spawned')
        savar_logger.debug('Filename: ' + self.savar_log_filename)
        savar_logger.debug('=================================================')

        cmpst_logger.debug(
            savar_color + '=================================================' + reset_color)
        cmpst_logger.debug(savar_color + 'SAVAR: ' +
                           'SAVAR Logger Spawned' + reset_color)
        cmpst_logger.debug(savar_color + 'SAVAR: ' +
                           'Filename: ' + self.savar_log_filename + reset_color)
        cmpst_logger.debug(
            savar_color + '=================================================' + reset_color)

        # GMOVE LOG SPAWN ENTRIES
        gmove_logger.debug('=================================================')
        gmove_logger.debug('GMOVE Logger Spawned')
        gmove_logger.debug('Filename: ' + self.gmove_log_filename)
        gmove_logger.debug('=================================================')

        cmpst_logger.debug(
            gmove_color + '=================================================' + reset_color)
        cmpst_logger.debug(gmove_color + 'GMOVE: ' +
                           'GMOVE Logger Spawned' + reset_color)
        cmpst_logger.debug(gmove_color + 'GMOVE: ' +
                           'Filename: ' + self.gmove_log_filename + reset_color)
        cmpst_logger.debug(
            gmove_color + '=================================================' + reset_color)

    # COMMANDS CALLED FROM PRINT-TIME GCODE - REGISTERED W/ KLIPPER ABOVE
    cmd_TRACE_LOG_help = "Write LOG MSG to TRACE_LOG"

    def cmd_TRACE_LOG(self, gcmd):
        global trace_color, reset_color
        trace_logger = logging.getLogger("user_trace")
        # write msg to the pseudo-rootLogger too
        cmpst_logger = logging.getLogger("user_cmpst")
        lmsg = gcmd.get('MSG')
        trace_logger.debug(lmsg)
        cmpst_logger.debug(trace_color + 'TRACE: ' + reset_color + lmsg)

    cmd_STATE_LOG_help = "Write LOG MSG to STATE_LOG"

    def cmd_STATE_LOG(self, gcmd):
        global state_color, reset_color
        state_logger = logging.getLogger("user_state")
        # write msg to the pseudo-rootLogger too
        cmpst_logger = logging.getLogger("user_cmpst")
        lmsg = gcmd.get('MSG')
        state_logger.debug(lmsg)
        cmpst_logger.debug(state_color + 'STATE: ' + reset_color + lmsg)

    cmd_SAVAR_LOG_help = "Write LOG MSG to SAVAR_LOG"

    def cmd_SAVAR_LOG(self, gcmd):
        global savar_color, reset_color
        savar_logger = logging.getLogger("user_savar")
        # write msg to the pseudo-rootLogger too
        cmpst_logger = logging.getLogger("user_cmpst")
        lmsg = gcmd.get('MSG')
        savar_logger.debug(lmsg)
        cmpst_logger.debug(savar_color + 'SAVAR: ' + reset_color + lmsg)

    cmd_GMOVE_LOG_help = "Write LOG MSG to GMOVE_LOG"

    def cmd_GMOVE_LOG(self, gcmd):
        global gmove_color, reset_color
        gmove_logger = logging.getLogger("user_gmove")
        # write msg to the pseudo-rootLogger too
        cmpst_logger = logging.getLogger("user_cmpst")
        lmsg = gcmd.get('MSG')
        gmove_logger.debug(lmsg)
        cmpst_logger.debug(gmove_color + 'GMOVE: ' + reset_color + lmsg)

    def get_status(self, eventtime):
        return {'status': 'userLogger module instantiated'}


def load_config(config):
    return UserLogger(config)
