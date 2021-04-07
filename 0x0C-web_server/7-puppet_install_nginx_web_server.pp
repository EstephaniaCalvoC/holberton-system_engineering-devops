# Install a web server Nginx
# listening on port 80
# GET root / return a page that contains the string Holberton School
# The redirection is “301 Moved Permanently”

package { 'nginx':
ensure => installed,
}

file { '/var/www/html/index.html':
content => 'Holberton School',
}

file_line {'Add redirection, 301':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server',
  line   => 'rewrite ^/redirect_me https://github.com/EstephaniaCalvoC/ permanent;',
}

service { 'nginx':
ensure  => running,
require => Package['nginx'],
}
