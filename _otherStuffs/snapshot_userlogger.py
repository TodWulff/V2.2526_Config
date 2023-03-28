import os, logging, logging.handlers, ast, configparser

class UserLogger:
    def __init__(self, config):
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

        # GET USER CONFIG-ASSERTED LOG SIZE LIMITS
        self.cmpst_log_maxbytes = int(config.get('cmpst_log_maxbytes'))
        self.trace_log_maxbytes = int(config.get('trace_log_maxbytes'))
        self.savar_log_maxbytes = int(config.get('savar_log_maxbytes'))
        self.state_log_maxbytes = int(config.get('state_log_maxbytes'))
        self.gmove_log_maxbytes = int(config.get('gmove_log_maxbytes'))

        # GET USER CONFIG-ASSERTED LOG ROTATED BACKUP COUNTS
        self.cmpst_log_bkupcnt = int(config.get('cmpst_log_bkupcnt'))
        self.trace_log_bkupcnt = int(config.get('trace_log_bkupcnt'))
        self.savar_log_bkupcnt = int(config.get('savar_log_bkupcnt'))
        self.state_log_bkupcnt = int(config.get('state_log_bkupcnt'))
        self.gmove_log_bkupcnt = int(config.get('gmove_log_bkupcnt'))

        # CREATE COMPOSITE LOGGER (THIS IS A MOCK ROOT LOGGER)
        cmpst_logger = logging.getLogger("user_cmpst")
        cmpst_logger.propagate = False
        cmpst_logger.setLevel(logging.DEBUG)
        cmpst_fhandler = logging.handlers.RotatingFileHandler(
              self.cmpst_log_filename,
              maxBytes=self.cmpst_log_maxbytes,
              backupCount=self.cmpst_log_bkupcnt)
#        cmpst_fhandler.doRollover()
        cmpst_fhandler.setLevel(logging.DEBUG)
        cmpst_formatter = logging.Formatter(self.cmpst_log_format)
        cmpst_fhandler.setFormatter(cmpst_formatter)
        cmpst_logger.addHandler(cmpst_fhandler)

        # CREATE TRACE LOGGER
        trace_logger = logging.getLogger("user_trace")
        trace_logger.propagate = False
        trace_logger.setLevel(logging.DEBUG)
        trace_fhandler = logging.handlers.RotatingFileHandler(
              self.trace_log_filename,
              maxBytes=self.trace_log_maxbytes,
              backupCount=self.trace_log_bkupcnt)
#        trace_fhandler.doRollover()
        trace_fhandler.setLevel(logging.DEBUG)
        trace_formatter = logging.Formatter(self.trace_log_format)
        trace_fhandler.setFormatter(trace_formatter)
        trace_logger.addHandler(trace_fhandler)
        
        # REGISTER TRACE LOGGER COMMANDS
        gcode = self.printer.lookup_object('gcode')
        gcode.register_command('TRACE_LOG', self.cmd_TRACE_LOG,
                               desc=self.cmd_TRACE_LOG_help)

        # CREATE STATE LOGGER
        state_logger = logging.getLogger("user_state")
        state_logger.propagate = False
        state_logger.setLevel(logging.DEBUG)
        state_fhandler = logging.handlers.RotatingFileHandler(
              self.state_log_filename,
              maxBytes=self.state_log_maxbytes,
              backupCount=self.state_log_bkupcnt)
#        state_fhandler.doRollover()
        state_fhandler.setLevel(logging.DEBUG)
        state_formatter = logging.Formatter(self.state_log_format)
        state_fhandler.setFormatter(state_formatter)
        state_logger.addHandler(state_fhandler)
        
        # REGISTER STATE LOGGER COMMANDS
        gcode = self.printer.lookup_object('gcode')
        gcode.register_command('STATE_LOG', self.cmd_STATE_LOG,
                               desc=self.cmd_STATE_LOG_help)

        # CREATE SAVE VAR LOGGER
        savar_logger = logging.getLogger("user_savar")
        savar_logger.propagate = False
        savar_logger.setLevel(logging.DEBUG)
        savar_fhandler = logging.handlers.RotatingFileHandler(
              self.savar_log_filename,
              maxBytes=self.savar_log_maxbytes,
              backupCount=self.savar_log_bkupcnt)
#        savar_fhandler.doRollover()
        savar_fhandler.setLevel(logging.DEBUG)
        savar_formatter = logging.Formatter(self.savar_log_format)
        savar_fhandler.setFormatter(savar_formatter)
        savar_logger.addHandler(savar_fhandler)

        # REGISTER SAVE VAR LOGGER COMMANDS
        gcode = self.printer.lookup_object('gcode')
        gcode.register_command('SAVAR_LOG', self.cmd_SAVAR_LOG,
                               desc=self.cmd_SAVAR_LOG_help)

        # CREATE GMOVE LOGGER
        gmove_logger = logging.getLogger("user_gmove")
        gmove_logger.propagate = False
        gmove_logger.setLevel(logging.DEBUG)
        gmove_fhandler = logging.handlers.RotatingFileHandler(
              self.gmove_log_filename,
              maxBytes=self.gmove_log_maxbytes,
              backupCount=self.gmove_log_bkupcnt)
