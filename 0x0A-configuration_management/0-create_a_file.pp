# Create a file in /tmp.

file { 'holberton':
  path => '/tmp/holberton',
  ensure  => 'present',
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
}
