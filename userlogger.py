import os, logging, logging.handlers, ast, configparser

class UserLogger:
    def __init__(self, config):
        self.printer = config.get_printer()

        # GET USER CONFIG ASSERTED LOG FILE PATH/NAME
        self.cmpst_log_filename = os.path.expanduser(config.get('cmpst_log_filename'))
        self.trace_log_filename = os.path.expanduser(config.get('trace_log_filename'))
        self.savar_log_filename = os.path.expanduser(config.get('savar_log_filename'))
        self.state_log_filename = os.path.expanduser(config.get('state_log_filename'))
        self.gmove_log_filename = os.path.expanduser(config.get('gmove_log_filename'))

        # GET USER CONFIG ASSERTED LOG ENTRY FORMATS
        self.cmpst_log_format = config.get('cmpst_log_format')
        self.trace_log_format = config.get('trace_log_format')
        self.savar_log_format = config.get('savar_log_format')
        self.state_log_format = config.get('state_log_format')
        self.gmove_log_format = config.get('gmove_log_format')

        # GET USER CONFIG ASSERTED LOG SIZE LIMITS
        self.cmpst_log_maxbytes = config.get('cmpst_log_maxbytes')
        self.trace_log_maxbytes = config.get('trace_log_maxbytes')
        self.savar_log_maxbytes = config.get('savar_log_maxbytes')
        self.state_log_maxbytes = config.get('state_log_maxbytes')
        self.gmove_log_maxbytes = config.get('gmove_log_maxbytes')

        # GET USER CONFIG ASSERTED LOG ROTATED BACKUPS
        self.cmpst_log_bkupcnt = config.get('cmpst_log_bkupcnt')
        self.trace_log_bkupcnt = config.get('trace_log_bkupcnt')
        self.savar_log_bkupcnt = config.get('savar_log_bkupcnt')
        self.state_log_bkupcnt = config.get('state_log_bkupcnt')
        self.gmove_log_bkupcnt = config.get('gmove_log_bkupcnt')

        # CREATE COMPOSITE (MOCK ROOT) LOGGER
        cmpst_logger = logging.getLogger("user_cmpst")
        cmpst_logger.setLevel(logging.DEBUG)
        cmpst_fhandler = logging.FileHandler(self.cmpst_log_filename)
        cmpst_formatter = logging.Formatter(self.cmpst_log_format)
        cmpst_fhandler.setLevel(logging.DEBUG)
        cmpst_fhandler.setFormatter(cmpst_formatter)
        cmpst_logger.addHandler(cmpst_fhandler)

#        cmpst_loghandler = logging.handlers.RotatingFileHandler(
#              self.cmpst_log_filename,
#              maxBytes=self.cmpst_log_maxbytes,
#              backupCount=self.cmpst_log_bkupcnt)
#        cmpst_logger.addHandler(cmpst_loghandler)

        # CREATE TRACE LOGGER
        trace_logger = logging.getLogger("user_trace")
        trace_logger.setLevel(logging.DEBUG)
        trace_fhandler = logging.FileHandler(self.trace_log_filename)
        trace_formatter = logging.Formatter(self.trace_log_format)
        trace_fhandler.setLevel(logging.DEBUG)
        trace_fhandler.setFormatter(trace_formatter)
        trace_logger.addHandler(trace_fhandler)
        gcode = self.printer.lookup_object('gcode')
        gcode.register_command('TRACE_LOG', self.cmd_TRACE_LOG,
                               desc=self.cmd_TRACE_LOG_help)

#        trace_loghandler = logging.handlers.RotatingFileHandler(
#              self.trace_log_filename,
#              maxBytes=self.trace_log_maxbytes,
#              backupCount=self.trace_log_bkupcnt)
#        trace_logger.addHandler(trace_loghandler)

        # CREATE STATE LOGGER
        state_logger = logging.getLogger("user_state")
        state_logger.setLevel(logging.DEBUG)
        state_fhandler = logging.FileHandler(self.state_log_filename)
        state_formatter = logging.Formatter(self.state_log_format)
        state_fhandler.setLevel(logging.DEBUG)
        state_fhandler.setFormatter(state_formatter)
        state_logger.addHandler(state_fhandler)
        gcode = self.printer.lookup_object('gcode')
        gcode.register_command('STATE_LOG', self.cmd_STATE_LOG,
                               desc=self.cmd_STATE_LOG_help)