#        gmove_fhandler.doRollover()
        gmove_fhandler.setLevel(logging.DEBUG)
        gmove_formatter = logging.Formatter(self.gmove_log_format)
        gmove_fhandler.setFormatter(gmove_formatter)
        gmove_logger.addHandler(gmove_fhandler)
        
        # REGISTER GMOVE LOGGER COMMANDS
        gcode = self.printer.lookup_object('gcode')
        gcode.register_command('GMOVE_LOG', self.cmd_GMOVE_LOG,
                               desc=self.cmd_GMOVE_LOG_help)
#        gcode.register_command('GMOVE_LOG_ROTATE', self.cmd_GMOVE_LOG_ROTATE,
#                               desc=self.cmd_GMOVE_LOG_ROTATE_help)

        # MAKE INAUGURAL LOG ENTRIES AFTER SPAWNING
        # CMPST LOG INITIAL ENTRY
        cmpst_logger.debug('=================================================')
        cmpst_logger.debug('COMPOSITE LOGGER SPAWNED')
        cmpst_logger.debug('Filename: ' + self.cmpst_log_filename)
        cmpst_logger.debug('RotateMaxBytes: ' + str(self.cmpst_log_maxbytes))
        cmpst_logger.debug('RotateBackupCnt: ' + str(self.cmpst_log_bkupcnt))
        cmpst_logger.debug('cmpst_logger: ' + str(cmpst_logger))
        cmpst_logger.debug('cmpst_fhandler: ' + str(cmpst_fhandler))
        cmpst_logger.debug('cmpst_formatter: ' + str(cmpst_formatter))
        cmpst_logger.debug('=================================================')

        # TRACE LOG INITIAL ENTRIES        
        trace_logger.debug('=================================================')
        cmpst_logger.debug('=================================================')
        trace_logger.debug('TRACE Logger Spawned')
        cmpst_logger.debug('TRACE: ' + 'TRACE Logger Spawned')
        trace_logger.debug('Filename: ' + self.trace_log_filename)
        cmpst_logger.debug('TRACE: ' + 'Filename: ' + self.trace_log_filename)
        trace_logger.debug('RotateMaxBytes: ' + str(self.trace_log_maxbytes))
        cmpst_logger.debug('TRACE: ' + 'RotateMaxBytes: ' + str(self.trace_log_maxbytes))
        trace_logger.debug('RotateBackupCnt: ' + str(self.trace_log_bkupcnt))
        cmpst_logger.debug('TRACE: ' + 'RotateBackupCnt: ' + str(self.trace_log_bkupcnt))
        trace_logger.debug('trace_logger: ' + str(trace_logger))
        cmpst_logger.debug('TRACE: ' + 'trace_logger: ' + str(trace_logger))
        trace_logger.debug('trace_fhandler: ' + str(trace_fhandler))
        cmpst_logger.debug('TRACE: ' + 'trace_fhandler: ' + str(trace_fhandler))
        trace_logger.debug('trace_formatter: ' + str(trace_formatter))
        cmpst_logger.debug('TRACE: ' + 'trace_formatter: ' + str(trace_formatter))
        trace_logger.debug('=================================================')
        cmpst_logger.debug('=================================================')

        # STATE LOG INITIAL ENTRIES
        state_logger.debug('=================================================')
        cmpst_logger.debug('=================================================')
        state_logger.debug('STATE Logger Spawned')
        cmpst_logger.debug('STATE: ' + 'STATE Logger Spawned')
        state_logger.debug('Filename: ' + self.state_log_filename)
        cmpst_logger.debug('STATE: ' + 'Filename: ' + self.state_log_filename)
        state_logger.debug('RotateMaxBytes: ' + str(self.state_log_maxbytes))
        cmpst_logger.debug('STATE: ' + 'RotateMaxBytes: ' + str(self.state_log_maxbytes))
        state_logger.debug('RotateBackupCnt: ' + str(self.state_log_bkupcnt))
        cmpst_logger.debug('STATE: ' + 'RotateBackupCnt: ' + str(self.state_log_bkupcnt))
        state_logger.debug('state_logger: ' + str(state_logger))
        cmpst_logger.debug('STATE: ' + 'state_logger: ' + str(state_logger))
        state_logger.debug('state_fhandler: ' + str(state_fhandler))
        cmpst_logger.debug('STATE: ' + 'state_fhandler: ' + str(state_fhandler))
        state_logger.debug('state_formatter: ' + str(state_formatter))
        cmpst_logger.debug('STATE: ' + 'state_formatter: ' + str(state_formatter))
        state_logger.debug('=================================================')
        cmpst_logger.debug('=================================================')
        
        # SAVAR LOG INITIAL ENTRIES
        savar_logger.debug('=================================================')
        cmpst_logger.debug('=================================================')
        savar_logger.debug('SAVAR Logger Spawned')
        cmpst_logger.debug('SAVAR: ' + 'SAVAR Logger Spawned')
        savar_logger.debug('Filename: ' + self.savar_log_filename)
        cmpst_logger.debug('SAVAR: ' + 'Filename: ' + self.savar_log_filename)
        savar_logger.debug('RotateMaxBytes: ' + str(self.savar_log_maxbytes))
        cmpst_logger.debug('SAVAR: ' + 'RotateMaxBytes: ' + str(self.savar_log_maxbytes))
        savar_logger.debug('RotateBackupCnt: ' + str(self.savar_log_bkupcnt))
        cmpst_logger.debug('SAVAR: ' + 'RotateBackupCnt: ' + str(self.savar_log_bkupcnt))
        savar_logger.debug('savar_logger: ' + str(savar_logger))
        cmpst_logger.debug('SAVAR: ' + 'savar_logger: ' + str(savar_logger))
        savar_logger.debug('savar_fhandler: ' + str(savar_fhandler))
        cmpst_logger.debug('SAVAR: ' + 'savar_fhandler: ' + str(savar_fhandler))
        savar_logger.debug('savar_formatter: ' + str(savar_formatter))
        cmpst_logger.debug('SAVAR: ' + 'savar_formatter: ' + str(savar_formatter))
        savar_logger.debug('=================================================')
        cmpst_logger.debug('=================================================')

        # GMOVE LOG INITIAL ENTRIES
        gmove_logger.debug('=================================================')
        cmpst_logger.debug('=================================================')
        gmove_logger.debug('GMOVE Logger Spawned')
        cmpst_logger.debug('GMOVE: ' + 'GMOVE Logger Spawned')
        gmove_logger.debug('Filename: ' + self.gmove_log_filename)
        cmpst_logger.debug('GMOVE: ' + 'Filename: ' + self.gmove_log_filename)
        gmove_logger.debug('RotateMaxBytes: ' + str(self.gmove_log_maxbytes))
        cmpst_logger.debug('GMOVE: ' + 'RotateMaxBytes: ' + str(self.gmove_log_maxbytes))
        gmove_logger.debug('RotateBackupCnt: ' + str(self.gmove_log_bkupcnt))
        cmpst_logger.debug('GMOVE: ' + 'RotateBackupCnt: ' + str(self.gmove_log_bkupcnt))
        gmove_logger.debug('gmove_logger: ' + str(gmove_logger))
        cmpst_logger.debug('GMOVE: ' + 'gmove_logger: ' + str(gmove_logger))
        gmove_logger.debug('gmove_fhandler: ' + str(gmove_fhandler))
        cmpst_logger.debug('GMOVE: ' + 'gmove_fhandler: ' + str(gmove_fhandler))
        gmove_logger.debug('gmove_formatter: ' + str(gmove_formatter))
        cmpst_logger.debug('GMOVE: ' + 'gmove_formatter: ' + str(gmove_formatter))
        gmove_logger.debug('=================================================')
        cmpst_logger.debug('=================================================')

    cmd_TRACE_LOG_help = "Write LOG MSG to TRACE_LOG"
    def cmd_TRACE_LOG(self, gcmd):
        trace_logger = logging.getLogger("user_trace")
        cmpst_logger = logging.getLogger("user_cmpst")
        lmsg = gcmd.get('MSG')
        trace_logger.debug(lmsg)
        cmpst_logger.debug('TRACE: ' + lmsg)
            
    cmd_STATE_LOG_help = "Write LOG MSG to STATE_LOG"
    def cmd_STATE_LOG(self, gcmd):
        state_logger = logging.getLogger("user_state")
        cmpst_logger = logging.getLogger("user_cmpst")
        lmsg = gcmd.get('MSG')
        state_logger.debug(lmsg)
        cmpst_logger.debug('STATE: ' + lmsg)
            
    cmd_SAVAR_LOG_help = "Write LOG MSG to SAVAR_LOG"
    def cmd_SAVAR_LOG(self, gcmd):
        savar_logger = logging.getLogger("user_savar")
        cmpst_logger = logging.getLogger("user_cmpst")
        lmsg = gcmd.get('MSG')
        savar_logger.debug(lmsg)
        cmpst_logger.debug('SAVAR: ' + lmsg)
            
    cmd_GMOVE_LOG_help = "Write LOG MSG to GMOVE_LOG"
    def cmd_GMOVE_LOG(self, gcmd):
        gmove_logger = logging.getLogger("user_gmove")
        cmpst_logger = logging.getLogger("user_cmpst")
        lmsg = gcmd.get('MSG')
        gmove_logger.debug(lmsg)
        cmpst_logger.debug('GMOVE: ' + lmsg)

    def get_status(self, eventtime):
        return {'status': 'userLogger module instantiated'}

def load_config(config):
    return UserLogger(config)
