# Create a file in /tmp.

file { 'holberton':
  ensure  => 'present',
  path    => '/tmp/holberton',
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
}
