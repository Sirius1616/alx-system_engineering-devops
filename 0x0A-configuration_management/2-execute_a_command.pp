# Execute the 'pkill' command to kill the process named 'killmenow'
exec { 'kill_killmenow':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
