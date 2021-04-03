# Creat a manifest that kills a process named killmenow.

exec { 'otros':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin/', '/usr/loca/bin/', '/bin/'],
}