#        state_loghandler = logging.handlers.RotatingFileHandler(
#              self.state_log_filename,
#              maxBytes=self.state_log_maxbytes,
#              backupCount=self.state_log_bkupcnt)
#        state_logger.addHandler(state_loghandler)

        # CREATE SAVE VAR LOGGER
        savar_logger = logging.getLogger("user_savar")
        savar_logger.setLevel(logging.DEBUG)
        savar_fhandler = logging.FileHandler(self.savar_log_filename)
        savar_formatter = logging.Formatter(self.savar_log_format)
        savar_fhandler.setLevel(logging.DEBUG)
        savar_fhandler.setFormatter(savar_formatter)
        savar_logger.addHandler(savar_fhandler)
        gcode = self.printer.lookup_object('gcode')
        gcode.register_command('SAVAR_LOG', self.cmd_SAVAR_LOG,
                               desc=self.cmd_SAVAR_LOG_help)

#        savar_loghandler = logging.handlers.RotatingFileHandler(
#              self.savar_log_filename,
#              maxBytes=self.savar_log_maxbytes,
#              backupCount=self.savar_log_bkupcnt)
#        savar_logger.addHandler(savar_loghandler)

        # CREATE GMOVE LOGGER
        gmove_logger = logging.getLogger("user_gmove")
        gmove_logger.setLevel(logging.DEBUG)
        gmove_fhandler = logging.FileHandler(self.gmove_log_filename)
        gmove_formatter = logging.Formatter(self.gmove_log_format)
        gmove_fhandler.setLevel(logging.DEBUG)
        gmove_fhandler.setFormatter(gmove_formatter)
        gmove_logger.addHandler(gmove_fhandler)
        gcode = self.printer.lookup_object('gcode')
        gcode.register_command('GMOVE_LOG', self.cmd_GMOVE_LOG,
                               desc=self.cmd_GMOVE_LOG_help)

#        gmove_loghandler = logging.handlers.RotatingFileHandler(
#              self.gmove_log_filename,
#              maxBytes=self.gmove_log_maxbytes,
#              backupCount=self.gmove_log_bkupcnt)
#        gmove_logger.addHandler(gmove_loghandler)

        # MAKE INAUGURAL LOG ENTRIES AFTER SPAWNING
        # TRACE LOG INITIAL ENTRY
        trace_logger.debug('Logger Instantiated')
        cmpst_logger.debug('TRACE: ' + 'Logger Instantiated')

        # STATE LOG INITIAL ENTRY
        state_logger.debug('Logger Instantiated')
        cmpst_logger.debug('STATE: ' + 'Logger Instantiated')

        # SAVAR LOG INITIAL ENTRY
        savar_logger.debug('Logger Instantiated')
        cmpst_logger.debug('SAVAR: ' + 'Logger Instantiated')

        # GMOVE LOG INITIAL ENTRY
        gmove_logger.debug('Logger Instantiated')
        cmpst_logger.debug('GMOVE: ' + 'Logger Instantiated')

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
            
#    cmd_ROTATE_USER_LOGS_help = "ROTATES USER LOGS"
#    def cmd_ROTATE_USER_LOGS(self, gcmd):
#        gmove_logger = logging.getLogger("user_gmove")
#        lmsg = gcmd.get('MSG')
#        try:
#            gmove_logger.debug(lmsg)
#        except:
#            msg = "Unable to write user_gmove log entry"
#            logging.exception(msg)

    def get_status(self, eventtime):
        return {'status': 'userLogger module instantiated'}

def load_config(config):
    return UserLogger(config)
