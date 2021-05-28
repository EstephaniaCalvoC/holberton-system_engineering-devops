# Increse the request's limit

# Increse ulimit value
exec { 'fix-config-nginx':
  onlyif  => 'test -e /etc/default/nginx',
  command => 'sed -i "5s/[0-9]\+/$( ulimit -n )/" /etc/default/nginx',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}

# Restart nginex service
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
