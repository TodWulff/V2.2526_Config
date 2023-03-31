echo going to rotate

# ok, this sucks a bit to have to do this...
# also, the logrotate binary requires that the .confs it is feed be owned by root

### ! | sudo /usr/sbin/logrotate -v -f /home/pi/printer_data/logs/klipper_userlogs.conf

# call any named bash function under sudo with arbitrary arguments
run_escalated_function() {
  local function_name args_q
  function_name=$1; shift || return
  printf -v args_q '%q ' "$@"
  sudo bash -c "$(declare -f "$function_name"); $function_name $args_q"
}

privileged_bits() {
  /usr/sbin/logrotate -v -f /home/pi/printer_data/logs/klipper_userlogs.conf
}

run_escalated_function privileged_bits
