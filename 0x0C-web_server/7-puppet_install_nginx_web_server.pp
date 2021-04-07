# Install a web server Nginx
# listening on port 80
# GET root / return a page that contains the string Holberton School
# The redirection is “301 Moved Permanently”

package {'install':
  ensure => installed,
  name   => 'nginx',
}
file {'root':
  path    => '/var/www/html/index.html',
  content => 'Holberton School',
}
file_line {'redirect':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_nme_;',
  line   => 'rewrite ^/redirect_me https://github.com/EstephaniaCalvoC/ permanent;',
}
service {'run':
  ensure  => running,
  require => Package['nginx'],
}
